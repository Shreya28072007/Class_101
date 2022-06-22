import dropbox
import os

from dropbox.files import WriteMode

class TransferData :

    def __init__(self , access_token) :
        self.access_token = access_token

    def upload_file(self , file_from , file_to) :
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs, files in os.walk(file_from) :
            for fileName in files :
                local_path = os.path.join(root , fileName)
                relative_path = os.path.relpath(local_path , file_from)
                dropbox_path = os.path.join(file_to , relative_path)
                with open(local_path , "rb") as f:
                    dbx.files_upload(f.read() , dropbox_path , mode= WriteMode("overwrite"))

def main() :
    access_token = "sl.BKADAdRTAwKdClZxpnXC5JEIghv1RISYn5iu3Mrfawu75OcPpewKq5YACuQCM8kNej76Qs3daPotI7AAjzxpKq7_1LipzyRHlzsc5r3BLdXxV8AJiS8X4YX8Bxw3NH7y-00DkyEt-NLv"
    tranferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer :-")
    file_to  = input("Enter thr full path to upload to dropbox :-")
    tranferData.upload_file(file_from , file_to)
    print("File has been moved")

main()