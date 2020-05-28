from mysql import connector

# TODO: Cambiar todos los select para leer los nombres en lugar de los ids
class Model:

    ######################     database settings          ######################
    ############################################################################

    def __init__(self,config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    
    def read_config_db(self):
        d ={}

        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
        self.cursor.execute("SET time_zone='-05:00'")

    def close_db(self):
        self.cnx.close()
    
    # For testing purpouse only
    def delete_all_tables(self):
        try:
            sql = 'DELETE FROM tickets; DELETE FROM seats; DELETE FROM schedules; DELETE FROM halls; DELETE FROM movies; DELETE FROM users; DELETE FROM admins;'
            self.cursor.execute(sql)
            return 0
        except connector.Error as err:
            print(err)
            return (err) 

    ########################     admins methods         ######################
    ##########################################################################
    def create_admin(self, username, password, names, last_name, last_name_m, job_title, birthdate):
        try:
            if last_name_m != '':
                sql = 'INSERT INTO admins(username, password, names, last_name, last_name_m, job_title, birthdate) VALUES(%s,%s,%s,%s,%s,%s,%s);'
                values = (username, password, names, last_name, last_name_m, job_title, birthdate)
            else:
                sql = 'INSERT INTO admins(username, password, names, last_name, job_title, birthdate) VALUES(%s,%s,%s,%s,%s,%s);'
                values = (username, password, names, last_name, job_title, birthdate)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_admin(self, username):
        try:
            sql = 'SELECT * FROM admins WHERE username = %s;'
            values = (username,)
            self.cursor.execute(sql, values)
            admin = self.cursor.fetchone()
            return admin
        except connector.Error as err:
            print(err)
            return (err)

    def read_admin_names(self, names):
        try:
            sql = "SELECT * FROM admins WHERE names LIKE '%" + names +"%';"
            self.cursor.execute(sql)
            admins = self.cursor.fetchall()
            return admins
        except connector.Error as err:
            print(err)
            return (err)


    def read_all_admins(self):
        try:
            sql = 'SELECT * FROM admins;'
            self.cursor.execute(sql)
            admins = self.cursor.fetchall()
            return admins
        except connector.Error as err:
            print(err)
            return (err)  

    def update_admin(self, username, password, names, last_name, last_name_m, job_title, birthdate):

        fields = []
        val = []

        if password !='':
            val.append(password)
            fields.append('password = %s')
        if names != '':
            val.append(names)
            fields.append('names = %s')
        if last_name != '':
            val.append(last_name)
            fields.append('last_name = %s')
        if last_name_m != '':
            val.append(last_name_m)
            fields.append('last_name_m = %s') 
        if job_title != '':
            val.append(job_title)
            fields.append('job_title = %s') 
        if birthdate != '':
            val.append(birthdate)
            fields.append('birthdate = %s') 

        val.append(username)
        val = tuple(val)         
        try:
            sql = 'UPDATE admins SET ' + ','.join(fields) +' WHERE username = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def delete_admin(self, username):
        try:
            sql = 'DELETE  FROM admins WHERE username = %s;'
            values = (username,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)

    ########################     users methods         ######################
    ##########################################################################
    def create_user(self, username, password, names, last_name, last_name_m, birthdate):
        try:
            if last_name_m != '':
                sql = 'INSERT INTO users(username, password, names, last_name, last_name_m, birthdate) VALUES(%s,%s,%s,%s,%s,%s);'
                values = (username, password, names, last_name, last_name_m, job_title, birthdate)
            else:
                sql = 'INSERT INTO users(username, password, names, last_name, birthdate) VALUES(%s,%s,%s,%s,%s);'
                values = (username, password, names, last_name, birthdate)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_user(self, username):
        try:
            sql = 'SELECT * FROM users WHERE username = %s;'
            values = (username,)
            self.cursor.execute(sql, values)
            user = self.cursor.fetchone()
            return user
        except connector.Error as err:
            print(err)
            return (err)

    def read_user_names(self, names):
        try:
            sql = "SELECT * FROM users WHERE names LIKE '%" + names +"%';"
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
        except connector.Error as err:
            print(err)
            return (err)


    def read_all_users(self):
        try:
            sql = 'SELECT * FROM users;'
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            return users
        except connector.Error as err:
            print(err)
            return (err)  

    def update_user(self, username, password, names, last_name, last_name_m, birthdate):

        fields = []
        val = []

        if password !='':
            val.append(password)
            fields.append('password = %s')
        if names != '':
            val.append(names)
            fields.append('names = %s')
        if last_name != '':
            val.append(last_name)
            fields.append('last_name = %s')
        if last_name_m != '':
            val.append(last_name_m)
            fields.append('last_name_m = %s') 
        if birthdate != '':
            val.append(birthdate)
            fields.append('birthdate = %s') 

        val.append(username)
        val = tuple(val)         
        try:
            sql = 'UPDATE users SET ' + ','.join(fields) +' WHERE username = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def delete_user(self, username):
        try:
            sql = 'DELETE FROM users WHERE username = %s;'
            values = (username,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)

    ######################     movies methods         ###################
    ##########################################################################
    def create_movie(self, title, duration, sinopsis, director, genre, rating, release_date):
        try:
            sql = 'INSERT INTO movies(title, duration, sinopsis, director, genre, rating, release_date) VALUES(%s,%s,%s,%s,%s,%s,%s);'
            values = (title, duration, sinopsis, director, genre, rating, release_date)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_movie(self, movie_id):
        try:
            sql = 'SELECT * FROM movies WHERE movie_id = %s;'
            values = (movie_id,)
            self.cursor.execute(sql, values)
            movie = self.cursor.fetchone()
            return movie
        except connector.Error as err:
            print(err)
            return (err)

    def read_movie_title(self, title):
        try:
            sql = "SELECT * FROM movies WHERE title LIKE '%" + title + "%';"
            print(sql)
            self.cursor.execute(sql)
            movies = self.cursor.fetchall()
            return movies
        except connector.Error as err:
            print(err)
            return (err)


    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM movies;'
            self.cursor.execute(sql)
            movies = self.cursor.fetchall()
            return movies
        except connector.Error as err:
            print(err)
            return (err)  

    def update_movie(self, movie_id, title, duration, sinopsis, director, genre, rating, release_date):

        fields = []
        val = []

        if title !='':
            val.append(title)
            fields.append('title = %s')
        if duration !='':
            val.append(duration)
            fields.append('duration = %s')
        if sinopsis != '':
            val.append(siposis)
            fields.append('sinopsis = %s')
        if director != '':
            val.append(director)
            fields.append('director = %s')
        if genre != '':
            val.append(genre)
            fields.append('genre = %s') 
        if rating != '':
            val.append(rating)
            fields.append('rating = %s') 
        if release_date != '':
            val.append(release_date)
            fields.append('release_date = %s') 

        val.append(movie_id)
        val = tuple(val)         
        try:
            sql = 'UPDATE movies SET ' + ','.join(fields) +' WHERE movie_id = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def delete_movie(self, movie_id):
        try:
            sql = 'DELETE  FROM movies WHERE movie_id = %s;'
            values = (movie_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)

    #########################     halls methods         ######################
    ##########################################################################
    def create_hall(self, hall_id, hall_type, n_rows, n_seats_row):
        try:
            sql = 'INSERT INTO halls(hall_id, hall_type, n_rows, n_seats_row) VALUES(%s,%s,%s,%s);'
            values = (hall_id, hall_type, n_rows, n_seats_row)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_hall(self, hall_id):
        try:
            sql = 'SELECT * FROM halls WHERE hall_id = %s;'
            values = (hall_id,)
            self.cursor.execute(sql, values)
            hall = self.cursor.fetchone()
            return hall
        except connector.Error as err:
            print(err)
            return (err)

    def read_hall_type(self, hall_type):
        try:
            sql = 'SELECT * FROM halls WHERE hall_type LIKE %s;'
            values = (hall_type,)
            self.cursor.execute(sql, values)
            halls = self.cursor.fetchall()
            return halls
        except connector.Error as err:
            print(err)
            return (err)


    def read_all_halls(self):
        try:
            sql = 'SELECT * FROM halls;'
            self.cursor.execute(sql)
            halls = self.cursor.fetchall()

            return halls
        except connector.Error as err:
            print(err)
            return (err)  

    def update_hall(self, hall_id, hall_type, n_rows, n_seats_row):

        fields = []
        val = []

        if hall_type !='':
            val.append(hall_type)
            fields.append('hall_type = %s')
        if n_rows !='':
            val.append(n_rows)
            fields.append('n_rows = %s')
        if n_seats_row != '':
            val.append(n_seats_row)
            fields.append('n_seats_row = %s')

        val.append(hall_id)
        val = tuple(val)         
        try:
            sql = 'UPDATE halls SET ' + ','.join(fields) +' WHERE hall_id = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def delete_hall(self, hall_id):
        try:
            sql = 'DELETE  FROM halls WHERE hall_id = %s;'
            values = (hall_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)

    #######################     scehdules methods         ####################
    ##########################################################################
    def create_schedule(self, movie_id, hall_id, day, hour):
        try:
            sql = 'INSERT INTO schedules(movie_id, hall_id, day, hour) VALUES(%s,%s,%s,%s);'
            values = (movie_id, hall_id, day, hour)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_schedule(self, schedule_id):
        try:
            sql = 'SELECT schedule_id, movie_id, hall_id, DATE_FORMAT(day, "%d/%m/%y"), DATE_FORMAT(hour, "%H:%i") FROM schedules WHERE schedule_id ='+str(schedule_id)+';'
            # values = (schedule_id,)
            self.cursor.execute(sql)
            schedule = self.cursor.fetchone()
            return schedule
        except connector.Error as err:
            print(err)
            return (err)

    def user_read_schedule_id(self, movie_id, hall_id, day, hour):
        try:
            sql = 'SELECT schedule_id FROM schedules WHERE movie_id = %s AND hall_id = %s AND day = %s AND hour = %s;'
            values = (movie_id, hall_id, day, hour)
            self.cursor.execute(sql, values)
            schedule = self.cursor.fetchone()
            return schedule
        except connector.Error as err:
            print(err)
            return (err)

    def read_schedule_movie(self, movie_id):
        try:
            sql = 'SELECT schedule_id, movie_id, hall_id, DATE_FORMAT(day, "%d/%m/%y"), DATE_FORMAT(hour, "%H:%i") FROM schedules WHERE movie_id ='+str(movie_id)+';'
            # values = (movie_id,)
            self.cursor.execute(sql)
            schedules = self.cursor.fetchall()
            return schedules
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_hall_with_schedule(self, schedule_id):
        try:
            sql = 'SELECT hall_id FROM schedules WHERE schedule_id ='+str(schedule_id)+';'
            # values = (movie_id,)
            self.cursor.execute(sql)
            schedules = self.cursor.fetchall()
            return schedules
        except connector.Error as err:
            print(err)
            return (err)

    def read_all_schedules(self):
        try:
            sql = 'SELECT schedule_id, movie_id, hall_id, DATE_FORMAT(day, "%d/%m/%y"), DATE_FORMAT(hour, "%H:%i") FROM schedules;'
            self.cursor.execute(sql)
            schedules = self.cursor.fetchall()
            return schedules
        except connector.Error as err:
            print(err)
            return (err)  

    def update_schedule(self, schedule_id, movie_id, hall_id, day, hour):

        fields = []
        val = []

        if movie_id !='':
            val.append(movie_id)
            fields.append('movie_id = %s')
        if hall_id !='':
            val.append(hall_id)
            fields.append('hall_id = %s')
        if day != '':
            val.append(day)
            fields.append('day = %s')
        if hour != '':
            val.append(hour)
            fields.append('hour = %s')

        val.append(schedule_id)
        val = tuple(val)         
        try:
            sql = 'UPDATE schedules SET ' + ','.join(fields) +' WHERE schedule_id = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def delete_schedule(self, schedule_id):
        try:
            sql = 'DELETE  FROM schedules WHERE schedule_id = %s;'
            values = (schedule_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)
    
    ##########################     seats methods         #####################
    ##########################################################################
    def create_seat(self, schedule_id, row, number, aviable):
        try:
            sql = 'INSERT INTO seats(schedule_id, row, number, aviable) VALUES(%s,%s,%s,%s);'
            values = (schedule_id, row, number, aviable)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_seat(self, seat_id):
        try:
            sql = 'SELECT * FROM seats WHERE seat_id = %s;'
            values = (seat_id,)
            self.cursor.execute(sql, values)
            seat = self.cursor.fetchone()
            return seat
        except connector.Error as err:
            print(err)
            return (err)

    def read_seat_schedule(self, schedule_id):
        try:
            sql = 'SELECT * FROM seats WHERE schedule_id = %s;'
            values = (schedule_id,)
            self.cursor.execute(sql, values)
            seats = self.cursor.fetchall()
            return seats
        except connector.Error as err:
            print(err)
            return (err)
    
    def read_seat_id(self, schedule_id, row, number):
        try:
            sql = 'SELECT * FROM seats WHERE schedule_id = %s AND row = %s AND number = %s;'
            values = (schedule_id,row,number,)
            self.cursor.execute(sql, values)
            seat = self.cursor.fetchone()
            return seat
        except connector.Error as err:
            print(err)
            return (err)

    def read_all_seats(self):
        try:
            sql = 'SELECT * FROM seats;'
            self.cursor.execute(sql)
            seats = self.cursor.fetchall()
            return seats
        except connector.Error as err:
            print(err)
            return (err)  

    def update_seat(self, seat_id, schedule_id, row, number, aviable):

        fields = []
        val = []

        if schedule_id !='':
            val.append(schedule_id)
            fields.append('schedule_id = %s')
        if row !='':
            val.append(row)
            fields.append('row = %s')
        if number != '':
            val.append(number)
            fields.append('number = %s')
        if aviable != '':
            val.append(aviable)
            fields.append('aviable = %s')

        val.append(seat_id)
        val = tuple(val)         
        try:
            sql = 'UPDATE seats SET ' + ','.join(fields) +' WHERE seat_id = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def user_buy_seat(self, seat_id):
        fields = []
        val = []
        val.append('N')
        fields.append('aviable = %s')
        val.append(seat_id)
        val = tuple(val) 
        try:
            sql = 'UPDATE seats SET ' + ','.join(fields) +' WHERE seat_id = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)


    def delete_seat(self, seat_id):
        try:
            sql = 'DELETE  FROM seats WHERE seat_id = %s;'
            values = (seat_id,)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)
    
    ##########################     tickets methods         #####################
    ##########################################################################
    def create_ticket(self, seat_id, username, price):
        try:
            sql = 'INSERT INTO tickets(seat_id, username, price) VALUES(%s,%s,%s);'
            values = (seat_id, username, price)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_ticket(self, seat_id, username):
        try:
            sql = 'SELECT seat_id, username, FORMAT(price,0), DATE_FORMAT(buy_date, ' + '"%H:%i %d/%m/%y"' + ') FROM tickets WHERE seat_id = '+str(seat_id)+' AND username = "' +username+'";'
            # values = (seat_id,username,)
            # print(sql)
            self.cursor.execute(sql)
            ticket = self.cursor.fetchone()
            return ticket
        except connector.Error as err:
            print(err)
            return (err)

    def read_ticket_username(self, username):
        try:
            sql = 'SELECT seat_id, username, FORMAT(price,0), DATE_FORMAT(buy_date, ' + '"%H:%i %d/%m/%y"' + ') FROM tickets WHERE  username = "' +username+'";'
            # values = (username,)
            self.cursor.execute(sql)
            tickets = self.cursor.fetchall()
            return tickets
        except connector.Error as err:
            print(err)
            return (err)
    
    def user_read_ticket_username(self, username):
        try:
            sql = 'SELECT movies.title, schedules.hall_id, CONCAT(schedules.day, " ", schedules.hour) AS date, tickets.seat_id, FORMAT(tickets.price,0) AS price, DATE_FORMAT(tickets.buy_date,"%H:%i %d/%m/%y") AS buy_date FROM tickets JOIN seats ON tickets.seat_id = seats.seat_id JOIN schedules ON seats.schedule_id = schedules.schedule_id JOIN movies ON schedules.movie_id = movies.movie_id WHERE  username = "' +username+'";'
            # values = (username,)
            self.cursor.execute(sql)
            tickets = self.cursor.fetchall()
            return tickets
        except connector.Error as err:
            print(err)
            return (err)

    def read_all_tickets(self):
        try:
            sql = 'SELECT seat_id, username, FORMAT(price,0), DATE_FORMAT(buy_date, ' + '"%H:%i %d/%m/%y"' + ') FROM tickets;'
            self.cursor.execute(sql)
            tickets = self.cursor.fetchall()
            return tickets
        except connector.Error as err:
            print(err)
            return (err)  

    def update_ticket(self, seat_id, username, price, buy_date ):

        fields = []
        val = []

        if price !='':
            val.append(price)
            fields.append('price = %s')
        if buy_date !='':
            val.append(buy_date)
            fields.append('buy_date = %s')

        val.append(seat_id)
        val.append(username)
        val = tuple(val)         
        try:
            sql = 'UPDATE tickets SET ' + ','.join(fields) +' WHERE seat_id = %s AND username = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def delete_ticket(self, seat_id, username):
        try:
            sql = 'DELETE  FROM tickets WHERE seat_id = %s AND username = %s;'
            values = (seat_id,username)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)

    def admin_login(self, username, password):
        try:
            sql = 'SELECT * FROM admins WHERE username = %s AND password = %s;'
            values = (username,password,)
            self.cursor.execute(sql, values)
            admin = self.cursor.fetchone()
            if admin != None:
                return username
            else:
                return 0
        except connector.Error as err:
            print(err)
            return (err)
    
    def user_login(self, username, password):
        try:
            sql = 'SELECT * FROM users WHERE username = %s AND password = %s;'
            values = (username,password,)
            self.cursor.execute(sql, values)
            user = self.cursor.fetchone()
            if user != None:
                return username
            else:
                return 0
        except connector.Error as err:
            print(err)
            return (err)
