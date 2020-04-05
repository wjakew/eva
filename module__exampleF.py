import time

# remember that name of your class and file has to include 'module__' string 
class module__exampleF:    # change the name of that class, the name must match the name of the file
#---------------------------------------------------------------------------------------------------------
# main prepared functions - do not edit the code or parameters

    invoke_words = []    # list of key words of the module
    name_of_the_class = ""
    developer_test = 1   
    
    # init function let module start properly
    
    def __init__(self):

        self.log = []   # object for storing logs from modules 
        name_of_the_class = str(self.__class__.__name__ )
        #----------------------DATA-TO-EDIT-FOR-THE-PROGRAMER-----------------------
        self.version = "v 1.0.0"    # insert your own version number
        self.date = "04.2020"       # insert your own date of publish
        self.short_desc = ""        # insert your short descryption of the module
        #---------------------------------------------------------------------------

        print( "Module : " + str(self.__class__.__name__ ) + " imported : " + str(time.asctime()) )
        print( " version: "+ self.version )
        print( " date: " + self.date )

        self.load_invoke_words()    # loading invoke keys for the module

    # function return name of the class and module
    def module_name(self):
        return str(self.__class__.__name__ )

    # fuction for logiing behaviour of the module
    def log(self,text):

        if type(text) == str : 
            self.log.append(text)

        elif type(text) == list:
            for line in text:
                self.log.append(line)

    def stop(self):
        self.log("Module " + self.module_name + " stopped.")
        return self.log

    # funcion write help for the user about the module
    def help(self):
        print ( "Help for module : " + str(str(self.__class__.__name__ )))
        print ( self.version + " " + self.date )
        print ( self.short_desc )
        print ( "help content: ")
         
        #----------------------DATA-TO-EDIT-FOR-THE-PROGRAMER-----------------------

        print ( "here add your help" )  # here add your help for the user, make descyption for every function

        #---------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------

    # function for adding invoke key words of the module
    def load_invoke_words(self):

        self.invoke_words.append("hello")

    # function checking if text contains any key words, returns list of that key words
    def check_invoke(self,text):
        
        keys_in_input = []      # object for storing found keys

        for key in self.invoke_words:
            key.upper()

            for word in text.split(" "):
                word.upper()

                if key == word:
                    keys_in_input.append(word)

        return keys_in_input

    # main fuction of the module, here enter your code
    def run(self, user_input):

        keys = self.check_invoke(self,user_input)   # in keys variable we have all founded keys
        
        if keys.count != 0 :   # here we get at least 1 key

            if self.developer_test == 1: 
                print ( "module: " + self.name_of_the_class + " run funcion:")
                print ( "keys found : "+str(keys))
                print ( "echo: " + user_input)
            
            else:
                
                #----------------------DATA-TO-EDIT-FOR-THE-PROGRAMER-----------------------
                pass # here u can add your code
                #---------------------------------------------------------------------------

        else:                                   # no matching keys with that module
            log.append("No keys found - "+ self.name_of_the_class)
            