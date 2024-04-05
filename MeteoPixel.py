#!/usr/bin/env python
#! coding: utf-8
#! python3
# TheDarkTiger 2024
# Generate sounds to make a weather bulletin from text files

import os
import subprocess


#==============================================================================
# Eye candy

def info( text ) :
	print( "   info   : " + text )

def good( text ) :
	print( "   good   : " + text )

def warning( text ) :
	print( "(warning) : " + text )

def error( text ) :
	print( "[ ERROR ] : " + text )

def draw_spacer( char="=" ) :
	print( char*79 )


#----------------------------------------------------------------------
# Create dir if nonexistant (no way!, really?)
def create_dir_if_nonexistant( folderPath ):
	if not os.path.exists( folderPath ) :
		os.mkdir( folderPath )
	

#----------------------------------------------------------------------
# Generate audio from text
# 
# default is espeak, British English
def generate_speech( text, file ):
	
	cmd = f'espeak -p 60 -s 150 -v mb\mb-en1 -w "{file}" "{text}"'
	info( f"Generate speech: {text}" )
	subprocess.call( cmd )
	


#----------------------------------------------------------------------
# Normalize sound
# 
# default is 44100Hz, 16bits, mono
def normalize_sound( fileIn, fileOut, volume=1 ):
	
	if os.path.exists( fileIn ):
		cmd = f'sox -v {volume} "{fileIn}" -r 44100 -b 16 -c 1 "{fileOut}"'
		info( f"Normalize file: {fileIn}" )
		subprocess.call( cmd )
	else:
		error( f"Can't normalize {fileIn}, file don't exist" )
	


#----------------------------------------------------------------------
# Load a bulletin project file
# 
# Simple text file for now, will probably change in the future
def bulletin_load( fileName ):
	
	bulletin = {}
	bulletin["project"] = {"file":fileName, "folder":os.path.dirname(fileName)}
	bulletin["lines"] = []
	
	if os.path.exists( fileName ) :
		with open( fileName, "r" ) as file :
			bulletin["lines"] = file.readlines()
	else :
		error( "File {fileName} don't exist" )
	
	return bulletin


#----------------------------------------------------------------------
# Generate the bulletin
def bulletin_generate( bulletin, path ):
	
	# Make sure path exists
	create_dir_if_nonexistant( path )
	create_dir_if_nonexistant( f"{path}\\speech" )
	
	# Read each lines of the bulletin
	# Generate speech when needed
	index = 0
	fileList = []
	for line in bulletin["lines"]:
		line = line.strip()
		if (line[0]=='[') and (line[-1]==']'):
			rawFile = line[1:-1]
			
			# If filepath is not absolute, make it so
			if rawFile != os.path.abspath( rawFile ) :
				rawFile = os.path.abspath( bulletin["project"]["folder"] + "\\" + rawFile )
			
			volume = 1
			
		else:
			rawFile = f"{path}\\speech\\{index:02}_speech.wav"
			generate_speech( line, rawFile )
			volume = 0.9
			
		
		file = f"{path}\\{index:02}.wav"
		
		# The normalize is necesary for sox to stich everything in the end
		normalize_sound( rawFile, file, volume )
		
		# If the normalization suceeded, add the file to the stich list
		if os.path.exists( file ):
			fileList.append( file )
		
		index += 1
	
	# Ask sox to stitch everything together
	cmd = f"sox " + " ".join(fileList) + f" {path}\\out.ogg"
	info( f"Stitch files: {cmd}" )
	subprocess.call( cmd )
	
	return 0


#=============================================================================
# Main

if __name__ == "__main__" :
	
	fileName = "bulletin.txt"
	
	bulletin = bulletin_load( fileName )
	bulletin_generate( bulletin, "generated" )
	
