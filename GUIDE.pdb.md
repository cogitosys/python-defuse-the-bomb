
# Guide to defusing the bomb using PDB

If you just want a quick and dirty walkthrough, check the SPOILERS guide.
It's suggested to use only the debugger to practice, and not look at the code.

Run the script using pdb:

```
python -mpdb bomb.py
```

The single most important command for pdb is `help`. Use it.

## Controlling the program execution

The `n(ext)` command will resume execution until the beginning of the next line.

The `s(tep)` command will resume execution for the shortest time possible.

The `r(eturn)` command will resume execution until the current function returns.

The `c(ont(inue))` command will resume execution until it hits a breakpoint.

The `b(reak)` command will set a breakpoint for a given line, function, or condition.

The `l(ist)` command will print out the next line to be executed, and the lines around it.

The `w(here)` and `bt` commands will print the current backtrace, indicating the current frame.

The `u(p)` and `d(own)` commands move the current frame up and down the backtrace.

The `j(ump)` command will set the next line to be executed

## Viewing and changing the program state

The `p` command will print the result of some python expression executed in the current frame.

The `pp` command does the same, but pretty-prints it.

The `a(rgs)` command prints the arguments to the current frame.

The `exec` and `!` commands will execute a python statement in the current frame.
This can be used to change the value of a variable, for example.
