# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Lab2


import seaborn as sns
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
sns.set(style="whitegrid")


df  = pd.read_csv('./vehicles.csv')
sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
#sns_plot.set_title("Scaterplot for Current  and New Fleet")
sns_plot.savefig("Scater plot 1.pdf",bbox_inches='tight')
plt.show()

df2=df.values.T[0]
plt.clf()
sns_plot2 = sns.distplot(df2, bins=20, kde=False, rug=False, label="Current Fleet")
sns_plot2.set_title("Histogram for Current Fleet")
sns_plot2.set_ylim(0, 50)
sns_plot2.set(xlabel='Current Fleet', ylabel='Frequency')
sns_plot2.get_figure().savefig("Current_Fleet_Histogram.png", bbox_inches='tight')
sns_plot2.get_figure().savefig("Current_Fleet_Histogram.pdf", bbox_inches='tight')

df3=df.values.T[1]
df3=pd.DataFrame(df3)
#df3.fillna(1)
df3.dropna(inplace=True)
plt.clf()
sns_plot3 = sns.distplot(df3, bins=20, kde=False, rug=True, label="New Fleet")
sns_plot3.set_title("Histogram2")
sns_plot3.set_ylim(0, 50)
sns_plot3.set(xlabel='New Fleet', ylabel='Frequency')
sns_plot3.get_figure().savefig("New_Fleet_Histogram.png", bbox_inches='tight')
sns_plot3.get_figure().savefig("New_Fleet_Histogram.pdf", bbox_inches='tight')
