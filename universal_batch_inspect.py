# -*- coding: utf-8 -*-

import gom
import glob
import os
usr=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
' <title>Batch Inspect</title>' \
' <style>Standard</style>' \
' <control id="OkCancel"/>' \
' <position>center</position>' \
' <embedding></embedding>' \
' <sizemode>fixed</sizemode>' \
' <size width="340" height="169"/>' \
' <content rows="2" columns="1">' \
'  <widget rowspan="1" row="0" column="0" columnspan="1" type="label">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Select Folder Where .STL\'s are located</text>' \
'  </widget>' \
'  <widget rowspan="1" row="1" column="0" columnspan="1" type="input::file">' \
'   <name>file</name>' \
'   <tooltip></tooltip>' \
'   <type>directory</type>' \
'   <title>Choose File</title>' \
'   <default>Y:/GE UNISON/PRODUCTION</default>' \
'   <limited>false</limited>' \
'   <file_types/>' \
'   <file_types_default></file_types_default>' \
'  </widget>' \
' </content>' \
'</dialog>')

os.chdir(usr.file)
filenames = glob.glob((usr.file + '\*.stl'))

DIALOG=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
' <title>Batch Inspect</title>' \
' <style>Standard</style>' \
' <control id="Close"/>' \
' <position>center</position>' \
' <embedding></embedding>' \
' <sizemode>fixed</sizemode>' \
' <size width="342" height="157"/>' \
' <content rows="2" columns="1">' \
'  <widget rowspan="1" row="0" column="0" columnspan="1" type="label">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Progress</text>' \
'  </widget>' \
'  <widget rowspan="1" row="1" column="0" columnspan="1" type="display::progressbar">' \
'   <name>progressbar</name>' \
'   <tooltip></tooltip>' \
'   <value>0</value>' \
'   <minimum>0</minimum>' \
'   <maximum>100</maximum>' \
'   <parts>1</parts>' \
'   <step>0</step>' \
'   <text>percentage</text>' \
'   <mode>system</mode>' \
'  </widget>' \
' </content>' \
'</dialog>')

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	pass

DIALOG.handler = dialog_event_handler

gom.script.sys.open_user_defined_dialog (dialog=DIALOG)

shortFilenames = [{} for i in range(len(filenames))]

for index in range(len(filenames)):
	
	# assigns shortFilenames the path to .STL file
	
	shortFilenames[index] = os.path.basename(str(filenames[index]))
	
	# imports STL, runs inspection, exports .CSV
	
	gom.script.sys.import_stl (
		bgr_coding=True, 
		files = [str(filenames[index])], 
		import_mode='replace_elements', 
		length_unit='inch', 
		stl_color_bit_set=False, 
		target_type='mesh')
	
	gom.script.sys.recalculate_project ()

	gom.script.table.export_table_contents (
	cell_separator=',', 
	codec='iso 8859-1', 
	decimal_separator='.', 
	elements= gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'inspection']}), 
	file= usr.file + '//' + str((shortFilenames[index])[:-4]) + '.csv', 
	header_export=True, 
	line_feed='\n', 
	sort_column=0, 
	sort_order='ascending', 
	template_name='Overview', 
	text_quoting='', 
	write_one_line_per_element=False)

	print(usr.file + '//' + str((shortFilenames[index])[:-4]) + '.csv')
