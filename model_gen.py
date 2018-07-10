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
	size.text = "129 129 20"

	pos = ET.SubElement(heightmap_collision,"pos")
	pos.text = "0 0 0"


	#Visual element of the model
	visual = ET.SubElement(link,"visual",name="visual")

	geometry_visual = ET.SubElement(visual,"geometry")

	heightmap_visual = ET.SubElement(geometry_visual,"heightmap")

	texture_grass = ET.SubElement(heightmap_visual,"texture")
	diffuse = ET.SubElement(texture_grass,"diffuse")
	diffuse.text = "file://media/materials/textures/grass_diffusespecular.png"
	normal = ET.SubElement(texture_grass,"normal")
	normal.text = "file://media/materials/textures/flat_normal.png"
	size = ET.SubElement(texture_grass,"size")
	size.text = "5"

	blend = ET.SubElement(heightmap_visual,"blend")

	uri = ET.SubElement(heightmap_visual,"uri")
	uri.text = "model://autogen_terrain/materials/textures/heightmap.png"

	size = ET.SubElement(heightmap_visual,"size")
	size.text = "129 129 20"

	pos = ET.SubElement(heightmap_visual,"pos")
	pos.text = "0 0 0"


	#print ET.tostring(sdf,pretty_print=True,xml_declaration=True)
	tree = ET.ElementTree(sdf)
	tree.write('model.sdf', pretty_print=True, xml_declaration=True)