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