#	gom.script.table.export_table_contents (
#	cell_separator=',', 
#	codec='iso 8859-1', 
#	decimal_separator='.', 
#	elements=[gom.app.project.inspection['Z1.dN'], gom.app.project.inspection['Y2.dN'], gom.app.project.inspection['X1.dN'], gom.app.project.inspection['Y1.dN'], gom.app.project.inspection['X3.dN'], gom.app.project.inspection['X2.dN'], gom.app.project.inspection['3.dN'], gom.app.project.inspection['5.dN'], gom.app.project.inspection['6.dN'], gom.app.project.inspection['4.dN'], gom.app.project.inspection['1.dN'], gom.app.project.inspection['12.dN'], gom.app.project.inspection['11.dN'], gom.app.project.inspection['10.dN'], gom.app.project.inspection['7.dN'], gom.app.project.inspection['8.dN'], gom.app.project.inspection['9.dN'], gom.app.project.inspection['2.dN'], gom.app.project.inspection['13.dN'], gom.app.project.inspection['15.dN'], gom.app.project.inspection['16.dN'], gom.app.project.inspection['17.dN'], gom.app.project.inspection['18.dN'], gom.app.project.inspection['14.dN'], gom.app.project.inspection['20.dN'], gom.app.project.inspection['19.dN'], gom.app.project.inspection['22.dN'], gom.app.project.inspection['21.dN'], gom.app.project.inspection['23.dN'], gom.app.project.inspection['25.dN'], gom.app.project.inspection['26.dN'], gom.app.project.inspection['24.dN'], gom.app.project.inspection['LEANGTH_2.L'], gom.app.project.inspection['LEANGTH_1.L'], gom.app.project.inspection['LEANGTH_3.L'], gom.app.project.inspection['28.dN'], gom.app.project.inspection['27.dN'], gom.app.project.inspection['29.dN'], gom.app.project.inspection['30.dN'], gom.app.project.inspection['31.dN'], gom.app.project.inspection['34.dN'], gom.app.project.inspection['32.dN'], gom.app.project.inspection['33.dN'], gom.app.project.inspection['35.dN'], gom.app.project.inspection['37.dN'], gom.app.project.inspection['36.dN'], gom.app.project.inspection['TEANGTH_2.L'], gom.app.project.inspection['TEANGTH_1.L'], gom.app.project.inspection['TEANGTH_3.L'], gom.app.project.inspection['41.dN'], gom.app.project.inspection['39.dN'], gom.app.project.inspection['38.dN'], gom.app.project.inspection['40.dN'], gom.app.project.inspection['43.dN'], gom.app.project.inspection['44.dN'], gom.app.project.inspection['42.dN'], gom.app.project.inspection['45.dN'], gom.app.project.inspection['46.dN'], gom.app.project.inspection['47.dN'], gom.app.project.inspection['48.dN'], gom.app.project.inspection['50.dN'], gom.app.project.inspection['49.dN'], gom.app.project.inspection['51.dN'], gom.app.project.inspection['53.dN'], gom.app.project.inspection['52.dN'], gom.app.project.inspection['54.dN'], gom.app.project.inspection['55.dN'], gom.app.project.inspection['56.dN'], gom.app.project.inspection['57.dN'], gom.app.project.inspection['58.dN'], gom.app.project.inspection['62.dN'], gom.app.project.inspection['61.dN'], gom.app.project.inspection['60.dN'], gom.app.project.inspection['59.dN'], gom.app.project.inspection['64.dN'], gom.app.project.inspection['63.dN'], gom.app.project.inspection['65.dN'], gom.app.project.inspection['66.dN'], gom.app.project.inspection['67.dN'], gom.app.project.inspection['69.dN'], gom.app.project.inspection['70.dN'], gom.app.project.inspection['71.dN'], gom.app.project.inspection['77.dN'], gom.app.project.inspection['79.dN'], gom.app.project.inspection['78.dN'], gom.app.project.inspection['76.dN'], gom.app.project.inspection['75.dN'], gom.app.project.inspection['74.dN'], gom.app.project.inspection['73.dN'], gom.app.project.inspection['72.dN'], gom.app.project.inspection['68.dN'], gom.app.project.inspection['81.dN'], gom.app.project.inspection['82.dN'], gom.app.project.inspection['83.dN'], gom.app.project.inspection['80.dN'], gom.app.project.inspection['85.dN'], gom.app.project.inspection['84.dN'], gom.app.project.inspection['87.dN'], gom.app.project.inspection['86.dN'], gom.app.project.inspection['Sec A-A.TE PET +0.035000 in.L'], gom.app.project.inspection['89.dN'], gom.app.project.inspection['88.dN'], gom.app.project.inspection['Sec A-A.TE PET +0.150000 in.L'], gom.app.project.inspection['90.dN'], gom.app.project.inspection['Sec A-A.Maximum chord.L'], gom.app.project.inspection['92.dN'], gom.app.project.inspection['94.dN'], gom.app.project.inspection['95.dN'], gom.app.project.inspection['96.dN'], gom.app.project.inspection['93.dN'], gom.app.project.inspection['91.dN'], gom.app.project.inspection['Sec B-B.TE PET +0.035000 in.L'], gom.app.project.inspection['Sec B-B.TE PET +0.150000 in.L'], gom.app.project.inspection['98.dN'], gom.app.project.inspection['99.dN'], gom.app.project.inspection['100.dN'], gom.app.project.inspection['97.dN'], gom.app.project.inspection['101.dN'], gom.app.project.inspection['Sec B-B.Maximum chord.L'], gom.app.project.inspection['106.dN'], gom.app.project.inspection['103.dN'], gom.app.project.inspection['102.dN'], gom.app.project.inspection['104.dN'], gom.app.project.inspection['105.dN'], gom.app.project.inspection['107.dN'], gom.app.project.inspection['108.dN'], gom.app.project.inspection['110.dN'], gom.app.project.inspection['111.dN'], gom.app.project.inspection['113.dN'], gom.app.project.inspection['118.dN'], gom.app.project.inspection['117.dN'], gom.app.project.inspection['114.dN'], gom.app.project.inspection['115.dN'], gom.app.project.inspection['116.dN'], gom.app.project.inspection['109.dN'], gom.app.project.inspection['112.dN'], gom.app.project.inspection['Sec C-C.TE PET +0.035000 in.L'], gom.app.project.inspection['Sec C-C.TE PET +0.150000 in.L'], gom.app.project.inspection['Sec C-C.Maximum chord.L'], gom.app.project.inspection['119.dN'], gom.app.project.inspection['PNT_1.dN'], gom.app.project.inspection['PNT_2.dN'], gom.app.project.inspection['PNT_3.dN'], gom.app.project.inspection['PNT1 to PNT2.LXY'], gom.app.project.inspection['PNT1 to PNT3.LXY'], gom.app.project.inspection['AD1.dN'], gom.app.project.inspection['AC1.dN'], gom.app.project.inspection['TIP STEP.L'], gom.app.project.inspection['127.dN'], gom.app.project.inspection['126.dN'], gom.app.project.inspection['124.dN'], gom.app.project.inspection['123.X'], gom.app.project.inspection['125.dN'], gom.app.project.inspection['122.Y'], gom.app.project.inspection['121.Y'], gom.app.project.inspection['120.Y'], gom.app.project.inspection['pt6.dN'], gom.app.project.inspection['CC_DO.dN'], gom.app.project.inspection['AA_DO.dN'], gom.app.project.inspection['DD_DO.dN'], gom.app.project.inspection['BB_DO.dN'], gom.app.project.inspection['128.dN'], gom.app.project.inspection['129.dN'], gom.app.project.inspection['130.dN'], gom.app.project.inspection['DD_DO.3.dN'], gom.app.project.inspection['DD_DO.4.dN'], gom.app.project.inspection['DD_DO.5.dN'], gom.app.project.inspection['DD_DO.6.dN'], gom.app.project.inspection['DD_DO.7.dN'], gom.app.project.inspection['DD_DO.8.dN'], gom.app.project.inspection['DD_DO.9.dN'], gom.app.project.inspection['DD_DO.10.dN'], gom.app.project.inspection['DD_DO.11.dN'], gom.app.project.inspection['DD_DO.12.dN'], gom.app.project.inspection['DD_DO.13.dN'], gom.app.project.inspection['DD_DO.14.dN'], gom.app.project.inspection['DD_DO.15.dN'], gom.app.project.inspection['DD_DO.16.dN'], gom.app.project.inspection['DD_DO.17.dN'], gom.app.project.inspection['DD_DO.1.dN'], gom.app.project.inspection['BB_DO.11.dN'], gom.app.project.inspection['BB_DO.3.dN'], gom.app.project.inspection['CC_DO.13.dN'], gom.app.project.inspection['CC_DO.14.dN'], gom.app.project.inspection['CC_DO.15.dN'], gom.app.project.inspection['CC_DO.16.dN'], gom.app.project.inspection['CC_DO.17.dN'], gom.app.project.inspection['CC_DO.1.dN'], gom.app.project.inspection['AA_DO.8.dN'], gom.app.project.inspection['AA_DO.7.dN'], gom.app.project.inspection['AA_DO.6.dN'], gom.app.project.inspection['BB_DO.16.dN'], gom.app.project.inspection['BB_DO.5.dN'], gom.app.project.inspection['BB_DO.17.dN'], gom.app.project.inspection['BB_DO.13.dN'], gom.app.project.inspection['BB_DO.14.dN'], gom.app.project.inspection['CC_DO.12.dN'], gom.app.project.inspection['AA_DO.13.dN'], gom.app.project.inspection['BB_DO.15.dN'], gom.app.project.inspection['BB_DO.8.dN'], gom.app.project.inspection['BB_DO.1.dN'], gom.app.project.inspection['AA_DO.2.dN'], gom.app.project.inspection['AA_DO.3.dN'], gom.app.project.inspection['AA_DO.4.dN'], gom.app.project.inspection['AA_DO.12.dN'], gom.app.project.inspection['AA_DO.5.dN'], gom.app.project.inspection['CC_DO.11.dN'], gom.app.project.inspection['CC_DO.10.dN'], gom.app.project.inspection['CC_DO.9.dN'], gom.app.project.inspection['CC_DO.8.dN'], gom.app.project.inspection['CC_DO.7.dN'], gom.app.project.inspection['BB_DO.4.dN'], gom.app.project.inspection['BB_DO.2.dN'], gom.app.project.inspection['BB_DO.10.dN'], gom.app.project.inspection['BB_DO.7.dN'], gom.app.project.inspection['AA_DO.1.dN'], gom.app.project.inspection['AA_DO.17.dN'], gom.app.project.inspection['AA_DO.16.dN'], gom.app.project.inspection['BB_DO.12.dN'], gom.app.project.inspection['AA_DO.15.dN'], gom.app.project.inspection['AA_DO.14.dN'], gom.app.project.inspection['AA_DO.10.dN'], gom.app.project.inspection['AA_DO.9.dN'], gom.app.project.inspection['AA_DO.11.dN'], gom.app.project.inspection['CC_DO.6.dN'], gom.app.project.inspection['CC_DO.5.dN'], gom.app.project.inspection['CC_DO.4.dN'], gom.app.project.inspection['CC_DO.3.dN'], gom.app.project.inspection['CC_DO.2.dN'], gom.app.project.inspection['BB_DO.9.dN'], gom.app.project.inspection['BB_DO.6.dN'], gom.app.project.inspection['DD_DO.2.dN']], 
#	file= usr.file + '//' + str((shortFilenames[index])[:-4]) + '.csv', 
#	header_export=True, 
#	line_feed='\n', 
#	sort_column=0, 
#	sort_order='ascending', 
#	template_name='Overview', 
#	text_quoting='', 
#	write_one_line_per_element=False)

gom.script.sys.close_user_defined_dialog (dialog=DIALOG)
DIALOG=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
' <title>Batch Inspect</title>' \
' <style>Standard</style>' \
' <control id="OkCancel"/>' \
' <position>center</position>' \
' <embedding>always_toplevel</embedding>' \
' <sizemode>fixed</sizemode>' \
' <size width="237" height="122"/>' \
' <content rows="1" columns="1">' \
'  <widget rowspan="1" row="0" column="0" columnspan="1" type="display::text">' \
'   <name>text</name>' \
'   <tooltip></tooltip>' \
'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
'p, li { white-space: pre-wrap; }' \
'&lt;/style>&lt;/head>&lt;body style="    ">' \
'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Batch Inspect Ran Successfully&lt;/p>&lt;/body>&lt;/html></text>' \
'   <wordwrap>false</wordwrap>' \
'  </widget>' \
' </content>' \
'</dialog>')

#
# Event handler function called if anything happens inside of the dialog
#
def dialog_event_handler (widget):
	pass

DIALOG.handler = dialog_event_handler

RESULT=gom.script.sys.show_user_defined_dialog (dialog=DIALOG)



