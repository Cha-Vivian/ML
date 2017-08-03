import logRegres
from numpy import *
dataArr, labelMat = logRegres.loadDataSet()
weights = logRegres.gradAscent(dataArr,labelMat)
logRegres.plotBestFit(weights.getA())