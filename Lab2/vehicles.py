# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Lab2
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#Import the dataset
#dataset = pd.read_csv('/Users/cynthiamasetto/Documents/ce888labs/Lab2/vehicles.csv')



def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))

#Describing the data a liitle
#df=pd.DataFrame(data=df)
#df.describe()
#df.isna().sum()

if __name__ == "__main__":
	df = pd.read_csv('vehicles.csv')
	print((df.columns))
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')

	data = df.values.T[0]
   # data2 = pd.DataFrame(data=data)
    #data2.isna().sum()
   # x=data2.head(78)
    
	print((("Mean: %f")%(np.mean(data))))
	print((("Median: %f")%(np.median(data))))
	print((("Var: %f")%(np.var(data))))
	print((("std: %f")%(np.std(data))))
	print((("MAD: %f")%(mad(data))))

	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('x') 
	axes.set_ylabel('y')

	sns_plot2.savefig("histogram.png",bbox_inches='tight')
	sns_plot2.savefig("histogram.pdf",bbox_inches='tight')
    
    data = pd.read_csv('vehicles.csv')
    data = data.values.T[1]
    data = data[~np.isnan(data)]
 
   # data2 = pd.DataFrame(data=data)
    #data2.isna().sum()
   # x=data2.head(78)
    
	print((("Mean: %f")%(np.mean(data))))
	print((("Median: %f")%(np.median(data))))
	print((("Var: %f")%(np.var(data))))
	print((("std: %f")%(np.std(data))))
	print((("MAD: %f")%(mad(data))))

	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('x') 
	axes.set_ylabel('y')

	sns_plot2.savefig("histogram2.png",bbox_inches='tight')
	sns_plot2.savefig("histogram2.pdf",bbox_inches='tight')
    

    
