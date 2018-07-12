#!usr/bin/env python
from lxml import etree as ET

def configGenerator():
    model = ET.Element("model")

    name = ET.SubElement(model,"name")
    name.text = "AutoGen Terrain"

    version = ET.SubElement(model,"version")
    version.text = "1.0"

    sdf = ET.SubElement(model,"sdf",version="1.4")
    sdf.text = "model.sdf"

    author = ET.SubElement(model,"author")

    name = ET.SubElement(author,"name")
    name.text = "Sarathkrishnan Ramesh"

    email = ET.SubElement(author,"email")
    email.text = "---"

    description = ET.SubElement(model,"description")
    description.text = "Auto Generated Terrain for Gazebo"


    #print ET.tostring(model,pretty_print=True,xml_declaration=True)

    tree = ET.ElementTree(model)
    tree.write('model.config', pretty_print=True, xml_declaration=True)
