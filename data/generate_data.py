#!/usr/bin/env python

#script to generate all the data for the GNU parallel exercises

import random
import os

def gen_data(start,end,dirname):
    machine='A'
    for filename in range(start,end):

        filenamestr="NENE%05d%s.txt" % (filename,machine)
        if machine == 'A':
            machine = 'B'
        else:
            machine = 'A'
        print("writing to ",filenamestr)
        f = open(dirname + "/" + filenamestr,"w")

        for _ in range(300):
            value = random.uniform(0,6.0)
            f.write(str(value)+"\n")

        f.close()


os.mkdir("north-pacific-gyre/2012-07-03")
os.mkdir("north-pacific-gyre/2012-07-04")
os.mkdir("north-pacific-gyre/2012-07-05")
os.mkdir("north-pacific-gyre/2012-07-06")

gen_data(0,1500,"north-pacific-gyre/2012-07-03")
gen_data(1500,3000,"north-pacific-gyre/2012-07-04")
gen_data(3000,4500,"north-pacific-gyre/2012-07-05")
gen_data(4500,6000,"north-pacific-gyre/2012-07-06")
