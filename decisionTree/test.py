import trees
import treePlotter
# myDat,labels = trees.createDataSet()
# myTree = trees.createTree(myDat, labels)
# treePlotter.createPlot(myTree)
# trees.storageTree(myTree, 'classifierStorage.txt')
fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript', 'astigmatic', 'treatRate']
lensesTree = trees.createTree(lenses, lensesLabels)
treePlotter.createPlot(lensesTree)