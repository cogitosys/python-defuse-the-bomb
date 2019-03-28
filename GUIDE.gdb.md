
# Guide to defusing the bomb using GDB and python-dbg

If you just want a quick and dirty walkthrough, check the SPOILERS guide.
It's suggested to use only the debugger to practice, and not look at the code.

First, you'll need to install python-dbg on your system.
Run the script and attach gdb to it.

```
python-dbg bomb.py
```

```
gdb -P $(pidof python-dbg)
```

Once you've attached, you'll probably want to 

## Controlling program execution

TODO

## Viewing python state

TODO

## Changing python state

Changing a global's value:

```
call PyDict_SetItemString(globals, "i", PyLong_FromLong(0))
```

TODO
