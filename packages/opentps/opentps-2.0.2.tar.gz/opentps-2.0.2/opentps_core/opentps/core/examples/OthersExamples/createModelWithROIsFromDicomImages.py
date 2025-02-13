"""
This file contains an example on how to:
- read dicom data from a 4DCT folder
- create a dynamic 3D sequence with the 4DCT data
- read an rtStruct dicom file
- create a dynamic 3D model and compute the midP image with the dynamic 3D sequence
- create a patient, give him the model and rtStruct and save it as serialized data

!!! does not work with public data for now since there is no struct in the public data !!!
"""

import os
import sys
import time
import numpy as np

from pydicom.uid import generate_uid
from opentps.core.io.dataLoader import readData
from opentps.core.data.dynamicData._dynamic3DSequence import Dynamic3DSequence
from opentps.core.io.serializedObjectIO import saveSerializedObjects
from opentps.core.data.dynamicData._dynamic3DModel import Dynamic3DModel
from opentps.core.data._patient import Patient


if __name__ == '__main__':

    # chose the patient folder, which will be used as the patient name
    patientName = 'Patient_0'
    organ = 'liver'
    basePath = 'D:/ImageData/'

    # chose the 4DCT data folder
    data4DPath = basePath + organ + '/' + patientName + '/4DCT'
    # chose the dicom rtStruct file
    dataStructPath = basePath + organ + '/' + patientName + '/MidP_CT_rtstruct.dcm'
    # chose a path to save the results
    savingPath = basePath + organ + '/' + patientName + '/dynModAndROIs'

    # load the 4DCT data
    data4DList = readData(data4DPath)
    print(len(data4DList), 'images found in the folder')
    print('Image type =', type(data4DList[0]))
    print('Image 0 shape =', data4DList[0].gridSize)

    ## create a Dynamic3DSequence and change its name
    dynSeq = Dynamic3DSequence(dyn3DImageList=data4DList)
    dynSeq.name = '4DCT'


    # load the rtStruct data and print its content
    structData = readData(dataStructPath)[0]
    print('Available ROIs')
    structData.print_ROINames()

    ## create Dynamic3DModel
    model3D = Dynamic3DModel()

    ## change its name
    model3D.name = 'MidP'

    ## give it an seriesInstanceUID
    model3D.seriesInstanceUID = generate_uid()

    ## generate the midP image and deformation fields from the dynamic 3D sequence
    startTime = time.time()
    model3D.computeMidPositionImage(dynSeq, tryGPU=True)
    stopTime = time.time()

    print(model3D.midp.name)
    print('MidP computed in ', np.round(stopTime-startTime))

    # Create a patient and give it the patient name
    patient = Patient()
    patient.name = patientName
    # Add the model and rtStruct to the patient
    patient.appendPatientData(model3D)
    patient.appendPatientData(structData)

    ## Save it as a serialized object
    saveSerializedObjects(patient, savingPath)
