
import shutil
import os
import time
import json
import sys
import re
import pandas as pd
import subprocess

sys.path.append('D:/work/github/PyTools/packages/tkutils/tkg_utils')
from SdkAdapter.SdkAdapter import SdkAdapter
from SdkInfoAdapter.SdkInfoAdapter import SdkInfoAdapter
from Utils.PrettyFile import PrettyFile
import Utils.FileUtils as FileUtils

#npm install -g --save-dev javascript-obfuscator
class SdkFile():
	def __init__(self, projectFolder):
		self.projectFolder = projectFolder;
		self.sdkFolder = f"{self.projectFolder}/sdk_configs"

		self.facebookSdkFile = "D:/work/github/MiniGamesCracker/FacebookUtils/SdkConfigs/Projects/FacebookSdk/build/web-mobile/assets/main/index.js"
		self.sdkUtilsFile = "D:/work/github/MiniGamesCracker/FacebookUtils/SdkConfigs/Projects/SdkUtils/build/web-mobile/assets/main/index.js"

		self.projectFacebookSdkFile = f"{self.sdkFolder}/tk_sdk_1.js"
		self.projectSdkUtilsFile = f"{self.sdkFolder}/tk_sdk_2.js"


	def doAddSdkFiles(self, obfuscateJsFile, isFB):
		FileUtils.copyFile(self.facebookSdkFile, self.projectFacebookSdkFile)
		if(not isFB):
			FileUtils.copyFile(self.sdkUtilsFile, self.projectSdkUtilsFile)

		if(not obfuscateJsFile):
			return

		self.obfuscateJsScript(self.projectFacebookSdkFile, self.projectFacebookSdkFile)
		if(not isFB):
			self.obfuscateJsScript(self.sdkUtilsFile, self.projectSdkUtilsFile)

	def obfuscateJsScript(self, indexJsFile, jsFile):
		options = {
			"debug-protection":"true",
			# "disable-console-output":"true"
		}
		optionStringList = ["--{} {}".format(item, options[item]) for item in options]
		optionString = " ".join(optionStringList)

		winCmd = 'javascript-obfuscator {} --output {} {}'.format(indexJsFile, jsFile, optionString)
		print(f"==> [obfuscateJsScript], indexJsFile: {indexJsFile}, jsFile: {jsFile}")
		os.system(winCmd)

