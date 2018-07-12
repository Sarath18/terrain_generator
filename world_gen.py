#!usr/bin/env python
from lxml import etree as ET

def worldGenerator():
    sdf = ET.Element("sdf",version="1.4")

    world = ET.SubElement(sdf,"world",name="AutoGen Terrain World")

    #setting up the scene
    scene = ET.SubElement(world,"scene")

    sky = ET.SubElement(scene,"sky")

    clouds = ET.SubElement(sky,"clouds")

    speed = ET.SubElement(clouds,"speed")
    speed.text = "12"


    #including models
    include = ET.SubElement(world,"include")
    uri = ET.SubElement(include,"uri")
    uri.text = "model://autogen_terrain"

    include = ET.SubElement(world,"include")
    uri = ET.SubElement(include,"uri")
    uri.text = "model://sun"

    #print ET.tostring(sdf,pretty_print=True,xml_declaration=True)
    tree = ET.ElementTree(sdf)
    tree.write('terrain.world', pretty_print=True, xml_declaration=True)
