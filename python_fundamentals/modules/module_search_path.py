import sys

# first look up> built in modules
# print(sys.builtin_module_names)
# ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_opcode', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha2', '_sha3', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'zlib')

# print(sys.path)
# ['/home/ricardo/PythonBasics/modules', '/usr/lib/python312.zip', '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload', '/home/ricardo/PythonBasics/venv/lib/python3.12/site-packages']

import site

print(site)
