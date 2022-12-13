import ftplib

class FileTransport:
    def __init__(self,host='127.0.0.1',user='',password=''):
        if(len(user)==0):
            self.FTP = ftplib.FTP(host=host)
            self.FTP.login()
        else:
            self.FTP = ftplib.FTP(host=host,user=user,passwd=password)
        self.FTP.encoding = 'gbk'
    def toRoute(self,route):
        try:
            self.FTP.cwd(route)
            print('Sucess!')
        except:
            print('The Route doesn\'t exist!')
    def PrintList(self):
        self.FTP.retrlines('LIST')
    def Download(self,FileRoute,FileName):
        # open(FileName,'gym+')
        try:
            self.FTP.retrbinary('RETR {}'.format(FileName), open(FileRoute, 'wb').write)
            print('Sucess!')
        except:
            print('The file Download error')
    def Upload(self,FileRoute,FileName):
        try:
            self.FTP.storbinary('STOR {}'.format(FileName), open(FileRoute, 'rb'))
            print('Sucess!')
        except:
            print('The file upload error!')

    def Delete(self, FileName):
        try:
            self.FTP.delete(FileName)
            print('Sucess!')
        except:
            print('Error to delete!')
    def Rename(self,OriginRoute,NewRoute):
        try:
            self.FTP.rename(OriginRoute,NewRoute)
            print('Sucess!')
        except:
            print('Error to rename!')
    def Quit(self):
        self.FTP.quit()
        print('Sucess!')
