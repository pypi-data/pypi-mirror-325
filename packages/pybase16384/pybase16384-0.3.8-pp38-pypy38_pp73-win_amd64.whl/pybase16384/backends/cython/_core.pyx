# cython: language_level=3
# cython: cdivision=True
from cpython.bytes cimport (PyBytes_AS_STRING, PyBytes_Check,
                            PyBytes_FromStringAndSize, PyBytes_GET_SIZE)
from cpython.mem cimport PyMem_Free, PyMem_Malloc
from cpython.object cimport PyObject, PyObject_HasAttrString
from libc.stdint cimport int32_t, uint8_t
from libc.string cimport memcpy

from pybase16384.backends.cython.base16384 cimport (
    BASE16384_DECBUFSZ, BASE16384_ENCBUFSZ,
    BASE16384_FLAG_DO_SUM_CHECK_FORCELY, BASE16384_FLAG_NOHEADER,
    BASE16384_FLAG_SUM_CHECK_ON_REMAIN, b14_decode, b14_decode_fd,
    b14_decode_fd_detailed, b14_decode_file, b14_decode_file_detailed,
    b14_decode_len, b14_decode_safe, b14_decode_stream,
    b14_decode_stream_detailed, b14_encode, b14_encode_fd,
    b14_encode_fd_detailed, b14_encode_file, b14_encode_file_detailed,
    b14_encode_len, b14_encode_safe, b14_encode_stream,
    b14_encode_stream_detailed, base16384_err_fopen_input_file,
    base16384_err_fopen_output_file, base16384_err_get_file_size,
    base16384_err_invalid_commandline_parameter,
    base16384_err_invalid_decoding_checksum, base16384_err_invalid_file_name,
    base16384_err_map_input_file, base16384_err_ok,
    base16384_err_open_input_file, base16384_err_read_file, base16384_err_t,
    base16384_err_write_file, base16384_io_function_t, base16384_stream_t,
    pybase16384_64bits)

from pathlib import Path

ENCBUFSZ = BASE16384_ENCBUFSZ
DECBUFSZ = BASE16384_DECBUFSZ
FLAG_NOHEADER = BASE16384_FLAG_NOHEADER
FLAG_SUM_CHECK_ON_REMAIN = BASE16384_FLAG_SUM_CHECK_ON_REMAIN
FLAG_DO_SUM_CHECK_FORCELY = BASE16384_FLAG_DO_SUM_CHECK_FORCELY

cdef inline bytes ensure_bytes(object inp):
    if isinstance(inp, unicode):
        return inp.encode()
    elif isinstance(inp, bytes):
        return inp
    elif isinstance(inp, Path):
        return str(inp).encode()
    else:
        return bytes(inp)

cdef inline uint8_t PyFile_Check(object file):
    if PyObject_HasAttrString(file, "read") and PyObject_HasAttrString(file, "write") and PyObject_HasAttrString(file,
                                                                                                                 "seek"):
        return 1
    return 0

cpdef inline int encode_len(int dlen) nogil:
    return b14_encode_len(dlen)

cpdef inline int decode_len(int dlen, int offset) nogil:
    return b14_decode_len(dlen, offset)

cpdef inline bytes _encode(const uint8_t[::1] data):
    cdef size_t length = data.shape[0]
    cdef size_t output_size = <size_t> b14_encode_len(<int>length) + 16
    cdef char *output_buf = <char*>PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError
    cdef int count
    with nogil:
        count = b14_encode(<const char*> &data[0],
                                        <int>length,
                                        output_buf) # encode 整数倍的那个
    try:
        return <bytes>output_buf[:count]
    finally:
        PyMem_Free(output_buf)

cpdef inline bytes _encode_safe(const uint8_t[::1] data):
    cdef size_t length = data.shape[0]
    cdef size_t output_size = <size_t> b14_encode_len(<int>length)
    cdef char *output_buf = <char*>PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError
    cdef int count
    with nogil:
        count = b14_encode_safe(<const char*> &data[0],
                                        <int>length,
                                        output_buf) # encode 整数倍的那个
    try:
        return <bytes>output_buf[:count]
    finally:
        PyMem_Free(output_buf)

cpdef inline bytes _decode(const uint8_t[::1] data):
    cdef size_t length = data.shape[0]
    cdef size_t output_size = <size_t> b14_decode_len(<int>length, 0) + 16
    cdef char *output_buf = <char *> PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError
    cdef int count
    with nogil:
        count = b14_decode(<const char *> &data[0],
                                        <int> length,
                                        output_buf)  # decode
    try:
        return <bytes> output_buf[:count]
    finally:
        PyMem_Free(output_buf)

