"""
The MIT License (MIT)

Copyright (c) 2014 Kacey Coley

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#printCamSpecs.py
# Kacey Coley
#Creates an xml file, print the position and orientation of houdini cameras
import hou
from lxml import etree
def printCamInfo(cam):
	if cam.name():
		print "=================="
		print "cam name = " + cam.name()
		print "tx = " + str(cam.parm('tx').eval())
		print "ty = " + str(cam.parm('ty').eval())
		print "tz = " + str(cam.parm('tz').eval())
		print "=================="
		print "rx = " + str(cam.parm('rx').eval())
		print "ry = " + str(cam.parm('ry').eval())
		print "rz = " + str(cam.parm('rz').eval())

def genCamXML(cam):
	
	camnode = etree.Element(cam.name())
	translateX = etree.Element('translateX')
	translateY = etree.Element('translateY')
	translateZ = etree.Element('translateZ')
	rotateX = etree.Element('rotateX')
	rotateY = etree.Element('rotateY')
	rotateZ = etree.Element('rotateZ')
	translateX.text = str(cam.parm('tx').eval())
	translateY.text = str(cam.parm('ty').eval())
	translateZ.text = str(cam.parm('tz').eval())
	rotateX.text = str(cam.parm('rx').eval())
	rotateY.text = str(cam.parm('ry').eval())
	rotateZ.text = str(cam.parm('rz').eval())
	camnode.append(translateX)
	camnode.append(translateY)
	camnode.append(translateZ)
	camnode.append(rotateX)
	camnode.append(rotateY)
	camnode.append(rotateZ)
	s = etree.tostring(camnode, pretty_print=True)
	print s
	


def buildCameraInfo():
	root = etree.Element('cam')
	nodes = hou.node('/obj')
	for child in nodes.children():
		if child.type().description() == "Camera":
		#	printCamInfo(child)
			genCamXML(child)

buildCameraInfo()
