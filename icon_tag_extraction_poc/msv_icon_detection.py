from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

images_folder = "/home/rits/Documents/Assets/UAE_identity/EID_back_images"
SUBSCRIPTION_KEY = 'abc1234hjkltttttttttttyyyyyyyyyyyyyyyyyyyyyy'
ENDPOINT = 'https://dfmscomputervision.cognitiveservices.azure.com'

computervision_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(SUBSCRIPTION_KEY))

local_image_path = os.path.join(images_folder, "eid_back6.jpg")
local_image = open(local_image_path, "rb")

# Call API
# description_result = computervision_client.describe_image_in_stream(local_image)
# print("--------description_result---------")
# print(description_result)
# print(dir(description_result))
# print(dir(description_result.captions))
# print("--------description_result---------")

local_image_features = ["categories"]

# # Call API
categorize_results_local = computervision_client.analyze_image_in_stream(local_image, local_image_features)
# print('-----------categorize_results_local----------------')
# print(categorize_results_local)
# print('-----------categorize_results_local----------------')

# Get the captions (descriptions) from the response, with confidence level
print("Description of local image: ")
if (len(description_result.captions) == 0):
    print("No description detected.")
else:
    for caption in description_result.captions:
        print("--------caption------------")
        print(caption)
        print("--------caption------------")
        # print("'{}' with confidence {:.2f}%".format(caption, caption.confidence * 100))
