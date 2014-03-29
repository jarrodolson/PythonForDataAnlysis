##Chapter 1 of Python for Data Analysis
## Baby Names

##Dta from: http://www.ssa.gov/oact/babynames/limits.html
import pandas as pd
from pylab import *
from optparse import OptionParser
import matplotlib.pyplot as plt

def add_prop(group):
    ##integer division floors
    births = group.births.astype(float)
    group['prop'] = births/births.sum()
    return(group)

def get_top1000(group):
    return(group.sort_index(by='births',ascending=False)[:1000])

def get_quantile_count(group,q=0.5):
    group = group.sort_index(by='prop',ascending=False)
    return(group.prop.cumsum().values.searchsorted(q)+1)

names1880 = pd.read_csv('names/yob1880.txt',names=['name','sex','births'])

print(names1880.groupby('sex').births.sum())

##Assemble all names into a single dataset
#2012 is the last year available right now
#Going to work through 2010 to match book
years = range(1880,2011)
pieces = []
columns = ['name','sex','births']

for year in years:
    path='names/yob%d.txt' % year
    frame = pd.read_csv(path,names=columns)

    frame['year']=year
    ##Saving iteration into a list of dataframes
    pieces.append(frame)
##Now we use pd.concat to put all of the list into a single dataframe
names = pd.concat(pieces,ignore_index=True)

##Look at data
total_births = names.pivot_table('births',rows='year',cols='sex',aggfunc=sum)
print(total_births.tail())
##Note - it is not the same number

##Visual
total_births.plot(title="Total births by sex and year")
show()

names = names.groupby(['year','sex']).apply(add_prop)

##Check that add_prop sums to 1
print(np.allclose(names.groupby(['year','sex']).prop.sum(),1))

##Get top 1000
grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
len(top1000)

##################################
##Analyze naming trends

boys = top1000[top1000.sex=='M']
girls = top1000[top1000.sex=='F']

total_births = top1000.pivot_table('births',rows='year',cols='name',aggfunc=sum)
subset = total_births[['Tom','Harry','Mary','Marilyn']]
subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of births per year")
show()

##Measuring the increase in naming diversity
## by looking at the top 1000 names as a proportion of the total names
table = top1000.pivot_table('prop',rows='year',cols='sex',aggfunc=sum)
table.plot(title='Sum of table1000.prop by year and sex',
           yticks=np.linspace(0,1.2,13),
           xticks=range(1880,2020,10))
show()

df = boys[boys.year == 2010]
prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
prop_cumsum[:10]
prop_cumsum.values.searchsorted(0.5)+1

df = boys[boys.year == 1900]
in1900 = df.sort_index(by='prop',ascending=False).prop.cumsum()
in1900.values.searchsorted(0.5)+1

diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

diversity.head()

diversity.plot(title='Number of popular names in top 50%')
show()

##The last letter revolution
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births',rows=last_letters,cols=['sex','year'],aggfunc=sum)

subtable = table.reindex(columns=[1910,1960,2010], level='year')
subtable.head()

subtable.sum()
letter_prop = subtable/subtable.sum().astype(float)

fig, axes = plt.subplots(2,1,figsize=(10,8))
letter_prop['M'].plot(kind='bar',rot=0,ax=axes[0],title='Male')
letter_prop['F'].plot(kind='bar',rot=0,ax=axes[1],title='Female',legend=False)
show()

letter_prop = table/table.sum().astype(float)
dny_ts = letter_prop.ix[['d','n','y'],'M'].T
dny_ts.head()

dny_ts.plot(title = "Proportion of names by letter over time")
show()

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
print(lesley_like)

filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()
table = filtered.pivot_table('births',rows='year',cols='sex',aggfunc='sum')
table = table.div(table.sum(1),axis=0)
table.tail()

table.plot(style={'M':'k-','F':'k--'},title="Male vs. Female for Name = Lesley")
show()
