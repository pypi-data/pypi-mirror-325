# About mod-table

`mod-table` prints the addition and multiplication tables for
the ring of integers modulo n, denoted
&#8484;/n&#8484; - and 
&#8484;/n&#8484; is a field if and only if n is prime.

## Installing `mod-table`

```
    python3 -m pip install modTable --upgrade
```
It's recommended to install into a local `venv`, or if installing systemwide
as the super-user to make a `venv` in `/usr/local/venv`, and install it there.
For some helpful hints about how to do this see the
[`addendum`](https://github.com/jrowellfx/lsseq?tab=readme-ov-file#addendum---more-on-installing-command-line-tools)
in the [`lsseq`](https://github.com/jrowellfx/lsseq) repo.

### Testing `mod-table`

Running `mod-table` on the command line should show you this.

```
$ mod-table 5
ℤ/5ℤ
 + |  0  1  2  3  4 
--------------------
 0 |  0  1  2  3  4 
 1 |  1  2  3  4  0 
 2 |  2  3  4  0  1 
 3 |  3  4  0  1  2 
 4 |  4  0  1  2  3 

 * |  0  1  2  3  4 
--------------------
 0 |  0  0  0  0  0 
 1 |  0  1  2  3  4 
 2 |  0  2  4  1  3 
 3 |  0  3  1  4  2 
 4 |  0  4  3  2  1 

$ mod-table 6
ℤ/6ℤ
 + |  0  1  2  3  4  5 
-----------------------
 0 |  0  1  2  3  4  5 
 1 |  1  2  3  4  5  0 
 2 |  2  3  4  5  0  1 
 3 |  3  4  5  0  1  2 
 4 |  4  5  0  1  2  3 
 5 |  5  0  1  2  3  4 

 * |  0  1  2  3  4  5 
-----------------------
 0 |  0  0  0  0  0  0 
 1 |  0  1  2  3  4  5 
 2 |  0  2  4  0  2  4 
 3 |  0  3  0  3  0  3 
 4 |  0  4  2  0  4  2 
 5 |  0  5  4  3  2  1 

```

See how ℤ/6ℤ can't be a field because 2, 3 and 4 don't have multiplicative inverses.
That is, there's no other number that when multiplied by 2, 3 or 4 gives 1.

But in ℤ/5ℤ all the non-zero numbers have multiplicative inverses, so it is a field!

Time to play - Enjoy!

