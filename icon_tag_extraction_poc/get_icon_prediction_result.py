import requests
image_loc = "/home/rits/Documents/Assets/UAE_identity/EID_New_Formats/eid_back9.jpg"
processed_image = open(image_loc, 'rb')

# Post Call -- Client is posting an image to MSV
# Post Call -- Client is posting an image to MSV
HEADERS = {'Prediction-Key': "abc12345555555lkhfg", "Content-Type": "application/json"}
body = {'Url': 'https://drive.google.com/u/1/uc?id=1PNFO1-ZSa4pcr8HxQfMg98YI_WQuJBVo&export=download'}
url = "https://westeurope.api.cognitive.microsoft.com/customvision/v3.0/Prediction/8907578GHJKl/detect/iterations/Iteration3/url"
# response = requests.post(
#     url,
#     headers=HEADERS,
#     # params=settings.PARMES,
#     data=body
# )
response = requests.request("POST", url, headers=HEADERS, json=body)
print(response.content)
# print(dir(response))
