# -*- coding: utf-8 -*-
import gom
import os
import glob
import csv

DIALOG=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
' <title>Universal Combine CSV</title>' \
' <style>Standard</style>' \
' <control id="OkCancel"/>' \
' <position>center</position>' \
' <embedding>always_toplevel</embedding>' \
' <sizemode>fixed</sizemode>' \
' <size width="318" height="244"/>' \
' <content rows="4" columns="1">' \
'  <widget rowspan="1" row="0" column="0" columnspan="1" type="label">' \
'   <name>label_1</name>' \
'   <tooltip></tooltip>' \
'   <text>Select Folder Location</text>' \
'  </widget>' \
'  <widget rowspan="1" row="1" column="0" columnspan="1" type="input::file">' \
'   <name>dir</name>' \
'   <tooltip></tooltip>' \
'   <type>directory</type>' \
'   <title>Choose File</title>' \
'   <default></default>' \
'   <limited>false</limited>' \
'   <file_types/>' \
'   <file_types_default></file_types_default>' \
'  </widget>' \
'  <widget rowspan="1" row="2" column="0" columnspan="1" type="label">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Select One: </text>' \
'  </widget>' \
'  <widget rowspan="1" row="3" column="0" columnspan="1" type="input::radiobutton">' \
'   <name>sel</name>' \
'   <tooltip></tooltip>' \
'   <items>' \
'    <item description="Export Deviations" state="Deviations"/>' \
'    <item description="Export Actuals" state="Actuals"/>' \
'    <item description="Export Nominals" state="Nominals"/>' \
'   </items>' \
'   <default>Deviations</default>' \
'  </widget>' \
' </content>' \
'</dialog>')

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	pass

DIALOG.handler = dialog_event_handler

usr=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)


#OVERWRITES THE FILE THAT IS BEING RAN, IF ITS ALREADY BEEN RAN PREVIOUSLY

for root, dirs, files in os.walk(usr.dir):
	
	for file in files:
		
		if os.path.exists(usr.dir + "\\" + usr.sel):
			
			os.remove(usr.dir + "\\" + usr.sel)

#CHANGES DIRECTORY TO THE WORKING DIRECTORY

os.chdir(usr.dir)

#GETS THE FILENAMES FROM THE WORKING DIRECTORY 

filenames = sorted(glob.glob((usr.dir + '\*.csv')))

#CREATES AN EMPTY LIST TO BE POPULATED WITH ELEMENTS

elements = []

#OPENS THE FIRST CSV FILE TO GET THE COLUMN/ROWS TO BE COMBINED

with open(str(filenames[0]), "r") as f:  
	
	#CREATES A LIST FROM THE OPENED CSV FILE
	
	first = list(csv.reader(f))
	
	#GETS THE NUMBER OF ROWS IN THE CSV FILES
	
	rows = len(first)
	
	#GETS THE NUMBER OF COLUMNS IN CSV FILE TO LOOK FOR NOMINAL, ACTUALS, DEVIATIONS, ETC. 

	columns = len(first[0])
	
	#CONDITIONAL STATEMENTS TO SELECT WHICH COLUMN TO EXPORT
	
	if usr.sel == 'Deviations': 
		
		type = 'Dev'
		
	elif usr.sel == 'Actuals': 
		
		type = 'Actual'
		
	elif usr.sel == 'Nominals': 
		
		type = 'Nominal'
		
	else: 
		
	#WILL PROBABLY NEVER RUN UNLESS SOMETHING GETS REALLY MESSED UP. 
	
		RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
		' <title>Error</title>' \
		' <style>Standard</style>' \
		' <control id="OkCancel"/>' \
		' <position>automatic</position>' \
		' <embedding>always_toplevel</embedding>' \
		' <sizemode>automatic</sizemode>' \
		' <size width="260" height="150"/>' \
		' <content rows="1" columns="2">' \
		'  <widget rowspan="1" row="0" column="0" columnspan="1" type="image">' \
		'   <name>image</name>' \
		'   <tooltip></tooltip>' \
		'   <use_system_image>true</use_system_image>' \
		'   <system_image>system_message_warning</system_image>' \
		'   <data><![CDATA[AAAAAAAAAA==]]></data>' \
		'   <file_name></file_name>' \
		'   <keep_original_size>true</keep_original_size>' \
		'   <keep_aspect>true</keep_aspect>' \
		'   <width>0</width>' \
		'   <height>0</height>' \
		'  </widget>' \
		'  <widget rowspan="1" row="0" column="1" columnspan="1" type="display::text">' \
		'   <name>text</name>' \
		'   <tooltip></tooltip>' \
		'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
		'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
		'p, li { white-space: pre-wrap; }' \
		'&lt;/style>&lt;/head>&lt;body style="    ">' \
		'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Something went wrong,&lt;/p>' \
		'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Try again!&lt;/p>&lt;/body>&lt;/html></text>' \
		'   <wordwrap>false</wordwrap>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	
	#ITERATES ACCROSS THE FIRST COLUMN IN FIRST CSV TO GET A LIST OF ALL ELEMENTS FROM INSPECTION
	
	for iter in range(0, rows):
		
		elements.append((first[iter][0]))
		
	#ITERATIVELY FINDS THE COLUMN WHICH 'DEV', 'NOMINAL', OR 'ACTUALS' IS LOCATED	
				
	for i in range(0, columns): 
	
		if first[0][i] == type: 
		
			column = i
			
			break
			
