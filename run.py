import requests
import json
import sys
import base64
import os

class DateEncoder(json.JSONEncoder ):  
    def default(self, obj):  
        if isinstance(obj, bytes):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj)  

class img:
    def __init__(self,image,collection_id,threshold):
        self.__img = self.__check(image)
        self.__collection_id = collection_id
        self.__threshold = threshold

    def request(self):
        url = 'https://o2vwzkvff4.execute-api.ap-northeast-1.amazonaws.com/beta/img'
        data = {"threshold":self.__threshold,"collection_id":self.__collection_id,"img_type":self.__type,"img":self.__img}
        return requests.post(url,json.dumps(data,cls=DateEncoder)).content

    def __check(self,image):
        if image.endswith('.jpg') or image.endswith('.png') or image.endswith('.jpeg'):
            self.__type = image.split('.')[-1]
            if os.path.isfile(image):
                img_file = open(image,'rb')
                img_b64encode = base64.b64encode(img_file.read())
                img_file.close()
                return img_b64encode.decode()
            else:
                print("Request file does not exist")
                sys.exit(1)
        else:
            print("Request has invalid image format")
            sys.exit(1)

if __name__ == "__main__":
    new_img = img('test_img/纵贯线.jpg','music',70)
    print(new_img.request())
