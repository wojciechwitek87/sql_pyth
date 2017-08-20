# -*- coding: utf-8 -*-
import pymysql

class MySqlConection:
    def __init__(self,mySqlUser, mySqlPass):
        self.conn = pymysql.connect("localhost", mySqlUser, mySqlPass, "Temperature_measurement_DB")
        self.c = self.conn.cursor() 
        
    def close(self):
        self.conn.close()
    
class Start:
    def __init__(self):
        i = ''
        while (i != 'esc'):
            print('Co chcesz zrobić?\n(1) -> zaloguj\n(2) -> zarejestruj się\n(esc) -> koniec')
            i = input()
            if(i == '1'):       # logowanie
                self.login()
            elif(i == '2'):     # rejestracja użytkownika
                self.registration()
            elif(i != 'esc'):   # zła komenda
                print('nie rozumiem')
        print('Koniec programu')   
    
    #LOGOWANIE    
    def login(self):
        name = input('Wprowadź nazwę użytkownika lub adres email: ')
        passw = input('Wprowadź hasło: ')
        conection = MySqlConection('root','Aakm7395') 
        
z        r = conection.c.execute("SELECT id_user, user_name, user_email, user_password, id_permission FROM users WHERE user_name = '"+ name +"' or user_email = '" +name +"';")
        if(r == 0):     # 0 rekordów => brak szukanego użytkownika
            print('Nie ma takiego użytkownika!') 
            conection.close()
            return
        # przypisanie wyników zapytania do zmiennych
        results = conection.c.fetchall()
        id_user = results[0][0]
        user_name = results[0][1]
        user_email = results[0][2]
        password = results[0][3]
        perm = results[0][4]
    
        if(passw == password):        # sprawdzenie hasła => udane logowanie
            print('Logowanie powiodło się')
            conection.close()
            user = User(id_user,user_name,user_email, password, perm)
            
        else:                         # złe hasło
            print('Złe hasło!')
            conection.close()
    
    #REJESTRACJA USERA      
    def registration(self):
        #sprawdzanie podanego email
        conection = MySqlConection('root','Aakm7395')
        email = input('Wproadz adres email: ')
        r = conection.c.execute("SELECT user_email FROM users WHERE user_email = '"+email+"';")
        if(r != 0):# jeśli istnieje taki urzytkownik w bazie
            print('ten adres email jest już zarejestrowany!')
            conection.close()
            self.registration()   
            
        #sprawdzanie podanej nazwy użytkownika
        name = input('Wproadź nazwę użytkownika: ')
        r = conection.c.execute("SELECT user_email FROM users WHERE user_name = '"+name+"';")
        if(r != 0):
            print('taki użytkownik jest już zarejestrowany!')
            conection.close()
            self.registration()
        
        # email i nazwa poprawne => wprowadz chasło   
        password = input('Wproadz hasło: ')
        password2 = input('Powtórz hasło: ')
        while(password != password2):
            print('hasła różnią się')
            password = input('Wproadz hasło: ')
            password2 = input('Powtórz hasło: ')            
        
        
        # insert nowego uźytkownika do bazy danych
        conection.c.execute("INSERT INTO users (user_name, user_email, id_permission, user_password) VALUES ('" + name + "', '"+ email + "', 1, '" + password + "');")
        conection.conn.commit()
        conection.close()
        print('Zarejestrowano urzytkownika')
        return
        
