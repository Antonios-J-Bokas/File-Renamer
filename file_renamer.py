''' File Renamer 1.0 by Antonios J. Bokas | https://smoothanalyst.com '''

''' Notes '''

# This program renames large numbers of files that all belong to the same group.
# For example, a set of 200 photographs from the same photo shoot.

''' Imports '''

import os
import shutil
import time
from pathlib import Path

''' User-Defined Functions '''


def get_folder():

	# Request and validate directory path
	keep_going = True
	while keep_going:

		folder = input('\nEnter target folder (e.g., C:\\Users\\name\\Documents): ')
		print('')

		# Check if directory exists, if not, request new path
		if os.path.isdir(folder) == False:
			time.sleep(.3)
			print('   Error: Invalid folder. Check path and try again.')

		else:
			time.sleep(.3)
			print('   Folder located.')

			# Check if directory is empty, if so, request new directory
			if len(os.listdir(folder)) == 0:
				time.sleep(.3)
				if input('   Error: No files found in folder. Try another folder? (Y/N): ').lower() == 'n':
					print('   Process terminated.')
					keep_going = False
					return [False]
			else:
				return [True, folder]


def get_ext():

	# Request file extension
	ext_missing = True
	while ext_missing:

		# Request file extension
		ext = input('\nEnter extension of target files (e.g., txt): ')
		print('')

		# Check if directory contains extension
		for file in os.listdir(folder):
			if file.lower().endswith('.' + ext):
				ext_missing = False
				break

		# Extension not found
		if ext_missing == True:
			time.sleep(.3)
			print('   Error: No ' + str(ext).upper() + ' files found. '
				  'Enter another extension. ')
			continue

	time.sleep(.3)
	print('   Extension found.')
	return ext


def rename_files():

	# Request new file name
	series = input('\nEnter new series name: ')

	old_names = []
	count = 1

	# Record old name of and rename each file in directory
	for file in os.listdir(folder):
		if file.lower().endswith('.' + ext):
			old_names.append(file)
			shutil.move(folder + '/' + file,
                            folder + '/' + series + '-' + str(count) + '.' + ext)
			count += 1
	time.sleep(.3)
	print('\n   Rename complete.',
		  str(count - 1) + ' files renamed "' + series + '".')
	return old_names


def record_changes():

	# Ask if user wants record of name changes
	if input('\nExport changes to log? (Y/N): ').lower() == 'y':

		# Check if History folder exists, if not, make it
		log_folder = Path(folder + '\\History')
		if log_folder.exists() == False:
			os.makedirs(folder + '\\History')

		# Open or create new log
		log = open(folder + '\\History\\Rename_History.txt', 'a')

		# Write header and old names
		log.write('>>> Time of report: ' + time.ctime()
				  + '\n\nLocation: ' + str(folder)
				  + '\n\nThe following files were renamed:\n')
		for item in range(len(old_names)):
			log.write('\n   ' + old_names[item])

		# Write new names
		log.write('\n\nNew file names:\n')
		for file in os.listdir(folder):
			if file.lower().endswith('.' + ext):
				log.write('\n   ' + file)

		# Write footer and close log
		log.write('\n\nEND OF REPORT\n\n')
		log.close()
		time.sleep(.3)
		print('\n   Record created in ' + str(log_folder) + '.')

	else:
		time.sleep(.3)


''' Main Function '''

# Program name, author, purpose, and instructions
print('FILE RENAMER 1.0 - Rename Multiple Files in a Folder\nby Antonios J. Bokas'
      '\n\n----------------------------------------------------------------------'
      '\nINSTRUCTIONS'
      '\n\nThis program renames all files with a certain extension in a folder.'
      '\nFor example, if a folder contains the files "house.txt" and "car.txt",'
      '\nand you want them both to be named "property", it will rename them'
      '\n"property-1.txt" and "property-2.txt".'
      '\n----------------------------------------------------------------------')

# Check if directory is valid and has files
results = get_folder()
if results[0] == True:

	# Request file type, rename files, and record changes
	folder = results[1]
	ext = get_ext()
	old_names = rename_files()
	record_changes()

quit = input('\nPress Enter to quit.')
