import os
import sys
import importlib.util   # import bilbioteki odpowiedzialnej za dynamiczny impot modulow
import gc               # import garbage colector - pozniej potrzebne do pilnowania pamieci po modulach
import time
class Main:
#--------------------------------------------------------------------------------------------------------
    # glowny kod programu

    def __init__(self):

        self.version = "v 1.0.0"
        self.date = "04.2020"
        self.build = hash(self.version)

        self.modules = []   # obiekt typu lista na wszystkie niezbedne moduly do pracy
        
        self.welcome_screen()   #ekran powitalny

        # zapis aktualnej sciezki do pliku main i modulow
        self.current_path = os.path.dirname(os.path.abspath(__file__)) + "/main.py"
        self.current_mod_path = os.path.dirname(os.path.abspath(__file__))

        # wywolanie metody ladujacej dostepne moduly
        self.load_modules(self.current_mod_path)

        # inicjalizacja znalezionych modulow
        self.init_modules()

        # w tym miejscu program gotowy do dzialania

        self.main_loop_()

#--------------------------------------------------------------------------------------------------------
    # metody zachowania programu 

    def main_brain_(self, user_input):

        if user_input != "exit":
            print( "echo : " +  user_input )
        else:
            sys.exit(0)

    # podstawowa petla programu
    def main_loop_(self):

        print("")
        self.center_print("Ready!")
        
        # glowna petla programu

        while(True):
            
            user_input = str( self.comunication_screen() )

            self.main_brain_(user_input)

#--------------------------------------------------------------------------------------------------------
    # metody importowania modulow

    # metoda ladujaca moduly ktore pracuja
    def load_modules(self,mod_path):

        print ( "Loading modules.. ")

        list_of_dirs = os.listdir(mod_path) # lista zawierajaca sciezki dostepu do plikow znajdujacych sie
                                            # w katalogu z programem

        for obj in list_of_dirs:

            # w tym momencie podczas kazdej iteracji mamy w zmiennej file nazwy plikow (wraz z rozszezeniami)
            if "module__" in obj :

                print ( "Module found : " + obj )
                
                # podejscie pierwsze do rozwiazania problemu

                print ( " Trying to import ... ")
                try:
                    spec = importlib.util.spec_from_file_location(obj[0 : len(obj)-3], obj) # wyszukiwanie modulu z 
                                                                                        # z podanej sciezki
                    module = importlib.util.module_from_spec(spec)      # importowanie kodu zrodlowego

                    spec.loader.exec_module(module)                     # ladowanie modulu

                    my_class = getattr(module,obj[0 : len(obj)-3])

                # dodawanie modulow do podanej sciezki
                    self.modules.append(my_class)   

                    print ( " Import succeeded." )

                except Exception as exception:
                    print ( " Module : " + obj + " failed to import.")   
                    print ( " Details: " )
                    print ( str(type(exception).__name__) )                   
                
                # na ta chwile wszystkie zaladowane moduly mamy w obiekcie typu lista
        
        if ( self.modules.count == 0 ):
            print ( " No modules found. Check your files." )
            sys.exit(0)
        print( "" )

    #metoda testujaca wszystkie zaladowane moduly
    def init_modules(self):
        self.center_print("Running self test:")
        count = 0
        for module in self.modules: # iterowanie po klasach z modulow
            try:
                print( "" )
                module()        # wykonywanie inicjalizacji klasy
                                # note: wydaje mi sie ze zostal on juz wykonany metoda getattr ale nie ma w docs
                count+=1
            except Exception as exception:
                print ( " WARNING!!!!! Module failed. Check module." )
                print ( " Details: " )
                print ( str(type(exception).__name__) )

                self.modules.remove(module) # usuniecie niedzialajacego modulu z puli
        self.center_print("Self test ended : "+ str(count) + " modules ready to use")
        print( "" )

#--------------------------------------------------------------------------------------------------------
    # metody wizualne 

    # metoda wypisujaca tekst na srodku terminala
    def center_print(self,text):
        spaces = int(os.get_terminal_size().columns)

        if type(text) == str:
            print ( text.center(spaces) )

        else:
            for line in text:
                print( line.center(spaces) )

    # ekran powitalny
    def welcome_screen(self):
        text = ["Eva",self.version,"by Jakub Wawak 2020"]
        self.center_print(text)

    # ekran wprowadzania tekstu
    def comunication_screen(self):

        # odtad mozna dowolnie edytowac
        user_input = input(time.asctime()+" >>>")
        # do tego momentu

        if not user_input:  #sprawdzanie czy wejscie nie jest puste
            return user_input
        else:
            return ""

#--------------------------------------------------------------------------------------------------------
    # wywolanie glownej funkcji programu
Main()