#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import os
import errno
import subprocess
import re
import jdk


def InstallModules():
	print("installing required modules....")
	tool_modules = ["install-jdk"]
	for i in range(len(tool_modules)):
		os.system("pip3 install "+tool_modules[i])


def checkJava():
	java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
	java_version = java_version.decode('utf-8')
	print(java_version)
	try:
		print("*************Java Version***************")
		pattern = '\"(\d+\.\d+).*\"'
		print(re.search(pattern, java_version).groups()[0])
	except AttributeError:
		print("Java not installed... re run the command and enter install with version...")


def installJava(java_version):
	print("Your OS :"+jdk.OS)
	print("Your CPU architecture :" + jdk.ARCH)
	jdk.install(java_version+'')


def helpCommand():
	print("1) 'exists' command to check if Java exists in your system or not")
	print("2) 'version' command to display Java Version installed")
	print("3) 'install' command to install java in your system")
	print("4) 'help' list all commands for the tool...")

if __name__ == "__main__":
	try:
		size = len(sys.argv)

		if size == 1:
			InstallModules()
			sys.exit()
		if sys.argv[1] == "help":
			helpCommand()
		elif sys.argv[1] == "exists":
			checkJava()
		elif sys.argv[1] == "version":
			checkJava()
		elif sys.argv[1] == "install":
			try:
				installJava(sys.argv[2])
			except IndexError:
				print("Enter Java Version to install")
				sys.exit()
		else:
			print("Command not found")
	except KeyboardInterrupt:
		print("Bye !!! Have a nice day!")
		sys.exit()


# In[ ]:




