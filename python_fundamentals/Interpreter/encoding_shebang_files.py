#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# segunda linea siempre de primero a no ser que venga el
#'!/usr/bin/env python3'

'''
First Line
 UNIX “shebang” line
 https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts
 Makes the file executable as a shell script

 '# -*- coding: cp1252 -*-'
this line modify the code encoding
https://docs.python.org/3/library/codecs.html#module-codecs

The classes for handling python encoding and decoding are defined there.
as well as error handling
'German ß, ♬'.encode(encoding='ascii', errors='backslashreplace')
b'German \\xdf, \\u266c'
'German ß, ♬'.encode(encoding='ascii', errors='xmlcharrefreplace')
b'German &#223;, &#9836;'
Encodings> https://docs.python.org/3/library/codecs.html#standard-encodings

you can also add command 
that are added when starting interactive sessions 
similar to unix shells .profile

other configuration options in the link above
'''