#!/usr/bin/env python

# 1. load a dataset from a file
# 2. "Organize" that file, so we can access columns *or* rows of it easily
# 3. compute some "summary statistics" about the dataset
# 4. print those summary statistics


# 1. load a dataset
# 1a. accept arbitrary filename as argument
# 1b. load the file

from argparse import ArgumentParser

parser = ArgumentParser(description=' A CSV reader + stats maker')
parser.add_argument('csvfile',
            help='Path to theinput csv file.')

parsed_args = parser.parse_args()

#print(parsed_args)
#print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

import os
import os.path as op
import pandas as pd

#assert os.path.isfile(my_csv_file), "bad filename"
assert op.isfile(my_csv_file), "bad filename"
print("hello")

# for housing.data use sep=s+
data = pd.read_csv(my_csv_file,sep='\s+|,',header=None)
print(data.head())
print (data.shape)

print(data.iloc[3:5,:])
print()
print(data.iloc[:3,-3:])

import numpy as np

print(np.mean(data))

