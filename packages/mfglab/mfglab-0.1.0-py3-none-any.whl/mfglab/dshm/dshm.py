from multiprocessing import shared_memory
import numpy as np

from mfglab.config.log import logger

class WriteMemory:
    def __init__(self, name: str, dtype: np.dtype , data: np.ndarray) -> None:
        '''
        dynamic shared memory write\n
        name is shared memory address\n
        dtype is numpy dtype\n
        data is numpy array
        '''
        assert isinstance(np.dtype(dtype), np.dtype), "dtype should be numpy dtype"
        assert isinstance(data, np.ndarray), "data should be list or numpy array"
        
        self.shm = None
        self.name = name
        self.dtype = dtype
        self.dtype_size = np.dtype(self.dtype).itemsize    # like np.int64().nbytes
        self.data = data
        self.arr_size = len(self.data)
    
    def write(self) -> None:
        self.shm = shared_memory.SharedMemory(name=self.name, create=True, size=self.arr_size * self.dtype_size)
        np_array = np.ndarray((self.arr_size,), dtype=self.dtype, buffer=self.shm.buf)
        np_array[:] = self.data
        logger.info(f"write shared memory: {self.name} (data array size: {self.arr_size})")
        
    def close(self) -> None:
        self.shm.close()
        self.shm.unlink()
        logger.info(f"unlink shared memory: {self.name}")


class ReadMemory:
    def __init__(self, name: str ,dtype: np.dtype , arr_size: int) -> None:
        '''
        dynamic shared memory read\n
        name is shared memory address\n
        dtype is numpy dtype\n
        size is data array size\n
        read function return numpy array
        '''
        assert isinstance(arr_size, int), "size should be integer"
        self.name = name
        self.dtype = dtype
        self.arr_size = arr_size
    
    def read(self) -> np.ndarray:
        shm = shared_memory.SharedMemory(name=self.name)
        np_array = np.ndarray((self.arr_size,), dtype=self.dtype, buffer=shm.buf)
        np_array = np.copy(np_array)    # copy to prevent shared memory delete at close shm
        shm.close()
        logger.info(f"read shared memory: {self.name}")

        return np_array
    