class AppletAdapter():
	def __init__(self, adapterFolder, projectFolder, sdkName):
		self.adapterFolder = adapterFolder;
		self.projectFolder = projectFolder;
		self.assetFolder = f"{self.projectFolder}/assets"
		self.sdkName = sdkName;
		self.checkCreateAdapterFolders(self.sdkName)

		print("==> [AppletAdapter] [Init] self.adapterFolder:", os.path.abspath(self.adapterFolder))

	def doCollectPictures(self):
		pictureFiles = []
		pictureFiles.extend(FileUtils.getFiles(self.projectFolder, ".jpg"))
		pictureFiles.extend(FileUtils.getFiles(self.projectFolder, ".png"))

		for pictureFile in pictureFiles:
			fileName = FileUtils.getFileName(pictureFile, True)
			newFile = f"{self.projectFolder}/sdk_configs/PictureFiles/{fileName}"
			FileUtils.copyFile(pictureFile, newFile)

	def checkCreateAdapterFolders(self, sdkName):
		subAdapterFolders = [
			"SdkInfoAdapter",
			"SdkAdapter"
		]

		for subAdapterFolder in subAdapterFolders:
			defaultSdkFolder = f"{self.adapterFolder}/{subAdapterFolder}/Default"
			newSdkFolder = f"{self.adapterFolder}/{subAdapterFolder}/{sdkName}"

			files = FileUtils.getFiles(defaultSdkFolder)
			for file in files:
				relFile = os.path.relpath(file, defaultSdkFolder)
				newSdkFile = f"{newSdkFolder}/{relFile}"

				FileUtils.checkCopyFile(file, newSdkFile)

	def doChangeFBInstantToTkSdk(self):
		assetJsFiles = FileUtils.getFiles(self.projectFolder, ".js")
		for assetJsFile in assetJsFiles:
			fileData = FileUtils.readFile(assetJsFile)
			fbInstantReferenceCount = fileData.count("FBInstant")

			for x in range(fbInstantReferenceCount):
				fileData = fileData.replace("FBInstant", "TkSdk")
				pass
			FileUtils.writeFile(assetJsFile, fileData)
			print(f"==> [AppletAdapter] [doChangeFBInstantToTkSdk], fbInstantReferenceCount: {fbInstantReferenceCount:03}, file:{os.path.relpath(assetJsFile, self.projectFolder)}")
		pass

	def doPrettyFiles(self, hasCocos2dJs = False):
		assetFiles = []
		assetFiles.extend(FileUtils.getFiles(self.projectFolder, ".js"))
		assetFiles.extend(FileUtils.getFiles(self.projectFolder, ".json"))
		assetFiles = [item for item in assetFiles if("tk_sdk" not in item)]

		if(not hasCocos2dJs):
			assetFiles = [item for item in assetFiles if("cocos2d" not in item)]

		for assetJsFile in assetFiles:
			prettyFile = PrettyFile(assetJsFile)
			prettyFile.prettyFile()

	def doHookCocosMethod(self):
		assetFiles = []
		assetFiles.extend(FileUtils.getFiles(self.projectFolder, ".js"))
		assetFiles = [item for item in assetFiles if("cocos2d" in item)]
		addLines = [
			# CocosAddLine("._instantiate(null, !0)", -1, "window.HookUtils && window.HookUtils.onNodeInstantiate && window.HookUtils.onNodeInstantiate(arguments);"),
			# CocosAddLine("this._super(), this._removeGraphics()", 0, "window.HookUtils && window.HookUtils.onNodeDestroy && window.HookUtils.onNodeDestroy(this.node);"),
			CocosAddLine('.emit("active-in-hierarchy-changed"', 0, "window.HookUtils && window.HookUtils.onNodeActive && window.HookUtils.onNodeActive(arguments[0],arguments[1]);")
		]

		for assetJsFile in assetFiles:
			for addLine in addLines:
				fileData = FileUtils.readFile(assetJsFile)
				fileLines = fileData.split("\n")
				tagLineComps = [(addLine.tagLine in item) for item in fileLines]
				tagLineIndex = tagLineComps.index(True)

				insertLineComps = [item for item in fileLines if(addLine.insertLine in item)]
				hasInsertLineInFileData = len(insertLineComps) > 0

				if(hasInsertLineInFileData):
					continue;

				insertLineIndex = tagLineIndex + addLine.offsetLineIndex
				fileLines.insert(insertLineIndex, addLine.insertLine)
				FileUtils.writeFile(assetJsFile, "\n".join(fileLines))
				print("==> [AppletAdapter] [doHookCocosMethod]:" + json.dumps(addLine.__dict__, indent = 4))

	def doUglyFiles(self):
		assetFiles = []
		assetFiles.extend(FileUtils.getFiles(self.assetFolder, ".js"))

		for assetJsFile in assetFiles:
			prettyFile = PrettyFile(assetJsFile)
			prettyFile.doUglyFile()

	def doAdaptSdk(self):
		sdkAdapter = SdkAdapter(self.adapterFolder, self.projectFolder, self.sdkName)
		sdkAdapter.doAddSdkFiles()
		sdkAdapter.doChangeSdkLines()

	def doChangeSdkInfos(self):
		sdkInfoAdapter = SdkInfoAdapter(self.adapterFolder, self.projectFolder, self.sdkName)
		sdkInfoAdapter.doChangeSdkInfos()

	def doAddSdkFiles(self, obfuscateJsFile, isFB):
		sdkFile = SdkFile(self.projectFolder)
		sdkFile.doAddSdkFiles(obfuscateJsFile, isFB)



class CocosAddLine():
	def __init__(self, tagLine, offsetLineIndex, insertLine):
		self.tagLine = tagLine
		self.offsetLineIndex = offsetLineIndex
		self.insertLine = insertLine