cpdef inline bytes _decode_safe(const uint8_t[::1] data):
    cdef size_t length = data.shape[0]
    cdef size_t output_size = <size_t> b14_decode_len(<int>length, 0)
    cdef char *output_buf = <char *> PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError
    cdef int count
    with nogil:
        count = b14_decode_safe(<const char *> &data[0],
                                        <int> length,
                                        output_buf)  # decode
    try:
        return <bytes> output_buf[:count]
    finally:
        PyMem_Free(output_buf)

cpdef inline int _encode_into(const uint8_t[::1] data, uint8_t[::1] dest) except -1:
    cdef size_t input_size = data.shape[0]
    cdef size_t output_size = <size_t> b14_encode_len(<int> input_size)
    cdef size_t output_buf_size = dest.shape[0]
    if output_buf_size < output_size:
        raise ValueError("Buffer is too small to hold result")
    with nogil:
        return b14_encode(<const char *> &data[0],
                                <int> input_size,
                                <char *> &dest[0])

cpdef inline int _encode_into_safe(const uint8_t[::1] data, uint8_t[::1] dest) except -1:
    cdef size_t input_size = data.shape[0]
    cdef size_t output_size = <size_t> b14_encode_len(<int> input_size)
    cdef size_t output_buf_size = dest.shape[0]
    if output_buf_size < output_size:
        raise ValueError("Buffer is too small to hold result")
    with nogil:
        return b14_encode_safe(<const char *> &data[0],
                                <int> input_size,
                                <char *> &dest[0])

cpdef inline int _decode_into(const uint8_t[::1] data, uint8_t[::1] dest) except -1:
    cdef size_t input_size = data.shape[0]
    cdef size_t output_size = <size_t> b14_decode_len(<int> input_size, 0)
    cdef size_t output_buf_size = dest.shape[0]
    if output_buf_size < output_size:
        raise ValueError("Buffer is too small to hold result")
    with nogil:
        return b14_decode(<const char *> &data[0],
                                <int> input_size,
                                <char *> &dest[0])

cpdef inline int _decode_into_safe(const uint8_t[::1] data, uint8_t[::1] dest) except -1:
    cdef size_t input_size = data.shape[0]
    cdef size_t output_size = <size_t> b14_decode_len(<int> input_size, 0)
    cdef size_t output_buf_size = dest.shape[0]
    if output_buf_size < output_size:
        raise ValueError("Buffer is too small to hold result")
    with nogil:
        return b14_decode_safe(<const char *> &data[0],
                                <int> input_size,
                                <char *> &dest[0])

def encode_file(object input,
                       object output,
                       bint write_head = False,
                       int32_t buf_rate = 10):
    if not PyFile_Check(input):
        raise TypeError("input except a file-like object, got %s" % type(input).__name__)
    if not PyFile_Check(output):
        raise TypeError("output except a file-like object, got %s" % type(output).__name__)
    if buf_rate <= 0:
        buf_rate = 1

    if write_head:
        output.write(b'\xfe\xff')

    cdef int32_t current_buf_len = buf_rate * 7  # 一次读取这么多字节
    cdef size_t output_size = <size_t> b14_encode_len(<int> current_buf_len) + 16 # 因为encode_len不是单调的 这16备用
    cdef char *output_buf = <char *> PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError

    cdef Py_ssize_t size
    cdef uint8_t first_check = 1  # 检查一次就行了 怎么可能出现第一次读出来是bytes 以后又变卦了的对象呢 不会吧不会吧
    cdef int count = 0
    cdef const char *chunk_ptr
    try:
        while True:
            chunk = input.read(current_buf_len)
            if first_check:
                first_check = 0
                if not PyBytes_Check(chunk):
                    raise TypeError(f"input must be a file-like rb object, got {type(input).__name__}")
            size = PyBytes_GET_SIZE(chunk)
            if <int32_t> size < current_buf_len:  # 数据不够了 要减小一次读取的量
                if buf_rate > 1:  # 重新设置一次读取的大小 重新设置流的位置 当然要是已经是一次读取7字节了 那就不能再变小了 直接encode吧
                    buf_rate = buf_rate / 2
                    current_buf_len = buf_rate * 7
                    input.seek(-size, 1)
                    continue
            chunk_ptr = <const char*>PyBytes_AS_STRING(chunk)
            with nogil:
                count = b14_encode(chunk_ptr, <int>size, output_buf)
            output.write(<bytes>output_buf[:count])
            if size < 7:
                break
    finally:
        PyMem_Free(output_buf)

