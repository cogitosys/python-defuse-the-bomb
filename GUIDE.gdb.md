
# Guide to defusing the bomb using GDB and python-dbg

If you just want a quick and dirty walkthrough, check the SPOILERS guide.
It's suggested to use only the debugger to practice, and not look at the code.

This guide has been tested on Ubuntu 16.04 using python2.7.

## Installing dependencies

### Ubuntu 16.04 and python 2.7:

```bash
sudo apt-get install -y python2.7-dbg gdb
```

The [gdb python helpers][gdb-python-helpers-2.7] are installed into the autoload path by the python2.7-dbg package, so everything should work out of the box.

There are some reports that this package provides symbols for regular python, and not only for python-dbg, but I've yet to confirm that.

[gdb-python-helpers-2.7]: https://github.com/python/cpython/blob/2.7/Tools/gdb/libpython.py

### Other systems

You'll need CPython, gdb, and debug symbols for CPython.
If your system has the gdb helpers installed to the wrong path, you can find them with:

```bash
find /usr -name 'python2.7-gdb.py'
```

And load them like this in gdb (with the path from the above):

```gdb
add-auto-load-safe-path /usr/share/gdb/auto-load/usr/bin/python2.7-gdb.py
```

## Debugging the script

```
python bomb.py
```

Then attach gdb to the process (will probably require sudo unless you've enabled permissive ptrace for your system)

```
gdb --pid $(pidof python)
```

Many of the gdb python helpers will only work when you're at a `PyEval_EvalFrameEx` frame.

## Controlling program execution

The helpers aren't great for controlling execution, but you can set breakpoints in 

The `py-up` and `py-down` commands move the current frame up and down the python backtrace.
There may be many non-python frames on the stack, these will skip over them.

## Viewing python state

The `py-bt` command will give a python traceback from the currently selected frame.
The `py-bt-full` command will show the python frames closer to the way gdb would normally show them.

The `py-locals` command will show you a listing of the local python variables.

The `py-print VARIABLE` command will print the repr of a variable from the current frame.

## Changing python state

### Changing a global variable

```
call PyDict_SetItemString(f->f_globals, "foo", PyLong_FromLong(0))
```

### Changing a local variable

TODO

### Controlling execution flow

TODO

## Additional material

* https://stripe.com/blog/exploring-python-using-gdb
* https://www.podoliaka.org/2016/04/10/debugging-cpython-gdb/
* https://fedoraproject.org/wiki/Features/EasierPythonDebugging
