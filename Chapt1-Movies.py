#=======================================
# Movielens examples from Python for Data Analysis

import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('ml-1m/users.dat',sep='::',header=None,names=unames)

rnames = ['user-id','movie_id','rating','timestamp']
ratings = pd.read_table('ml-1m/ratings.dat',sep="::",header=None,names=rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table('ml-1m/movies.dat',sep="::",header=None,names=mnames)

##Merge
## should go automatically and detect common column names, but not working
##  so i specified it, which seems to be causing problems
data = pd.merge(pd.merge(ratings,users,left_index="user_id",right_index="user_id",how="left"),movies,left_index="movie_id",right_index="movie_id",how="left")

##Look at column names
data.ix[0]

