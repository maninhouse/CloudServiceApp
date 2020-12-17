import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def visual_recognition(api_key = 'wcuBCIc7I_KCIQQW-goNo4m8FFioGUnWDgPKPd6fsluu', api_url = 'https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/55753b10-37c4-4896-887e-aef29ca77bef'):
apikey = 'wcuBCIc7I_KCIQQW-goNo4m8FFioGUnWDgPKPd6fsluu'#input('api key:')
apiurl = 'https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/55753b10-37c4-4896-887e-aef29ca77bef'#input('url:')

authenticator = IAMAuthenticator(apikey)
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url(apiurl)

url = 'https://ibm.biz/BdzLPG'
url = 'C:\\Users\\user\\Desktop\\venv_test\\cloud_final\\CloudServiceApp\\app\\static\\img\\01.jpg'
images_file = open('C:\\Users\\user\\Desktop\\venv_test\\cloud_final\\CloudServiceApp\\app\\static\\img\\01.jpg', "rb")


#classes_result = visual_recognition.classify(url=url).get_result()
classes_result = visual_recognition.classify(images_file=images_file).get_result()
print(json.dumps(classes_result, indent=2))
