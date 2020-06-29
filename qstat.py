#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:29:15 2018

@author: timothystachowski
"""

import os
import matplotlib.pyplot as plt
import re
import numpy as np
import csv
import argparse

CLI = argparse.ArgumentParser(prog='qstat', usage='%(prog)s [options]',
                              description='from saxs curves calculates total integrated'
                              'intensity or averaged intensity based on qmin and qmax'
                              ' More information available at github.com/stachowskitim')

CLI.add_argument(
    '-i',
    '--qintrange',
    nargs="+",
    type=float,
    help='integration over qmin and qmax'
)

CLI.add_argument(
    '-a',
    '--iqavg',
    nargs="+",
    type=float,
    help='average i(q) for qmin and qmax'
)

ARGS = CLI.parse_args()

A = np.array(ARGS.qintrange)
B = np.array(ARGS.iqavg)

def qint(qintrange):


	cwd = os.getcwd()

	for file in os.listdir(cwd):

		qie = []
		splitlist = []
		q = []
		i = []
		intint = []

		##filename = os.fsdecode(file)
		if file.endswith(".dat"):
			with open(file, 'r') as data:
				lines = data.readlines()
				for line in lines[int(qintrange[0]):int(qintrange[1])]:
					splitline = line.replace(" ",",")
					splitlist.append(splitline)
				csvform = csv.reader(splitlist)
				qie = list(csvform)
			
				for tuple in qie:
					fltq = float(tuple[0])
					flti = float(tuple[1])
					q.append(fltq)
					i.append(flti)
				
				qx = np.array(q)
				iy = np.array(i)
				area = np.trapz(iy, qx)
				print(area)

def intavg(iqavg):


	cwd = os.getcwd()

	for file in os.listdir(cwd):

		qie = []
		splitlist = []
		q = []
		i = []
		intint = []

		##filename = os.fsdecode(file)
		if file.endswith(".dat"):
			with open(file, 'r') as data:
				lines = data.readlines()
				for line in lines[int(iqavg[0]):int(iqavg[1])]:
					splitline = line.replace(" ",",")
					splitlist.append(splitline)
				csvform = csv.reader(splitlist)
				qie = list(csvform)
			
				for tuple in qie:
					fltq = float(tuple[0])
					flti = float(tuple[1])
					q.append(fltq)
					i.append(flti)
				
				ix = np.array(i)
				mean = np.mean(ix)
				print(mean)
		

if ARGS.qintrange is not None:
	qint(A)


if ARGS.iqavg is not None:
	intavg(B)

	
