# times-table

A utility to print a nicely formatted n-by-n times-table for any base from two to sixty-two.

```
optional arguments:
  --base N, -b N  The base of the number system. Base must be in range [2, 62]. (default=10).
  --size N, -n N  The largest number in the table. Must be greater than 1. (default=13).
  --primes        only print out the multiplication table for prime numbers
  --limit MAX     Limit printing the table to numbers of length MAX-digits or less
```
## Installing `times-table`

```
    python3 -m pip install timesTable
```
If you already have `times-table` installed, upgrade to newer versions like this:

```
    python3 -m pip install timesTable --upgrade
```
It's recommended to install into a local `venv`, or if installing systemwide
as the super-user to make a `venv` in `/usr/local/venv`, and install it there.
For some helpful hints about how to do this see the 
[`addendum`](https://github.com/jrowellfx/lsseq?tab=readme-ov-file#addendum---more-on-installing-command-line-tools)
in the [`lsseq`](https://github.com/jrowellfx/lsseq) repo.

### Testing `times-table`

Running `times-table` on the command line should show you this.

```
$ times-table
  * |   2    3    4    5    6    7    8    9   10   11   12   13
----+-------------------------------------------------------------
  2 |   4*   6    8   10   12   14   16   18   20   22   24   26
  3 |   6    9*  12   15   18   21   24   27   30   33   36   39
  4 |   8   12   16*  20   24   28   32   36   40   44   48   52
  5 |  10   15   20   25*  30   35   40   45   50   55   60   65
  6 |  12   18   24   30   36*  42   48   54   60   66   72   78
  7 |  14   21   28   35   42   49*  56   63   70   77   84   91
  8 |  16   24   32   40   48   56   64*  72   80   88   96  104
  9 |  18   27   36   45   54   63   72   81*  90   99  108  117
 10 |  20   30   40   50   60   70   80   90  100* 110  120  130
 11 |  22   33   44   55   66   77   88   99  110  121* 132  143
 12 |  24   36   48   60   72   84   96  108  120  132  144* 156
 13 |  26   39   52   65   78   91  104  117  130  143  156  169*
```

Now you can play with the various options. Enjoy!
