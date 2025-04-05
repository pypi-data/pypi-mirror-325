#!/usr/bin/python
# -*-coding: utf-8-*-

import jsbeautifier
import json
import Utils.FileUtils as FileUtils

class PrettyFile():
	def __init__(self, assetFile):
		self.assetFile = assetFile

	def doUglyFile(self):
		if(not self.assetFile.endswith(".js")):
			return

		print("==> [PrettyFile] [uglyFile]", self.assetFile)
		options = {
			"eol": "",
		    "indent_size": 0
		}
		jsData = FileUtils.readFile(self.assetFile)
		newJsData = jsbeautifier.beautify(jsData, options)
		FileUtils.writeFile(self.assetFile, newJsData)

	def prettyFile(self):
		# self.doPrettyJsonFile()
		self.doPrettyJavaScriptFile()
		self.doPrettyHtmlFile()
		pass

	def doPrettyJsonFile(self):
		if(not self.assetFile.endswith(".json")):
			return

		print("==> [PrettyFile] [doPrettyJsonFile]", self.assetFile)
		jsonData = FileUtils.readFile(self.assetFile)
		jsonMap = json.loads(jsonData)
		newData = json.dumps(jsonMap, indent = 4, ensure_ascii = False)
		FileUtils.writeFile(self.assetFile, newData)

	def doPrettyJavaScriptFile(self):
		if(not self.assetFile.endswith(".js")):
			return

		print("==> [PrettyFile] [doPrettyJavaScriptFile]", self.assetFile)
		jsData = FileUtils.readFile(self.assetFile)
		newJsData = jsbeautifier.beautify(jsData)
		FileUtils.writeFile(self.assetFile, newJsData)


	def doPrettyHtmlFile(self):
		if(not self.assetFile.endswith(".html")):
			return

		print("==> [PrettyFile] [doPrettyHtmlFile]", self.assetFile)
		jsData = FileUtils.readFile(self.assetFile)
		newJsData = jsbeautifier.beautify(jsData)
		FileUtils.writeFile(self.assetFile, newJsData)

		

