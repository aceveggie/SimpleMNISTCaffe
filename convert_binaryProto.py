import os
import cv2
import glob
import numpy as np
import shutil
import time
import lmdb
import sys

from os.path import expanduser
curDirName = os.path.dirname(os.path.abspath(__file__))
os.chdir(expanduser("~")+'/Programs/caffe/')
import caffe

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( curDirName+"/"+ str(sys.argv[1]) , 'rb' ).read()
blob.ParseFromString(data)
print 'opened ', sys.argv[1]
arr = np.array( caffe.io.blobproto_to_array(blob) )
print 'arr.shape', arr.shape
np.save(curDirName+"/"+str(sys.argv[1].split(".")[0]+".npy") , arr)
if(arr.shape[1] == 3):
	arr = np.reshape(arr, (arr.shape[2], arr.shape[3], arr.shape[1]))
elif(arr.shape[1] == 1):
	arr = np.reshape(arr, (arr.shape[2], arr.shape[3]))
cv2.imwrite(curDirName+"/"+str(sys.argv[1].split(".")[0]+".png") , arr)
print curDirName+"/"+str(sys.argv[1].split(".")[0]+".png")