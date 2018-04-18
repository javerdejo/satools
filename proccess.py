#!/usr/bin/env python
# ECOSUR-ERIS Project
# Author: Javier Arellano-Verdejo
# Date: april 2018
# How to use: ./proccess.py -p ./data/terra/
# ./data/terra/ is the path to the nc files data

from netCDF4 import Dataset
import numpy as np
import sys, getopt
from os import listdir
from os.path import isfile, join

def ls(ruta):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]

def read_file(filepath,filename):
    dataset = Dataset(filepath+'/'+filename,'r')
    d = np.array(dataset.variables['chlor_a'])
    # 1708:1720, 2219:2228 son las coordenadas de banco chinchorro
    data=d[1708:1720, 2219:2228]
    np.set_printoptions(precision=8)
    np.savetxt(filename+".csv", data, delimiter=",", fmt="%s")

def main(filepath):
    files=ls(filepath)
    for filename in files:
        print ("Processing "+filename+"...")
        read_file(filepath,filename)

if __name__ == "__main__":
    argv = sys.argv[1:]
    filepath=''
    try:
        opts, args = getopt.getopt(argv,"hp:",["path="])
    except getopt.GetoptError:
        print ('test.py -p <path>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('proccess.py -p <path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            filepath = arg
            print ('Path: ' + filepath)
            main(filepath)
