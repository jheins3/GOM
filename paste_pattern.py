# -*- coding: utf-8 -*-

import gom
import math


DIALOG=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
' <title>Pattern</title>' \
' <style>Standard</style>' \
' <control id="OkCancel"/>' \
' <position></position>' \
' <embedding></embedding>' \
' <sizemode></sizemode>' \
' <size width="197" height="328"/>' \
' <content rows="9" columns="1">' \
'  <widget rowspan="1" row="0" column="0" columnspan="1" type="label">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Enter Angle:</text>' \
'  </widget>' \
'  <widget rowspan="1" row="1" column="0" columnspan="1" type="input::number">' \
'   <name>angle</name>' \
'   <tooltip></tooltip>' \
'   <value>0</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'   <precision>2</precision>' \
'   <background_style></background_style>' \
'  </widget>' \
'  <widget rowspan="1" row="2" column="0" columnspan="1" type="label">' \
'   <name>label_1</name>' \
'   <tooltip></tooltip>' \
'   <text>How many Iterations?</text>' \
'  </widget>' \
'  <widget rowspan="1" row="3" column="0" columnspan="1" type="input::integer">' \
'   <name>times</name>' \
'   <tooltip></tooltip>' \
'   <value>0</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'  </widget>' \
'  <widget rowspan="1" row="4" column="0" columnspan="1" type="label">' \
'   <name>label_2</name>' \
'   <tooltip></tooltip>' \
'   <text>Axis of Rotation:</text>' \
'  </widget>' \
'  <widget rowspan="1" row="5" column="0" columnspan="1" type="input::list">' \
'   <name>rotate</name>' \
'   <tooltip></tooltip>' \
'   <items>' \
'    <item>x-axis</item>' \
'    <item>y-axis</item>' \
'    <item>z-axis</item>' \
'   </items>' \
'   <default>x-axis</default>' \
'  </widget>' \
'  <widget rowspan="1" row="6" column="0" columnspan="1" type="input::point3d">' \
'   <name>dir</name>' \
'   <tooltip></tooltip>' \
'   <supplier>lines</supplier>' \
'  </widget>' \
'  <widget rowspan="1" row="7" column="0" columnspan="1" type="label">' \
'   <name>label_3</name>' \
'   <tooltip></tooltip>' \
'   <text>Invert Selection?</text>' \
'  </widget>' \
'  <widget rowspan="1" row="8" column="0" columnspan="1" type="input::checkbox">' \
'   <name>invert</name>' \
'   <tooltip></tooltip>' \
'   <value>false</value>' \
'   <title>Yes</title>' \
'  </widget>' \
' </content>' \
'</dialog>')

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	pass

DIALOG.handler = dialog_event_handler
selection = gom.app.project.inspection.filter ('is_selected')

usr=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)

#print(selection)
#print(usr.angle)
#print(usr.times)
#print(usr.rotate)
#print(usr.invert)
#print(len(selection))
print(usr.dir)

# creates empty list the same length as selected points

newNames = [None] * len(selection)
print(newNames)

# produces which axis is axis for rotation

if usr.rotate == 'x-axis':
	sel = 'system_line_x'
	
elif usr.rotate == 'y-axis': 
	sel = 'system_line_y'
		
else:
	sel = 'system_line_z'
	
#print(sel)

# produces steping angle for rotation

step = usr.angle / usr.times

#print (step)

#loops the pattern however many times usr specifies.

start = len(selection) 
space = ''
	
for iter in range(usr.times):

		
	names = gom.app.project.inspection.filter ('is_selected')
		
	gom.script.sys.copy_to_clipboard (elements= names)	
		
	gom.script.sys.paste_from_clipboard (destination= names)
	
	#renaming pasted values



	for x in range(0, len(selection)):
		
					#print (x)
			
		#print(selection)
		
		
		rCopy = (str(selection[x]))[:-10]
		
		y = len(rCopy) 
		
		#print(y)	
		
		
		while True:
			
			if space == ' ':
				
				break
				
			elif space == '.':
				break
				
			else: 
				#print (rCopy[y-1])	
				space = (rCopy)[y-1]  	
				y -= 1
				#print(space)
				#print(y)
		
			
		if space == '.':
			#print ('its a friggin set up pnt')
			newNames[x] = (str(selection[x]))[28:y+1] + str(start+1)
			#print(newNames)
			start += 1
			space = ''	
		elif space == ' ':
			#print ('its a friggin inspections pnt')
			newNames[x] = (str(selection[x]))[28:y+1] + str(start+1)
			#print(newNames)
			start += 1
			space = ''

	gom.script.sys.rename_elements(elements = names, names = newNames)
		
	CAD_ALIGNMENT=gom.script.transform_element.by_rotation (
		angle=math.radians(step), 
		elements=names, 
		invert_transformation=usr.invert, 
		line=gom.app.system[sel])

			


#was sel in line = gom.app.system[sel]
	
#y = -len(str(selection[x])[y]) 
#space = None
#while space != ' ':	
#	space = str(selection[x])[y]
#	y += 1
	
#for x in range(len(selection)):

	#print(selection[x])
	
	#nSelection[x] = (str(selection[x]))[28:-2] + '.' + str(iter+1)
	
	#print(nSelection)
	#print(selection)
