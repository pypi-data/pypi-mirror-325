"""
Copyright (c) 2008-2021 synodriver <synodriver@gmail.com>
"""

import platform
import sys

from cffi import FFI

if sys.maxsize > 2**32:
    CPUBIT = 64
else:
    CPUBIT = 32

system = platform.system()
if system == "Windows":
    macro_base = [("_WIN64", None)]
elif system == "Linux":
    macro_base = [("__linux__", None)]
elif system == "Darwin":
    macro_base = [("__MAC_10_0", None)]
else:
    macro_base = []

if sys.byteorder != "little":
    macro_base.append(("WORDS_BIGENDIAN", None))

if CPUBIT == 64:
    macro_base.append(("CPUBIT64", None))
    macro_base.append(("IS_64BIT_PROCESSOR", None))
else:
    macro_base.append(("CPUBIT32", None))

ffibuilder = FFI()
ffibuilder.cdef(
    """
// base16384_err_t is the return value of base16384_en/decode_file
enum base16384_err_t {
	base16384_err_ok,
	base16384_err_get_file_size,
	base16384_err_fopen_output_file,
	base16384_err_fopen_input_file,
	base16384_err_write_file,
	base16384_err_open_input_file,
	base16384_err_map_input_file,
	base16384_err_read_file,
    base16384_err_invalid_file_name,
    base16384_err_invalid_commandline_parameter,
    base16384_err_invalid_decoding_checksum
};
// base16384_err_t is the return value of base16384_en/decode_file
typedef enum base16384_err_t base16384_err_t;
int base16384_encode_len(int dlen);
int base16384_decode_len(int dlen, int offset);
int base16384_encode(const char* data, int dlen, char* buf);
int base16384_decode(const char* data, int dlen, char* buf);
base16384_err_t base16384_encode_file(const char* input, const char* output, char* encbuf, char* decbuf);
base16384_err_t base16384_decode_file(const char* input, const char* output, char* encbuf, char* decbuf);

// base16384_encode_fp encodes input file to output file.
//    encbuf & decbuf must be no less than BASE16384_ENCBUFSZ & BASE16384_DECBUFSZ
base16384_err_t base16384_encode_fp(FILE* input, FILE* output, char* encbuf, char* decbuf);

// base16384_encode_fd encodes input fd to output fd.
//    encbuf & decbuf must be no less than BASE16384_ENCBUFSZ & BASE16384_DECBUFSZ
base16384_err_t base16384_encode_fd(int input, int output, char* encbuf, char* decbuf);

// base16384_decode_fp decodes input file to output file.
//    encbuf & decbuf must be no less than BASE16384_ENCBUFSZ & BASE16384_DECBUFSZ
base16384_err_t base16384_decode_fp(FILE* input, FILE* output, char* encbuf, char* decbuf);

// base16384_decode_fd decodes input fd to output fd.
//    encbuf & decbuf must be no less than BASE16384_ENCBUFSZ & BASE16384_DECBUFSZ
base16384_err_t base16384_decode_fd(int input, int output, char* encbuf, char* decbuf);

int base16384_encode_unsafe(const char * data, int dlen, char * buf);
int base16384_decode_unsafe(const char * data, int dlen, char * buf);
int base16384_encode_safe(const char * data, int dlen, char * buf);
int base16384_decode_safe(const char * data, int dlen, char * buf);

base16384_err_t base16384_encode_file_detailed(const char* input, const char* output, char* encbuf, char* decbuf, int flag);
base16384_err_t base16384_decode_file_detailed(const char* input, const char* output, char* encbuf, char* decbuf, int flag);
base16384_err_t base16384_encode_fd_detailed(int input, int output, char* encbuf, char* decbuf, int flag);
base16384_err_t base16384_decode_fd_detailed(int input, int output, char* encbuf, char* decbuf, int flag);
base16384_err_t base16384_encode_fp_detailed(FILE* input, FILE* output, char* encbuf, char* decbuf, int flag);
base16384_err_t base16384_decode_fp_detailed(FILE* input, FILE* output, char* encbuf, char* decbuf, int flag);

int32_t pybase16384_64bits();

int get_encsize();

int get_decsize();

int BASE16384_FLAG_NOHEADER_();

int BASE16384_FLAG_SUM_CHECK_ON_REMAIN_();

int BASE16384_FLAG_DO_SUM_CHECK_FORCELY_();

typedef ssize_t (*base16384_reader_t)(const void *client_data, void *buffer, size_t count);

/**
 * @brief custom writer function interface
 * @param client_data the data pointer defined by the client
 * @param buffer from where read data
 * @param count write bytes count
 * @return the size written
*/
typedef ssize_t (*base16384_writer_t)(const void *client_data, const void *buffer, size_t count);

union base16384_io_function_t {
	base16384_reader_t reader;
	base16384_writer_t writer;
};
typedef union base16384_io_function_t base16384_io_function_t;

struct base16384_stream_t {
	base16384_io_function_t f;
	void *client_data;
};
/**
 * @brief for stream encode/decode
*/
typedef struct base16384_stream_t base16384_stream_t;

base16384_err_t base16384_encode_stream_detailed(base16384_stream_t* input, base16384_stream_t*  output, char* encbuf, char* decbuf, int flag);
base16384_err_t base16384_decode_stream_detailed(base16384_stream_t* input, base16384_stream_t*  output, char* encbuf, char* decbuf, int flag);

extern "Python" ssize_t b14_readcallback(const void *client_data, void *buffer, size_t count);

extern "Python" ssize_t b14_writecallback(const void *client_data, const void *buffer, size_t count);
    """
)

source = """
#include "base16384.h"

#ifdef CPUBIT32
#define pybase16384_64bits() (0)
#else
#define pybase16384_64bits() (1)
#endif

int get_encsize()
{
    return BASE16384_ENCBUFSZ;
}

int get_decsize()
{
    return BASE16384_DECBUFSZ;
}

int BASE16384_FLAG_NOHEADER_()
{
    return BASE16384_FLAG_NOHEADER;
}

int BASE16384_FLAG_SUM_CHECK_ON_REMAIN_()
{
    return BASE16384_FLAG_SUM_CHECK_ON_REMAIN;
}

int BASE16384_FLAG_DO_SUM_CHECK_FORCELY_()
{
    return BASE16384_FLAG_DO_SUM_CHECK_FORCELY;
}
"""

ffibuilder.set_source(
    "pybase16384.backends.cffi._core",
    source,
    sources=[
        f"./base16384/base14{CPUBIT}.c",
        "./base16384/file.c",
        "./base16384/wrap.c",
    ],
    include_dirs=["./base16384"],
    define_macros=macro_base,
)

if __name__ == "__main__":
    ffibuilder.compile()
