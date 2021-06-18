import statistics
import pandas as pd 
import csv

df = pd.read_csv('StudentsPerformance.csv')
mathlist = df['math score'].to_list()

#mean
mathmean = statistics.mean(mathlist)

#mode
mathmode = statistics.mode(mathlist)

#median
mathmedian = statistics.median(mathlist)


print('Mean, Median, Mode of mathScores is {}, {}, {}'.format(mathmean, mathmedian, mathmode))

