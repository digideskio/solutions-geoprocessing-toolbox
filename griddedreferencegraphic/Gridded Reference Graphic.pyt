# coding: utf-8
'''
------------------------------------------------------------------------------
 Copyright 2017-2018 Esri
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
------------------------------------------------------------------------------
 ==================================================
 Gridded Reference Graphic.pyt
 --------------------------------------------------
 requirements: ArcGIS 10.3.1+, ArcGIS Pro 2.1+
 author: ArcGIS Solutions
 contact: support@esri.com
 company: Esri
 ==================================================
 description: 
 Python toolbox container for Gridded Reference Graphic.
 ==================================================
'''


from scripts.GRGTools import *


class Toolbox(object):
    '''
    Gridded Reference Graphic Toolbox class container.
    '''

    def __init__(self):
        ''' constructor '''
        self.label = u'Gridded Reference Graphic'
        self.alias = "grg"
		# NOTE: this description doesn't do anything, description shown in ArcGIS 
		# comes from the pyt.xml file
        self.description = u'A Geoprocessing Toolbox for ArcGIS for Desktop that contains collections of tools GRG operations.'

        self.tools = [

					# GRG
					CreateGRGFromArea,
					CreateGRGFromPoint,
					CreateReferenceSystemGRGFromArea,
					NumberFeatures,

					]
