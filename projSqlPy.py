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
        print("Wprowadz dane do rejestracji: ")
        conn = pymysql.connect("localhost", "root", "Hwdpik.hwdpik4", "event") #otwarcie poloczenia 
        c = conn.cursor() 
        

    
        imie_u = input("Imie: ")
        r = c.execute("SELECT imie_u FROM uzytkownik WHERE imie_u = '"+imie_u+"';")
        if(r != 0):# jeśli istnieje taki urzytkownik w bazie
            print('Podany Login jest już zarezerwowany, uzyj innego. ')
            conn.close()
            self.rejestracja()
            
        pseudo_u = input("Pseudonim: ") 
        sex_u = input("Plec k/m: ") 
        while (sex_u != "k" and  sex_u !=  "m"):
            print('>> Nieprawidlowa plec, wybierz (k/m) <<')
            sex_u = input("Plec k/m: ") 
        kraj_u = input("Kraj: ") 
        woj_u = input("Wojewodztwo: ") 
        
        
        miasto_u = input("Miasto: ") 
        haslo = input("Haslo: ")    
        haslo2 = input('Powtórz Hasło: ')
        while(haslo != haslo2):
            print('>> rozne hasla <<')
            haslo = input("Haslo: ")    
            haslo2 = input('Powtórz Hasło: ')            
        
        conn = pymysql.connect("localhost", "root", "Hwdpik.hwdpik4", "event") #otwarcie poloczenia 
        c = conn.cursor()         
        c.execute("INSERT INTO uzytkownik (imie_u, pseudo_u, sex_u, kraj_u, woj_u, miasto_u, haslo) VALUES ('" + imie_u + "', '" + pseudo_u + "', '" + sex_u + "', '" + kraj_u + "', '" + woj_u + "', '" + miasto_u + "', '" + haslo + "');")
        conn.commit()
        conn.close()
        print('>> Zarejestrowano urzytkownika <<')        
        return
    #--------------------------------
    #główna petla
    def start(self):
        s = ""
        while(s != "esc"): 
            print(" ")
            print("(1) - Zaloguj \n(2) - Rejestracja \n(esc) - Koniec ")
            s = input()
        
            if(s == "1"):
                self.logowanie()
            elif(s == "2"):
                self.rejestracja()
                
            elif(s != "esc"):
                print("niezrozumiala komenda")
                
    #----------------------------------------------
   