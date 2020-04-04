import time

# remember that name of your class and file has to include 'module__' string 
class module__exampleF:    # change the name of that class, the name must match the name of the file
#---------------------------------------------------------------------------------------------------------
# main prepared functions - do not edit the code or parameters

    # init function let module start properly
    def __init__(self):

        #----------------------DATA-TO-EDIT-FOR-THE-PROGRAMER-----------------------
        self.version = "v 1.0.0"    # insert your own version number
        self.date = "04.2020"       # insert your own date of publish
        self.short_desc = ""        # insert your short descryption of the module
        #---------------------------------------------------------------------------

        print( "Module : " + str(self.__class__.__name__ ) + " imported : " + str(time.asctime()) )
        print( " version: "+ self.version )
        print( " date: " + self.date )

    # function return name of the class and module
    def module_name(self):
        return str(self.__class__.__name__ )

    # funcion write help for the user about the module
    def help(self):
        print ( "Help for module : " + str(str(self.__class__.__name__ )))
        print ( self.version + " " + self.date )
        print ( self.short_desc )
        print ( "help content: ")
        # here add your help for the user, make descyption for every function 
        #----------------------DATA-TO-EDIT-FOR-THE-PROGRAMER-----------------------
        print ( "here add your help" )
        #---------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

    def run(self, user_input):
        pass