def encode_file_safe(object input,
                       object output,
                       bint write_head = False,
                       int32_t buf_rate = 10):
    if not PyFile_Check(input):
        raise TypeError("input except a file-like object, got %s" % type(input).__name__)
    if not PyFile_Check(output):
        raise TypeError("output except a file-like object, got %s" % type(output).__name__)
    if buf_rate <= 0:
        buf_rate = 1

    if write_head:
        output.write(b'\xfe\xff')

    cdef int32_t current_buf_len = buf_rate * 7  # 一次读取这么多字节
    cdef size_t output_size = <size_t> b14_encode_len(<int> current_buf_len) # 因为encode_len不是单调的 这16备用
    cdef char *output_buf = <char *> PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError

    cdef Py_ssize_t size
    cdef uint8_t first_check = 1  # 检查一次就行了 怎么可能出现第一次读出来是bytes 以后又变卦了的对象呢 不会吧不会吧
    cdef int count = 0
    cdef const char *chunk_ptr
    try:
        while True:
            chunk = input.read(current_buf_len)
            if first_check:
                first_check = 0
                if not PyBytes_Check(chunk):
                    raise TypeError(f"input must be a file-like rb object, got {type(input).__name__}")
            size = PyBytes_GET_SIZE(chunk)
            if <int32_t> size < current_buf_len:  # 数据不够了 要减小一次读取的量
                if buf_rate > 1:  # 重新设置一次读取的大小 重新设置流的位置 当然要是已经是一次读取7字节了 那就不能再变小了 直接encode吧
                    buf_rate = buf_rate / 2
                    current_buf_len = buf_rate * 7
                    input.seek(-size, 1)
                    continue
            chunk_ptr = <const char*>PyBytes_AS_STRING(chunk)
            with nogil:
                count = b14_encode_safe(chunk_ptr, <int>size, output_buf)
            output.write(<bytes>output_buf[:count])
            if size < 7:
                break
    finally:
        PyMem_Free(output_buf)

def decode_file(object input,
                       object output,
                       int32_t buf_rate = 10):
    if not PyFile_Check(input):
        raise TypeError("input except a file-like object, got %s" % type(input).__name__)
    if not PyFile_Check(output):
        raise TypeError("output except a file-like object, got %s" % type(output).__name__)
    if buf_rate <= 0:
        buf_rate = 1

    chunk = input.read(1)  # type: bytes
    if not PyBytes_Check(chunk):
        raise TypeError(f"input must be a file-like rb object, got {type(input).__name__}")
    if chunk == b"\xfe":  # 去头
        input.read(1)
    else:
        input.seek(0, 0)  # 没有头 回到开头

    cdef int32_t current_buf_len = buf_rate * 8
    cdef size_t output_size = <size_t> b14_decode_len(<int> current_buf_len, 0) + 16
    cdef char *output_buf = <char *> PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError
    cdef Py_ssize_t size
    cdef int count = 0
    cdef const char *chunk_ptr
    try:
        while True:
            chunk = input.read(current_buf_len)  # 8的倍数
            size = PyBytes_GET_SIZE(chunk)
            if size == 0:
                break
            if <int32_t> size < current_buf_len:  # 长度不够了
                if buf_rate > 1:  # 还能继续变小
                    buf_rate = buf_rate / 2  # 重新设置一次读取的大小
                    current_buf_len = buf_rate * 8
                    input.seek(-size, 1)
                    continue
            tmp = input.read(2)  # type: bytes
            if PyBytes_GET_SIZE(tmp) == 2:
                if tmp[0] == 61:  # = stream完了   一次解码8n+2个字节
                    chunk += tmp
                    size += 2
                else:
                    input.seek(-2, 1)
            chunk_ptr = <const char *> PyBytes_AS_STRING(chunk)
            with nogil:
                count = b14_decode(chunk_ptr, <int> size, output_buf)
            output.write(<bytes>output_buf[:count])
    finally:
        PyMem_Free(output_buf)

