# coding: utf-8
# -----------------------------------------------------------------------------
# Copyright 2015 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

# ==================================================
# IncidentDensityTestCase.py
# --------------------------------------------------
# requirments: ArcGIS X.X, Python 2.7 or Python 3.4
# author: ArcGIS Solutions
# company: Esri
# ==================================================
# history:
# 12/16/2015 - JH - initial creation
# ==================================================

import unittest
import arcpy
import os
import UnitTestUtilities
import Configuration

class IncidentDensityTestCase(unittest.TestCase):
    ''' Test all tools and methods related to the Incident Density tool
    in the Incident Analysis toolbox'''
    
    #TODO: consolidate these common Incident Analysis variables
    proToolboxPath = os.path.join(Configuration.patterns_ToolboxesPath, "Incident Analysis Tools.tbx")
    desktopToolboxPath = os.path.join(Configuration.patterns_ToolboxesPath, "Incident Analysis Tools_10.3.tbx")
    scratchGDB = None
    incidentDataPath = os.path.join(Configuration.patternsPaths, "data")
    incidentGDB = os.path.join(incidentDataPath, "IncidentAnalysis.gdb")
    
    inputPointFeatures = None
    inputBoundaryFeatures = None
    
    def setUp(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.setUp")    
        UnitTestUtilities.checkArcPy()
        UnitTestUtilities.checkFilePaths([self.incidentDataPath, self.proToolboxPath, self.desktopToolboxPath])
        if (self.scratchGDB == None) or (not arcpy.Exists(self.scratchGDB)):
            self.scratchGDB = UnitTestUtilities.createScratch(self.incidentDataPath)
            
        
        self.inputPointFeatures = os.path.join(self.incidentGDB, "Incidents")
        self.inputBoundaryFeatures = os.path.join(self.incidentGDB, "Districts")
        
        
    def tearDown(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.tearDown")
        UnitTestUtilities.deleteScratch(self.scratchGDB)
        
    def test_incident_density_pro(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.test_incident_density_pro")
        arcpy.AddMessage("Testing Incident Density (Pro).")
        self.test_incident_density(self.proToolboxPath)
    
    def test_incident_density_desktop(self):
        if Configuration.DEBUG == True: print("     IncidentDensityTestCase.test_incident_density_desktop")
        arcpy.AddMessage("Testing Incident Density (Desktop).")
        self.test_incident_density(self.desktopToolboxPath)
        
    def test_incident_density(self, toolboxPath):
        try:
            if Configuration.DEBUG == True: print("     IncidentDensityTestCase.test_incident_density")
            
            arcpy.CheckOutExtension("Spatial")        
            # import the toolbox
            arcpy.ImportToolbox(toolboxPath, "iaTools")
            outputDensity = os.path.join(self.scratchGDB, "outputDensity")
            arcpy.IncidentDensity_iaTools(self.inputPointFeatures, self.inputBoundaryFeatures, outputDensity)
            arcpy.CheckInExtension("Spatial")
            self.assertTrue(arcpy.Exists(outputDensity))
            
        except arcpy.ExecuteError:
            UnitTestUtilities.handleArcPyError()
            
        except:
            UnitTestUtilities.handleGeneralError()
            
            