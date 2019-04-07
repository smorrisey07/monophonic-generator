from music21 import *
import pandas as pd

# Loads all csv files and converts them back into Series
majSeries = pd.read_csv('majSeries.csv', header=-1, index_col=0)
majSeries = pd.Series(majSeries.iloc[:, 0])
majSeriesEnd = pd.read_csv('majSeriesEnd.csv', header=-1, index_col=0)
majSeriesEnd = pd.Series(majSeriesEnd.iloc[:, 0])
minSeries = pd.read_csv('minSeries.csv', header=-1, index_col=0)
minSeries = pd.Series(minSeries.iloc[:, 0])
minSeriesEnd = pd.read_csv('minSeriesEnd.csv', header=-1, index_col=0)
minSeriesEnd = pd.Series(minSeriesEnd.iloc[:, 0])

# Find 0th order probabilities
majProb = majSeries.value_counts(normalize=True, sort=True)
minProb = minSeries.value_counts(normalize=True, sort=True)
# majProb.to_csv('majProb0.csv', header=False)
# minProb.to_csv('minProb0.csv', header=False)

# Working on finding second order probabilities
# Getting error "unhashable type: 'Note'" in line 27
# Even though type(majSeriesEnd[0] is a string

# Create shifted Series and crosstab
# A0 = note.Note('A0')
# majSerNext = majSeriesEnd.shift(periods=-1, fill_value=A0)
# s1 = pd.crosstab(majSeriesEnd, majSerNext)

print(majSeriesEnd)
print(type(majSeriesEnd[0]))
