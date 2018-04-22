import numpy as np
import pickle
import os
import feature_extraction
file1 = open('vecdict_all2.p', 'r')
file2 = open('classif_all2.p','r')

vec = pickle.load(file1)
classifier = pickle.load(file2)

file1.close()
file2.close()

def getSarcasmScore(sentence):
    sentence = sentence.encode('ascii', 'ignore')
    features = feature_extraction.getallfeatureset(sentence)
    
    features_vec = vec.transform(features)
    score = classifier.predict(features_vec)[0]
    percentage = int(round(2.0*(1.0/(1.0+np.exp(-score))-0.5)*100.0))
    
    return score

while True:
    print "enter the sentence to get sarcastic score or type exit to quit"
    data = str(raw_input())
    if data == "exit":
        break;
    else:
        print getSarcasmScore(data)
