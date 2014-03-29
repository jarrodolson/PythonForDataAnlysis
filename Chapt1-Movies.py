#=======================================
# Movielens examples from Python for Data Analysis

import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('ml-1m/users.dat',sep='::',header=None,names=unames)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('ml-1m/ratings.dat',sep="::",header=None,names=rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table('ml-1m/movies.dat',sep="::",header=None,names=mnames)

##Merge
## should go automatically and detect common column names, but not working
##  so i specified it, which seems to be causing problems
data = pd.merge(pd.merge(ratings,users),movies)
##data = pd.merge(pd.merge(ratings,
##                         users,
##                         left_index="user_id",
##                         right_index="user_id",how="left"),
##                movies,
##                left_index="movie_id",
##                right_index="movie_id",
##                how="left")

##Look at column names
data.ix[0]

##Loook at ratings by movie and gender
mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')
mean_ratings[:5]

##Find number of ratings per moview, regardless of gender
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]

##Find movies that have received >=250 reviews
active_titles = ratings_by_title.index[ratings_by_title>=250]
>>> active_titles

##Just use movies with >=250 reviews
mean_ratings = mean_ratings.ix[active_titles]
mean_ratings

##Find top female reviews
top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
top_female_ratings[:10]

########################
##Measuring disagreement

##Create variable
mean_ratings['diff'] = mean_ratings['M']-mean_ratings['F']

##See biggest difference (things women like more than men)
sorted_by_diff = mean_ratings.sort_index(by="diff")
sorted_by_diff[:15]

##Now see biggest difference in reverse order
sorted_by_diff[::-1][:15]

##Standard deviation of ratings, grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]
print(rating_std_by_title.order(ascending=False)[:10])