class User:
    def __init__(self, id, name, email, password, permission):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.perm = permission
        self.userNav()
        
    def userNav(self):
        i = ''
        while (i != 'esc'):
            print('ZALOGOWANY jako urzytkownik: ' + self.name)
            print('Co chcesz zrobić?\n(1) -> lista czujników\n(2) -> wyniki pomiarów\n(3) -> rejestruj nowy czujnik\n(4) -> udostępnienia\n(esc) -> wyloguj')
            i = input()
            if(i == '1'):# lista czujników
                self.sensorList()
            
            elif(i == '2'):# wyniki pomiarów
                self.measurments()
            
            elif(i == '3'):# dodawanie nowego czujnika
                self.newSensor()
            
            elif(i == '4'):# udostempnienia
                self.sensorShering()
            
            elif(i != 'esc'):
                print('Nie rozumiem!')
            else:
                print('Wylogowano')
                print()
    
    # Wyświetlanie list dostępnych czujników
    # własych i udostępnionych
    def sensorList(self):
        i = ''
        while (i != 'esc'):
            print('ZALOGOWANY jako urzytkownik: ' + self.name)
            print('Co chcesz zrobić?\n(1) -> moje czujnikiki\n(2) -> czujniki udostępnione\n(esc) -> wstecz')
            i = input()
            if(i == '1'):# czujniki usera
                conection = MySqlConection('root','Aakm7395') 
                conection.c.execute("select id_sensor, adress, accuracy, range_min, range_max, next_calibration FROM sensors_v WHERE id_owner = "+ str(self.id) +";")
                results = conection.c.fetchall()
                conection.close()
                print()
                print('Twoje czujniki:')
                print('%4s | %10s | %8s | %4s | %4s | %12s' % ('nr', 'adres', '+/-', 'Tmin', 'Tmax', 'kalibracja'))
                print('_'*57)
                for v in results:
                    print('%4i | %10s | %8f | %4i | %4i | %12s' % (v[0], v[1], round(v[2],2), v[3], v[4], v[5]))
                print()
                
            elif(i == '2'):# czujniki udostępnione
                conection = MySqlConection('root','Aakm7395') 
                conection.c.execute("SELECT owner_name AS 'od kogo', sensors_v.id_sensor AS 'id sensor', adress, accuracy, range_min, range_max, next_calibration FROM sensors_v, user_sensor WHERE sensors_v.id_sensor = user_sensor.id_sensor AND user_sensor.id_user = "+str(self.id)+";")
                results = conection.c.fetchall()
                conection.close()
                print()
                print('Czujniki udostępnione:')
                print('%12s | %4s | %10s | %8s | %4s | %4s | %12s' % ('właściciel', 'nr', 'adres', '+/-', 'Tmin', 'Tmax', 'kalibracja'))
                print('_'*72)
                for v in results:
                    print('%12s | %4i | %10s | %8f | %4i | %4i | %12s' % (v[0], v[1], v[2], v[3], v[4], v[5], v[6]))
                print()
            elif(i != 'esc'):
                print('Nie rozumiem!')              
    
    # wyświetlanie wyników pomiarów wskazanego czujnika
    def measurments(self):
        nr = input('podaj nr czujnika: ')
        conection = MySqlConection('root','Aakm7395')
        
        # sprawdzenie czu user ma dostęp do wskazanego czujnika
        n = conection.c.execute("SELECT     sensors_v.id_sensor FROM    sensors_v,    user_sensor WHERE    sensors_v.id_sensor = user_sensor.id_sensor        AND user_sensor.id_user = " + str(self.id) + " AND user_sensor.id_sensor = " + str(nr) + " UNION SELECT     id_sensor FROM    sensors_v WHERE    id_owner = " + str(self.id) + " AND id_sensor = " + str(nr) + ";")
        if(n == 0): # brak dostępu do wskazanego czujnika
            print('Nie masz dostempu do tego czujnika.')
            conection.close()
            return
        else:       #użytkownik ma dostęp do wskazanego czujnika
            print('Uzyskano dostęp do czujnika.')
            conection.c.execute("SELECT DISTINCT temperature, date(measurement_time) as 'date', time(measurement_time) as 'time' from measurement WHERE id_sensor = "+str(nr)+";")
            results = conection.c.fetchall()
            conection.close()            
            i = ''
            while (i != 'esc'):
                print('Drukowanie pomiarów czujnika nr: '+str(nr)+'\n(1) -> na ekran\n(2) -> do pliku\n(esc) -> wstecz')
                i = input()
                if(i == '1'):     #drukowanie na ekran
                    print()
                    print('wyniki pomiarów czujnika nr: ' + str(nr))
                    print()
                    print('%10s | %11s | %11s' % ('temp','data', 'godzina'))
                    print('_'*38)
                    for v in results:
                        print('%10f | %11s | %11s' % (v[0], v[1], v[2]))
                    print()
                    return
                elif(i == '2'):   # drukowanie do pliku
                    F = open("pomiaty_sensor_"+str(nr)+".txt","w")  # otwarcie pliku
                    F.write('wyniki pomiarów czujnika nr: ' + str(nr)+'\n')
                    F.write('temp;data;godzina\n')
                    for v in results:
                        F.write(str(v[0])+';'+str(v[1])+';'+str(v[2])+'\n')
                    F.close()                             # zamknięcie pliku
                    return
                elif(i != 'esc'):
                    print('Nie rozumiem!')
    
    # rejestrownie nowego czujnika
    def newSensor(self):
        print('Rejestrowanie czujnika...')
    
    # udostępnianie czujnika
    def sensorShering(self):
        print('Twoje udostępnienia:')
        print()
        conection = MySqlConection('root','Aakm7395')
        conection.c.execute("select	sensors_v.id_sensor , adress, users.user_name from sensors_v NATURAL JOIN user_sensor NATURAL join users where id_owner = "+str(self.id)+";") 
        results = conection.c.fetchall()
        conection.close()
        print('nr czujnika |  adres  | komu')
        print('_'*30)
        for v in results:
            print('%11i | %7s | %s'%(v[0],v[1],v[2]))
        print()
        i = ''
        while (i != 'esc'):
            print('Co chcesz zrobić?\n(1) -> dodaj udostępnienie\n(2) -> usuń udostępnienie\n(esc) -> wstecz')
            i = input()
            if(i == '1'):
                print()
                print('Dodawanie udostępnienia')
                
                sensor = input('Podaj nr czujnika: ')
                #sprawdzenie dostępu do czujnika...
                conection = MySqlConection('root','Aakm7395')
                n = conection.c.execute("SELECT id_sensor FROM sensors WHERE id_owner = " + str(self.id) + " AND id_sensor = " + sensor + ";")
                conection.close()
                
                
                if(n == 0): # brak dostępu do wskazanego czujnika
                    print('\nNie masz dostempu do tego czujnika.\n')
                    self.sensorShering()
                    
                else:
                    #sprawdzenie czy user istnieje i czy nie jest sobą
                    user = input('podaj nazwę użytkownika: ')
                    conection = MySqlConection('root','Aakm7395')
                    n = conection.c.execute("SELECT id_user, user_name FROM users WHERE user_name = '"+user+"' AND id_user != " + str(self.id) + ";")
                    results = conection.c.fetchall()
                    idU = results[0][0]
                    print(idU, results[0][1])
                    print('id usera: '+str(idU))
                    conection.close()
                    
                    if(n == 0): # brak wskazanego usera
                        print('\n Nie ma takiego użytkownika.\n')
                        self.sensorShering()
                        
                    else:       # user podany prawidłowo
                        
                        # insert udostępnienia do bazy
                        conection = MySqlConection('root','Aakm7395')
                        conection.c.execute("INSERT INTO user_sensor (id_sensor, id_user) VALUES("+sensor+", "+str(idU)+");")
                        conection.conn.commit()
                        conection.close()                     
                        print('\nDodano udostępnienie!\n')
                        break
                
            elif( i == '2'):
                print('Usówanie udostępnienia')
            elif(i != 'esc'):
                print('Nie rozumiem!')
        
        

start = Start()