# -*- coding: utf-8 -*-
""" Script for archiving the master report file (Microsoft XLSM file) and the corresponding .STLs (point cloud files)
related to J&L Dimensional GE Unison Production for the GE Parts: M19, M07, M90, M84, and M30 respectively"""

# Company: J&L Dimensional Incorporated
# Author: Jonathan Thomas Heins
# Date: 11/16/2016

import os
import zipfile
import re
import glob


def change_dir(location):
    # !!FIX: could remove this worthless function, functionality/purpose changed shortly after I created it.
    os.chdir(location)


def master_file(directory, filetype='.xlsm'):
    """finds the master report file in a given directory"""
    files = []

    for file in os.listdir(directory):

        if file.endswith(filetype):
            files = file

        return files


def file_list(directory, filetype='.stl'):
    """Appends all files with specified extension in chosen directory to a list called files"""

    files = []

    for file in os.listdir(directory):

        if file.endswith(filetype):
            files.append(file)

    return files


def master_file_name(full_file):
    """Creates the master file name from the file name with an extension"""

    # removes the extension from a file and returns just the filename
    return os.path.splitext(full_file)[0]


def first_run_name(part_number_input):
    """Creates the basename from the path and user input of the part number"""
    # !!FIX: probably a better way to get the last directory without the full path.
    mold_and_number = re.split(r"\\", os.getcwd())[-1]
    first_name = part_number_input + ' ' + mold_and_number

    return first_name


def rework_name(basename):
    """Creates the rework names for compressed folders from the output (or basename) from the first_run_name Function"""
    # !!FIX: probably a better way to get the last directory without the full path.
    rework_number = re.split(r"\\", os.getcwd())[-1]
    rework_file_name = basename + ' ' + rework_number
    return rework_file_name


def zip(folder_name, files_to_be_zipped):
    """Creates a zip object from folder_name and zips a list of files (files_to_be_zipped)"""

    # creates the zipped folder, D'OH
    zip_file_name = folder_name + '.zip'

    if type(files_to_be_zipped) != type([]):
        files_to_be_zipped = [files_to_be_zipped]

    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_folder:

        # !!FIX: could use a list comprehension here instead.
        for item in files_to_be_zipped:

            zip_folder.write(item)

            if not re.findall(".xlsm", item):
                os.remove(item)

    zipfile.ZipFile.close(zip_folder)


def master_zip(path, extension='xlsm'):
    """Instantiates the compression functions for zipping the master report file seperately"""
    # Kind of lame, could probably do in less steps.
    master_with_extension = master_file(path, extension)
    master_name = master_file_name(master_with_extension)
    zip(master_name, master_with_extension)


def stl_zip(path, output_file_name):
    """Instantiates the compression functions for zipping the .STL files separately"""

    # Checks to see if directory is empty, removes if it is.
    # Also finds if there is an mistake in any directory
    stl_list = file_list(path)

    # !!FIX: find a less "special" way of doing this so that PEP will shut up.
    if stl_list != []:

        zip(output_file_name, stl_list)

    elif os.listdir(path) == []:

        os.chdir('..')
        os.rmdir(path)

    else:
        print('There appears to be something in:\n\n{}\n\nHere is the contents:\n\n{}'.format(os.getcwd(),
                                                                                              os.listdir(path)))


def subdirectories():
    """returns the subdirectories in the current path"""
    # !!FIX: another stupid function, but might as well leave alone.
    current_subdirectories = glob.glob('*/')
    return current_subdirectories


def reworks(first_run):
    """Instantiates the stl_zip functions for rework scans"""
    # moves to the rework folder and gets rework 1,2,3,4,etc.
    rework_switch = subdirectories()
    change_dir(DIR_PATH + '\\' + rework_switch[0])
    new_directory = os.getcwd()

    rework_directories = subdirectories()

    for folders in rework_directories:
        # jumps into _Rework directory
        os.chdir(new_directory + '\\' + folders)
        present_directory = os.getcwd()

        # creates the rework folder compressed folder name
        re_work_name = rework_name(first_run)
        # print(re_work_name)

        # instantiates zipping of .STL's
        stl_zip(present_directory, re_work_name)


# !!! TO_DO: basically copy script functionality from below from the if name is main statement and
#            use inputs for from GUI.

if __name__ == '__main__':
    # change this to dialog box variable someday
    change_dir('C://Users//jheins3//Desktop//GE UNISON//PRODUCTION//GE2679M19 Production//Mold 281')

    DIR_PATH = os.getcwd()
    print(DIR_PATH)

    output_file_basename = 'M07 '
    # print(output_file_basename)

    # zips the master file separately
    master_zip(DIR_PATH)

    # Creates the first name for first run, reused to rename the rework folders
    FIRST_RUN = first_run_name('M07')
    # print(FIRST_RUN)

    # Runs the compression functions on first run .STL files, HOORAY
    stl_zip(DIR_PATH, FIRST_RUN)

    # Runs the compression functions iteratively over the .STL files in the Rework Folders, Winter is Coming
    reworks(FIRST_RUN)
