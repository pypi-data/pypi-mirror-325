
import shutil
import os
import time
import json
import sys
import re
import pandas as pd
import subprocess

import Utils.FileUtils as FileUtils
from Normal.ItemInfo import ItemInfo

from SdkAdapter.FileItem import FileItem
from SdkAdapter.FileContentAdapter import FileContentAdapter
from SdkAdapter.FileAdapter import FileAdapter

class SdkAdapter():
	def __init__(self, adapterFolder, projectFolder, sdkName):
		self.projectFolder = projectFolder
		self.adapterFolder = adapterFolder
		self.sdkName = sdkName
		self.sdkAdapterFolder = f"{self.adapterFolder}/SdkAdapter/{self.sdkName}"
		self.sdkAdapterExcel = f"{self.projectFolder}/sdk_configs/{sdkName}/SdkAdapter.xls"
		configSdkAdapterExcel = f"{self.sdkAdapterFolder}/SdkAdapter.xls"
		if(not os.path.exists(self.sdkAdapterExcel)):
			FileUtils.copyFile(configSdkAdapterExcel, self.sdkAdapterExcel)
		self.sdkAdapterInfos = FileUtils.readConfigExcel(self.sdkAdapterExcel)
		self.sdkAdapterInfos = [ItemInfo(item) for item in self.sdkAdapterInfos]

	def doAddSdkFiles(self):
		for sdkAdapterInfo in self.sdkAdapterInfos:
			if(sdkAdapterInfo.isForAdapt):
				sdkName = sdkAdapterInfo.sdkName
				self._doAddSdkFiles(sdkName)
	
	def doChangeSdkLines(self):
		for sdkAdapterInfo in self.sdkAdapterInfos:
			if(sdkAdapterInfo.isForAdapt):
				sdkName = sdkAdapterInfo.sdkName
				self._doChangeSdkLines(sdkName)

	def _doAddSdkFiles(self, sdkName):
		fileAdapter = FileAdapter(self.projectFolder)
		fileAdapter.doAdapt(self.sdkAdapterFolder, sdkName)

	def _doChangeSdkLines(self, sdkName):
		fileContentAdapter = FileContentAdapter(self.projectFolder)
		fileContentAdapter.doAdapt(self.sdkAdapterFolder, sdkName)



