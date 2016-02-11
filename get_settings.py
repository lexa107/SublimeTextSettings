import sys
import os
from shutil import copyfile

def printHelp():
	print " Sublime Text 2 (3 not tested) settings getter. \
Part of Sublime Text 2 settings saver. Gets settings \
from Sublime Text folder and saves them into 'saved' \
folder. Settings can be committed to any repo and then \
be set into another instance of the editor. \n\n\
	Usage: \n\
	python get_setting.py <path>\n\n\
	<path> - path to the Sublime Text 2 root folder. If empty \
user will be prompt to enter this later."

def readFilesList(path):
	f = open(path, 'rt')
	file_type = None
	lists = { 'User':[] }
	for line in f:
		line = line[:-1]	# remove \n at the end of the line
		if line == 'User':
			file_type = line
		else:
			if (file_type is not None):
				lists[file_type].append(line)
	return lists

def gatherSettings(sublime_path):
	user_path = "/Data/Packages/User/"
	save_path = "saved"
	user_save_path = save_path + "/User/"

	lists = readFilesList("FilesToSave.txt")
	user_files = lists['User']

	if not os.path.exists(user_save_path):
		os.makedirs(user_save_path)

	for f in user_files:
			copyfile(sublime_path + user_path + f, user_save_path + f)

def main():
	if len(sys.argv) == 0:
		path = raw_input("Please enter path to sublime text or . to use current dir\n > ")
	else:
		if sys.argv[1] == "help":
			printHelp()
			exit()
		else:
			path = sys.argv[1]

	gatherSettings(path)

if __name__ == '__main__':
	main()