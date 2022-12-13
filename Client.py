import FTPModule
def main():
    print('Welcome to the Transport file system based on FTP!')
    print('At first, you need to Login with UserName and PassWord (Or direct enter da anonymous login!')
    print('UserName:',end='')
    UserName=input()
    if(len(UserName)==0):
        ftp=FTPModule.FileTransport()
    else:
        print('PassWord:', end='')
        PassWord = input()
        ftp = FTPModule.FileTransport(user=UserName, password=PassWord)
    print('---------------------------------------------------------------------------------------')
    print('Welcome ', UserName)
    print('D to Download, U to Upload, R to Rename, Del to Delete, T to Route, P to Print the files, Q to Quit')
    while True:
        Event=input()
        if(Event=='D'):
            print('FileName(In cloud):', end='')
            FileRoute = input()
            print('FileName(In local):', end='')
            FileName = input()
            ftp.Download(FileName,FileRoute)
        elif(Event=='U'):
            print('FileName(In local):', end='')
            FileName = input()
            print('FileName(In cloud):', end='')
            FileRoute = input()
            ftp.Upload( FileName,FileRoute)
        elif(Event=='R'):
            print('OriginName:', end='')
            OriginName = input()
            print('NewName:', end='')
            NewName = input()
            ftp.Rename(OriginName,NewName)
        elif(Event=='Del'):
            print('Route:', end='')
            Route = input()
            ftp.Delete(Route)
        elif(Event=='T'):
            print('Route:',end='')
            Route=input()
            ftp.toRoute(Route)
        elif(Event=='P'):
            ftp.PrintList()
        elif(Event=='Q'):
            ftp.Quit()
            break
        else:
            print('Error Event!')

if __name__=='__main__':
    main()