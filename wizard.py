#!usr/bin/env python
import os
import shutil
from config_gen import *
from model_gen import *
from world_gen import *
from subprocess import call
import time
import cv2
from urllib import urlretrieve

class worldSettings(object):
    def __init__(self):
        self.ambient = "120 120 120 255"
        self.time = "10:00"

    def worldScene(self):
        self.time = raw_input("Enter time of day[24 hrs](hh:mm): ")
        time = self.time[0:2]
        time = int(time)

        #Night / Early Morning
        if time<6 or time>=21:
            self.ambient = "20 40 50 255"
        #Dawn
        elif time<7 and time>=6:
            self.ambient = "120 80 60 255"
        #After Dawn
        elif time<8 and time>=7:
            self.ambient = "120 70 80 255"
        #Before Dusk
        elif time<20 and time>19:
            self.ambient = "120 70 80 255"
        #Dusk
        elif time<21 and time>=20:
            self.ambient = "120 80 60 255"


def modelFolderGenerator(heightmap):

    #Creating our auto generated terrain model directory
    os.chdir(os.path.expanduser("~/.gazebo/models/"))
    path = os.getcwd()
    items = os.listdir(path)

    for item in items:
        if "autogen_terrain" == item:
            shutil.rmtree("autogen_terrain")

    os.mkdir("autogen_terrain")

    #Changing the current working directory
    os.chdir("autogen_terrain")

    #Creating the model.config file
    configGenerator()

    #Creatinf the model.sdf file
    modelGenerator()

    #Creating the model materials folder
    os.mkdir("materials")
    os.chdir("materials")
    os.mkdir("textures")
    os.chdir("textures")

    #Saving the heightmap inside terrain model textures
    cv2.imwrite("heightmap.png",heightmap)


def imageResizer(path):
    hm = cv2.imread(path)
    hm_resize = cv2.resize(hm,(129,129))

    return hm_resize



if __name__ == "__main__":

    #Welcome text
    cwd = os.getcwd()
    print cwd
    print "WELCOME TO AUTOMATIC TERRAIN GENEREATOR"

    #Ask user for heightmap input
    check = raw_input("Do you have a heightmap?(y/n):")

    #Take in heightmap as a url or as file on disk
    if check=="y" or check=="Y":
        path = raw_input("Enter the location of the heightmap:")
    else:
        link = raw_input("Enter the url of heightmap:")
        urlretrieve(link,"img.png")
        path = "./img.png"

    #Resizing the image to 2*n+1 dimention: (129x129)
    heightmap = imageResizer(path)

    #Creating a autogen_terrain folder with terrain information and also the world file
    modelFolderGenerator(heightmap)

    #Saving Textures into the terrain model
    os.chdir(os.path.expanduser(cwd))
    os.chdir("textures")
    texture_path = os.getcwd()
    imgfiles = os.listdir(texture_path)
    for imgfile in imgfiles:
        command = "cp "+str(imgfile)+" ~/.gazebo/models/autogen_terrain/materials/textures/"
        os.system(command)

    #Changing the directory to the output path for the .world
    destination = raw_input("World file destination(Press Enter to pass):")
    if destination=="":
        destination=cwd
    os.chdir(destination)


    #Creating our world file
    w = worldSettings()
    w.worldScene()
    worldGenerator(w)


    #Success output
    print "Terrain successully generated"

    #Opening the generated world in Gazebo
    time.sleep(1)
    print "Loading World..."

    call(["gazebo","terrain.world"])

    os.chdir(os.path.expanduser(cwd))
    print os.listdir()
