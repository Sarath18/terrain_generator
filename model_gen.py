#!usr/bin/env python
"""
HIERARCHY:

sdf
  model
    static
    link
      collision
        geometry
          heightmap
            uri
            size
            pos

      visual
        geometry
          heightmap
            texture -- number of textures you want
              diffuse
              normal
              size
            blend   -- number of textures - 1
              min_height
              fade_dist
            uri
            size
            pos
"""
from lxml import etree as ET

def modelGenerator():
	sdf = ET.Element("sdf",version="1.4")

	model = ET.SubElement(sdf,"model",name="AutoGen Terrain")

	static = ET.SubElement(model,"static")
	static.text = "true"

	link = ET.SubElement(model,"link",name="link")

	#Collision element of the model
	collision = ET.SubElement(link,"collision",name="collision")

	geometry_collision = ET.SubElement(collision,"geometry")

	heightmap_collision = ET.SubElement(geometry_collision,"heightmap")

	uri = ET.SubElement(heightmap_collision,"uri")
	uri.text = "model://autogen_terrain/materials/textures/heightmap.png"

	size = ET.SubElement(heightmap_collision,"size")
	size.text = "129 129 12"

	pos = ET.SubElement(heightmap_collision,"pos")
	pos.text = "0 0 0"


	#Visual element of the model
	visual = ET.SubElement(link,"visual",name="visual")

	geometry_visual = ET.SubElement(visual,"geometry")

	heightmap_visual = ET.SubElement(geometry_visual,"heightmap")

	#Texture1
	texture1 = ET.SubElement(heightmap_visual,"texture")
	diffuse = ET.SubElement(texture1,"diffuse")
	diffuse.text = "model://autogen_terrain/materials/textures/water.jpg"
	normal = ET.SubElement(texture1,"normal")
	normal.text = "file://media/materials/textures/flat_normal.png"
	size = ET.SubElement(texture1,"size")
	size.text = "5"

	#Texture2
	texture2 = ET.SubElement(heightmap_visual,"texture")
	diffuse = ET.SubElement(texture2,"diffuse")
	diffuse.text = "model://autogen_terrain/materials/textures/sand.jpg"
	normal = ET.SubElement(texture2,"normal")
	normal.text = "file://media/materials/textures/flat_normal.png"
	size = ET.SubElement(texture2,"size")
	size.text = "5"

	#Texture3
	texture3 = ET.SubElement(heightmap_visual,"texture")
	diffuse = ET.SubElement(texture3,"diffuse")
	diffuse.text = "model://autogen_terrain/materials/textures/grass.jpg"
	normal = ET.SubElement(texture3,"normal")
	normal.text = "file://media/materials/textures/flat_normal.png"
	size = ET.SubElement(texture3,"size")
	size.text = "5"

	#Texture4
	texture4 = ET.SubElement(heightmap_visual,"texture")
	diffuse = ET.SubElement(texture4,"diffuse")
	diffuse.text = "file://media/materials/textures/dirt_diffusespecular.png"
	normal = ET.SubElement(texture4,"normal")
	normal.text = "file://media/materials/textures/flat_normal.png"
	size = ET.SubElement(texture4,"size")
	size.text = "5"

	#Blending Textures 1 and 2
	blend = ET.SubElement(heightmap_visual,"blend")
	min_height = ET.SubElement(blend,"min_height")
	min_height.text = "0"
	fade_dist = ET.SubElement(blend,"fade_dist")
	fade_dist.text = "0.8"

	#Blending Textures 2 and 3
	blend = ET.SubElement(heightmap_visual,"blend")
	min_height = ET.SubElement(blend,"min_height")
	min_height.text = "0.1"
	fade_dist = ET.SubElement(blend,"fade_dist")
	fade_dist.text = "1.5"

	#Blending Textures 3 and 4
	blend = ET.SubElement(heightmap_visual,"blend")
	min_height = ET.SubElement(blend,"min_height")
	min_height.text = "3"
	fade_dist = ET.SubElement(blend,"fade_dist")
	fade_dist.text = "6"


	uri = ET.SubElement(heightmap_visual,"uri")
	uri.text = "model://autogen_terrain/materials/textures/heightmap.png"

	size = ET.SubElement(heightmap_visual,"size")
	size.text = "129 129 12"

	pos = ET.SubElement(heightmap_visual,"pos")
	pos.text = "0 0 0"


	#print ET.tostring(sdf,pretty_print=True,xml_declaration=True)
	tree = ET.ElementTree(sdf)
	tree.write('model.sdf', pretty_print=True, xml_declaration=True)