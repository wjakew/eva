import os
import sys
import importlib.util

class main:

    # glowny kod programu
    def __init__(self):

        self.modules = []   # obiekt typu lista na wszystkie niezbedne moduly do pracy
        
        # zapis aktualnej sciezki do pliku main i modulow
        self.current_path = os.path.dirname(os.path.abspath(__file__)) + "/main.py"
        self.current_mod_path = os.path.dirname(os.path.abspath(__file__))

        # wywolanie metody ladujacej dostepne moduly
        self.load_modules(self.current_mod_path)

        # inicjalizacja znalezionych modulow
        self.init_modules(self.modules)

        # w tym miejscu program gotowy do dzialania

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

                except:
                    print ( " Module : " + obj + " failed to import.")                      
                
                # na ta chwile wszystkie zaladowane moduly mamy w obiekcie typu lista
        
        if ( self.modules.count == 0 ):
            print ( " No modules found. Check your files." )
            sys.exit(0)
        print( "" )

    #metoda testujaca wszystkie zaladowane moduly
    def init_modules(self,mod_list):
        print ( "Running self test:" )
        for module in mod_list: # iterowanie po klasach z modulow
            try:
                module()        # wykonywanie inicjalizacji klasy
                                # note: wydaje mi sie ze zostal on juz wykonany metoda getattr ale nie ma w docs
            except:
                print ( " Modules failed. Check module." )
        print( "" )


# wywolanie glownej funkcji programu
main()