def decode_file_safe(object input,
                       object output,
                       int32_t buf_rate = 10):
    if not PyFile_Check(input):
        raise TypeError("input except a file-like object, got %s" % type(input).__name__)
    if not PyFile_Check(output):
        raise TypeError("output except a file-like object, got %s" % type(output).__name__)
    if buf_rate <= 0:
        buf_rate = 1

    chunk = input.read(1)  # type: bytes
    if not PyBytes_Check(chunk):
        raise TypeError(f"input must be a file-like rb object, got {type(input).__name__}")
    if chunk == b"\xfe":  # 去头
        input.read(1)
    else:
        input.seek(0, 0)  # 没有头 回到开头

    cdef int32_t current_buf_len = buf_rate * 8
    cdef size_t output_size = <size_t> b14_decode_len(<int> current_buf_len, 0)
    cdef char *output_buf = <char *> PyMem_Malloc(output_size)
    if output_buf == NULL:
        raise MemoryError
    cdef Py_ssize_t size
    cdef int count = 0
    cdef const char *chunk_ptr
    try:
        while True:
            chunk = input.read(current_buf_len)  # 8的倍数
            size = PyBytes_GET_SIZE(chunk)
            if size == 0:
                break
            if <int32_t> size < current_buf_len:  # 长度不够了
                if buf_rate > 1:  # 还能继续变小
                    buf_rate = buf_rate / 2  # 重新设置一次读取的大小
                    current_buf_len = buf_rate * 8
                    input.seek(-size, 1)
                    continue
            tmp = input.read(2)  # type: bytes
            if PyBytes_GET_SIZE(tmp) == 2:
                if tmp[0] == 61:  # = stream完了   一次解码8n+2个字节
                    chunk += tmp
                    size += 2
                else:
                    input.seek(-2, 1)
            chunk_ptr = <const char *> PyBytes_AS_STRING(chunk)
            with nogil:
                count = b14_decode_safe(chunk_ptr, <int> size, output_buf)
            output.write(<bytes>output_buf[:count])
    finally:
        PyMem_Free(output_buf)

cpdef inline bint is_64bits() nogil:
    return pybase16384_64bits()

cdef inline str err_to_str(base16384_err_t ret):
    if ret == base16384_err_get_file_size:
        return "base16384_err_get_file_size"
    elif ret == base16384_err_fopen_output_file:
        return "base16384_err_fopen_output_file"
    elif ret == base16384_err_fopen_input_file:
        return "base16384_err_fopen_input_file"
    elif ret == base16384_err_write_file:
        return "base16384_err_write_file"
    elif ret == base16384_err_open_input_file:
        return "base16384_err_open_input_file"
    elif ret == base16384_err_map_input_file:
        return "base16384_err_map_input_file"
    elif ret == base16384_err_read_file:
        return "base16384_err_read_file"
    elif ret == base16384_err_invalid_file_name:
        return "base16384_err_invalid_file_name"
    elif ret == base16384_err_invalid_commandline_parameter:
        return "base16384_err_invalid_commandline_parameter"
    elif ret == base16384_err_invalid_decoding_checksum:
        return "base16384_err_invalid_decoding_checksum"

cpdef inline encode_local_file(object inp, object out):
    cdef bytes inp_name = ensure_bytes(inp)
    cdef bytes out_name = ensure_bytes(out)
    cdef const char * inp_name_ptr = <const char *> inp_name
    cdef const char * out_name_ptr = <const char *> out_name
    cdef char * encbuf = <char*>PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char*>PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_encode_file(inp_name_ptr, out_name_ptr, encbuf, decbuf)
        if ret !=  base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

cpdef inline decode_local_file(object inp, object out):
    cdef bytes inp_name = ensure_bytes(inp)
    cdef bytes out_name = ensure_bytes(out)
    cdef const char * inp_name_ptr = <const char *> inp_name
    cdef const char * out_name_ptr = <const char *> out_name
    cdef char * encbuf = <char*>PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char*>PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_decode_file(inp_name_ptr, out_name_ptr, encbuf, decbuf)
        if ret !=  base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

cpdef inline encode_fd(int inp, int out):
    cdef char * encbuf = <char *> PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char *> PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_encode_fd(inp, out, encbuf, decbuf)
        if ret != base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

cpdef inline decode_fd(int inp, int out):
    cdef char * encbuf = <char *> PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char *> PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_decode_fd(inp, out, encbuf, decbuf)
        if ret != base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

