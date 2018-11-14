
qstat.py is a simple program for both calculating the integrated intensity or average intensity as a function of q for radially integrated SAXS curves. This program is particularly useful when one is interested in doing so for many curves, and is functional with the ASCII files printed at most beamlines. 

To calculate integrated intensity, define `a` with the lines of the file that represent qmin and qmax:
```
qstat.py -a 4 700
```
Similarly, to calculate average intensity, define `b` with the lines of the file that represent qmin and qmax:
```
qstat.py -b 25 30 
```
