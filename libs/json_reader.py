import json
import sys
import os
from glob import glob

from libs import const
from libs.shotgunmanager import getentitiesfromshotgun, getentitydatafromshotgun


def buildPath(fileName):
    if getattr(sys, 'frozen', False):
        return os.path.join(os.path.dirname(sys.executable), str(fileName))
    return fileName


def read(filename):
    with open(buildPath(filename+".json"), 'rb') as jsonfile:
        jsondata = json.load(jsonfile)
    return jsondata


def write(obj, filename):
    with open(buildPath(filename+".json"), 'wb') as jsonfile:
        json.dump(obj, jsonfile, default=lambda o: o.__dict__, sort_keys=True)


def validateLocalFile(filename, datapath=""):
    return datapath+filename+".json" in glob(buildPath(datapath+"*.json"))


def getcomplexdata(filename, datapath="", forcePull=False):
    if validateLocalFile(filename, datapath) and not forcePull:
        data = read(datapath+filename)
        print "Loaded from file"
    else:
        
        if datapath == const.ENTITY_PATH:
            data = getentitiesfromshotgun(filename)
        else:
            data = getentitydatafromshotgun()

        write(data, datapath+filename)
        print "Loaded from Shotgun"
    return data