#CREATES A LIST WITH THE LENGTH OF SERIAL NUMBER IN DIRECTORY

shortFilenames = [{} for i in range(len(filenames))]

#CREATES A LIST OF LISTS FOR HOWEVER MANY ROWS IN CSV. 
#USED AS BLUEPRINT FOR EXPORTING A NEW CSV

newCSV = [[] for x in range(rows)]

#Scrapes through directory, opens each .csv file, stores the deviations in empty lists

def combine(shortFilenames):
	
	#APPENDS LIST OF ALL ELEMENTS TO THE FIRST COLUMN
	
	for shi in range(0, rows): 
		
		newCSV[shi].append(elements[shi])
		
	#ITERATIVELY GETS EACH SN, OPENS EACH CSV FILE, AND PASTES VALUES INTO NEWCSV
	
	for index in range(len(shortFilenames)):
		
		#ASSIGNS THE SERIAL NUMBER IN THE INDEXED PLACE 
		
		shortFilenames[index] = os.path.basename(str(filenames[index]))
		
		#REMOVES THE '.STL' FROM THE END OF THE FILE NAME
		
		serialNums = (shortFilenames[index])[:-4]
		
		#BUILDS THE DIRECTORY FILE FROM PREVIOUS VARIABLES
		
		directoryFile = str(usr.dir) + '/' + str(serialNums) + '.csv'
		
		#CHECKS TO SEE IF A NOMINAL/ACTUAL/DEVIATIONS FILE EXISTS, IF IT DOES, EXCLUDE IT FROM APPENDING DATA FROM IT
		
		if directoryFile != usr.dir + '/Nominals.csv' and directoryFile != usr.dir + '/Deviations.csv' and directoryFile != usr.dir + '/Actuals.csv': 
			
			#APPENDS THE SERIAL NUMBERS TO THE TOP OF THE NEWCSV FILE
			
			newCSV[0].append(serialNums)
		
			#OPENS THE DIRECTORY FILE INTO PYTHON
	
			csvFile = open(directoryFile)
			
			#CREATES AN OPEN FILE VARIABLE IN PYTHON
			
			csvReader = csv.reader(csvFile)
			
			#CREATES A LIST FROM THE OPEN FILE VARIABLE
			
			csvList = list(csvReader)
			
			#CREATES THE ITERABLE TO RUN BASE ON HOW MANY ROWS
			
			runThis = (len(csvList))
			
			#ITERATIVELY APPENDS VALUES TO CORRESPONDING COLUMN FROM OPEN CSV
		
			for x in range(1, runThis):
								
				nextVal = csvList[x][column]
				
				newCSV[x].append(nextVal)
							
#CALLS THE FUNCTION TO RUN 							

combine(shortFilenames)	

# function exports the newCSV list as an .CSV file

def export(newCSV):
	
	outputFile = open (usr.sel + '.csv', 'w', newline='')
	
	outputWriter = csv.writer(outputFile)
			
	outputWriter.writerows(newCSV)
		
	outputFile.close()
		
export(newCSV)



	

		








