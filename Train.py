import nltk
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np


#Set Reshape to avoid warning???

data= np.array([(16.88, 7.78,   0.54,   0.64,   0.0,    0.0,    0.25,   0.16,   0.15,   0.14,   0.12,   0.14),
                (26.5,  8.5,    0.83,   1.5,    0.0,    0.0,    0.23,   0.18,   0.16,   0.18,   0.07,   0.15),
                (21.8,  9.16,   0.59,   1.4,    0.0,    0.0,    0.24,   0.17,   0.15,   0.18,   0.11,   0.12),
                (30.15, 19.34,  0.64,   2.76,   0.0,    0.23,   0.14,   0.29,   0.14,   0.12,   0.22,   0.06),
                (30.12, 18.50,  0.59,   2.43,   0.0,    0.12,   0.17,	0.27,   0.14,   0.12,   0.20,   0.06),
                (27.33, 9.68,   0.58,   1.58,	0.0,    0.0,    0.26,   0.12,   0.20,   0.17,	0.16,   0.07),
                (23.63, 11.57,  0.52,   1.03,	0.0,    0.0,    0.23,   0.09,   0.17,   0.20,   0.14,   0.14),
                (25.79, 11.62,  0.51,   1.08,	0.0,    0.0,    0.27,   0.12,   0.15,   0.18,   0.12,   0.13),
                (21.81, 10.22,  0.49,   0.86,	0.0,    0.0,    0.29,   0.16,   0.16,   0.15,   0.11,   0.10),
                (21.87, 0.48,   10.13,  1.25,	0.0,	0.04,	0.29,	0.12,	0.17,	0.23,	0.086,	0.07),
                (21.48, 9.28,   0.46,   1.22,   0.0,    0.0,    0.29,   0.14,   0.16,   0.19,	0.12,	0.08),
                (20.28,	9.47,	0.49,	0.90,	0.0,	0.0,	0.21,	0.18,	0.13,	0.21,	0.11,	0.13),
                (21.23,	8.72,	0.52,	0.88,	0.0,	0.0,	0.25,	0.25,	0.087,	0.17,	0.15,	0.07),
                (22.79, 9.67,	0.46,	0.75,	0.0,	0.041,	0.25,	0.12,	0.155,	0.23,	0.11,	0.11),
                (23.10,	12.87,	0.45,	1.03,	0.0,	0.0,	0.18,	0.36,	0.105,	0.16,	0.11,	0.06)])
 


target = [[0],[0],[0],
           [1],[1],[1],
           [2],[2],[2],
           [3],[3],[3],
           [4],[4],[4]]

#target_name= ['Author a', 'Author b','Author c','Author d', 'Author e']


x = data
y = target

# KNN
knn = KNeighborsClassifier(n_neighbors = 1)
#print knn
knn.fit(x,y)

test1 = [32.75,7.71,0.54, 1.91,0.0,0.0,0.211, 0.18, 0.19, 0.23, 0.11, 0.05]
test2 =[24.45, 9.55, 0.48, 1.0, 0.0, 0.0, 0.23, 0.22, 0.13, 0.20, 0.09, 0.09]
test3 =[32, 8.91, 0.53,	1.22,	0.055,	0.0 ,0.23,0.10,0.16, 0.19, 0.14, 0.14]
test =[(32.75,7.71,0.54, 1.91,0.0,0.0,0.211, 0.18, 0.19, 0.23, 0.11, 0.05),(24.45, 9.55, 0.48, 1.0, 0.0, 0.0, 0.23, 0.22, 0.13, 0.20, 0.09, 0.09),(32, 8.91, 0.53,1.22,0.055,0.0 ,0.23,0.10,0.16, 0.19, 0.14, 0.14)]

predicted = knn.predict(test)
print "kNN predict :Author with array"
print predicted

true_pred1 = [1]
true_pred2 = [4]
true_pred =[1,4,3]

acc1 = accuracy_score(true_pred, predicted)
print "Accuracy Rate NB, which is calculated by accuracy_score() is: %f" % acc1

'''
for item, labels in zip(test1, predicted):
    print '%s => %s' % (item, ', '.join(target_name[x] for x in labels))
'''

#NaiveBayes

clf = GaussianNB()
clf.fit(x, y)
predicts = clf.predict(test)
print "NB predict : Author with array"
print predicts
acc2 = accuracy_score(true_pred, predicts)
print "Accuracy Rate NB, which is calculated by accuracy_score() is: %f" % acc2

#SVM
'''
clf = LinearSVC()
clf.fit(x,y)
predict = clf.predict(test1)
print "SVM predict : Author with array"
print predict
'''

svc = svm.SVC(kernel='linear')
svc.fit(x, y)
predict1 = svc.predict(test)
print "Linear SVM predict : Author with array"
print predict1
acc3 = accuracy_score(true_pred, predict1)
print "Accuracy Rate Linear SVM, which is calculated by accuracy_score() is: %f" % acc3


svc = svm.SVC(kernel='poly',degree=3)
svc.fit(x, y)
predict2 = svc.predict(test)
print "Polynomial SVM predict : Author with array"
print predict2
acc4 = accuracy_score(true_pred, predict2)
print "Accuracy Rate Polynomial SVM, which is calculated by accuracy_score() is: %f" % acc4

svc = svm.SVC(kernel='rbf')
svc.fit(x, y)
predict3 = svc.predict(test)
print "Kernel SVM predict : Author with array"
print predict3
acc5 = accuracy_score(true_pred, predict3)
print "Accuracy Rate Linear SVM, which is calculated by accuracy_score() is: %f" % acc5
