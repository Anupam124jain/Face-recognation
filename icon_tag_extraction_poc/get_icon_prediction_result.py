import requests
image_loc = "/home/rits/Documents/Assets/UAE_identity/EID_New_Formats/eid_back9.jpg"
processed_image = open(image_loc, 'rb')

# Post Call -- Client is posting an image to MSV
# Post Call -- Client is posting an image to MSV
HEADERS = {'Prediction-Key': "e295f34c63df4cc6b4fedafd4a6a2134", "Content-Type": "application/json"}
body = {'Url': 'https://drive.google.com/u/1/uc?id=1PNFO1-ZSa4pcr8HxQfMg98YI_WQuJBVo&export=download'}
url = "https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/78cc487c-e8d7-4245-84ea-30b6caeb89b0/detect/iterations/Iteration3/url"
# response = requests.post(
#     url,
#     headers=HEADERS,
#     # params=settings.PARMES,
#     data=body
# )
response = requests.request("POST", url, headers=HEADERS, json=body)
print(response.content)
# print(dir(response))
