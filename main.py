import os
import xml.dom
from xml.dom import minidom
import xml.etree.ElementTree as ET
import powerdesigner

CURRWD = os.getcwd()
PDFILES = []
FIRST = True
#Find all pdfiles
for file in os.listdir(CURRWD):
    if file.endswith(".pdm") or file.endswith(".cdm"):
        PDFILES.append(file)

# Process file
fid = "{"+"amogus"+"}"
tid = "TID"
name = "WorkspaceProject"
currfile = "Filename.cdm"
# Create xml container to add to
data = ET.Element('Workspace')
local = ET.SubElement(data, 'Local')
local.set('Expanded', "Yes")
# Set some other stuff??
browsermodule = ET.SubElement(data, 'BrowserModule')
browsermodule.set('Name', "Repository")


for cfile in PDFILES:
    lines = tuple(open(cfile, 'r')) # Get all lines
    header= lines[1]                # Get the first line with Important stuff
    fid = powerdesigner.getFID(header) # Get Fid from header
    tid = powerdesigner.getTID(header) # Get Tid from header
    pfile = ET.SubElement(local, 'Model')# create one model
    pfile.set('Expanded', 'Yes')
    pfile.set('ID', "{"+fid+ "}")
    pfile.set('Name', cfile[:len(str(cfile))-4])
    pfile.set('Type', "{"+ tid+ "}")
    pfile.set('URL', cfile)
    if FIRST == True:
        pfile.set("Selected", "Yes")
        FIRST = False

powerdesigner.makeSWS(data=data, wsname="WorkspaceNew.sws")




