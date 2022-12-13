import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers

username='SetYourUserName'
password='SetYourPassword'

def main(username,password):
    #At first set the User and its password, also can anonymous login in its route
    authorizer = pyftpdlib.authorizers.DummyAuthorizer()
    authorizer.add_user(username, password, "./", perm="elradfmw")
    authorizer.add_anonymous('./')

    #Set some setting
    handler = pyftpdlib.handlers.FTPHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(2000, 3000)

    #it can control its raed and write speed
    dtp_handler = pyftpdlib.handlers.ThrottledDTPHandler
    dtp_handler.read_limit = 900 * 1024
    dtp_handler.write_limit = 900 * 1024

    #start to server and set the number of connect
    server = pyftpdlib.servers.FTPServer(("127.0.0.1", 21), handler)
    server.max_cons = 9
    server.max_cons_per_ip = 9
    server.serve_forever()

if __name__=='__main__':
    main(username,password)