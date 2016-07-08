# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 17:55:47 2016

@author: WuJianping
"""

import os
import random

def GenStrList(dbPath):
    
    allList = []    
    label = 0
    
    rootDir = os.listdir(dbPath)
    for fold in rootDir:
        subDir = dbPath + "\\" + fold
        if os.path.isdir(subDir):
#            print subDir
            filenames = os.listdir(subDir)
            for fname in filenames:
                temp = fold + "\\" + fname
                saveStr = "%s %d" %(temp, label)
                allList.append(saveStr)
                
            label = label + 1
        
    random.shuffle(allList)
    
    return allList
            
            
def SaveList(allList, trainRate = 0.8):
    cnt = len(allList)
    trainNum = int(cnt*trainRate)
    
    ftrain = open("train.txt", 'w')
    for idx in xrange(0, trainNum):
        ftrain.write(allList[idx])
        ftrain.write('\n')
        
    fval = open("val.txt", 'w')
    for idx in xrange(trainNum, cnt):
        fval.write(allList[idx])
        fval.write('\n')
        
    ftrain.close()
    fval.close()
    
    
def GenListFile(dbPath, trainRate = 0.8):
    allList = GenStrList(dbPath)
    SaveList(allList, trainRate)
        
            

        
if __name__ == "__main__":
    dbPath = r'E:\DATA\FaceData\casia-maxpy-clean\CASIA-maxpy-clean'
    GenListFile(dbPath)
    
    
    
    
    