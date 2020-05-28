from string import ascii_lowercase

class View:
    def start(self):
        print("\033[94m**********************************\033[0m")
        print("\033[94m==================================\033[0m")
        print("    \033[92mWelcome to Classic cinema\033[0m     ")
        print("   \033[4m'Only the best movies ever'\033[0m    ")
        print("\033[94m==================================\033[0m")
        print("\033[94m**********************************\033[0m")
        
    def end(self):
        print("\n\033[94m----------------------------------\033[0m")
        print("\033[92m    Hope you enjoyed the film!    \033[0m")
        print("         \033[4mCome back soon!😁\033[0m          ")
        print("\033[94m----------------------------------\033[0m")

    def first_menu(self):
        print("\n----------------------------------")
        print("        1) 👤 Enter as user         ")
        print("-----------------------------------")
        print("  2) 👨‍💻 Enter as an administrator   ")
        print("-----------------------------------")

    def select_option(self):
        print("Select an option: ", end = '')

    def option_invalid(self):
        print("¡Invalid option try again!") 

    def ask(self, output):
        print(output, end = '')   

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('\033[92m+'*(len(str(id))+len(op)+24)+'\033[0m')
        print('\033[92m+ ¡'+str(id)+' added '+op+' correctly! +\033[0m')
        print('\033[92m+'*(len(str(id))+len(op)+24)+'\033[0m')

    def error(self, err):
        print('\033[91m ¡ERROR! \033[0m'.center(len(err)+4,'-'))
        print('\033[91m- '+err+' -\033[0m')
        print('\033[91m-\033[0m'*(len(err)+4)) 
        
    def success(self):    
        print("\033[94mChanges were applied succesfully \033[0m")
    
    def invalid_id(self):
        print("\033[93mError. Invalid id\033[0m") 

    def show_update(self):
        print("Update the needed fields")
    
    """
    *********************************************************
    **************Actions performed by admin*****************
    *********************************************************
    """
    def admin_login(self):
        print("\n\033[94m----------------------------------\033[0m")
        print("\033[94m        👨‍💻  Admin login           \033[0m")
        print("\033[94m----------------------------------\033[0m") 
    
    def admin_main_menu(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m             Main menu:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("Choice an option")
        print("1. Administrators")
        print("2. Users") 
        print("3. Movies")
        print("4. Halls")
        print("5. Schedules")
        print("6. Seats")
        print("7. Tickets\n")
        print("\033[91m0. Log out\033[0m\n")

    """
    -----------------------------------------------------------
    Admin methods
    -----------------------------------------------------------
    """

    def menu_admin(self):
        print("\n-----------------------")
        print("        👩‍💻 Admins       ")
        print("-----------------------") 
        print("1. Create Admin")
        print("2. Read admin") 
        print("3. Find admin by name(s)")
        print("4. Show all admins")
        print("5. Update admin")
        print("6. Delete admin")
        print("0. Go back to main menu\n") 

    def show_admin(self, admin):
        print('username: ', admin[0])
        print('password: ', admin[1])
        print('name(s): ', admin[2])
        print('last name: ', admin[3])
        print('last name (m): ', admin[4])
        print('Job title: ', admin[5])
        print('bitrhdate: ', admin[6])

    def show_all_admins(self, admins):
        print('\n' + 'username'.ljust(20) + '|' + 'password'.ljust(15) + '|' + 'names'.ljust(20)+ '|'+'last name'.ljust(15)+'|'+'last name m'.ljust(15)+'|' +'job title'.ljust(20)+'|' +'birthdate'.ljust(8)+'|')   
        print('-'*113)
        for record in admins:
            if record[4] != None:
                print(f'{record[0]:<20}|{record[1]:<15}|{record[2]:<20}|{record[3]:<15}|{record[4]:<15}|{record[5]:<20}|{record[6]}|')
            else:
                print(f'{record[0]:<20}|{record[1]:<15}|{record[2]:<20}|{record[3]:<15}|               |{record[5]:<20}|{record[6]}|')
        print('-'*113)
    
    def show_admin_header(self, header):
        print(header.center(113,'*'))
        print('-'*113)
    
    def show_admin_midder(self):
        print('-'*113)

    def show_admin_footer(self):
        print('*'*113)

    """
    -----------------------------------------------------------
    User methods
    -----------------------------------------------------------
    """
    def menu_user(self):
        print("\n-----------------------")
        print("        👨 Users        ")
        print("-----------------------") 
        print("1. Create User")
        print("2. Read user") 
        print("3. Find user by name(s)")
        print("4. Show all users")
        print("5. Update user")
        print("6. Delete user")
        print("0. Go back to main menu\n") 

    def show_user(self, user):
        print('username: ', user[0])
        print('password: ', user[1])
        print('name(s): ', user[2])
        print('last name: ', user[3])
        print('last name (m): ', user[4])
        print('bitrhdate: ', user[5])

    def show_all_users(self, users):
        print('\n' + 'username'.ljust(20) + '|' + 'password'.ljust(15) + '|' + 'names'.ljust(20)+ '|'+'last name'.ljust(15)+'|'+'last name m'.ljust(15)+'|' +'birthdate'.ljust(8)+'|')   
        print('-'*93)
        for record in users:
            if record[4] != None:
                print(f'{record[0]:<20}|{record[1]:<15}|{record[2]:<20}|{record[3]:<15}|{record[4]:<15}|{record[5]}|')
            else:
                print(f'{record[0]:<20}|{record[1]:<15}|{record[2]:<20}|{record[3]:<15}|               |{record[5]}|')

        print('-'*93)
    
    def show_user_header(self, header):
        print(header.center(93,'*'))
        print('-'*93)
    
    def show_user_midder(self):
        print('-'*93)

    def show_user_footer(self):
        print('*'*93)
    """
    -----------------------------------------------------------
    Movies methods
    -----------------------------------------------------------
    """
    def menu_movie(self):
        print("\n-----------------------")
        print("        🎞️ Movies       ")
        print("-----------------------") 
        print("1. Create Movie")
        print("2. Read movie") 
        print("3. Find movie by title")
        print("4. Show all movies")
        print("5. Update movie")
        print("6. Delete movie")
        print("0. Go back to main menu\n") 

    def show_movie(self, movie):
        print('movie_id: ', movie[0])
        print('title: ', movie[1])
        print('duration: ', movie[2])
        print('sinopsis: ', movie[3])
        print('director: ', movie[4])
        print('genre: ', movie[5])
        print('rating: ', movie[6])
        print('release_date: ', movie[7])

    def show_all_movies(self, movies):
        # print('\n'+'id'.ljust(3)+'|'+'title'.ljust(20)+'|'+'duration'.ljust(8)+'|'+'sinopsis'.ljust(80)+'|'+'director'.ljust(35)+'|'+'genre'.ljust(15)+'|'+'rating'.ljust(6)+'|'+'release'.ljust(8)+'|')   
        print('-'*175)
        for record in movies:
            # print(f'{record[0]:<3}|{record[1]:<20}|{record[2]:<8}|{record[3]:<80}|{record[4]:<35}|{record[5]:<15}|{record[6]:<6}|{record[7]:<8}|')
            self.show_movie(record)
            print('-'*140)
        print('='*140)
    
    def show_movie_header(self, header):
        print(header.center(175,'*'))
        print('-'*175)
    
    def show_movie_midder(self):
        print('-'*175)

    def show_movie_footer(self):
        print('*'*175)
    """
    -----------------------------------------------------------
    Halls methods
    -----------------------------------------------------------
    """
    def menu_hall(self):
        print("\n-----------------------")
        print("        🎦 Halls        ")
        print("-----------------------") 
        print("1. Create hall")
        print("2. Read hall") 
        print("3. Find hall by type")
        print("4. Show all halls")
        print("5. Update hall")
        print("6. Delete hall")
        print("0. Go back to main menu\n") 

    def show_created_hall(self, hall):
        print("Hall",hall[0],"created succesfully!")
        print(hall[2]*hall[3],"empty seats added to the hall")
    
    def show_hall(self, hall):
        print('hall_id: ', hall[0])
        print('hall type: ', hall[1])
        print('number of rows: ', hall[2])
        print('seats per row: ', hall[3])

    def show_all_halls(self, halls):
        print('\n'+'hall_id'.ljust(7)+'|'+'hall type'.ljust(15)+'|'+'# rows'.ljust(6)+'|'+'seats per row'.ljust(12)+'|')   
        print('-'*45)
        for record in halls:
            print(f'{record[0]:<7}|{record[1]:<15}|{record[2]:<6}|{record[3]:<13}|')
        print('-'*45)
    
    def show_hall_header(self, header):
        print(header.center(45,'*'))
        print('-'*45)
    
    def show_hall_midder(self):
        print('-'*45)

    def show_hall_footer(self):
        print('*'*45)
    """
    -----------------------------------------------------------
    Schedules methods
    -----------------------------------------------------------
    """
    def menu_schedule(self):
        print("\n-----------------------")
        print("      📆 Schedules      ")
        print("-----------------------") 
        print("1. Create schedule")
        print("2. Read schedule") 
        print("3. Find schedule by movie")
        print("4. Show all schedules")
        print("5. Update schedule")
        print("6. Delete schedule")
        print("0. Go back to main menu\n") 

    def show_schedule(self, schedule):
        print('schedule_id: ', schedule[0])
        print('movie_id: ', schedule[1])
        print('hall_id: ', schedule[2])
        print('day: ', schedule[3])
        print('hour: ', schedule[4])

    def show_all_schedules(self, schedules):
        print('\n'+'schedule_id'.ljust(11)+'|'+'movie_id'.ljust(8)+'|'+'hall_id'.ljust(6)+'|'+'day'.ljust(8)+'|'+'hour'.ljust(6)+'|')   
        print('-'*39)
        for record in schedules:
            print(f'{record[0]:<11}|{record[1]:<8}|{record[2]:<6}|{record[3]:<8}|{record[4]:<6}|')
        print('-'*39)
    
    def show_schedule_header(self, header):
        print(header.center(39,'*'))
        print('-'*39)
    
    def show_schedule_midder(self):
        print('-'*39)

    def show_schedule_footer(self):
        print('*'*39)
    """
    -----------------------------------------------------------
    Seats methods
    -----------------------------------------------------------
    """
    def menu_seat(self):
        print("\n-----------------------")
        print("        💺 Seats        ")
        print("-----------------------") 
        print("1. Create seat")
        print("2. Read seat") 
        print("3. Find seat by schedule")
        print("4. Show all seats")
        print("5. Update seat")
        print("6. Delete seat")
        print("0. Go back to main menu\n") 

    def show_seat(self, seat):
        print('seat_id: ', seat[0])
        print('schedule_id: ', seat[1])
        print('row: ', seat[2])
        print('number: ', seat[3])
        print('aviable: ', seat[4])

    def show_all_seats(self, seats):
        print('\n'+'seat_id'.ljust(7)+'|'+'schedule_id'.ljust(11)+'|'+'row'.ljust(3)+'|'+'number'.ljust(6)+'|'+'aviable'.ljust(7)+'|')   
        print('-'*39)
        for record in seats:
            # print(f'{record[0]:<11}|{record[1]:<8}|{record[2]:<6}|{record[3]:<8}|{record[4]:<6}|')
            print(f'{record[0]:<7}|{record[1]:<11}|{record[2]:<3}|{record[3]:<6}|{record[4]}  |')
        print('-'*39)
    
    def show_seat_header(self, header):
        print(header.center(39,'*'))
        print('-'*39)
    
    def show_seat_midder(self):
        print('-'*39)

    def show_seat_footer(self):
        print('*'*39)
    """
    -----------------------------------------------------------
    Tickets methods
    -----------------------------------------------------------
    """
    def menu_ticket(self):
        print("\n-----------------------")
        print("       🎟️  Tickets       ")
        print("-----------------------") 
        print("1. Create ticket")
        print("2. Read ticket") 
        print("3. Find ticket by username")
        print("4. Show all tickets")
        print("5. Update ticket")
        print("6. Delete ticket")
        print("0. Go back to main menu\n") 

    def show_ticket(self, ticket):
        print('seat_id: ', ticket[0])
        print('username: ', ticket[1])
        print('price: ', ticket[2])
        print('buy date: ', ticket[3])
    
    def user_show_ticket(self, ticket):
        print('movie title: ', ticket[0])
        print('hall_id: ', ticket[1])
        print('movie date: ', ticket[2])
        print('price: ', ticket[3])
        print('buy date: ', ticket[4])

    def show_all_tickets(self, tickets):
        print('\n'+'seat_id'.ljust(7)+'|'+'username'.ljust(20)+'|'+'price'.ljust(6)+'|'+'buy date'.ljust(15)+'|')   
        print('-'*48)
        for record in tickets:
            print(f'{record[0]:<7}|{record[1]:<20}|{record[2]:<6}|{record[3]:<15}|')
        print('-'*48)
    
    def show_ticket_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)
    
    def show_ticket_midder(self):
        print('-'*48)

    def show_ticket_footer(self):
        print('*'*48)

    """
    *********************************************************
    **************Actions performed by user *****************
    *********************************************************
    """
    
    def user_main_menu(self):
        print("\033[92m\n----------------------------------\033[0m")
        print("\033[92m             Main menu:           \033[0m")
        print("\033[92m----------------------------------\033[0m") 
        print("Choice an option")
        print("1. Mi user info")
        print("2. Movies")
        print("3. My Tickets\n")
        print("\033[91m0. Exit\033[0m\n")

    def user_menu_movies(self):
        print("\n-----------------------------------")
        print("            🎬  Movies             ")
        print("----------------------------------") 
        print("Choice an option")
        print("1. Watch all movies")
        print("2. Search movie by title")
        print("0. Go back\n")


    def user_login(self):
        print("\n----------------------------------")
        print("           👤 User login           ")
        print("----------------------------------") 

    def user_show_hall(self, seats):
        letterToNumber = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}
        numberToLetter = [[index, letter] for index, letter in enumerate(ascii_lowercase, start=1)]
        # print(letterToNumber)
        rows = letterToNumber[str(seats[-1][2]).lower()]
        seatsPerRow = seats[-1][3]
        seatsPerRow += 1
        counter = 0
        for i in range(rows):
            r = numberToLetter[i][1]
            print("\033[94mRow:", r.upper(),'\033[0m')
            for j in range(seatsPerRow):
                if list(seats[counter][4])[0] == 'Y':
                    n = str(seats[counter][3])
                    # print(list(seats[counter][4])[0], end='')
                    print(n.rjust(2), end=' ')
                else:
                    print("\033[91m * \033[0m", end='')
                counter +=1
            print("")
        print("")
        print('-'*seatsPerRow*3)
        print('\033[93m SCREEN \033[0m'.center((seatsPerRow*3+9),'='))
        print('-'*seatsPerRow*3)

