import time

class module__mainF:

    def __init__(self):
        self.version = "v 1.0.0"
        self.date = "04.2020"

        print( "Module : " + str(self.__class__.__name__ ) + " imported : " + str(time.asctime()) )
        print( " version: "+ self.version )
        print( " date: " + self.date )
