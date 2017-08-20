# -*- coding: utf-8 -*-

import pymysql
#-------------------------------
#deklarcje funkcji
#funscka logowania
class Funkcje:
    
    def logowanie(self):
        print("LOGOWANIE \npodaj nazwę uzytkownika oraz haslo: ")
        login = input("Nazwa: ")
        haslo = input("Haslo: ") 
        
        #zapytanie do bazy danych czy taki uzytkownik istenieje 
        conn = pymysql.connect("localhost", "root", "Hwdpik.hwdpik4", "event") #otwarcie poloczenia 
        c = conn.cursor() 
        r = c.execute("select  imie_u, haslo from uzytkownik where imie_u = '"+login+"';")
        if(r>0):
            print("Logowanie...") 
            self.userData = c.fetchall()#wpisanie rekordw do listy dwuwymiarowej userData / wszytskie dane uzytkownika [rzechwywane w userData
    
            conn.close() #zakniecie poloczenia 
            if(haslo == self.userData[0][1]): 
                print("Jestes zalogowany.")
                self.zalogowany()
            else:
                print("bledne haslo")
                
            
                
        else: 
            print("nie ma takiego uzytkownika") 
    #funkcja wywolujaca sie po zalogowaniu
    def zalogowany(self):
        print("Zalogowany jako: "+ self.userData[0][0])
        
        s = ""
        while(s != "esc"): 
            print("(1) - funkconalnosc 1")
            print("(2) - funkconalnosc 2")
            print("(esc) - wyloguj")
            
            s = input()
        
            if(s == "1"):
                print("funkcjonalnosc 1 w budowie ...")
            elif(s == "2"):
                print("funkcjonalnosc 2 w budowie ...")        
               
            elif(s != "esc"):
                print("Niezrozumiala komenda")
            
    #--------------------------------------
    def rejestracja(self):
        print("Wprowadz swoje dane do rejestracji: ")
        
        #conection = MySqlConection('root','Hwdpik.hwdpik4')
        
        imie_u = input("Imie: ")
        '''
         #sprawdzanie podanego email
         conn = pymysql.connect("localhost", "root", "Hwdpik.hwdpik4", "event") #otwarcie poloczenia 
         c = conn.cursor() 
         r = c.execute("select  imie_u, haslo from uzytkownik where imie_u = '"+login+"';")
        if(r>0):
        email = input('Wproadz adres email: ')
        r = conection.c.execute("SELECT user_email FROM users WHERE user_email = '"+email+"';")
        if(r != 0):# jeśli istnieje taki urzytkownik w bazie
            print('ten adres email jest już zarejestrowany!')
            conection.close()
            self.registration()   
        '''
        #r = c.execute("SELECT imie_u FROM uzytkownik WHERE imie_u = '"+imie_u+"';")
        pseudo_u = input("Pseudonim: ") 
        sex_u = input("Plec k/m: ") 
        kraj_u = input("Kraj: ") 
        woj_u = input("Wojewodztwo: ") 
        miasto_u = input("Miasto: ") 
        haslo = input("Haslo: ")    
        conn = pymysql.connect("localhost", "root", "Hwdpik.hwdpik4", "event") #otwarcie poloczenia 
        c = conn.cursor()         
        c.execute("INSERT INTO uzytkownik (imie_u, pseudo_u, sex_u, kraj_u, woj_u, miasto_u, haslo) VALUES ('" + imie_u + "', '" + pseudo_u + "', '" + sex_u + "', '" + kraj_u + "', '" + woj_u + "', '" + miasto_u + "', '" + haslo + "');")
        conn.commit()
        conn.close()
        print('sukces')        
        
    #--------------------------------
    #główna petla
    def start(self):
        s = ""
        while(s != "esc"): 
            print("(1) - Zaloguj \n(2) - Rejestracja \n(esc) - Koniec ")
            s = input()
        
            if(s == "1"):
                self.logowanie()
            elif(s == "2"):
                self.rejestracja()
                
            elif(s != "esc"):
                print("niezrozumiala komenda")
                
    #----------------------------------------------
   