# detailed
cpdef inline encode_local_file_detailed(object inp, object out, int flag):
    cdef bytes inp_name = ensure_bytes(inp)
    cdef bytes out_name = ensure_bytes(out)
    cdef const char * inp_name_ptr = <const char *> inp_name
    cdef const char * out_name_ptr = <const char *> out_name
    cdef char * encbuf = <char*>PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char*>PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_encode_file_detailed(inp_name_ptr, out_name_ptr, encbuf, decbuf, flag)
        if ret !=  base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

cpdef inline decode_local_file_detailed(object inp, object out, int flag):
    cdef bytes inp_name = ensure_bytes(inp)
    cdef bytes out_name = ensure_bytes(out)
    cdef const char * inp_name_ptr = <const char *> inp_name
    cdef const char * out_name_ptr = <const char *> out_name
    cdef char * encbuf = <char*>PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char*>PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_decode_file_detailed(inp_name_ptr, out_name_ptr, encbuf, decbuf, flag)
        if ret !=  base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

cpdef inline encode_fd_detailed(int inp, int out, int flag):
    cdef char * encbuf = <char *> PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char *> PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_encode_fd_detailed(inp, out, encbuf, decbuf, flag)
        if ret != base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

cpdef inline decode_fd_detailed(int inp, int out, int flag):
    cdef char * encbuf = <char *> PyMem_Malloc(<size_t>BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char *> PyMem_Malloc(<size_t>BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError
    cdef base16384_err_t ret
    try:
        with nogil:
            ret = b14_decode_fd_detailed(inp, out, encbuf, decbuf, flag)
        if ret != base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

# stream
cdef ssize_t b14_readcallback(const void *client_data, void *buffer, size_t count) except -100  with gil:
    cdef object file = <object>client_data
    cdef bytes data = file.read(count)
    cdef char* data_ptr = PyBytes_AS_STRING(data)
    cdef ssize_t data_size = <ssize_t>PyBytes_GET_SIZE(data)
    memcpy(buffer, data_ptr, <size_t>data_size)
    return data_size

cdef ssize_t b14_writecallback(const void *client_data, const void *buffer, size_t count) except -100 with gil:
    cdef object file = <object>client_data
    cdef bytes data = PyBytes_FromStringAndSize(<char*>buffer, <Py_ssize_t>count)
    cdef ssize_t ret = <ssize_t>file.write(data)
    return ret

cpdef inline encode_stream_detailed(object inp, object out, int flag):
    cdef char * encbuf = <char *> PyMem_Malloc(<size_t> BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char *> PyMem_Malloc(<size_t> BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError

    cdef base16384_err_t ret

    cdef base16384_stream_t inpstream = base16384_stream_t(f=base16384_io_function_t(reader=b14_readcallback),
                                                           client_data=<void *> inp)
    # inpstream.f.reader = b14_readcallback
    # inpstream.client_data = <const void*>inp

    cdef base16384_stream_t outstream = base16384_stream_t(f=base16384_io_function_t(writer=b14_writecallback),
                                                           client_data=<void *> out)
    # outstream.f.writer = b14_writecallback
    # outstream.client_data = <const void*>out
    try:
        with nogil:
            ret = b14_encode_stream_detailed(&inpstream, &outstream, encbuf, decbuf, flag)
        if ret != base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)

cpdef inline decode_stream_detailed(object inp, object out, int flag):
    cdef char * encbuf = <char *> PyMem_Malloc(<size_t> BASE16384_ENCBUFSZ)
    if encbuf == NULL:
        raise MemoryError
    cdef char * decbuf = <char *> PyMem_Malloc(<size_t> BASE16384_DECBUFSZ)
    if decbuf == NULL:
        PyMem_Free(encbuf)
        raise MemoryError

    cdef base16384_err_t ret

    cdef base16384_stream_t inpstream = base16384_stream_t(f=base16384_io_function_t(reader=b14_readcallback),client_data= <void*>inp)
    # inpstream.f.reader = b14_readcallback
    # inpstream.client_data = <const void*>inp

    cdef base16384_stream_t outstream = base16384_stream_t(f=base16384_io_function_t(writer=b14_writecallback),client_data= <void*>out)
    # outstream.f.writer = b14_writecallback
    # outstream.client_data = <const void*>out
    try:
        with nogil:
            ret = b14_decode_stream_detailed(&inpstream, &outstream, encbuf, decbuf, flag)
        if ret != base16384_err_ok:
            raise ValueError(err_to_str(ret))
    finally:
        PyMem_Free(encbuf)
        PyMem_Free(decbuf)
