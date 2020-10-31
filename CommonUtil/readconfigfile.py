import configparser

config = configparser.RawConfigParser()
config.read("C://Users//home//PycharmProjects//orangehrmlive//Config//config.ini")

class Readconfig:
    @staticmethod
    def getAppurl():
        url = config.get('Application Info','baseurl')
        return url

    @staticmethod
    def getUsername():
        uname = config.get('Application Info','username')
        return uname

    @staticmethod
    def getPassword():
        psswrd = config.get('Application Info','password')
        return psswrd

class Read2:
    @staticmethod
    def getappurl():
        aurl = config.get('Login Check','baseurl')
        return aurl