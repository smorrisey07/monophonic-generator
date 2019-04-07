###################################################
# This file generates 4 single column csv files of
# monophonic music from the essenFolksong dataset.
# They are 2 files for each mode, major or minor,
# one with and one without a marker at the end of each piece.
# They are stored as note objects.
###################################################

from music21 import *
import pandas as pd

corp = corpus.getComposer('essenFolksong')
essenmaj = []
essenmin = []


# Opens files, sorts and transposes them to C major or A minor
def parsecorp(x, y):
    for z in range(x, y):
        corppar = [converter.parse(corp[z])]
        for file in corppar:
            k = file.analyze('key')
            if k.mode == 'major':
                disttoc = interval.Interval(k.tonic, pitch.Pitch('C'))
                essenmaj.append(file.transpose(disttoc))
            elif k.mode == 'minor':
                disttoa = interval.Interval(k.tonic, pitch.Pitch('A'))
                essenmin.append(file.transpose(disttoa))
        print(z)


# Runs parsecorp for files 0-13
# Running to 31 causes it to crash in file 16 due to running out of memory
i = 0
while i <= 14:
    if i == 27:
        parsecorp(27, 31)
    else:
        parsecorp(i, i+3)
    i += 3


# verifying keys of each list
# essenmajKeys = []
# essenminKeys = []
# for d in essenmaj:
#     essenmajKeys.append(d.analyze('key'))
# for e in essenmin:
#     essenminKeys.append(e.analyze('key'))

# creates single column vector and saves csv of all pitches in all major keys,
# with and without note "A0" denoting end of piece
essenMajNAR = []
essenMajNARend = []
A0 = note.Note('A0')
for opus in essenmaj:
    for score in opus:
        for values in score.flat.notesAndRests:
            essenMajNARend.append(values)
            essenMajNAR.append(values)
        essenMajNARend.append(A0)
majNARend = pd.Series(essenMajNARend)
majNAR = pd.Series(essenMajNAR)
majNAR.to_csv('majSeries.csv', header=False)
majNARend.to_csv('majSeriesEnd.csv', header=False)

# creates single column vector and saves csv of all pitches in all minor keys,
# with and without note "A0" denoting end of piece
essenMinNAR = []
essenMinNARend = []
A0 = note.Note('A0')
for opus in essenmin:
    for score in opus:
        for values in score.flat.notesAndRests:
            essenMinNARend.append(values)
            essenMinNAR.append(values)
        essenMinNARend.append(A0)
minNARend = pd.Series(essenMinNARend)
minNAR = pd.Series(essenMinNAR)
minNAR.to_csv('minSeries.csv', header=False)
minNARend.to_csv('minSeriesEnd.csv', header=False)
