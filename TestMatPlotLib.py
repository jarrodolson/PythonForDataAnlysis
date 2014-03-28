from pylab import *
from optparse import OptionParser
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

### make a square figure and axes
##figure(1, figsize=(6,6))
##ax = axes([0.1, 0.1, 0.8, 0.8])
##
##labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
##fracs = [15,30,45, 10]
##
##explode=(0, 0.05, 0, 0)
##pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
##title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
##
##show() # actually, don't show, just save to foo.png
    

#########################################3
####Plotting with raw matplotlib
##########################################
####Firt plot figure background
##fig = plt.figure()
####Then declare the subplots and axes
##ax = fig.add_subplot(1,1,1)
####Then draw plot
##ax.plot(randn(30).cumsum(),color='k',linestyle="dashed",marker="o",label="Manual")
##ax.plot(randn(30).cumsum(),color='r',linestyle="dashed",marker="x",label="Manual 2")
####Then draw the title
##ax.set_title("Testing")
####Then draw legend (uses "label")
##ax.legend(loc="best")
####Then show
####show()
####Then save
##plt.savefig("test.png")

########################################
##Plotting with pandas
########################################
#s=Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
#s.plot()

##Multi-line
df = DataFrame(np.random.randn(10,4).cumsum(0),
              columns=pd.Index(['A','B','C','D'],name="Random"),
              index=np.arange(0,100,10))
df.plot(title="Testing random plot")
show()
