import time,cv2,random,dropbox
from unicodedata import name

from matplotlib import image

startTime=time.time()

def takeSnapshot():
    number=random.randint(0,1000)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
    print("Image Saved",imageName)
    videoCaptureObject.release()
    #videoCaptureObject.destroyAllWindows()
    return imageName
    

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
            
        print('Your file has been uploaded to Dropbox')   

def main():
    access_token = 'sl.BF_H9m8_IxCwDeXnfcQSTFGF3O6kGMs3wuKArithCVEn2HWC-egTzfbtbCJGv8BeO1B4j2BdRfYfKwp6nyARKdajvxl_cITayx2Rz4ntCxBAiEWu0lOBJMGUAP2HV_L8tPPPz96HLJUz'
    transferData = TransferData(access_token)

    file_from = takeSnapshot()
    file_to = "/class102/" + file_from

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()