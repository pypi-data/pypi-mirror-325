#!/usr/bin/env python3

# startdard
import sys
import os
import time
import math
import struct
# type extension
from typing import TypeVar, Callable, Any
from abc import ABC, abstractmethod
# match string
import re

# serial
import serial

# types
from collections import namedtuple

__version__ = "1.0"
__author__ = "emofalling"

micropython_code_file = f"{os.path.dirname(__file__)}/on_micropython/src.py"
encoding = "utf-8"
# Serial Terminal Codes
TER_INTP = b"\x03" # Terminal_Interrupt
TER_NEWL = b"\r\n" # Terminal_NewLine
# Serial None Parity
SER_PARITY_NONE = serial.PARITY_NONE
# Commands
ANS = b"\xaa" # Answer
ERR = b"\xff" # Error
SUC = b"\x00" # Success

TRUE = b"\x00"
FALSE = b"\x01"
NONE = b"\x02"

GSV = b"\x00" # get source version
GUN = b"\x01" # get uname
GID = b"\x02" # get uid
GFQ = b"\x03" # get cpu freq

GWD = b"\x10" # getcwd
SWD = b"\x11" # setcwd
LSDIR = b"\x12" # listdir
ILDIR = b"\x13" # ilistdir

FW = b"\x20" # file write
FR = b"\x21" # file read
BW = b"\x00" # [in file write / file read]block writing
BE = b"\xff" # [in file write / file read]block end
FRM = b"\x22" # remove file = remove
DRM = b"\x23" # remove dir = rmdir
MKDIR = b"\x24" # mkdir
RN = b"\x25" # rename

STAT  = b"\x30" # stat
VSTAT = b"\x31" # statvfs

GCI = b"\x40" # gc_info

RST = b"\xff" # reset
# Micropython match re-string
MPY_PART = r"MicroPython.*\n>>>" # .* match any string, include \n

class MpyFileOptError(Exception):
    pass
class _SupportsReadBinaryIO(ABC):
    @abstractmethod
    def readable(self) -> bool:
        pass
    @abstractmethod
    def read(self, size: int | None = -1) -> bytes:
        pass
    @abstractmethod
    def readinto(self, buffer: Any) -> bytes:
        pass
class _SupportsWriteBinaryIO(ABC):
    @abstractmethod
    def write(self, b: Any) -> int:
        pass
    @abstractmethod
    def writable(self) -> bool:
        pass
SupportsWriteBinaryIO = TypeVar("SupportsWriteBinaryIO", bound=_SupportsWriteBinaryIO)
SupportsReadBinaryIO = TypeVar("SupportsReadBinaryIO", bound=_SupportsReadBinaryIO)
class uname_result(namedtuple("uname_result", ["sysname", "nodename", "release", "version" ,"machine"])):
    pass
class ilistdir_item(namedtuple("ilistdir_item", ["name", "type", "inode"])):
    pass
class stat_result(namedtuple("stat_result", ["st_mode", "st_ino", "st_dev", "st_nlink", "st_uid", "st_gid", "st_size", "st_atime", "st_mtime", "st_ctime"])):
    pass
class statvfs_result(namedtuple("statvfs_result", ["f_bsize", "f_frsize", "f_blocks", "f_bfree", "f_bavail", "f_files", "f_ffree", "f_favail", "f_flag", "f_namemax"])):
    pass
class gc_info(namedtuple("gc_info", ["used", "free"])):
    pass

