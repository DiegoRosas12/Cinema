from model.model import Model
from view.view import View
from string import ascii_lowercase

class Controller:
    """
    *******************************
    * A controller for a movie DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.local_user_username = ''
        self.local_admin_username = ''
        self.numberToLetter = [[index, letter] for index, letter in enumerate(ascii_lowercase, start=1)]
        self.letterToNumber = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}

    def start(self):
        self.view.start()
        self.view.first_menu()
        o = input('Select an option: ')
        if o == '2':
            self.admin_login()
        elif o == '1':
            self.user_login()
        else:
            print("invalid option, try again")
            return

    """
    ****************************
    * General controller  admin*
    ****************************
    """
    def admin_login(self):
        self.view.admin_login()
        self.view.ask('username: ')
        username = input()
        self.view.ask('password: ')
        password = input()
        log = self.model.admin_login(username, password)
        if type(log) == str:
            self.local_admin_username = log
            print("")
            print("\n\033[92mWelcome again!: \033[0m",log)
            self.admin_main_menu()
        else:
            print('\033[91musername or password are incorrect\033[0m')
            return
        
    def admin_main_menu(self):
        while True:
            self.view.admin_main_menu()
            self.view.select_option()
            o = input()
            if o == '1':
                self.menu_admin()
            elif o == '2':
                self.menu_user()
            elif o == '3':
                self.menu_movie()
            elif o == '4':
                self.menu_hall()
            elif o == '5':
                self.menu_schedule()
            elif o == '6':
                self.menu_seat()
            elif o == '7':
                self.menu_ticket()
            elif o == '0':
                self.model.close_db()
                self.view.end()
                return
            else:
                self.view.option_invalid()
    
    """
    *********************
    * Admin controllers *
    *********************
    """
    def menu_admin(self):
        while True:
            self.view.menu_admin()
            self.view.select_option()
            o = input()
            if o == '1':
                self.create_admin()
            elif o == '2':
                self.read_admin()
            elif o == '3':
                self.read_admin_names()
            elif o == '4':
                self.read_all_admins()
            elif o == '5':
                self.update_admin()
            elif o == '6':
                self.delete_admin()
            elif o == '0':
                return
            else:
                self.view.option_invalid()
    
    def ask_admin(self):
        self.view.ask('username: ')
        username = input()
        self.view.ask('password: ')
        password = input()
        self.view.ask('name(s): ')
        names = input()
        self.view.ask('last name: ')
        last_name = input()
        self.view.ask('last name (m): ')
        last_name_m = input()
        self.view.ask('Job title: ')
        job_title = input()
        self.view.ask('birthdate (YYYY/MM/DD): ')
        birthdate = input()
        return [username, password, names, last_name, last_name_m, job_title, birthdate]
    
    def ask_admin_update(self):
        self.view.ask('password: ')
        password = input()
        self.view.ask('name(s): ')
        names = input()
        self.view.ask('last name: ')
        last_name = input()
        self.view.ask('last name (m): ')
        last_name_m = input()
        self.view.ask('Job title: ')
        job_title = input()
        self.view.ask('birthdate (YYYY/MM/DD): ')
        birthdate = input()
        return [password, names, last_name, last_name_m, job_title, birthdate]
    
    def create_admin(self):
        username, password, names, last_name, last_name_m, job_title, birthdate = self.ask_admin()
        out = self.model.create_admin(username, password, names, last_name, last_name_m, job_title, birthdate)
        if out == True:
            self.view.ok(username, 'added')
        else:
            self.view.error("admin couldn't be added")
        return
    
    def read_admin(self):
        self.view.ask('Admin username: ')
        a_id = input()
        admin = self.model.read_admin(a_id)
        if type(admin) == tuple:
            self.view.show_admin_header(' Admin info '+a_id+' ')
            self.view.show_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('The admin does not exists.')
            else:
                self.view.error('Problem getting admin. Try again.')
        return

    def read_admin_names(self):
        self.view.ask('Admin name(s): ')
        name = input()
        admins = self.model.read_admin_names(name)
        if type(admins) == list:
            self.view.show_admin_header(' Admins with the name '+name+' ')
            for admin in admins:
                self.view.show_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('Error trying to read admins list.')
        return
    
    def read_all_admins(self):
        admins = self.model.read_all_admins()
        if type(admins) == list:
            self.view.show_all_admins(admins)
        else:
            self.view.error('Error trying to read all admins.')
        return
    
    def update_admin(self):
        self.view.ask('Admin username: ')
        a_id = input()
        admin = self.model.read_admin(a_id)
        if type(admin) == tuple:
            self.view.show_admin_header(' Admin data '+a_id+' ')
            self.view.show_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('The admin does not exists.')
            else:
                self.view.error('Problem getting admin. Try again.')
            return
        self.view.msg('Enter the values to moddify (leave empty for unchanged):')
        password, names, last_name, last_name_m, job_title, birthdate = self.ask_admin_update()
        out = self.model.update_admin(a_id, password, names, last_name, last_name_m, job_title, birthdate)
        if out == True:
            self.view.ok(a_id, 'updated')
        else:
            self.view.error('Admin could not be updated')
        return
    
    def delete_admin(self):
        self.view.ask('Admin username: ')
        a_id = input()
        self.view.ask('¿Are you sure you want to delete this admin? (Y = Yes) ')
        confirm = input()
        if confirm.lower() == 'y':
            count = self.model.delete_admin(a_id)
            if count != 0:
                self.view.ok(a_id, 'deleted')
            else:
                if count == 0:
                    self.view.error('Admin does not exist')
                else:
                    self.view.error('Error deleting this admin')
        else:
            self.view.msg("Admin won't be deleted. Canceling operation...")
        return
    """
    *********************
    * User controllers *
    *********************
    """
    def menu_user(self):
        while True:
            self.view.menu_user()
            self.view.select_option()
            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_user()
            elif o == '3':
                self.read_user_names()
            elif o == '4':
                self.read_all_users()
            elif o == '5':
                self.update_user()
            elif o == '6':
                self.delete_user()
            elif o == '0':
                return
            else:
                self.view.option_invalid()
    
    def ask_user(self):
        self.view.ask('username: ')
        username = input()
        self.view.ask('password: ')
        password = input()
        self.view.ask('name(s): ')
        names = input()
        self.view.ask('last name: ')
        last_name = input()
        self.view.ask('last name (m): ')
        last_name_m = input()
        self.view.ask('birthdate (YYYY/MM/DD): ')
        birthdate = input()
        return [username, password, names, last_name, last_name_m, birthdate]
    
    def ask_user_update(self):
        self.view.ask('password: ')
        password = input()
        self.view.ask('name(s): ')
        names = input()
        self.view.ask('last name: ')
        last_name = input()
        self.view.ask('last name (m): ')
        last_name_m = input()
        self.view.ask('birthdate (YYYY/MM/DD): ')
        birthdate = input()
        return [password, names, last_name, last_name_m, birthdate]
    
    def create_user(self):
        username, password, names, last_name, last_name_m, birthdate = self.ask_user()
        out = self.model.create_user(username, password, names, last_name, last_name_m, birthdate)
        if out == True:
            self.view.ok(username, 'added')
        else:
            self.view.error("user couldn't be added")
        return
    
    def read_user(self):
        self.view.ask('User username: ')
        a_id = input()
        user = self.model.read_user(a_id)
        if type(user) == tuple:
            self.view.show_user_header(' User info '+a_id+' ')
            self.view.show_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('The user does not exists.')
            else:
                self.view.error('Problem getting user. Try again.')
        return

    def read_user_names(self):
        self.view.ask('User name(s): ')
        name = input()
        users = self.model.read_user_names(name)
        if type(users) == list:
            self.view.show_user_header(' Users with the name '+name+' ')
            for user in users:
                self.view.show_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('Error trying to read users list.')
        return
    
    def read_all_users(self):
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_all_users(users)
        else:
            self.view.error('Error trying to read all users.')
        return
    
    def update_user(self):
        self.view.ask('User username: ')
        a_id = input()
        user = self.model.read_user(a_id)
        if type(user) == tuple:
            self.view.show_user_header(' User data '+a_id+' ')
            self.view.show_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('The user does not exists.')
            else:
                self.view.error('Problem getting user. Try again.')
            return
        self.view.msg('Enter the values to moddify (leave empty for unchanged):')
        password, names, last_name, last_name_m, birthdate = self.ask_user_update()
        out = self.model.update_user(a_id, password, names, last_name, last_name_m, birthdate)
        if out == True:
            self.view.ok(a_id, 'updated')
        else:
            self.view.error('User could not be updated')
        return
    
    def delete_user(self):
        self.view.ask('User username: ')
        a_id = input()
        self.view.ask('¿Are you sure you want to delete this user? (Y = Yes) ')
        confirm = input()
        if confirm.lower() == 'y':
            count = self.model.delete_user(a_id)
            if count != 0:
                self.view.ok(a_id, 'deleted')
            else:
                if count == 0:
                    self.view.error('User does not exist')
                else:
                    self.view.error('Error deleting this user')
        else:
            self.view.msg("User won't be deleted. Canceling operation...")
        return
    """
    *********************
    * Movie controllers *
    *********************
    """
    def menu_movie(self):
        while True:
            self.view.menu_movie()
            self.view.select_option()
            o = input()
            if o == '1':
                self.create_movie()
            elif o == '2':
                self.read_movie()
            elif o == '3':
                self.read_movie_title()
            elif o == '4':
                self.read_all_movies()
            elif o == '5':
                self.update_movie()
            elif o == '6':
                self.delete_movie()
            elif o == '0':
                return
            else:
                self.view.option_invalid()
    
    def ask_movie(self):
        self.view.ask('title: ')
        title = input()
        self.view.ask('duration: ')
        duration = input()
        self.view.ask('sinopsis: ')
        sinopsis = input()
        self.view.ask('director: ')
        director = input()
        self.view.ask('genre: ')
        genre = input()
        self.view.ask('rating: ')
        rating = input()
        self.view.ask('release date: ')
        release_date = input()
        return [title, duration, sinopsis, director, genre, rating, release_date]
    
    def create_movie(self):
        title, duration, sinopsis, director, genre, rating, release_date = self.ask_movie()
        out = self.model.create_movie(title, duration, sinopsis, director, genre, rating, release_date)
        if out == True:
            self.view.ok(title, 'added')
        else:
            self.view.error("movie couldn't be added")
        return
    
    def read_movie(self):
        self.view.ask('Movie ID: ')
        a_id = input()
        movie = self.model.read_movie(a_id)
        if type(movie) == tuple:
            self.view.show_movie_header(' Movie info '+a_id+' ')
            self.view.show_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('The movie does not exists.')
            else:
                self.view.error('Problem getting movie. Try again.')
        return

    def read_movie_title(self):
        self.view.ask('Movie name(s): ')
        title = input()
        movies = self.model.read_movie_title(title)
        if type(movies) == list:
            self.view.show_movie_header(' Movies with the title '+title+' ')
            for movie in movies:
                self.view.show_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Error trying to read movies list.')
        return
    
    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) == list:
            self.view.show_all_movies(movies)
        else:
            self.view.error('Error trying to read all movies.')
        return
    
    def update_movie(self):
        self.view.ask('Movie ID: ')
        a_id = input()
        movie = self.model.read_movie(a_id)
        if type(movie) == tuple:
            self.view.show_movie_header(' Movie data '+a_id+' ')
            self.view.show_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('The movie does not exists.')
            else:
                self.view.error('Problem getting movie. Try again.')
            return
        self.view.msg('Enter the values to moddify (leave empty for unchanged):')
        title, duration, sinopsis, director, genre, rating, release_date = self.ask_movie()
        out = self.model.update_movie(a_id, title, duration, sinopsis, director, genre, rating, release_date)
        if out == True:
            self.view.ok(a_id, 'updated')
        else:
            self.view.error('Movie could not be updated')
        return
    
    def delete_movie(self):
        self.view.ask('Movie moviename: ')
        a_id = input()
        self.view.ask('¿Are you sure you want to delete this movie? (Y = Yes) ')
        confirm = input()
        if confirm.lower() == 'y':
            count = self.model.delete_movie(a_id)
            if count != 0:
                self.view.ok(a_id, 'deleted')
            else:
                if count == 0:
                    self.view.error('Movie does not exist')
                else:
                    self.view.error('Error deleting this movie')
        else:
            self.view.msg("Movie won't be deleted. Canceling operation...")
        return
    """
    *********************
    * Hall controllers *
    *********************
    """
    def menu_hall(self):
        while True:
            self.view.menu_hall()
            self.view.select_option()
            o = input()
            if o == '1':
                self.create_hall()
            elif o == '2':
                self.read_hall()
            elif o == '3':
                self.read_hall_type()
            elif o == '4':
                self.read_all_halls()
            elif o == '5':
                self.update_hall()
            elif o == '6':
                self.delete_hall()
            elif o == '0':
                return
            else:
                self.view.option_invalid()
    
    def ask_hall(self):
        self.view.ask('hall ID: ')
        hall_id = input()
        self.view.ask('type: ')
        hall_type = input()
        self.view.ask('number of rows: ')
        n_rows = input()
        self.view.ask('number of seats per row: ')
        n_seats_row = input()
        return [hall_id, hall_type, n_rows, n_seats_row]
    
    def ask_hall_update(self):
        self.view.ask('type: ')
        hall_type = input()
        self.view.ask('number of rows: ')
        n_rows = input()
        self.view.ask('number of seats per row: ')
        n_seats_row = input()
        return [hall_type, n_rows, n_seats_row]
    
    def create_hall(self):
        hall_id, hall_type, n_rows, n_seats_row = self.ask_hall()
        out = self.model.create_hall(hall_id, hall_type, n_rows, n_seats_row)
        if out == True:
            self.view.ok(hall_id, 'added')
        else:
            self.view.error("hall couldn't be added")
        return
    
    def read_hall(self):
        self.view.ask('Hall ID: ')
        a_id = input()
        hall = self.model.read_hall(a_id)
        if type(hall) == tuple:
            self.view.show_hall_header(' Hall info '+a_id+' ')
            self.view.show_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('The hall does not exists.')
            else:
                self.view.error('Problem getting hall. Try again.')
        return

    def read_hall_type(self):
        self.view.ask('Hall type: ')
        hall_type = input()
        halls = self.model.read_hall_type(hall_type)
        if type(halls) == list:
            self.view.show_hall_header(' Halls of type '+hall_type+' ')
            for hall in halls:
                self.view.show_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('Error trying to read halls list.')
        return

    def read_all_halls(self):
        halls = self.model.read_all_halls()
        if type(halls) == list:
            self.view.show_all_halls(halls)
        else:
            self.view.error('Error trying to read all halls.')
        return
    
    def update_hall(self):
        self.view.ask('Hall ID: ')
        a_id = input()
        hall = self.model.read_hall(a_id)
        if type(hall) == tuple:
            self.view.show_hall_header(' Hall data '+a_id+' ')
            self.view.show_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('The hall does not exists.')
            else:
                self.view.error('Problem getting hall. Try again.')
            return
        self.view.msg('Enter the values to moddify (leave empty for unchanged):')
        hall_type, n_rows, n_seats_row = self.ask_hall_update()
        out = self.model.update_hall(a_id, hall_type, n_rows, n_seats_row)
        if out == True:
            self.view.ok(a_id, 'updated')
        else:
            self.view.error('Hall could not be updated')
        return
    
    def delete_hall(self):
        self.view.ask('Hall hallname: ')
        a_id = input()
        self.view.ask('¿Are you sure you want to delete this hall? (Y = Yes) ')
        confirm = input()
        if confirm.lower() == 'y':
            count = self.model.delete_hall(a_id)
            if count != 0:
                self.view.ok(a_id, 'deleted')
            else:
                if count == 0:
                    self.view.error('Hall does not exist')
                else:
                    self.view.error('Error deleting this hall')
        else:
            self.view.msg("Hall won't be deleted. Canceling operation...")
        return
    """
    *********************
    * Schedule controllers *
    *********************
    """
    def menu_schedule(self):
        while True:
            self.view.menu_schedule()
            self.view.select_option()
            o = input()
            if o == '1':
                self.create_schedule()
            elif o == '2':
                self.read_schedule()
            elif o == '3':
                self.read_schedule_movie()
            elif o == '4':
                self.read_all_schedules()
            elif o == '5':
                self.update_schedule()
            elif o == '6':
                self.delete_schedule()
            elif o == '0':
                return
            else:
                self.view.option_invalid()
    
    def ask_schedule(self):
        self.view.ask('movie id: ')
        movie_id = input()
        self.view.ask('hall id: ')
        hall_id = input()
        self.view.ask('day (YYYY/MM/DD): ')
        day = input()
        self.view.ask('hour: ')
        hour = input()
        return [movie_id, hall_id, day, hour]
    
    def create_schedule(self):
        movie_id, hall_id, day, hour = self.ask_schedule()
        out = self.model.create_schedule(movie_id, hall_id, day, hour)
        if out == True:
            print('schedule added')
            # Get schedule_id
            schedule_id = self.model.user_read_schedule_id(movie_id, hall_id, day, hour)[0]
            hall = self.model.read_hall(hall_id)
            for i in range(hall[2]+1): # Number of rows (Letter)
                l = self.numberToLetter[i][1].upper()
                for j in range(hall[3]+1): # number of seats per row
                    self.model.create_seat(schedule_id, l, j, 'Y')
                    # print(schedule_id, l, j, 'N')
            print((hall[2]+1)*(hall[3]+1), " seats were added to this schedule")
            # row, number, aviable=Y
            # get nrows, ncolumns with hall_id
        else:
            self.view.error("schedule couldn't be added")
        return
    
    def read_schedule(self):
        self.view.ask('Schedule ID: ')
        a_id = input()
        schedule = self.model.read_schedule(a_id)
        if type(schedule) == tuple:
            self.view.show_schedule_header(' Schedule info '+a_id+' ')
            self.view.show_schedule(schedule)
            self.view.show_schedule_midder()
            self.view.show_schedule_footer()
        else:
            if schedule == None:
                self.view.error('The schedule does not exists.')
            else:
                self.view.error('Problem getting schedule. Try again.')
        return
        
    def user_read_schedule(self, schedule_id):
        schedule = self.model.read_schedule(schedule_id)
        if type(schedule) == tuple:
            self.view.show_schedule_header(' Schedule selected '+schedule_id+' ')
            self.view.show_schedule(schedule)
            self.view.show_schedule_midder()
            self.view.show_schedule_footer()
            return True
        else:
            if schedule == None:
                self.view.error('The schedule does not exists.')
            else:
                self.view.error('Problem getting schedule. Try again.')
            return False
        return

    def read_schedule_movie(self):
        self.view.ask('ID of the movie: ')
        movie_id = input()
        schedules = self.model.read_schedule_movie(movie_id)
        if type(schedules) == list:
            self.view.show_schedule_header(' Schedules of the movie with id: '+movie_id
            +' ')
            for schedule in schedules:
                self.view.show_schedule(schedule)
                self.view.show_schedule_midder()
            self.view.show_schedule_footer()
        else:
            self.view.error('No aviable schedules were found for this movie')
        return
    
    def user_read_schedule_movie(self, movie_id):
        schedules = self.model.read_schedule_movie(movie_id)
        if type(schedules) == list:
            if len(schedules) == 0:
                print('----------------------------------------------')
                print('No aviable schedules were found for this movie')
                print('----------------------------------------------')
                return 0
            self.view.show_schedule_header(' Schedules of the movie with id: '+movie_id
            +' ')
            for schedule in schedules:
                self.view.show_schedule(schedule)
                self.view.show_schedule_midder()
            self.view.show_schedule_footer()
            return 1
        else:
            self.view.error('Error getting schedules for this movie')
        return
    
    def read_all_schedules(self):
        schedules = self.model.read_all_schedules()
        if type(schedules) == list:
            self.view.show_all_schedules(schedules)
        else:
            self.view.error('Error trying to read all schedules.')
        return
    
    def update_schedule(self):
        self.view.ask('Schedule ID: ')
        a_id = input()
        schedule = self.model.read_schedule(a_id)
        if type(schedule) == tuple:
            self.view.show_schedule_header(' Schedule data '+a_id+' ')
            self.view.show_schedule(schedule)
            self.view.show_schedule_midder()
            self.view.show_schedule_footer()
        else:
            if schedule == None:
                self.view.error('The schedule does not exists.')
            else:
                self.view.error('Problem getting schedule. Try again.')
            return
        self.view.msg('Enter the values to moddify (leave empty for unchanged):')
        movie_id, hall_id, day, hour = self.ask_schedule()
        out = self.model.update_schedule(a_id, movie_id, hall_id, day, hour)
        if out == True:
            self.view.ok(a_id, 'updated')
        else:
            self.view.error('Schedule could not be updated')
        return
    
    def delete_schedule(self):
        self.view.ask('Schedule ID: ')
        a_id = input()
        self.view.ask('¿Are you sure you want to delete this schedule? (Y = Yes) ')
        confirm = input()
        if confirm.lower() == 'y':
            count = self.model.delete_schedule(a_id)
            if count != 0:
                self.view.ok(a_id, 'deleted')
            else:
                if count == 0:
                    self.view.error('Schedule does not exist')
                else:
                    self.view.error('Error deleting this schedule')
        else:
            self.view.msg("Schedule won't be deleted. Canceling operation...")
        return
    """
    *********************
    * Seat controllers *
    *********************
    """
    def menu_seat(self):
        while True:
            self.view.menu_seat()
            self.view.select_option()
            o = input()
            if o == '1':
                self.create_seat()
            elif o == '2':
                self.read_seat()
            elif o == '3':
                self.read_seat_schedule()
            elif o == '4':
                self.read_all_seats()
            elif o == '5':
                self.update_seat()
            elif o == '6':
                self.delete_seat()
            elif o == '0':
                return
            else:
                self.view.option_invalid()
    
    def ask_seat(self):
        self.view.ask('schedule id: ')
        schedule_id = input()
        self.view.ask('row: ')
        row = input()
        self.view.ask('number: ')
        number = input()
        self.view.ask('aviable: ')
        aviable = input()
        return [schedule_id, row, number, aviable]
    
    def create_seat(self):
        schedule_id, row, number, aviable = self.ask_seat()
        out = self.model.create_seat(schedule_id, row, number, aviable)
        if out == True:
            print('seat added succesfully')
        else:
            self.view.error("seat couldn't be added")
        return
    
    def read_seat(self):
        self.view.ask('Seat ID: ')
        a_id = input()
        seat = self.model.read_seat(a_id)
        if type(seat) == tuple:
            self.view.show_seat_header(' Seat info '+a_id+' ')
            self.view.show_seat(seat)
            self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            if seat == None:
                self.view.error('The seat does not exists.')
            else:
                self.view.error('Problem getting seat. Try again.')
        return

    def read_seat_schedule(self):
        self.view.ask('ID of the schedule: ')
        schedule_id = input()
        seats = self.model.read_seat_schedule(schedule_id)
        if type(seats) == list:
            self.view.show_seat_header(' Seats of the schedule with id: '+schedule_id
            +' ')
            self.view.show_all_seats(seats)
            self.view.show_seat_footer()
        else:
            self.view.error('Error trying to read seats list.')
        return
    
    def user_read_seat_schedule(self, schedule_id):
        seats = self.model.read_seat_schedule(schedule_id)
        if type(seats) == list:
            self.view.show_seat_header(' Seats of the schedule with id: '+schedule_id
            +' ')
            self.view.show_all_seats(seats)
            self.view.show_seat_footer()
        else:
            self.view.error('Error trying to read seats list.')
        return

    def read_all_seats(self):
        seats = self.model.read_all_seats()
        if type(seats) == list:
            self.view.show_all_seats(seats)
        else:
            self.view.error('Error trying to read all seats.')
        return
    
    def update_seat(self):
        self.view.ask('Seat ID: ')
        a_id = input()
        seat = self.model.read_seat(a_id)
        if type(seat) == tuple:
            self.view.show_seat_header(' Seat data '+a_id+' ')
            self.view.show_seat(seat)
            self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            if seat == None:
                self.view.error('The seat does not exists.')
            else:
                self.view.error('Problem getting seat. Try again.')
            return
        self.view.msg('Enter the values to moddify (leave empty for unchanged):')
        schedule_id, row, number, aviable = self.ask_seat()
        out = self.model.update_seat(a_id, schedule_id, row, number, aviable)
        if out == True:
            self.view.ok(a_id, 'updated')
        else:
            self.view.error('Seat could not be updated')
        return
    
    def delete_seat(self):
        self.view.ask('Seat ID: ')
        a_id = input()
        self.view.ask('¿Are you sure you want to delete this seat? (Y = Yes) ')
        confirm = input()
        if confirm.lower() == 'y':
            count = self.model.delete_seat(a_id)
            if count != 0:
                self.view.ok(a_id, 'deleted')
            else:
                if count == 0:
                    self.view.error('Seat does not exist')
                else:
                    self.view.error('Error deleting this seat')
        else:
            self.view.msg("Seat won't be deleted. Canceling operation...")
        return
    """
    *********************
    * Ticket controllers *
    *********************
    """
    def menu_ticket(self):
        while True:
            self.view.menu_ticket()
            self.view.select_option()
            o = input()
            if o == '1':
                self.create_ticket()
            elif o == '2':
                self.read_ticket()
            elif o == '3':
                self.read_ticket_username()
            elif o == '4':
                self.read_all_tickets()
            elif o == '5':
                self.update_ticket()
            elif o == '6':
                self.delete_ticket()
            elif o == '0':
                return
            else:
                self.view.option_invalid()
    
    def ask_ticket(self):
        self.view.ask('seat id: ')
        seat_id = input()
        self.view.ask('username: ')
        username = input()
        self.view.ask('price: ')
        price = input()
        return [seat_id, username, price]
    
    def ask_ticket_update(self):
        self.view.ask('price: ')
        price = input()
        self.view.ask('buy date (YYY-MM-DD HH:MM:SS): ')
        buy_date = input()
        return [price, buy_date]
    
    def create_ticket(self):
        seat_id, username, price = self.ask_ticket()
        out = self.model.create_ticket(seat_id, username, price)
        if out == True:
            print('ticket added')
        else:
            self.view.error("ticket couldn't be added")
        return
    
    def user_create_ticket(self, seat_id, username, price):
        out = self.model.create_ticket(seat_id, username, price)
        if out == True:
            print('ticket added')
        else:
            self.view.error("ticket couldn't be added")
        return
    
    def read_ticket(self):
        self.view.ask('seat ID: ')
        a_id = input()
        self.view.ask('username: ')
        username = input()
        ticket = self.model.read_ticket(a_id, username)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Ticket info '+a_id+' '+username)
            self.view.show_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('The ticket does not exists.')
            else:
                self.view.error('Problem getting ticket. Try again.')
        return

    def read_ticket_username(self):
        self.view.ask('username: ')
        username = input()
        tickets = self.model.read_ticket_username(username)
        if type(tickets) == list:
            self.view.show_ticket_header(' Tickets of the user: '+username
            +' ')
            for ticket in tickets:
                self.view.show_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Error trying to read tickets list.')
        return

    def read_all_tickets(self):
        tickets = self.model.read_all_tickets()
        if type(tickets) == list:
            self.view.show_all_tickets(tickets)
        else:
            self.view.error('Error trying to read all tickets.')
        return
    
    def update_ticket(self):
        self.view.ask('seat ID: ')
        a_id = input()
        self.view.ask('username: ')
        username = input()
        ticket = self.model.read_ticket(a_id, username)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Ticket data '+a_id+' '+username)
            self.view.show_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('The ticket does not exists.')
            else:
                self.view.error('Problem getting ticket. Try again.')
            return
        self.view.msg('Enter the values to moddify (leave empty for unchanged):')
        price, buy_date = self.ask_ticket_update()
        out = self.model.update_ticket(a_id, username, price, buy_date)
        if out == True:
            print('+'*(len(str(a_id))+len(username)+24))
            print('+ ¡seat '+str(a_id)+' of '+username+' updated correctly! +')
            print('+'*(len(str(a_id))+len(username)+24))
        else:
            self.view.error('Ticket could not be updated')
        return
    
    def delete_ticket(self):
        self.view.ask('seat ID: ')
        a_id = input()
        self.view.ask('username: ')
        username = input()
        self.view.ask('¿Are you sure you want to delete this ticket? (Y = Yes) ')
        confirm = input()
        if confirm.lower() == 'y':
            count = self.model.delete_ticket(a_id, username)
            if count != 0:
                print('+'*(len(str(a_id))+len(username)+24))
                print('+ ¡seat '+str(a_id)+' of '+username+' deleted correctly! +')
                print('+'*(len(str(a_id))+len(username)+24))
            else:
                if count == 0:
                    self.view.error('Ticket does not exist')
                else:
                    self.view.error('Error deleting this ticket')
        else:
            self.view.msg("Ticket won't be deleted. Canceling operation...")
        return

    """
    ****************************
    * General controller  user *
    ****************************
    """
    def user_login(self):
        self.view.user_login()
        self.view.ask('username: ')
        username = input()
        self.view.ask('password: ')
        password = input()
        log = self.model.user_login(username, password)
        if type(log) == str:
            print("")
            print("\033[92mWelcome again!: \033[0m",log)
            self.local_user_username = log
            self.user_main_menu()
        else:
            print('\033[91musername or password are incorrect\033[0m')
            return

    def user_main_menu(self):
        while True:
            self.view.user_main_menu()
            self.view.select_option()
            o = input()
            if o == '1':
                self.user_menu_user()
            elif o == '2':
                self.user_menu_movies()
            elif o == '3':
                self.user_menu_tickets()
            elif o == '0':
                self.model.close_db()
                self.view.end()
                return
            else:
                self.view.option_invalid()
    
    def user_menu_user(self):
        user = self.model.read_user(self.local_user_username)
        self.view.show_user_header(self.local_user_username+' profile info: ')
        self.view.show_user(user)
        self.view.show_user_midder()
        self.view.show_user_footer()
    
    def user_menu_movies(self):
        self.view.user_menu_movies()
        self.view.select_option()
        o = input()
        if o == '1':
            self.read_all_movies()
            self.user_buy_ticket()
        elif o == '2':
            self.read_movie_title()
        elif o == '3':
            return
        else:
            self.view.option_invalid()
        
    def user_buy_ticket(self):
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
        print('1) Buy a ticket')
        print('2) Exit')
        self.view.ask("Your choice: ")
        o = input()
        if o == '1':
            self.view.ask("id of the movie: ")
            movie_id = input()
            m = self.model.read_movie(movie_id)
            if m != None:
                print("--------------------------------------")
                print('****MOVIE "',m[1], '" SELECTED*****')
                print("--------------------------------------")
                s = self.user_read_schedule_movie(movie_id)
                if s == 1:
                    self.view.ask("id of the schedule: ")
                    schedule_id = input()
                    s2 = self.user_read_schedule(schedule_id)
                    if (s2):
                        h = self.model.read_hall_with_schedule(schedule_id)
                        # print(h)
                        # self.user_read_seat_schedule(schedule_id)
                        seats = self.model.read_seat_schedule(schedule_id)
                        self.view.user_show_hall(seats)
                        # Falta validar si hay asientos disponibles
                        self.view.ask("Row: ")
                        row = input()
                        row = row.upper()
                        self.view.ask("Number: ")
                        num = input()
                        num = int(num)
                        seat_id = self.model.read_seat_id(schedule_id, row, num)[0]
                        seat_aviable = list(self.model.read_seat_id(schedule_id, row, num)[4])[0]
                        print(seat_id)
                        print(seat_aviable)
                        if not type(seat_id) == int:
                            print("")
                            print("Trouble getting that seat. The number may be incorrect")
                            return
                        if (seat_aviable == 'N'):
                            print("That seat is occupied. Try again")
                            return
                        print("Are you sure to buy this ticket with price: $55? (Y/N)")
                        o2 = input()
                        if o2.lower() == 'y':
                            self.model.user_buy_seat(seat_id)
                            self.user_create_ticket(seat_id, self.local_user_username, 55)
                            print("\n\033[92m*******************************************\033[0m")
                            print("\033[92mThank you! We bet you will enjoy this film! 🍿\033[0m")
                            print("\033[92m*******************************************\033[0m")
                            return
                    else:
                        print("wrong schedule id")
                        return
                else:
                    print("Wrong schedule")
                    return
            else:
                print("Wrong movie ID")
                return
        elif o == '2':
            return
        else:
            self.view.option_invalid()


    def user_menu_tickets(self):
        tickets = self.model.user_read_ticket_username(self.local_user_username)
        if type(tickets) == list:
            self.view.show_ticket_header(' Tickets of the user: '+self.local_user_username
            +' ')
            for ticket in tickets:
                self.view.user_show_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('Error trying to read tickets list.')
        return


    