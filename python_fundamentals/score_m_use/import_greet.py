import greet

greet.greet("Ricardo")
# When running like this, doesn't matter if you put another name as a arg, it will not display

# When running this modulem a __pycache__ folder is created
"""
Understanding the pycache Folder in Python
1
The __pycache__ folder in Python is a directory where the interpreter stores compiled bytecode files (.pyc) for imported modules. This mechanism helps speed up the loading of Python modules by avoiding the need to recompile the source code every time the module is imported.

Purpose of the pycache Folder

When you run a Python script or import a module, the interpreter compiles the high-level Python source code into bytecode, an intermediate binary representation. This bytecode is stored in the __pycache__ folder, allowing the interpreter to skip the compilation step on subsequent runs, provided the source code hasn't changed
1
.
"""
