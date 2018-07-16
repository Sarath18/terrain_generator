#!usr/bin/env python
from lxml import etree as ET
from wizard import worldSettings


def worldGenerator(w):
    sdf = ET.Element("sdf",version="1.4")

    world = ET.SubElement(sdf,"world",name="AutoGen Terrain World")

    #setting up the scene
    scene = ET.SubElement(world,"scene")

    ambient = ET.SubElement(scene,"ambient")
    ambient.text = w.ambient

    #Day: 120 120 120 255
    #Night: 20 40 50 255
    #Dawm/Dusk: 120 80 60 255
    #AfterDawn/BeforeDusk: 120 70 80 255

    sky = ET.SubElement(scene,"sky")

    clouds = ET.SubElement(sky,"clouds")

    speed = ET.SubElement(clouds,"speed")
    speed.text = "12"

    time = ET.SubElement(sky,"time")
    time.text  = w.time


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
