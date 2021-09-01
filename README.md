# auto-judge-for-cpp

>  This is an auto judge for `.cpp` source code files.

### Prerequisites

You’ll need:

1. The ability to build your own data generator with *Python*, in `data.py`;
2. A standard, or already-knew-it-is-correct, code to be `std.cpp`;
3. Your code to be tested, here is `test.cpp`.

------

### Using

When you finish building your data generator in `data.py`, and making sure everything is compilable and good, run:

```shell
bash judge.bash --times
```

> like ***bash judge.bash 50***

in your **Terminal**, where `times` is how many sets of data you want to test.

If an error’s been found, you’ll see:

```
---- DIFF FOUND! ----
***"THE CORRECT LINE"***
***"YOUR WRONG LINE"***

-> data:
"THE DATA THAT FOUND THIS ERROR"

-> std:
"THE EXPECTED FINAL ANSWER"

-> test:
"YOUR FINAL ANSWER"

---------------------
```

Otherwise, you’ve passed this data, and you’ll see:

```
----- ACCEPTED! -----
```

