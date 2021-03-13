# encoding:	utf-8
# ----------------------------------------------------
# SCRIPT: 	TagLib Installer
# DESCR:	A simple installer
# ----------------------------------------------------
# (C) Vassil Kateliev, 2021  
# (C) http://www.kateliev.com
# (C) https://github.com/kateliev
# ----------------------------------------------------

# No warranties. By using this you agree
# that you use it at your own risk!

# - Dependencies --------------------------
from __future__ import print_function
from distutils.sysconfig import get_python_lib
import os, sys

# - Init
moduleName = 'taglib'
moduleSubPath = 'lib'

# - String
tr_head = '''
TagLib : A simple and tiny markup language library.
---------------------------------------------------
(C) Vassil Kateliev, 2021  
(C) https://github.com/kateliev
'''

# - Functions --------------------------
def installModule(srcDir, modulePathName):
	sitePackDir = get_python_lib()
	fileName = os.path.join(sitePackDir, '%s.pth' %modulePathName)
	
	print(tr_head)
	print('\nINFO:\t Installing %s library...\nPATH:\t%r\nFILE:\t%r\n\n' %(moduleName, srcDir, fileName))

	file = open(fileName, 'w')
	file.write(srcDir)
	file.close()

	return fileName

# - Run --------------------------
intallDir = os.path.join(os.path.dirname(os.path.normpath(os.path.abspath(sys.argv[0]))), moduleSubPath)
fileName = installModule(intallDir, moduleName)
print('DONE:\t%s installed!\nNOTE:\tRun script again if you change the location of the library' %moduleName)
