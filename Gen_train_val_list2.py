# -*- coding: utf-8 -*-
"""
every subclass separate by trainRate

Created on Sat Jul 09 17:31:04 2016

@author: WuJianping
"""

import os
import random

def GenStrList(dbPath, trainRate = 0.85):
    
    trainList = []
    valList = []
    
    label = 0
    
    rootDir = os.listdir(dbPath)
    for fold in rootDir:
        subDir = dbPath + "\\" + fold
        if os.path.isdir(subDir):
#            print subDir
            filenames = os.listdir(subDir)
            subList = [] 
            for fname in filenames:
                temp = fold + "\\" + fname
                saveStr = "%s %d" %(temp, label)
                subList.append(saveStr)
                
            lstLen = int(len(subList)*trainRate)
#            trainList.extend(subList[:lstLen])
#            valList.extend(subList[lstLen:])   
            trainList[len(trainList):len(trainList)] = subList[:lstLen]
            valList[len(valList):len(valList)] = subList[lstLen:]
            label = label + 1
        
    random.shuffle(trainList)
    random.shuffle(valList)
    
    return trainList, valList
            
            
def SaveList(trainList, valList):
    
    ftrain = open("train.txt", 'w')
    for trainSample in trainList:
        ftrain.write(trainSample)
        ftrain.write('\n')
        
    fval = open("val.txt", 'w')
    for valSample in valList:
        fval.write(valSample)
        fval.write('\n')
        
    ftrain.close()
    fval.close()
    
    
def GenListFile(dbPath, trainRate = 0.85):
    trainList, valList = GenStrList(dbPath, trainRate)
    SaveList(trainList, valList)
        
            

        
if __name__ == "__main__":
    dbPath = r'E:\DATA\FaceData\casia-maxpy-clean\CASIA-maxpy-clean'
    GenListFile(dbPath, 0.85)