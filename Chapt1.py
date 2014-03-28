#==================================
# Code from book: Python for data analysis
#==================================

import json
##load 'defaultdic' which initializes values to 0
from collections import defaultdict
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from pylab import *
from optparse import OptionParser

def get_counts2(sequence):
    ##This function uses default dict to initialize to 0 and then count
    counts = defaultdict(int)# values initialize to 0
    for x in sequence:
        ##Add to counter in dictionary
        counts[x]+=1
    return(counts)

def top_counts(count_dict, n=10):
    ##Gets top 10 counts by default, but takes a variable number
    ##uses dictionary comprehension, returns tuple with count and key (tz) into list
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return(value_key_pairs[-n:])

path = 'cho2/usagov_bitly_data2012-03-16-1331923249'
##list comprehension to load json dataset, equivalent to "for line...: json.loads(line)"
records = [json.loads(line) for line in open(path)]
##print(records[0]['tz'])

##list comprehension to get timezones, with if statement to skip missing data
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
##print(time_zones[:10])

counts = get_counts2(time_zones)
##print(top_counts(counts))
##Now we load as a dataframe
frame = DataFrame(records)
##Clean missing and unknown values
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()
##NOTE: To plot in script/idle, need to load to libraries:
## from pylab import *
## from optparse import OptionParser
tz_counts[:10].plot(kind='barh',rot=0)
show()
