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

	cv2.imwrite("heightmap.png",heightmap)


def imageResizer(path):
	hm = cv2.imread(path)
	hm_resize = cv2.resize(hm,(129,129))
	'''
	cv2.imshow("Heightmap",hm_resize)
	k = cv2.waitKey(0)
	if k==27:
		destroyWindow('Heightmap')
	'''
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

	destination = raw_input("World file destination:")
	if destination=="":
		destination=cwd
	os.chdir(destination)

	#Creating our world file
	worldGenerator()

	#Success output
	print "Terrain successully generated"

	#Opening the generated world in Gazebo
	time.sleep(1)
	print "Loading World..."

	call(["gazebo","terrain.world"])

	os.chdir(os.path.expanduser(cwd))
	print os.listdir()
