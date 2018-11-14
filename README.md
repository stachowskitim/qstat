
qstat.py is a simple program for calculating the integrated intensity and the average intensity as a function of q for a radially integrated SAXS curve. This program is particularly useful when one is interested in comparing many curves, and is functional with the ASCII files printed at most beamlines. 

To calculate integrated intensity, define `a` with the lines of the file that represent qmin and qmax:
```
qstat.py -a 4 700
```
Similarly, to calculate average intensity across a region of q, define `b` with the lines of the file that represent qmin and qmax:
```
qstat.py -b 25 30 
```