class MpyFileOpt:
    def __init__(self, 
                 port: str, 
                 baudrate: int                  = 115200, 
                 parity: str                    = SER_PARITY_NONE, 
                 stopbits: float                = 1, 
                 timeout: int | None            = 1, 
                 write_timeout: int | None      = 1,
                 inter_byte_timeout: int | None = 0.1,
                 wait_timeout: int              = 10,
                 immediate_connect: bool        = True,
                 *,
                 verbose: bool = True
                ) -> None:
        """Connect to micropython device

            Args
            ---
            `port`: Port name to connect to micropython device
            `baudrate` ... `inter_byte_timeout`: Serial port settings, see `serial.Serial`
            `verbose`: if True, print debug info
    
            Returns
            ---
            None
    
            Raises
            ---
            `TimeoutError`: if read or write time out
            `MpyFileOptError`: if device return error string
            Other: not to elaborate 
        """
        self.verbose = verbose
        self.wait_timeout = math.inf if wait_timeout is None else wait_timeout
        if not isinstance(self.wait_timeout, (int, float)):
            raise TypeError(f"wait_timeout must be int or float, but got {type(self.wait_timeout)}")
        if self.wait_timeout < 0.0:
            raise ValueError(f"wait_timeout must be positive, but got {self.wait_timeout}")
        self.ser = None
        self.ser = serial.Serial(port     ,          # port
                                 baudrate ,          # baudrate
                                 8        ,          # bytesize
                                 parity   ,          # parity
                                 stopbits ,          # stopbits
                                 timeout  ,          # timeout
                                 False    ,          # xonxoff
                                 False    ,          # rtscts
                                 write_timeout,      # write_timeout
                                 False    ,          # dsrdtr
                                 inter_byte_timeout, # inter_byte_timeout
                                )
        if immediate_connect:
            self.connect(verbose = self.verbose)
    def _dev_raise(self, funcname: str, errstr: bytes) -> None:
        """If the error throwed from micropython device, call it to throw error"""
        raise MpyFileOptError(f"On {funcname}(): In Micropython Device: \n    {errstr.decode(encoding, "ignore")}")
    def _dev_reset(self) -> None:
        """reset device"""
        self.ser.dtr = False
        time.sleep(0.01)
        self.ser.dtr = True
    def _dev_wait_in_repl(self) -> None:
        """send interrupt until device in REPL mode"""
        start_time = time.perf_counter()
        recs = ""
        while time.perf_counter() - start_time < self.wait_timeout:
            self._com_write(TER_INTP)
            time.sleep(0.05)
            s = self.ser.read_all()
            if s is not None:
                recs += s.decode(encoding, "ignore")
                # print(recs)
                if re.search(MPY_PART, recs, re.DOTALL) is not None:
                    ## Special Code: If this code is not included, the serial port output error rate will reach 50%
                    time.sleep(0.1)
                    self.ser.reset_input_buffer()
                    ## Special Code End
                    break
        else:
            raise TimeoutError("Wait time out.")
    def _dev_send_src(self) -> None:
        """send source code to device"""
        with open(micropython_code_file, "r", encoding=encoding) as f:
            self._com_write(b"exec(\'")
            self._com_write(repr(f.read())[1:-1].encode(encoding))
            self._com_write(b"\',globals())")
        self._com_write(TER_NEWL)
    def _com_write(self, data: bytes) -> int:
        """write data to the serial port, but it can handling the timeout error."""
        ret = self.ser.write(data)
        if ret == None:
            raise TimeoutError("Write time out.")
        return ret
    def _com_wait_ans(self):
        """wait device answer"""
        start_time = time.perf_counter()
        while time.perf_counter() - start_time < self.wait_timeout:
            #rdall = self.ser.read_all()
            #print(rdall.decode(encoding, "ignore"),end="")
            #if ANS in rdall:
            #    break
            if self.ser.read(1) == ANS:
                break
        else:
            raise TimeoutError("Wait time out.")
    def _com_read_bool(self) -> bool | None:
        """read boolean data or nonetype from the serial port"""
        ret = self.ser.read(1)
        if ret == b"":
            raise TimeoutError("Read time out.")
        if ret == TRUE:
            return True
        elif ret == FALSE:
            return False
        elif ret == NONE:
            return None
        else:
            raise MpyFileOptError(f"Unknown code: {ret}")
    def _com_write_bool(self, b: bool | None) -> None:
        """write boolean data or nonetype to the serial port"""
        if b is None:
            self._com_write(NONE)
        else:
            self._com_write(TRUE if b else FALSE)
    def _com_read_int(self) -> int:
        """read int data from the serial port"""
        ret = self.ser.read(4)
        if ret == b"":
            raise TimeoutError("Read time out.")
        return struct.unpack("<i", ret)[0]
    def _com_write_int(self, i: int) -> None:
        """write int data to the serial port"""
        ret = self.ser.write(struct.pack("<i", i))
        if ret == None:
            raise TimeoutError("Write time out.")
    def _com_read_uint(self) -> int:
        """read unsigned int data from the serial port"""
        ret = self.ser.read(4)
        if ret == b"":
            raise TimeoutError("Read time out.")
        return struct.unpack("<I", ret)[0]
    def _com_write_uint(self, i: int) -> None:
        """write unsigned int data to the serial port"""
        ret = self.ser.write(struct.pack("<I", i))
        if ret == None:
            raise TimeoutError("Write time out.")
    def _com_read_string(self) -> bytes:
        """read string data from the serial port"""
        len = self._com_read_uint()
        ret = self.ser.read(len)
        if ret == b"":
            raise TimeoutError("Read time out.")
        return ret
    def _com_write_string(self, str: bytes | bytearray) -> None:
        """write string data to the serial port"""
        self._com_write_uint(len(str))
        ret = self.ser.write(str)
        if ret == None:
            raise TimeoutError("Write time out.")

    def connect(self, *, verbose: bool = True) -> None:
        """Connect to device

            Args
            ---
            `verbose`: if True, print debug info

            Returns
            ---
            None

            Raises
            ---
            `TimeoutError`: if read or write time out
            `MpyFileOptError`: if device return error string
            Other: not to elaborate 
        """
        if verbose: print("[1/5] Reset device...")
        self._dev_reset()
        if verbose: print("[2/5] Wait device in REPL...")
        self._dev_wait_in_repl()
        if verbose: print("[3/5] Send source code...")
        self._dev_send_src()
        if verbose: print("[4/5] Wait device answer...")
        self._com_wait_ans()
        if verbose: print("[5/5] Done.")
    
    def get_source_version(self, *, verbose: bool = False) -> tuple[int, int]:
        """Get source version

           Args
           ---
           `verbose`: if True, print debug info

           Returns
           ---
           a tuple, info is `(major, minir)`

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate 
        """
        if verbose: print("[1/4] Send command VER...")
        self._com_write(GSV)
        if verbose: print("[2/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[3/4] Success, Read version...")
            ver = (self._com_read_int(), self._com_read_int())
            if verbose: print("[4/4] Done.")
            return ver
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[3/4] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[4/4] Done.")
            self._dev_raise("get_source_version", err)
    def uname(self, isstr: bool = True, *, verbose: bool = False) -> uname_result:
        """Read sys.uname from the device

           Args
           ---
           `isstr`: if True, return str, else return bytes
           `verbose`: if True, print debug info

           Returns
           ---
           a tuple, info is `uname_result(sysname=sysname, nodename=nodename, release=release, version=version, machine=machine)`

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate
        """
        if verbose: print("[1/4] Send command GUN...")
        self._com_write(GUN)
        if verbose: print("[2/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[3/4] Success, Read uname...")
            result = uname_result(
                self._com_read_string().decode(encoding, "ignore") if isstr else self._com_read_string(),
                self._com_read_string().decode(encoding, "ignore") if isstr else self._com_read_string(),
                self._com_read_string().decode(encoding, "ignore") if isstr else self._com_read_string(),
                self._com_read_string().decode(encoding, "ignore") if isstr else self._com_read_string(),
                self._com_read_string().decode(encoding, "ignore") if isstr else self._com_read_string()
            )
            if verbose: print("[4/4] Done.")
            return result
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[3/4] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[4/4] Done.")
            self._dev_raise("uname", err)
    def get_uid(self, *, verbose: bool = False) -> bytes:
        """Read unique(machine.unique_id) id from the device

           Args
           ---
           `verbose`: if True, print debug info

           Returns
           ---
           unique id. About content of unique_id, see `machine.unique_id`

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate
        """
        if verbose: print("[1/4] Send command GID...")
        self._com_write(GID)
        if verbose: print("[2/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[3/4] Success, Read unique id...")
            uid = self._com_read_string()
            if verbose: print("[4/4] Done.")
            return uid
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[3/4] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[4/4] Done.")
            self._dev_raise("unique_id", err)
    def get_freq(self, *, verbose: bool = False) -> int:
        """Read CPU frequency from the device

           Args
           ---
           `verbose`: if True, print debug info

           Returns
           ---
           CPU frequency

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate
        """
        if verbose: print("[1/4] Send command GFQ...")
        self._com_write(GFQ)
        if verbose: print("[2/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[3/4] Success, Read frequency...")
            freq = self._com_read_uint()
            if verbose: print("[4/4] Done.")
            return freq
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[3/4] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[4/4] Done.")
            self._dev_raise("get_freq", err)

    def getcwd(self, isstr: bool = True, *, verbose: bool = False) -> str | bytes:
        """Read current workdir(os.getcwd) from the device  

           Args
           ---
           `isstr`: if True, return str, else return bytes
           `verbose`: if True, print debug info

           Returns
           ---
           current workdir. If `isstr` is True, return type is `str`, else `bytes`

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate
        """
        if verbose: print("[1/4] Send command GWD...")
        self._com_write(GWD)
        if verbose: print("[2/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[3/4] Success, Read path string...")
            wd = self._com_read_string()
            if verbose: print("[4/4] Done.")
            return wd.decode(encoding, "ignore") if isstr else wd
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[3/4] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[4/4] Done.")
            self._dev_raise("getcwd", err)
    def chdir(self, path: str | bytes | bytearray, *, verbose: bool = False) -> None:
        """Change current workdir(os.chdir) to the device

           Args
           ---
           `path`: path to change to
           `verbose`: if True, print debug info

           Returns
           ---
           None

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate
        """
        if isinstance(path, str): 
            if verbose: print("[?/5] Convert path str to bytes...")
            path = path.encode(encoding)
        if verbose: print("[1/4] Send command SWD...")
        self._com_write(SWD)
        if verbose: print("[2/4] Send path string...")
        self._com_write_string(path)
        if verbose: print("[3/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/4] Success.")
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("chdir", err)
    def listdir(self, path: str | bytes | bytearray = b".", isstr: bool = True, *, verbose: bool = False) -> list[str | bytes]:
        """Read path list(os.listdir) from the device

           Args
           ---
           `path`: path to read. default is current directory(.)
           `isstr`: if True, path in list is str, else is bytes
           `verbose`: if True, print debug info

           Returns
           ---
           path list. If `isstr` is True, return type is `list[str]`, else `list[bytes]`

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate
        """
        if isinstance(path, str): 
            if verbose: print("[?/5] Convert path str to bytes...")
            path = path.encode(encoding)
        if verbose: print("[1/5] Send command LSDIR...")
        self._com_write(LSDIR)
        if verbose: print("[2/5] Send path string...")
        self._com_write_string(path)
        if verbose: print("[3/5] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/5] Success, Read dir list...")
            result = []
            length = self._com_read_uint()
            for _ in range(length):
                dir = self._com_read_string()
                result.append(dir.decode(encoding, "ignore") if isstr else dir)
            if verbose: print("[5/5] Done.")
            return result
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("listdir", err)
    def ilistdir(self, path: str | bytes | bytearray = b".", isstr: bool = True, *, verbose: bool = False) -> list[ilistdir_item]:
        """Read path info list(os.ilistdir) from the device

           Args
           ---
           `path`: path to read. default is current directory(.)
           `isstr`: if True, path in list is str, else is bytes
           `verbose`: if True, print debug info

           Returns
           ---
           path info list. If `isstr` is True, return type is `list[tuple[str, int, int]]`, else `list[tuple[bytes, int, int]]`.  

           It likes `[ilistdir_item(path=path, type=type, inode=inode), ...]`

           Raises
           ---
           `TimeoutError`: if read or write time out
           `MpyFileOptError`: if device return error string
           Other: not to elaborate
        """
        if isinstance(path, str): 
            if verbose: print("[?/5] Convert path str to bytes...")
            path = path.encode(encoding)
        if verbose: print("[1/5] Send command ILDIR...")
        self._com_write(ILDIR)
        if verbose: print("[2/5] Send path string...")
        self._com_write_string(path)
        if verbose: print("[3/5] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/5] Success, Read dir list...")
            result = []
            length = self._com_read_uint()
            for _ in range(length):
                name  = self._com_read_string()
                type  = self._com_read_uint()
                inode = self._com_read_uint()
                result.append(ilistdir_item(name.decode(encoding, "ignore") if isstr else name, type, inode))
            if verbose: print("[5/5] Done.")
            return result
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("ilistdir", err)
    def upload(self, mpy_dst_file: str | bytes | bytearray, src_fp: SupportsReadBinaryIO, src_size: int, write_callback_function: Callable[[int, int], None] = None, block_size: int = 4096, *, verbose: bool = False) -> None:
        """Upload file to the device

            Args
            ---
            `mpy_dst_file`: path to write in the device
            `src_fp`: BytesIO object in host that writable. If it is return value from `open()` , the mode must be `rb` or any readable binary mode.
            `src_size`: size of the file
            `write_callback_function`: callback function to print progress. If it isn't callable, there will not use it.
             - `write_callback_function(total:int, cur:int)` is called every time a block is transmitted. `total` is the total size of the file, `cur` is the current size of the file.
            
            `block_size`: block size to transmit data. It must be > 0. The larger `block_size`, the faster write speed, but the more memory usage on device.
        
            `verbose`: if True, print debug info

            Returns
            ---
            None

            Raises
            ---
            `ValueError`: if block_size <= 0
            `TypeError`: if read_callback_function is not callable
            `TimeoutError`: if read or write time out
            `MpyFileOptError`: if device return error string
            Other: not to elaborate
        """

        if isinstance(mpy_dst_file, str): 
            if verbose: print("[?/5] Convert path str to bytes...")
            mpy_dst_file = mpy_dst_file.encode(encoding)
        if verbose: print("[?/5] Check something...")
        if not callable(write_callback_function):
            write_callback_function = lambda total, cur: None
        if block_size <= 0:
            raise ValueError("block_size must be > 0")
        if not isinstance(src_size, int) and src_size < 0:
            raise TypeError("src_size must be integer and >= 0")
        if not src_fp.readable():
            raise IOError("src_fp must be readable")
        if verbose: print("[1/5] Send command FW...")
        self._com_write(FW)
        if verbose: print("[2/5] Send path string, file size, and block size...")
        self._com_write_string(mpy_dst_file)
        file_size = src_size
        self._com_write_uint(file_size)
        self._com_write_uint(block_size)
        if verbose: print("[3/5] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/5] Success, Send data...")
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("upload", err)
        buffer = bytearray(block_size)
        total = file_size
        cur = 0
        write_callback_function(total, cur)
        while file_size > 0:
            if file_size >= block_size:
                self._com_write(BW)
                lendata = block_size
                src_fp.readinto(buffer)
            else:
                del buffer
                self._com_write(BE)
                lendata = file_size
                self._com_write_uint(lendata)
                buffer = src_fp.read(lendata)
            self._com_write(buffer)
            if verbose: print(f"Send {lendata} bytes")
            ret = self.ser.read(1)
            if ret != SUC:
                if ret == b"":
                    raise TimeoutError("Read time out.")
                else:
                    if verbose: print("[5/6] Failed, Read error string...")
                    err = self._com_read_string()
                    if verbose: print("[6/6] Done.")
                    self._dev_raise("upload", err)
            file_size -= lendata
            cur += lendata
            write_callback_function(total, cur)
            if verbose: print(f"Sended {lendata} bytes, {cur}/{total}")
        if verbose: print("[5/5] Done.")
    def download(self, mpy_src_file: str | bytes | bytearray, dst_fp: SupportsWriteBinaryIO, read_callback_function: Callable[[int, int], None] = None, block_size: int = 4096, *, verbose: bool = False) -> None:
        """Download file from the device

            Args
            ---
            `mpy_src_file`: path to read in the device
            `dst_fp`: BytesIO object in host that writable. If it is return value from `open()` , the mode must be `wb` or any writable binary mode.
            `read_callback_function`: callback function to print progress. If it isn't callable, there will not use it.
                - `read_callback_function(total:int, cur:int)` is called every time a block is transmitted. `total` is the total size of the file, `cur` is the current size of the file.
            
            `block_size`: block size for read/write

            `verbose`: if True, print debug info

            Returns
            ---
            None

            Raises
            ---
            `ValueError`: if block_size <= 0
            `TypeError`: if read_callback_function is not callable
            `TimeoutError`: if read or write time out
            `MpyFileOptError`: if device return error string
            Other: not to elaborate

        """
        if isinstance(mpy_src_file, str):
            if verbose: print("[?/5] Convert path str to bytes...")
            mpy_src_file = mpy_src_file.encode(encoding)
        if verbose: print("[?/5] Check something...")
        if not callable(read_callback_function):
            read_callback_function = lambda total, cur: None
        if block_size <= 0:
            raise ValueError("block_size must be > 0")
        if not dst_fp.writable():
            raise IOError("dst_fp must be writable")
        if verbose: print("[1/5] Send command FR...")
        self._com_write(FR)
        if verbose: print("[2/5] Send path string, and block size...")
        self._com_write_string(mpy_src_file)
        self._com_write_uint(block_size)
        if verbose: print("[3/5] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/5] Success, Read file data...")
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("download", err)
        file_size = self._com_read_uint()
        if verbose: print(f"File size: {file_size}")
        total = file_size
        cur = 0
        read_callback_function(total, cur)
        while file_size > 0:
            if file_size >= block_size:
                lendata = block_size
                self._com_write(BW)
            else:
                lendata = file_size
                self._com_write(BE)
                self._com_write_uint(lendata)
            if verbose: print(f"Read {lendata} bytes")
            ret = self.ser.read(1)
            if ret != SUC:
                if ret == b"":
                    raise TimeoutError("Read time out.")
                else:
                    if verbose: print("[5/6] Failed, Read error string...")
                    err = self._com_read_string()
                    if verbose: print("[6/6] Done.")
                    self._dev_raise("download", err)
            dst_fp.write(self.ser.read(lendata))
            file_size -= lendata
            cur += lendata
            read_callback_function(total, cur)
            if verbose: print(f"Readed {lendata} bytes, {cur}/{total}")
        if verbose: print("[5/5] Done.")
    def remove(self, file: str | bytes | bytearray, *, verbose: bool = False) -> None:
        """Remove file(os.remove) from the device

        Args
        ---
        `file`: file path to remove
        `verbose`: if True, print debug info

        Returns
        ---
        None

        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        if isinstance(file, str): 
            if verbose: print("[?/4] Convert path str to bytes...")
            file = file.encode(encoding)
        if verbose: print("[1/4] Send command FRM...")
        self._com_write(FRM)
        if verbose: print("[2/4] Send path string...")
        self._com_write_string(file)
        if verbose: print("[3/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/4] Success.")
            return
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("remove", err)
    def rmdir(self, dir: str | bytes | bytearray, *, verbose: bool = False) -> None:
        """Remove dir(os.rmdir) from the device

        Args
        ---
        `dir`: dir path to remove
        `verbose`: if True, print debug info

        Returns
        ---
        None

        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        if isinstance(dir, str): 
            if verbose: print("[?/4] Convert path str to bytes...")
            dir = dir.encode(encoding)
        if verbose: print("[1/4] Send command DRM...")
        self._com_write(DRM)
        if verbose: print("[2/4] Send path string...")
        self._com_write_string(dir)
        if verbose: print("[3/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/4] Success.")
            return
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("rmdir", err)
    def mkdir(self, dir: str | bytes | bytearray, *, verbose: bool = False) -> None:
        """Make dir(os.mkdir) from the device

        Args
        ---
        `dir`: dir path to make
        `verbose`: if True, print debug info

        Returns
        ---
        None

        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        if isinstance(dir, str): 
            if verbose: print("[?/4] Convert path str to bytes...")
            dir = dir.encode(encoding)
        if verbose: print("[1/4] Send command MKDIR...")
        self._com_write(MKDIR)
        if verbose: print("[2/4] Send path string...")
        self._com_write_string(dir)
        if verbose: print("[3/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/4] Success.")
            return
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("mkdir", err)
    def rename(self, old: str | bytes | bytearray, new: str | bytes | bytearray, *, verbose: bool = False) -> None:
        """Rename path(os.rename) from the device

        Args
        ---
        `old`: old path
        `new`: new path
        `verbose`: if True, print debug info

        Returns
        ---
        None

        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        if isinstance(old, str): 
            if verbose: print("[?/4] Convert old path str to bytes...")
            old = old.encode(encoding)
        if isinstance(new, str):
            if verbose: print("[?/4] Convert new path str to bytes...")
            new = new.encode(encoding)
        if verbose: print("[1/4] Send command RN...")
        self._com_write(RN)
        if verbose: print("[2/4] Send old path string and new path string...")
        self._com_write_string(old)
        self._com_write_string(new)
        if verbose: print("[3/4] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/4] Success.")
            return
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("rename", err)

    def stat(self, path: str | bytes | bytearray, *, verbose: bool = False) -> stat_result:
        """Get stat(os.stat) from the device

        Args
        ---
        `path`: path to get stat
        `verbose`: if True, print debug info

        Returns
        ---
        a tuple, info is `stat_result(st_mode=st_mode, st_ino=st_ino, st_dev=st_dev, st_nlink=st_nlink, st_uid=st_uid, st_gid=st_gid, st_size=st_size, st_atime=st_atime, st_mtime=st_mtime, st_ctime=st_ctime)`
        
        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        if isinstance(path, str): 
            if verbose: print("[?/5] Convert path str to bytes...")
            path = path.encode(encoding)
        if verbose: print("[1/5] Send command STAT...")
        self._com_write(STAT)
        if verbose: print("[2/5] Send path string...")
        self._com_write_string(path)
        if verbose: print("[3/5] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/5] Success, Read stat...")
            result = stat_result(
                self._com_read_int(), # st_mode
                self._com_read_int(), # st_ino
                self._com_read_int(), # st_dev
                self._com_read_int(), # st_nlink
                self._com_read_int(), # st_uid
                self._com_read_int(), # st_gid
                self._com_read_int(), # st_size
                self._com_read_int(), # st_atime
                self._com_read_int(), # st_mtime
                self._com_read_int()  # st_ctime
            )
            if verbose: print("[5/5] Done.")
            return result
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("stat", err)
    def statvfs(self, path: str | bytes | bytearray, *, verbose: bool = False) -> statvfs_result:
        """Get filesystem stat(os.statvfs) from the device

        Args
        ---
        `path`: path to get stat
        `verbose`: if True, print debug info

        Returns
        ---
        a tuple, info is `statvfs_result(f_bsize=f_bsize, f_frsize=f_frsize, f_blocks=f_blocks, f_bfree=f_bfree, f_bavail=f_bavail, f_files=f_files, f_ffree=f_ffree, f_favail=f_favail, f_flag=f_flag, f_namemax=f_namemax)`
        
        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        if isinstance(path, str): 
            if verbose: print("[?/5] Convert path str to bytes...")
            path = path.encode(encoding)
        if verbose: print("[1/5] Send command VSTAT...")
        self._com_write(VSTAT)
        if verbose: print("[2/5] Send path string...")
        self._com_write_string(path)
        if verbose: print("[3/5] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/5] Success, Read statvfs...")
            result = statvfs_result(
                self._com_read_int(), # f_bsize
                self._com_read_int(), # f_frsize
                self._com_read_int(), # f_blocks
                self._com_read_int(), # f_bfree
                self._com_read_int(), # f_bavail
                self._com_read_int(), # f_files
                self._com_read_int(), # f_ffree
                self._com_read_int(), # f_favail
                self._com_read_int(), # f_fsid
                self._com_read_int()  # f_flag
            )
            if verbose: print("[5/5] Done.")
            return result
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("statvfs", err)

    def get_gc_info(self, collect: bool = True, *, verbose: bool = False) -> gc_info:
        """Get GC info from the device

        Args
        ---
        `collect`: if True, call gc.collect() before get info
        `verbose`: if True, print debug info

        Returns
        ---
        a tuple, info is `gc_info(used=mem_alloc, free=mem_free)`

        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        if verbose: print("[1/5] Send command GCI...")
        self._com_write(GCI)
        if verbose: print("[2/5] Send collect bool...")
        self._com_write_bool(collect)
        if verbose: print("[3/5] Wait answer...")
        ret = self.ser.read(1)
        if ret == SUC:
            if verbose: print("[4/5] Success, Read gc info...")
            result = gc_info(
                self._com_read_int(), # mem_alloc
                self._com_read_int(), # mem_free
            )
            if verbose: print("[5/5] Done.")
            return result
        elif ret == b"":
            raise TimeoutError("Read time out.")
        else:
            if verbose: print("[4/5] Failed, Read error string...")
            err = self._com_read_string()
            if verbose: print("[5/5] Done.")
            self._dev_raise("gc_info", err)
    def _reset(self, *, verbose: bool = False) -> None:
        """reset device"""
        if verbose: print("[1/2] Send command RST...")
        self._com_write(RST)
        if verbose: print("[2/2] Done.")
    def close(self, *, verbose: bool = False) -> None:
        """Reset device and close the serial port
        
        Args
        ---
        `verbose`: if True, print debug info
        
        Raises
        ---
        `TimeoutError`: if read or write time out
        `MpyFileOptError`: if device return error string
        Other: not to elaborate
        """
        self._reset(verbose = verbose)
        self.ser.close()
    def __del__(self):
        """call self.close when this object is deleted"""
        if self.ser is None:
            return
        if self.ser.is_open:
            self.close()

def main():
    import stat
    import datetime
    import traceback
    import argparse
    import shlex
    import binascii
    import math
    import json
    from io import BytesIO
    argv = sys.argv[1:]
    # terminal codes
    ANSI_RESET_ALL          = "\x1b[0m"
    ANSI_COLOR_BLACK        = "\x1b[30m"
    ANSI_COLOR_RED          = "\x1b[31m"
    ANSI_COLOR_GREEN        = "\x1b[32m"
    ANSI_COLOR_YELLOW       = "\x1b[33m"
    ANSI_COLOR_BLUE         = "\x1b[34m"
    ANSI_COLOR_PURPLE       = "\x1b[35m"
    ANSI_COLOR_CYAN         = "\x1b[36m"
    ANSI_COLOR_WHITE        = "\x1b[37m"
    ANSI_COLOR_LIGHT_BLACK  = "\x1b[90m"
    ANSI_COLOR_LIGHT_RED    = "\x1b[91m"
    ANSI_COLOR_LIGHT_GREEN  = "\x1b[92m"
    ANSI_COLOR_LIGHT_YELLOW = "\x1b[93m"
    ANSI_COLOR_LIGHT_BLUE   = "\x1b[94m"
    ANSI_COLOR_LIGHT_PURPLE = "\x1b[95m"
    ANSI_COLOR_LIGHT_CYAN   = "\x1b[96m"
    ANSI_COLOR_LIGHT_WHITE  = "\x1b[97m"
    ANSI_CTRL_CLRLINE       = "\x1b[A1\r\x1b[K"
    ANSI_CTRL_HIDM          = "\x1b[?25l"
    ANSI_CTRL_SIDM          = "\x1b[?25h"
    ANSI_CHAR_TNODE         = "\u251c"
    ANSI_CHAR_TEND          = "\u2514"
    ANSI_CHAR_VLINE         = "\u2502"
    ANSI_CHAR_HLINE         = "\u2500"
    ANSI_CHAR_PGLINE        = "\u2501"
    # colors
    ERROR_COLOR = ANSI_COLOR_RED

    BASE_BI = 1024
    BASE_SI = 1000
    SUFFIX_LIST_BI          = ["", "K" , "M" , "G" , "T" , "P" , "E" , "Z" , "Y" , "B"]
    SUFFIX_LIST_BI_MONO     = SUFFIX_LIST_BI.copy(); SUFFIX_LIST_BI_MONO[0] = " "
    SUFFIX_LIST_SI          =  ["", "k" , "M" , "G" , "T" , "P" , "E" , "Z" , "Y" , "B"]
    SUFFIX_LIST_SI_MONO     = SUFFIX_LIST_SI.copy(); SUFFIX_LIST_SI_MONO[0] = " "
    def auto_suffix(num: int | float, base: int | float, suffix_list: list[str]) -> tuple[int, str]:
        try:
            lf = math.floor(math.log(num, base))
        except ValueError:
            lf = 0
        try:
            suffix = suffix_list[lf]
        except IndexError:
            return 1, suffix_list[0]
        return base ** lf, suffix
    def _repr(obj: object) -> str:
        reprobj = repr(obj)
        if type(obj) is str:
            return f'"{reprobj[1:-1]}"'
        else:
            return reprobj

    main_parser = argparse.ArgumentParser(description = "Connect to MicroPython device and do something with subcommands.", epilog = "See README.md for more information.", add_help = True)
    main_parser.add_argument("--subcmd-help"              ,                                             default="",              help="print help message of subcommand")
    main_parser.add_argument("-V" , "--version", action="version", version=f"{__version__}")
    main_parser.add_argument("-p" , "--port"              ,                                             default="",              help="serial port")
    main_parser.add_argument("-B" , "--baudrate"          , type=int,                                   default=115200,          help="serial baudrate. default 115200")
    main_parser.add_argument("-P" , "--parity"            ,             choices=serial.Serial.PARITIES, default=SER_PARITY_NONE, help="serial parity. default N")
    main_parser.add_argument("-S" , "--stopbits"          , type=float, choices=serial.Serial.STOPBITS, default=1,               help="serial stopbits. default 1")
    main_parser.add_argument("-To", "--timeout"           , type=float,                                 default=1,               help="serial timeout. if 0, no timeout. default 1")
    main_parser.add_argument("-Tw", "--write-timeout"     , type=float,                                 default=1,               help="serial write timeout. if 0, no timeout. default 1")
    main_parser.add_argument("-Tb", "--inter-byte-timeout", type=float,                                 default=0.1,             help="serial inter-byte timeout. default 0.1")
    main_parser.add_argument("-wt", "--wait-timeout"      , type=float,                                 default=10,              help="serial wait timeout. default 10")

    
    main_parser.add_argument("-pbmaxw", "--progressbar-maxwidth", type=int, default=50, help="progressbar max width. unit is chars. it must be > 0. default 50.")
    main_parser.add_argument("-pbminw", "--progressbar-minwidth", type=int, default=5, help="progressbar min width. unit is chars. it must be > 0. default 5.")

    main_parser.add_argument("-nc" , "--no-colorful"      , action="store_false", help="make output not colorful. if terminal not support ANSI color escape sequence, recommended select this option")
    main_parser.add_argument("-v" , "--verbose"           , action="store_true", help="output debug info")
    
    parser_dict = {}

    # help
    subcmd_help_parser = argparse.ArgumentParser("help", description = "Print help message of subcommand.", epilog = "See README.md for more information.", add_help = True)
    subcmd_help_parser.add_argument("cmds", nargs="*", help="subcommands to print help message. if not specified, print help message of all subcommands.")
    subcmd_help_parser.add_argument("-u", "--usage", action="store_true", help="print usage")
    parser_dict["help"]=subcmd_help_parser
    # shell
    subcmd_shell_parser = argparse.ArgumentParser("shell", description = "Into a shell to key and run subcommands conveniently.", epilog = "See README.md for more information.", add_help = True)
    parser_dict["shell"]=subcmd_shell_parser
    # shell-exit
    subcmd_shell_exit_parser = argparse.ArgumentParser("exit", description = "Exit shell.", epilog = "See README.md for more information.", add_help = True)
    # ver
    subcmd_ver_parser = argparse.ArgumentParser("ver", description="Print version of this project", epilog="See README.md for more information.", add_help = True)
    subcmd_ver_parser.add_argument("-c", "--csv", action="store_true", help="output csv format")
    subcmd_ver_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["ver"]=subcmd_ver_parser
    # uname
    subcmd_uname_parser = argparse.ArgumentParser("uname", description="Print device's system information. if no option(except --csv(-c) and --verbose), output kernel name.", epilog="See README.md for more information.", add_help = True)
    subcmd_uname_parser.add_argument("-a", "--all", action="store_true", help="output all information")
    subcmd_uname_parser.add_argument("-s", "--kernel-name", action="store_true", help="output the kernel name. this is the normal option")
    subcmd_uname_parser.add_argument("-n", "--nodename", action="store_true", help="output the network node hostname")
    subcmd_uname_parser.add_argument("-r", "--kernel-release", action="store_true", help="output the kernel release")
    subcmd_uname_parser.add_argument("-v", "--kernel-version", action="store_true", help="output the kernel version")
    subcmd_uname_parser.add_argument("-m", "--machine", action="store_true", help="output the machine hardware name")
    subcmd_uname_parser.add_argument("-c", "--csv", action="store_true", help="output csv format")
    subcmd_uname_parser.add_argument(      "--verbose", action="store_true", help="output debug info")
    parser_dict["uname"]=subcmd_uname_parser
    # uid
    subcmd_uid_parser = argparse.ArgumentParser("uid", description="Print device's unique id", epilog="See README.md for more information.", add_help = True)
    subcmd_uid_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["uid"]=subcmd_uid_parser
    # freq
    subcmd_freq_parser = argparse.ArgumentParser("freq", description="Print device's cpu frequency", epilog="See README.md for more information.", add_help = True)
    subcmd_freq_parser.add_argument("-r", "--raw", action="store_true", help="output raw cpu frequency. it has no suffix, unit Hz.")
    subcmd_freq_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["freq"]=subcmd_freq_parser
    # pwd
    subcmd_pwd_parser = argparse.ArgumentParser("pwd", description="Print device's current working directory", epilog="See README.md for more information.", add_help = True)
    subcmd_pwd_parser.add_argument("-l", "--local", action="store_true", help="output localhost's current working directory")
    subcmd_pwd_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["pwd"]=subcmd_pwd_parser
    # cd
    subcmd_cd_parser = argparse.ArgumentParser("cd", description="Change device's current working directory", epilog="See README.md for more information.", add_help = True)
    subcmd_cd_parser.add_argument("dir", nargs="?", default="/", help="dir to change to. if not specified, change to /")
    subcmd_cd_parser.add_argument("-l", "--local", action="store_true", help="output localhost's current working directory")
    subcmd_cd_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["cd"]=subcmd_cd_parser
    # ls
    subcmd_ls_parser = argparse.ArgumentParser("ls", description="List device's files and directories", epilog="See README.md for more information.", add_help = True)
    subcmd_ls_parser.add_argument("-a", "--all", action="store_true", help="show all files and directories, including hidden ones")
    subcmd_ls_parser.add_argument("-R", "--recursive", action="store_true", help="recursively list directories")
    subcmd_ls_parser.add_argument("-l", "--long", action="store_true", help="show detailed information about files and directories")
    subcmd_ls_sort_parser_group = subcmd_ls_parser.add_mutually_exclusive_group()
    subcmd_ls_sort_parser_group.add_argument("-S", "--sort-size", action="store_true", help="sort by size")
    subcmd_ls_sort_parser_group.add_argument("-N", "--sort-name", action="store_true", help="sort by name")
    subcmd_ls_parser.add_argument("-r", "--reverse", action="store_true", help="reverse the order of the sort")
    subcmd_ls_pack_parser_group = subcmd_ls_parser.add_mutually_exclusive_group()
    subcmd_ls_pack_parser_group.add_argument(      "--row", action="store_true", help="only show itesms in a single row")
    subcmd_ls_pack_parser_group.add_argument("-c", "--column", action="store_true", help="only show itesms in a single column")
    subcmd_ls_parser.add_argument("--sep", default=3, type=int, help="number of spaces between items. It must be >= 0. default 3")
    subcmd_ls_parser.add_argument("-sC", "--sep-comma", action="store_true", help="use comma as separator")
    subcmd_ls_parser.add_argument("-Q", "--quote", action="store_true", help="quote items")
    subcmd_ls_parser.add_argument("-s", "--slash", action="store_true", help="append / to directories")
    subcmd_ls_size_parser_group = subcmd_ls_parser.add_mutually_exclusive_group()
    subcmd_ls_size_parser_group.add_argument("-si", "--si", action="store_true", help="use SI units. 1K = 1000")
    subcmd_ls_size_parser_group.add_argument("-bi", "--bi", action="store_true", help="use binary units. 1K = 1024")
    subcmd_ls_parser.add_argument("-dp", "--decimal-places", default=3, type=int, help="number of decimal places. It must be >= -1. if it is -1, the decimal places is no limits. default 3")
    subcmd_ls_parser.add_argument("-J", "--json", action="store_true", help="output json format")
    subcmd_ls_parser.add_argument("dir", nargs="?", default=".", help="dir to list. if not specified, list .")
    subcmd_ls_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["ls"]=subcmd_ls_parser
    # tree
    subcmd_tree_parser = argparse.ArgumentParser("tree", description="List device's files and directories in tree format", epilog="See README.md for more information.", add_help = True)
    subcmd_tree_parser.add_argument("-sl", "--slash", action="store_true", help="append / to directories")
    subcmd_tree_parser.add_argument("-hl", "--hline-len", default=2, type=int, help="number of horizontal line with every items. It must be >= 0. default 2")
    subcmd_tree_parser.add_argument("--noreport", action="store_true", help="Turn off file/directory count at end of tree listing")
    subcmd_tree_parser.add_argument("-Q", "--quote", action="store_true", help="quote items")
    subcmd_tree_parser.add_argument("-L", "--level", default=-1, type=int, help="max display depth of the directory tree. It must be > 0. default not limited")
    subcmd_tree_outfmt_parser_group = subcmd_tree_parser.add_mutually_exclusive_group()
    subcmd_tree_outfmt_parser_group.add_argument("-J", "--json", action="store_true", help="output json format")
    subcmd_tree_outfmt_parser_group.add_argument("-X", "--xml", action="store_true", help="output xml format")
    subcmd_tree_parser.add_argument("dir", nargs="*", default=["."], help="dir to list. if not specified, list .")
    subcmd_tree_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["tree"]=subcmd_tree_parser
    # write
    subcmd_write_parser = argparse.ArgumentParser("write", description="Write file to file on device", epilog="See README.md for more information.", add_help = True)
    subcmd_write_parser.add_argument("-b", "--blocksize", type=int, default=4096, help="block size to write. A larger block size can bring faster transmission speed, but it need larger memory for micropython device. default 4096.")
    subcmd_write_parser.add_argument("dst", type=str, help="destination file on device to write")
    subcmd_write_parser.add_argument("src", type=str, help="source file on localhost to transmit")
    subcmd_write_parser.add_argument("-q", "--quiet", action="store_true", help="do not output progress bar and report.")
    subcmd_write_parser.add_argument("--noreport", action="store_true", help="do not output report")
    subcmd_write_parser.add_argument("-w", "--warning", action="store_true", help="If the dst file exists, user can choose whether to overwrite it. If not specified, always overwrite it.")
    subcmd_write_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["write"]=subcmd_write_parser
    # push
    subcmd_push_parser = argparse.ArgumentParser("push", description="Push items to device", epilog="See README.md for more information.", add_help = True)
    subcmd_push_parser.add_argument("-b", "--blocksize", type=int, default=4096, help="block size to push. A larger block size can bring faster transmission speed, but it need larger memory for micropython device. default 4096.")
    subcmd_push_parser.add_argument("-nr", "--no-recursive", action="store_true", help="when push the directory, not push recursively subitems")
    subcmd_push_parser.add_argument("dst", help="destination path on device to receive items")
    subcmd_push_parser.add_argument("src", nargs="+", help="Items to push on localhost. It can be files or directories")
    subcmd_push_parser.add_argument("-q", "--quiet", action="store_true", help="do not output progress bar and report.")
    subcmd_push_parser.add_argument("--noreport", action="store_true", help="do not output report")
    subcmd_push_parser.add_argument("-w", "--warning", action="store_true", help="If the dst file exists, user can choose whether to overwrite it. If not specified, always overwrite it.")
    subcmd_push_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["push"]=subcmd_push_parser
    # read
    subcmd_read_parser = argparse.ArgumentParser("read", description="Read file from device", epilog="See README.md for more information.", add_help = True)
    subcmd_read_parser.add_argument("-b", "--blocksize", type=int, default=4096, help="block size to write. A larger block size can bring faster transmission speed, but it need larger memory for micropython device. default 4096.")
    subcmd_read_parser.add_argument("dst", type=str, help="destination file on localhost to receive")
    subcmd_read_parser.add_argument("src", type=str, help="source file on device to read")
    subcmd_read_parser.add_argument("-q", "--quiet", action="store_true", help="do not output progress bar and report.")
    subcmd_read_parser.add_argument("--noreport", action="store_true", help="do not output report")
    subcmd_read_parser.add_argument("-w", "--warning", action="store_true", help="If the dst file exists, user can choose whether to overwrite it. If not specified, always overwrite it.")
    subcmd_read_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["read"]=subcmd_read_parser
    # cat
    subcmd_cat_parser = argparse.ArgumentParser("cat", description="Print file content", epilog="See README.md for more information.", add_help = True)
    subcmd_cat_parser.add_argument("-b", "--blocksize", type=int, default=4096, help="block size to write. A larger block size can bring faster transmission speed, but it need larger memory for micropython device. default 4096.")
    subcmd_cat_parser.add_argument("src", nargs="+", help="source files on device to print")
    subcmd_cat_parser.add_argument("-n", "--number", action="store_true", help="number all output lines")
    subcmd_cat_parser.add_argument("-s", "--squeeze-blank", action="store_true", help="suppress repeated empty output lines")
    subcmd_cat_parser.add_argument("-q", "--quiet", action="store_true", help="do not output progress bar and report.")
    subcmd_cat_parser.add_argument("-w", "--warning", action="store_true", help="If the dst file exists, user can choose whether to overwrite it. If not specified, always overwrite it.")
    subcmd_cat_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["cat"]=subcmd_cat_parser
    # pull
    subcmd_pull_parser = argparse.ArgumentParser("pull", description="Pull items from device", epilog="See README.md for more information.", add_help = True)
    subcmd_pull_parser.add_argument("-b", "--blocksize", type=int, default=4096, help="block size to push. A larger block size can bring faster transmission speed, but it need larger memory for micropython device. default 4096.")
    subcmd_pull_parser.add_argument("-nr", "--no-recursive", action="store_true", help="when push the directory, not push recursively subitems")
    subcmd_pull_parser.add_argument("dst", help="destination path on localhost to receive items")
    subcmd_pull_parser.add_argument("src", nargs="+", help="Items to pull on device. It can be files or directories")
    subcmd_pull_parser.add_argument("-q", "--quiet", action="store_true", help="do not output progress bar and report.")
    subcmd_pull_parser.add_argument("--noreport", action="store_true", help="do not output report")
    subcmd_pull_parser.add_argument("-w", "--warning", action="store_true", help="If the dst file exists, user can choose whether to overwrite it. If not specified, always overwrite it.")
    subcmd_pull_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["pull"]=subcmd_pull_parser
    # rm
    subcmd_rm_parser = argparse.ArgumentParser("rm", description="Remove file or directory on device", epilog="See README.md for more information.", add_help = True)
    subcmd_rm_parser.add_argument("-d", "--dir", action="store_true", help="support remove directory")
    subcmd_rm_parser.add_argument("-R", "-r", "--recursive", action="store_true", help="remove items. if it is a directory, remove their contents recursively too")
    subcmd_rm_parser.add_argument("-p", "--print", action="store_true", help="output items to remove")
    subcmd_rm_parser.add_argument("paths", nargs="+", help="Items to remove on device. It can be files or directories")
    subcmd_rm_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["rm"]=subcmd_rm_parser
    # rmdir
    subcmd_rmdir_parser = argparse.ArgumentParser("rmdir", description="Remove empty directory on device", epilog="See README.md for more information.", add_help = True)
    subcmd_rmdir_parser.add_argument("dirs", nargs="+", help="Directories to remove on device. It must be only directories")
    subcmd_rmdir_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["rmdir"]=subcmd_rmdir_parser
    # mkdir
    subcmd_mkdir_parser = argparse.ArgumentParser("mkdir", description="Make directory on device", epilog="See README.md for more information.", add_help = True)
    subcmd_mkdir_parser.add_argument("dirs", nargs="+", help="Items to make on device. It can be files or directories")
    subcmd_mkdir_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["mkdir"]=subcmd_mkdir_parser
    # mv
    subcmd_mv_parser = argparse.ArgumentParser("mv", description="Move (or Rename) file or directory on device", epilog="See README.md for more information.", add_help = True)
    subcmd_mv_parser.add_argument("src", help="source file or directory on device to move")
    subcmd_mv_parser.add_argument("dst", help="destination file or directory on device to move")
    subcmd_mv_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["mv"]=subcmd_mv_parser
    # gc
    subcmd_gc_parser = argparse.ArgumentParser("gc", description="Get GC info from device", epilog="See README.md for more information.", add_help = True)
    subcmd_gc_parser.add_argument("-r", "--raw", action="store_true", help="output raw gc info. it has no suffix, unit Hz. if not specified, output human readable format with 1024 base.")
    subcmd_gc_parser.add_argument("-cl", "--collect", action="store_true", help="call gc.collect() before get info")
    subcmd_gc_parser.add_argument("-c", "--csv", action="store_true", help="output csv format")
    subcmd_gc_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["gc"]=subcmd_gc_parser
    # stat
    subcmd_stat_parser = argparse.ArgumentParser("stat", description="Get stat(os.stat/os.statvfs) from device", epilog="See README.md for more information.", add_help = True)
    subcmd_stat_parser.add_argument("-f", "--file-system", action="store_true", help="get filesystem stat(os.statvfs)")
    subcmd_stat_parser.add_argument("paths", nargs="+", help="paths to get stat")
    subcmd_stat_parser.add_argument("-v", "--verbose", action="store_true", help="output debug info")
    parser_dict["stat"]=subcmd_stat_parser

    all_commands = ["help", "shell", "ver", "uname", "uid", "freq", "pwd", "cd", "ls", "tree", "write", "push", "read", "cat", "pull", "rm", "rmdir", "mkdir", "mv", "gc", "stat"]
    colorful = False
    def logerr(msg, prefix = "Error: "):
        print((ERROR_COLOR if colorful else "") + prefix + msg + (ANSI_RESET_ALL if colorful else ""))
    def subcmd_parse_args(parser: argparse.ArgumentParser, args: list[str]):
        try:
            return parser.parse_args(args[1:])
        except SystemExit:
            return False
    def get_term_size() -> tuple[int, int]:
        try:
            return os.get_terminal_size()
        except OSError:
            return 80, 25
    def inputcheck(msg: str, ist: str = "(Y/n)", default: Any = False) -> bool:
        while True:
            try:
                ans = input(msg + ist + ": ")
                if ans == "":
                    return default
                if ans.lower() in ["y", "yes"]:
                    return True
                if ans.lower() in ["n", "no"]:
                    return False
            except:
                return default
    def get_last_four_octal_digits(mode: int) -> str:
        octs = oct(mode)[2:]
        oocts = octs[-4:].zfill(4)
        return oocts

    maincmd_argv = []
    subcmd_argv_list = []
    is_subcmd = False
    for i in argv:
        if i in all_commands:
            is_subcmd = True
            current_subcmd_argv = [i]
            subcmd_argv_list.append(current_subcmd_argv)
        else:
            if is_subcmd:
                current_subcmd_argv.append(i)
            else:
                maincmd_argv.append(i)
    if "-v" in maincmd_argv or "--verbose" in maincmd_argv:
        print("Main command:", shlex.join(maincmd_argv))
        print("Subcommands:")
        for i in subcmd_argv_list:
            print("    "+_repr(shlex.join(i))[1:-1])
    args = main_parser.parse_args(maincmd_argv)
    colorful = args.no_colorful
    progressbar_maxwidth = args.progressbar_maxwidth
    progressbar_minwidth = args.progressbar_minwidth
    if progressbar_maxwidth <= 0:
        logerr("progressbar-maxwidth must be > 0")
    if progressbar_minwidth <= 0:
        logerr("progressbar-minwidth must be > 0")
    shell_workdir = ""
    rstcolor = ANSI_RESET_ALL if colorful else ""
    DIR_COLOR   = ANSI_COLOR_GREEN
    FILE_COLOR  = ""
    LINK_COLOR  = ANSI_COLOR_BLUE
    CHAR_COLOR  = ANSI_COLOR_YELLOW
    BLOCK_COLOR = ANSI_COLOR_LIGHT_BLACK
    FIFO_COLOR  = ANSI_COLOR_PURPLE
    SOCK_COLOR  = ANSI_COLOR_CYAN
    UNKNOWN_COLOR = ANSI_COLOR_RED
    TYPE_COLOR = ANSI_COLOR_GREEN
    dircolor = DIR_COLOR if colorful else ""
    filecolor = FILE_COLOR if colorful else ""
    linkcolor = LINK_COLOR if colorful else ""
    charcolor = CHAR_COLOR if colorful else ""
    blockcolor = BLOCK_COLOR if colorful else ""
    fifocolor = FIFO_COLOR if colorful else ""
    sockcolor = SOCK_COLOR if colorful else ""
    unknowncolor = UNKNOWN_COLOR if colorful else ""
    typecolor = TYPE_COLOR if colorful else ""
    LOADED_COLOR = ANSI_COLOR_LIGHT_RED
    WLLOAD_COLOR = ANSI_COLOR_LIGHT_BLACK
    FINISH_COLOR = ANSI_COLOR_LIGHT_GREEN
    TINFO_COLOR = ANSI_COLOR_GREEN
    SPEED_COLOR = ANSI_COLOR_RED
    ETA_COLOR = ANSI_COLOR_LIGHT_BLUE
    loaded_color = LOADED_COLOR if colorful else ""
    wlload_color = WLLOAD_COLOR if colorful else ""
    finish_color = FINISH_COLOR if colorful else ""
    tinfo_color = TINFO_COLOR if colorful else ""
    speed_color = SPEED_COLOR if colorful else ""
    eta_color = ETA_COLOR if colorful else ""
    LINENUM_COLOR = ANSI_COLOR_LIGHT_BLACK
    linenum_color = LINENUM_COLOR if colorful else ""
    def progress_bar(total: int, cur: int, speed: int | float = 0) -> str:
        # color:
        #[" " max=4 min=1]["\u2501" max=$max_width min=1 rules=[finished:green, running:[loaded:lightred, other:gray]]] XX/XX XB XX.X XB/s eta XX:XX
        # example:    ---------------------------------------- 11.0/12.6 MB 27.1 KB/s eta 0:01:00
        ter_w, _ = get_term_size()
        if total == 0:
            prog = 100
        else:
            prog = int(cur / total * 100)
        eta = math.ceil((total - cur) / speed) if speed != 0 else 0
        if speed == 0:
            speeds = "?"
            etas = "--:--:--"
        else:
            etads = datetime.timedelta(seconds=eta).seconds
            etas = f"{int(etads/3600)}:{int(etads/60)%60:02}:{etads%60:02}"
            div_s, suffix_s = auto_suffix(speed, BASE_BI, SUFFIX_LIST_BI)
            speeds = f"{speed / div_s:.2f} {suffix_s}B/s"
        div_t, suffix_t = auto_suffix(total, BASE_BI, SUFFIX_LIST_BI)
        pstr         = f" {tinfo_color}{cur / div_t:.2f}/{total / div_t:.2f} {suffix_t}B{rstcolor} {speed_color}{speeds}{rstcolor} eta {eta_color}{etas}{rstcolor} "
        pstr_nocolor = f" {     ""    }{cur / div_t:.2f}/{total / div_t:.2f} {suffix_t}B{   ""   } {     ""    }{speeds}{   ""   } eta {    ""   }{etas}{   ""   } "
        tabs = "  "
        if colorful:
            pgslen_raw = ter_w - len(pstr_nocolor) - len(tabs)
        else:
            pgslen_raw = ter_w - len(pstr_nocolor) - len(tabs) - 2
        pgslen = min(max(pgslen_raw, progressbar_minwidth), progressbar_maxwidth)
        if colorful:
            if cur == total:
                pgss = f"{finish_color}{ANSI_CHAR_PGLINE * pgslen}{rstcolor}"
            else:
                pgss = f"{loaded_color}{ANSI_CHAR_PGLINE * int(pgslen * prog / 100)}{wlload_color}{ANSI_CHAR_PGLINE * int(math.ceil(pgslen * (100 - prog) / 100))}{rstcolor}"
        else:
            if cur == total:
                pgss = f"|{ANSI_CHAR_PGLINE * pgslen}|"
            else:
                pgss = f"|{ANSI_CHAR_PGLINE * int(pgslen * prog / 100)}{" " * int(math.ceil(pgslen * (100 - prog) / 100))}|"
        print(ANSI_CTRL_CLRLINE+tabs+pgss+pstr)
    def mpy_path_append(p0: str, p1: str):
        if p0[-1] == "/":
            return p0 + p1
        else:
            return p0 + "/" + p1
    last_cur = 0
    last_time = 0
    speed_ctl = []
    def progress_bar_callback(total: int, cur: int):
        global last_cur, last_time
        cur_time = time.perf_counter()
        speed = (cur - last_cur) / (cur_time - last_time)
        if cur != 0:
            speed_ctl.append(speed)
        progress_bar(total, cur, speed)
        last_cur = cur
        last_time = cur_time
    class HideCursor:
        def __init__(self, printline = True, clearctinfo = True):
            self.printline = printline
            self.clearctinfo = clearctinfo
        def __enter__(self):
            global last_cur, last_time, speed_ctl
            if self.printline: print()
            if self.clearctinfo:
                last_cur = 0
                last_time = 0
                speed_ctl = []
            print(ANSI_CTRL_HIDM, end="")
        def __exit__(self, exc_type, exc_value, traceback):
            print(ANSI_CTRL_SIDM, end="")
    def _subcmd_write_lfunc(s_args, dst, src):
        if not os.path.isfile(src):
            logerr(f"Source file not found: {src}", "")
            return
        if s_args.verbose: print("Checking destination file type")
        ov = False
        try:
            st = opt.stat(dst, verbose = s_args.verbose)
        except MpyFileOptError:
            # path not exists
            if s_args.verbose: print("Destination file not found, will create it")
        except:
            # error
            logerr(traceback.format_exc(), "")
            return
        else:
            # path exists
            if s_args.verbose: print("Destination file found, checking type")
            if stat.S_ISREG(st.st_mode):
                if s_args.verbose: print("Destination file is file, success")
                ov = True
            else:
                logerr(f"destination is not a file: {dst}", "")
                return
        if ov and s_args.warning:
            chk = inputcheck("Destination file exists, overwrite it?")
            if not chk:
                return
        if s_args.verbose: print("Writing file")
        fsize = os.path.getsize(src)
        def __callback_progressbar(total: int, cur: int):
            if not (s_args.quiet or s_args.verbose):
                progress_bar_callback(total, cur)
        start_time = time.perf_counter()
        try:
            with HideCursor():
                with open(src, "rb") as f:
                    opt.upload(dst, f, fsize, __callback_progressbar, s_args.blocksize, verbose = s_args.verbose)
        except BaseException:
            logerr(traceback.format_exc(), "")
            return
        drtime = time.perf_counter() - start_time
        # avspeed = fsize / drtime
        if not (s_args.noreport or s_args.quiet):
            try:
                avspeed = sum(speed_ctl) / len(speed_ctl)
            except ZeroDivisionError:
                avspeed = 0
            div_a, suf_a = auto_suffix(avspeed, BASE_BI, SUFFIX_LIST_BI)
            print(f"Wrote in {drtime:.2f} seconds, average speed: {avspeed / div_a:.2f} {suf_a}B/s")
    def _subcmd_read_lfunc(s_args, dst: str | BytesIO, src, enable_report = True):
        custom_io = False
        if isinstance(dst, str):
            # path-string, else custom IO
            if os.path.exists(dst):
                if os.path.isfile(dst):
                    if s_args.warning:
                        chk = inputcheck("Destination file exists, overwrite it?")
                        if not chk:
                            return 1
                else:
                    logerr(f"destination isn't a file: {dst}", "")
                    return 1
        else:
            custom_io = True
        try:
            st = opt.stat(src, verbose = s_args.verbose)
        except MpyFileOptError:
            # path not exists
            logerr(f"Source file {src} not found")
            return 1
        except:
            # error
            logerr(traceback.format_exc(), "")
            return 1
        else:
            # path exists
            if s_args.verbose: print("Source file found, checking type")
            if not stat.S_ISREG(st.st_mode):
                logerr(f"Source is not a file: {src}", "")
                return 1
        if s_args.verbose: print("Reading file")
        def __callback_progressbar(total: int, cur: int):
            if not (s_args.quiet or s_args.verbose):
                progress_bar_callback(total, cur)
        start_time = time.perf_counter()
        try:
            with HideCursor():
                if custom_io:
                    opt.download(src, dst, __callback_progressbar, s_args.blocksize, verbose = s_args.verbose)
                else:
                    with open(dst, "wb") as f:
                        opt.download(src, f, __callback_progressbar, s_args.blocksize, verbose = s_args.verbose)
        except BaseException:
            logerr(traceback.format_exc(), "")
            return 1
        drtime = time.perf_counter() - start_time
        # avspeed = fsize / drtime
        if enable_report:
            if not (s_args.noreport or s_args.quiet):
                try:
                    avspeed = sum(speed_ctl) / len(speed_ctl)
                except ZeroDivisionError:
                    avspeed = 0
                div_a, suf_a = auto_suffix(avspeed, BASE_BI, SUFFIX_LIST_BI)
                print(f"Read in {drtime:.2f} seconds, average speed: {avspeed / div_a:.2f} {suf_a}B/s")

        
        if s_args.verbose: print("Reading file")
    def match_subcmd(subcmd_argv: list[str]):
        global shell_workdir, last_cur, last_time, speed_ctl
        subcmd = subcmd_argv[0]
        match subcmd:
            case "help":
                s_args = subcmd_parse_args(subcmd_help_parser, subcmd_argv)
                if not s_args: return
                def __subcmd_help_printsubcmdusg_lfunc(s_args, subcmd_name: str):
                    subcmd_parser: argparse.ArgumentParser = parser_dict[subcmd_name]
                    print(subcmd_parser.prog+":")
                    if s_args.usage:
                        print("    "+subcmd_parser.format_help().replace("\n", "\n    "))
                    else:
                        print("    "+subcmd_parser.description)
                if len(s_args.cmds) == 0:
                    cmds = all_commands
                else:
                    cmds = s_args.cmds
                for cmd in cmds:
                    if cmd in all_commands:
                        __subcmd_help_printsubcmdusg_lfunc(s_args, cmd)
                    else:
                        logerr(f"help: unknown subcommand: {cmd}", "")
            case "shell":
                s_args = subcmd_parse_args(subcmd_shell_parser, subcmd_argv)
                if not s_args: return
                try:
                    shell()
                except KeyboardInterrupt:
                    logerr("\nKeyboardInterrupt", "")
                except BaseException:
                    logerr(traceback.format_exc(), "")
                    pass
            case "ver":
                s_args = subcmd_parse_args(subcmd_ver_parser, subcmd_argv)
                if not s_args: return
                try:
                    srcver = opt.get_source_version(verbose = s_args.verbose)
                except BaseException:
                    logerr(traceback.format_exc(), "")
                    return
                if s_args.csv:
                    print(f"{__version__},{srcver[0]}.{srcver[1]}")
                else:
                    print(f"mpyfopt version: {__version__}")
                    print(f"   code version: {srcver[0]}.{srcver[1]}")
            case "uname":
                s_args = subcmd_parse_args(subcmd_uname_parser, subcmd_argv)
                if not s_args: return
                try:
                    uname = opt.uname(verbose = s_args.verbose)
                except BaseException:
                    logerr(traceback.format_exc(), "")
                    return
                if s_args.csv:
                    uname_infos = []
                    if s_args.kernel_name or s_args.all or not any([s_args.kernel_name, s_args.nodename, s_args.kernel_release, s_args.kernel_version, s_args.machine]):
                        uname_infos.append(uname[0])
                    if s_args.nodename or s_args.all:
                        uname_infos.append(uname[1])
                    if s_args.kernel_release or s_args.all:
                        uname_infos.append(uname[2])
                    if s_args.kernel_version or s_args.all:
                        uname_infos.append(uname[3])
                    if s_args.machine or s_args.all:
                        uname_infos.append(uname[4])
                    print(",".join(uname_infos))
                else:
                    if s_args.kernel_name or s_args.all or not any([s_args.kernel_name, s_args.nodename, s_args.kernel_release, s_args.kernel_version, s_args.machine]):
                        print("Kernel name:", uname[0])
                    if s_args.nodename or s_args.all:
                        print("Node name:", uname[1])
                    if s_args.kernel_release or s_args.all:
                        print("Kernel release:", uname[2])
                    if s_args.kernel_version or s_args.all:
                        print("Kernel version:", uname[3])
                    if s_args.machine or s_args.all:
                        print("Machine:", uname[4])
            case "uid":
                s_args = subcmd_parse_args(subcmd_uid_parser, subcmd_argv)
                if not s_args: return
                try:
                    uid = opt.get_uid(verbose = s_args.verbose)
                except BaseException:
                    logerr(traceback.format_exc(), "")
                    return
                uid_s = binascii.hexlify(uid).decode("ascii", "ignore")
                print(uid_s)
            case "freq":
                s_args = subcmd_parse_args(subcmd_freq_parser, subcmd_argv)
                if not s_args: return
                try:
                    freq = opt.get_freq(verbose = s_args.verbose)
                except BaseException:
                    logerr(traceback.format_exc(), "")
                    return
                if s_args.raw:
                    print(freq)
                else:
                    div, sif = auto_suffix(freq, BASE_SI, SUFFIX_LIST_SI)
                    print(f"{freq / div} {sif}Hz")
            case "pwd":
                s_args = subcmd_parse_args(subcmd_pwd_parser, subcmd_argv)
                if not s_args: return
                if s_args.local:
                    try:
                        path = os.getcwd()
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        return
                else:
                    try:
                        path = opt.getcwd()
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        return
                    shell_workdir = path
                print(path)
            case "cd":
                s_args = subcmd_parse_args(subcmd_cd_parser, subcmd_argv)
                if not s_args: return
                if s_args.local:
                    try:
                        os.chdir(s_args.dir)
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        return
                else:
                    try:
                        opt.chdir(s_args.dir)
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        return
                shell_workdir = opt.getcwd()
            case "ls":
                s_args = subcmd_parse_args(subcmd_ls_parser, subcmd_argv)
                ter_w, _ = get_term_size()
                if not s_args: return
                if s_args.sep < 0:
                    logerr("sep must be greater than 0", "")
                    return
                if s_args.sep_comma:
                    rowsep = ("," if s_args.sep > 0 else "") + (" " * max(s_args.sep - 1, 0))
                    q_quote = ","
                else:
                    rowsep = " " * s_args.sep
                    q_quote = ""
                if s_args.decimal_places > 0:
                    _round = round
                elif s_args.decimal_places == 0:
                    _round = lambda x, _: round(x)
                elif s_args.decimal_places == -1:
                    _round = lambda x, _: x
                else:
                    logerr("decimal places must be greater than or equal to -1", "")
                    return
                if s_args.json:
                    if s_args.recursive:
                        json_data = {}
                    else:
                        json_data = []
                def __subcmd_ls_lfunc(s_args, path: str):
                    if s_args.recursive:
                        path_p = path
                        path_p = _repr(path_p) if s_args.quote else path_p
                        if s_args.slash:
                            path_p += "/"
                        if s_args.json:
                            json_data[path_p] = []
                        else:
                            print(f"{dircolor}{path_p}{rstcolor}:")
                    try:
                        dlist = opt.ilistdir(path, verbose = s_args.verbose)
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        return
                    maxi_dlist = len(dlist) - 1
                    colorlist = []
                    itemslist = []
                    itemsstat: list[stat_result] = []
                    itemstotal = 0
                    authority = "????????? "
                    namemax_nlink = 0
                    namemax_uid = 0
                    namemax_gid = 0
                    itemssizelist = []
                    namemax_size = 0
                    itemstype: list[str] = []
                    dirlist = []
                    namemax = 0
                    for dr in dlist:
                        d = dr.name
                        if s_args.long or s_args.sort_size:
                            try:
                                st = opt.stat(mpy_path_append(path, d), verbose = s_args.verbose)
                            except BaseException:
                                logerr(traceback.format_exc(), "")
                                continue
                            itemsstat.append(st)
                            itemstotal += st.st_size
                            namemax_nlink = max(namemax_nlink, len(str(st.st_nlink)))
                            namemax_uid = max(namemax_uid, len(str(st.st_uid)))
                            namemax_gid = max(namemax_gid, len(str(st.st_gid)))
                            size_raw = st.st_size
                            if s_args.bi:
                                div, sif = auto_suffix(size_raw, 1024, SUFFIX_LIST_BI_MONO)
                            elif s_args.si:
                                div, sif = auto_suffix(size_raw, 1000, SUFFIX_LIST_SI_MONO)
                            else:
                                div, sif = 1, ""
                            size = _round(size_raw / div, s_args.decimal_places) if sif != "" else size_raw
                            itemssizelist.append((size, sif))
                            namemax_size = max(namemax_size, len(str(size)))

                        else:
                            itemsstat.append(None)
                            itemssizelist.append((0, ""))
                        if stat.S_ISDIR(dr.type):
                            icolor = DIR_COLOR
                            dirlist.append(d)
                            if s_args.slash:
                                d += "/"
                            itemstype.append("d")
                        elif stat.S_ISREG(dr.type):
                            icolor = FILE_COLOR
                            itemstype.append("-")
                        elif stat.S_ISLNK(dr.type):
                            icolor = LINK_COLOR
                            itemstype.append("l")
                        elif stat.S_ISCHR(dr.type):
                            icolor = CHAR_COLOR
                            itemstype.append("c")
                        elif stat.S_ISBLK(dr.type):
                            icolor = BLOCK_COLOR
                            itemstype.append("b")
                        elif stat.S_ISFIFO(dr.type):
                            icolor = FIFO_COLOR
                            itemstype.append("p")
                        elif stat.S_ISSOCK(dr.type):
                            icolor = SOCK_COLOR
                            itemstype.append("s")
                        else:
                            icolor = UNKNOWN_COLOR
                        icolors = icolor if colorful else ""
                        if s_args.quote:
                            d = f"{_repr(d)}"
                        itemslist.append(d)
                        colorlist.append(icolors)
                        namemax = max(namemax, len(d))
                    cw = 0
                    if s_args.sort_name:
                        sort_index = 0
                    elif s_args.sort_size:
                        sort_index = 3
                    else:
                        sort_index = None
                    if sort_index is not None:
                        itemslist, colorlist, itemstype, itemssizelist, itemsstat = zip(*sorted(zip(itemslist, colorlist, itemstype, itemssizelist, itemsstat), key = lambda x: x[sort_index], reverse = s_args.reverse))
                    for i, (d, icolor, type, isize, istat) in enumerate(zip(itemslist, colorlist, itemstype, itemssizelist, itemsstat)):
                        if s_args.long:

                            nlink = istat.st_nlink if istat.st_nlink>0 else "/"
                            uid = istat.st_uid if istat.st_uid>0 else "/"
                            gid = istat.st_gid if istat.st_gid>0 else "/"
                            mtime = istat.st_mtime
                            if mtime > 0:
                                dtm = datetime.datetime.fromtimestamp(istat.st_mtime).strftime("%b %d %H:%M:%S")
                            else:
                                #     "Jan 01 08:00:00"
                                dtm = "/              "

                            listr = f"{type}{authority} {nlink:<{namemax_nlink}} {uid:<{namemax_uid}} {gid:<{namemax_gid}} {isize[0]:>{namemax_size}}{isize[1]} {dtm}  {icolor}{d}{rstcolor}"
                            if s_args.json:
                                #print(f"    {{\"name\":{_repr(d)}, \"uid\":{_repr(uid)}, \"gid\":{_repr(gid)}}}", end="")
                                if s_args.recursive:
                                    json_data[path_p].append({"name":d, "uid":uid, "gid":gid})
                                else:
                                    json_data.append({"name":d, "uid":uid, "gid":gid})
                            else:
                                if s_args.row:
                                    print(listr, end=rowsep if i != maxi_dlist else "")
                                else:
                                    print(listr + (q_quote if i != maxi_dlist else ""))
                        else:
                            if s_args.json:
                                #print(f"    {_repr(d)}", end="")
                                if s_args.recursive:
                                    json_data[path_p].append(d)
                                else:
                                    json_data.append(d)
                            else:
                                if s_args.column:
                                    print(f"{icolor}{d}{rstcolor}{(q_quote if i != maxi_dlist else "")}")
                                elif s_args.row:
                                    print(f"{icolor}{d}{rstcolor}", end=rowsep if i != maxi_dlist else "")
                                else:
                                    print(f"{icolor}{(d + (q_quote if i != maxi_dlist else "")):<{namemax + s_args.sep}}{rstcolor}", end="")
                                    cw += namemax + s_args.sep
                                    if cw >= (ter_w - namemax):
                                        print()
                                        cw = 0
                    if not any([s_args.column,  s_args.json]):
                        print()
                    if s_args.recursive:
                        if not s_args.json: print()
                        for d in dirlist:
                            __subcmd_ls_lfunc(s_args, mpy_path_append(path, d))
                __subcmd_ls_lfunc(s_args, s_args.dir)
                if s_args.json:
                    print(json.dumps(json_data))
            case "tree":
                s_args = subcmd_parse_args(subcmd_tree_parser, subcmd_argv)
                ter_w, _ = get_term_size()
                if not s_args: return
                if s_args.hline_len < 0:
                    logerr("hline-len must be >= 0", "")
                    return
                if s_args.level <= 0 and s_args.level != -1:
                    logerr("level must be > 0", "")
                    return
                def __subcmd_tree_lfunc(s_args, path: str, _depthinfo: list[bool], _countinfo: list[int]):
                    try:
                        dlist = opt.ilistdir(path, verbose = s_args.verbose)
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        return
                    if len(_depthinfo) == 0:
                        _countinfo[0] += 1
                    maxi_dlist = len(dlist) - 1
                    dpstr = ""
                    dpstr_tab = "    "
                    for dp in _depthinfo:
                        dpstr += (ANSI_CHAR_VLINE if dp else " ") + " " * s_args.hline_len + " "
                        dpstr_tab += "  "
                    for i, dr in enumerate(dlist):
                        d = dr.name
                        if s_args.quote:
                            d = _repr(d)
                        if stat.S_ISDIR(dr.type):
                            icolor = DIR_COLOR
                            types = "directory"
                            _countinfo[0] += 1
                            if s_args.slash:
                                d += "/"
                        elif stat.S_ISREG(dr.type):
                            icolor = FILE_COLOR
                            types = "file"
                            _countinfo[1] += 1
                        elif stat.S_ISLNK(dr.type):
                            icolor = LINK_COLOR
                            types = "link"
                            _countinfo[1] += 1
                        elif stat.S_ISCHR(dr.type):
                            icolor = CHAR_COLOR
                            types = "character"
                            _countinfo[1] += 1
                        elif stat.S_ISBLK(dr.type):
                            icolor = BLOCK_COLOR
                            types = "block"
                            _countinfo[1] += 1
                        elif stat.S_ISFIFO(dr.type):
                            icolor = FIFO_COLOR
                            types = "fifo"
                            _countinfo[1] += 1
                        elif stat.S_ISSOCK(dr.type):
                            icolor = SOCK_COLOR
                            types = "socket"
                            _countinfo[1] += 1
                        else:
                            icolor = UNKNOWN_COLOR
                            _countinfo[2] += 1
                        icolors = icolor if colorful else ""
                        not_limit = s_args.level == -1 or len(_depthinfo) + 1 < s_args.level
                        canls = dr.type == stat.S_IFDIR and not_limit
                        comma = "," if i != maxi_dlist else ""
                        if s_args.json:
                            print(f"{dpstr_tab}{{\"type\":\"{types}\",\"name\":\"{repr(d)[1:-1]}\"{",\"contents\":[" if canls else ("}"+comma)}")
                        elif s_args.xml:
                            print(f"{dpstr_tab}<{types} name=\"{repr(d)[1:-1]}\">{"" if canls else f"</{types}>"}")
                        else:
                            print(f"{dpstr}{ANSI_CHAR_TNODE if i != maxi_dlist else ANSI_CHAR_TEND}{ANSI_CHAR_HLINE * s_args.hline_len} {icolors}{d}{rstcolor}")

                        if canls:
                            __subcmd_tree_lfunc(s_args, mpy_path_append(path, dr.name), _depthinfo + [i != maxi_dlist], _countinfo)
                            if s_args.json:
                                print(f"{dpstr_tab}]}}{comma}")
                            if s_args.xml:
                                print(f"{dpstr_tab}</directory>")
                countinfo = [0, 0, 0]
                if s_args.json:
                    print("[")
                elif s_args.xml:
                    print(f"<?xml version=\"1.0\" encoding=\"{encoding}\"?>\n<tree>")
                maxdiri = len(s_args.dir) - 1
                for i,d in enumerate(s_args.dir):
                    dn = d
                    if s_args.slash:
                        dn += "/"
                    if s_args.quote:
                        dn = _repr(dn)
                    if s_args.json:
                        print(f"  {{\"type\":\"directory\",\"name\":\"{repr(dn)[1:-1]}\",\"contents\":[")
                    elif s_args.xml:
                        print(f"  <directory name=\"{repr(dn)[1:-1]}\">")
                    else:
                        print(f"{dircolor}{dn}{rstcolor}")
                    try:
                        __subcmd_tree_lfunc(s_args, d, [], countinfo)
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        continue
                    if s_args.json:
                        print(f"  ]}}{"" if i == maxdiri else ","}")
                    elif s_args.xml:
                        print(f"  </directory>")
                if not s_args.noreport:
                    showunknown = countinfo[2] > 0
                    if s_args.json:
                        print(f",\n  {{\"type\":\"report\",\"directories\":{countinfo[0]},\"files\":{countinfo[1]},\"unknown\":{countinfo[2]}}}")
                    elif s_args.xml:
                        print(f"  <report>\n    <directories>{countinfo[0]}</directories>\n    <files>{countinfo[1]}</files>\n    <unknown>{countinfo[2]}</unknown>\n  </report>")
                    else:
                        print(f"{countinfo[0]} directories, {countinfo[1]} files", end = "")
                        if showunknown: print(f", {countinfo[2]} unknown", end = "")
                        print()
                if s_args.json:
                    print("]")
                elif s_args.xml:
                    print("</tree>")
            case "write":
                s_args = subcmd_parse_args(subcmd_write_parser, subcmd_argv)
                if not s_args: return
                if s_args.blocksize <= 0:
                    logerr("block-size must be > 0", "")
                    return
                _subcmd_write_lfunc(s_args, s_args.dst, s_args.src)
            case "push":
                s_args = subcmd_parse_args(subcmd_push_parser, subcmd_argv)
                if not s_args: return
                if s_args.blocksize <= 0:
                    logerr("block-size must be > 0", "")
                    return
                def __subcmd_push_lfunc(s_args, dst: str, src: list[str], _countinfo: list[int]):
                    for s in src:
                        s_stat = os.stat(s)
                        if stat.S_ISREG(s_stat.st_mode):
                            _countinfo[1] += 1
                            fp = mpy_path_append(dst, os.path.basename(s))
                            print("Write file:", fp)
                            _subcmd_write_lfunc(s_args, fp, s)
                        elif stat.S_ISDIR(s_stat.st_mode):
                            _countinfo[0] += 1
                            try:
                                dp = mpy_path_append(dst, os.path.basename(s))
                                print("Create directory:", dp)
                                opt.mkdir(dp, verbose = s_args.verbose)
                            except BaseException:
                                logerr(traceback.format_exc(), "")
                            if s_args.no_recursive:
                                continue
                            try:
                                dlist = os.listdir(s)
                            except BaseException:
                                logerr(traceback.format_exc(), "")
                                continue
                            __subcmd_push_lfunc(s_args, dp, [os.path.join(s, d) for d in dlist], _countinfo)
                        else:
                            _countinfo[2] += 1
                            logerr(f"unknown item type: {s}", "")
                countinfo = [0, 0, 0]
                __subcmd_push_lfunc(s_args, s_args.dst, s_args.src, countinfo)
                if not s_args.noreport:
                    showunknown = countinfo[2] > 0
                    print(f"Total report: Wrote {countinfo[0]} directories, {countinfo[1]} files", end = "")
                    if showunknown: print(f", {countinfo[2]} unknown", end = "")
                    print()
            case "read":
                s_args = subcmd_parse_args(subcmd_read_parser, subcmd_argv)
                if not s_args: return
                if s_args.blocksize <= 0:
                    logerr("block-size must be > 0", "")
                    return
                _subcmd_read_lfunc(s_args, s_args.dst, s_args.src)
            case "cat":
                s_args = subcmd_parse_args(subcmd_cat_parser, subcmd_argv)
                if not s_args: return
                if s_args.blocksize <= 0:
                    logerr("block-size must be > 0", "")
                    return
                buf = BytesIO()
                for src in s_args.src:
                    ret = _subcmd_read_lfunc(s_args, buf, src, enable_report = False)
                    if ret:
                        return
                    print(ANSI_CTRL_CLRLINE, end="") 
                    if buf.getvalue()[-1] != 10: # ord("\n")==10
                        buf.write(b"\n")
                buf.seek(0)
                lastct = None
                show_n = s_args.number
                squeeze_blank = s_args.squeeze_blank
                linesct = buf.readlines()
                maxnumsl = len(str(len(linesct))) + 1
                for n, line in enumerate(linesct, 1):
                    if squeeze_blank and lastct == b"\n" and line == b"\n":
                        continue
                    if show_n:
                        sys.stdout.write(f"{linenum_color}{n:>{maxnumsl}}{rstcolor} ")
                    sys.stdout.buffer.write(line)
                    lastct = line
            case "pull":
                s_args = subcmd_parse_args(subcmd_pull_parser, subcmd_argv)
                if not s_args: return
                if s_args.blocksize <= 0:
                    logerr("block-size must be > 0", "")
                    return
                def __subcmd_pull_lfunc(s_args, dst: str, src: list[str], _countinfo: list[int]):
                    for s in src:
                        if s_args.verbose: print("Read item stat:", s)
                        try:
                            st = opt.stat(s, verbose = s_args.verbose)
                        except BaseException:
                            logerr(traceback.format_exc(), "")
                            continue
                        if stat.S_ISREG(st.st_mode):
                            fp = os.path.join(dst, os.path.basename(s))
                            print("Read file:", s)
                            _countinfo[1] += 1
                            _subcmd_read_lfunc(s_args, fp, s)
                        elif stat.S_ISDIR(st.st_mode):
                            if s_args.verbose: print("Read item listdir:", s)
                            _countinfo[0] += 1
                            try:
                                dp = os.path.join(dst, os.path.basename(s))
                                print("Create directory:", dp)
                                if os.path.normpath(dp.replace("\\", "/")) == os.path.normpath(dst.replace("\\", "/")):
                                    print("Warning: destination path is same as source path", "")
                                else:
                                    os.mkdir(dp)
                                if s_args.no_recursive:
                                    continue
                                dlist = opt.ilistdir(s, verbose = s_args.verbose)
                            except BaseException:
                                logerr(traceback.format_exc(), "")
                                continue
                            for d in dlist:
                                __subcmd_pull_lfunc(s_args, os.path.join(dst, os.path.basename(s)), [mpy_path_append(s, d.name)], _countinfo)
                        else:
                            _countinfo[2] += 1
                            logerr(f"unknown item type: {s}", "")
                countinfo = [0, 0, 0]
                if not os.path.exists(s_args.dst):
                    print(f"Warning: Destination path not exists: {s_args.dst}, will create it")
                    os.makedirs(s_args.dst)
                __subcmd_pull_lfunc(s_args, s_args.dst, s_args.src, countinfo)
                if not s_args.noreport:
                    showunknown = countinfo[2] > 0
                    print(f"Total report: Read {countinfo[0]} directories, {countinfo[1]} files", end = "")
                    if showunknown: print(f", {countinfo[2]} unknown", end = "")
                    print()
            case "rm":
                s_args = subcmd_parse_args(subcmd_rm_parser, subcmd_argv)
                if not s_args: return
                support_rmdir = s_args.dir or s_args.recursive
                if s_args.verbose: print("Checking item type")
                def __subcmd_rm_lfunc(s_args, path: str):
                    if s_args.print:
                        print("Removing:", path)
                    try:
                        st = opt.stat(path, verbose = s_args.verbose)
                    except MpyFileOptError:
                        logerr(f"Path not exists: {path}", "")
                        return
                    except BaseException:
                        logerr(traceback.format_exc(), "")
                        return
                    if stat.S_ISREG(st.st_mode):
                        if s_args.verbose: print("Remove file")
                        try:
                            opt.remove(path, verbose = s_args.verbose)
                        except BaseException:
                            logerr(traceback.format_exc(), "")
                    elif stat.S_ISDIR(st.st_mode):
                        if not support_rmdir:
                            logerr(f"Path is a directory: {path}", "")
                            return
                        if s_args.verbose: print("Remove directory")
                        try:
                            ls = opt.listdir(path, verbose = s_args.verbose)
                        except BaseException:
                            logerr(traceback.format_exc(), "")
                            return
                        if len(ls) != 0:
                            if not s_args.recursive:
                                logerr(f"Directory not empty: {path}", "")
                                return
                            if s_args.verbose: print("Remove directory recursively")
                            for l in ls:
                                __subcmd_rm_lfunc(s_args, mpy_path_append(path, l))
                        try:
                            opt.rmdir(path, verbose = s_args.verbose)
                        except BaseException:
                            logerr(traceback.format_exc(), "")
                    else:
                        logerr(f"Unknown item type: {path}", "")
                for p in s_args.paths:
                    __subcmd_rm_lfunc(s_args, p)
            case "rmdir":
               s_args = subcmd_parse_args(subcmd_rmdir_parser, subcmd_argv)
               if not s_args: return
               for d in s_args.dirs:
                    if s_args.verbose: print("Removing directory:", d)
                    try:
                        opt.rmdir(d, verbose = s_args.verbose)
                    except BaseException:
                        logerr(traceback.format_exc(), "")
            case "mkdir":
                s_args = subcmd_parse_args(subcmd_mkdir_parser, subcmd_argv)
                if not s_args: return
                for d in s_args.dirs:
                    if s_args.verbose: print("Creating directory:", d)
                    try:
                        opt.mkdir(d, verbose = s_args.verbose)
                    except BaseException:
                        logerr(traceback.format_exc(), "")
            case "mv":
                s_args = subcmd_parse_args(subcmd_mv_parser, subcmd_argv)
                if not s_args: return
                if s_args.verbose: print("Checking source path")
                try:
                    opt.stat(s_args.src, verbose = s_args.verbose)
                except MpyFileOptError:
                    logerr(f"Source path not exists: {s_args.src}", "")
                    return
                except BaseException:
                    logerr(traceback.format_exc(), "")
                    return
                if s_args.verbose: print("Checking destination path")
                try:
                    opt.stat(s_args.dst, verbose = s_args.verbose)
                except MpyFileOptError:
                    # path not exists, ok
                    pass
                except BaseException:
                    logerr(traceback.format_exc(), "")
                    return
                else:
                    logerr(f"Cannot overwrite {s_args.dst} with {s_args.src}")
                    return
                opt.rename(s_args.src, s_args.dst, verbose = s_args.verbose)
            case "gc":
                s_args = subcmd_parse_args(subcmd_gc_parser, subcmd_argv)
                if not s_args: return
                try:
                    info = opt.get_gc_info(s_args.collect, verbose = s_args.verbose)
                except BaseException:
                    logerr(traceback.format_exc(), "")
                used, free = info
                total = free + used
                if not s_args.raw:
                    div_t, suf_t = auto_suffix(total, BASE_BI, SUFFIX_LIST_BI)
                    div_f, suf_f = auto_suffix(free, BASE_BI, SUFFIX_LIST_BI)
                    div_u, suf_u = auto_suffix(used, BASE_BI, SUFFIX_LIST_BI)
                    total = round(total / div_t, 2)
                    free = round(free / div_f, 2)
                    used = round(used / div_u, 2)
                    total_c = f"{total:.2f}{suf_t}"
                    free_c = f"{free:.2f}{suf_f}"
                    used_c = f"{used:.2f}{suf_u}"
                else:
                    suf_t, suf_f, suf_u = "bytes", "bytes", "bytes"
                    total_c = total; free_c = free; used_c = used
                if s_args.csv:
                    print(f"{total_c},{free_c},{used_c}")
                else:
                    print(f"Total: {total} {suf_t}")
                    print(f" Free: {free} {suf_f}")
                    print(f" Used: {used} {suf_u}")
            case "stat":
                s_args = subcmd_parse_args(subcmd_stat_parser, subcmd_argv)
                if not s_args: return
                for p in s_args.paths:
                    if s_args.verbose: print("Getting stat:", p)
                    if s_args.file_system:
                        try:
                            st = opt.statvfs(p, verbose = s_args.verbose)
                        except BaseException:
                            logerr(traceback.format_exc(), "")
                            continue
                        print(f"  File: {p}")
                        print(f"    ID: /    Namelen: {st.f_namemax:<10}  Flag: {st.f_flag if st.f_flag>0 else "/"}")
                        print(f"Block size: {st.f_bsize:<10}  Fundamental block size: {st.f_frsize}")
                        print(f"Blocks: {st.f_blocks:<10}  Free: {st.f_bfree:<10}  Available: {st.f_bavail}")
                        print(f" Files: {st.f_files if st.f_files>0 else '/':<10}  Free: {st.f_ffree if st.f_files>0 else '/':<10}  Available: {st.f_favail if st.f_files>0 else '/'}")
                    else:
                        try:
                            st = opt.stat(p, verbose = s_args.verbose)
                        except BaseException:
                            logerr(traceback.format_exc(), "")
                            continue
                        if stat.S_ISDIR(st.st_mode):
                            icolor = dircolor
                            itype = "d"
                            itypec = "directory"
                        elif stat.S_ISREG(st.st_mode):
                            icolor = filecolor
                            itype = "-"
                            itypec = "regular file"
                        elif stat.S_ISLNK(st.st_mode):
                            icolor = linkcolor
                            itype = "l"
                            itypec = "symbolic link"
                        elif stat.S_ISCHR(st.st_mode):
                            icolor = charcolor
                            itype = "c"
                            itypec = "character device"
                        elif stat.S_ISBLK(st.st_mode):
                            icolor = blockcolor
                            itype = "b"
                            itypec = "block device"
                        elif stat.S_ISFIFO(st.st_mode):
                            icolor = fifocolor
                            itype = "p"
                            itypec = "FIFO"
                        elif stat.S_ISSOCK(st.st_mode):
                            icolor = sockcolor
                            itype = "s"
                            itypec = "socket"
                        else:
                            icolor = unknowncolor
                            itype = "u"
                            itypec = "unknown"
                        print(f"  File: {icolor}{p}{rstcolor}")
                        print(f"  Size: {st.st_size}    {itypec}")
                        print(f"Device: {"/" if st.st_dev<=0 else st.st_dev}  Inode: {"/" if st.st_ino<=0 else st.st_ino}     Links: {"/" if st.st_nlink<=0 else st.st_nlink}")
                        stostr = get_last_four_octal_digits(st.st_mode)
                        print(f"Access: ({stostr if stostr!="0000" else "-"}/{itype}????????? )  Uid: {"/" if st.st_uid<=0 else st.st_uid}  Gid: {"/" if st.st_gid<=0 else st.st_gid}")
                        atime = datetime.datetime.fromtimestamp(st.st_atime).strftime("%Y-%m-%d %H:%M:%S.%f")
                        mtime = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S.%f")
                        ctime = datetime.datetime.fromtimestamp(st.st_ctime).strftime("%Y-%m-%d %H:%M:%S.%f")
                        print(f"Access: {atime if st.st_atime>0 else "/"}")
                        print(f"Modify: {mtime if st.st_mtime>0 else "/"}")
                        print(f"Change: {ctime if st.st_ctime>0 else "/"}")
            case _:
                logerr(f"unknown subcommand: {subcmd}", "")
    def shell():
        global shell_workdir
        shell_workdir = opt.getcwd()
        while True:
            line = ""
            while True:
                if line == "":
                    line += input(f"{DIR_COLOR if colorful else ""}{shell_workdir}{ANSI_RESET_ALL if colorful else ""} > ")
                else:
                    line += input("> ")
                try:
                    args = shlex.split(line)
                except ValueError:
                    pass
                else:
                    break
            if len(args) == 0:
                continue
            if args[0] == "exit":
                if len(args) > 1:
                    subcmd_parse_args(subcmd_shell_exit_parser, args)
                    continue
                else:
                    break
            elif args[0] == "echo":
                try:
                    print(" ".join(args[1:]))
                except IndexError:
                    print("")
                continue
            match_subcmd(args)
    if args.subcmd_help != "":
        if args.subcmd_help == "*":
            match_subcmd(["help"])
        else:
            match_subcmd(["help", args.subcmd_help[1:], "--usage"])
        exit()
    if args.port == "":
        logerr("port is not specified")
        exit(1)
    try:
        opt = MpyFileOpt(
            args.port,
            baudrate = args.baudrate,
            parity = args.parity,
            stopbits = args.stopbits,
            timeout            = None if args.timeout            == 0.0 else args.timeout,
            write_timeout      = None if args.write_timeout      == 0.0 else args.write_timeout,
            inter_byte_timeout = None if args.inter_byte_timeout == 0.0 else args.inter_byte_timeout,
            wait_timeout       = None if args.wait_timeout       == 0.0 else args.wait_timeout,

            verbose = args.verbose,
        )
    except BaseException:
        logerr(traceback.format_exc(), "")
        exit(1)
    for subcmd_argv in subcmd_argv_list:
        match_subcmd(subcmd_argv)

    opt.close(verbose=args.verbose)

if __name__ == "__main__":
    main()