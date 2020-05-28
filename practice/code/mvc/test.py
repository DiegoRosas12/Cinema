from model.model import Model
from view.view import View
from controller.controller import Controller
from string import ascii_lowercase

m = Model()
v = View()
c = Controller()
print("connected...")
# m.create_admin("admin", "12345", "Diego","Rosas", "González", "Manager", "1997/12/12")
# m.create_user("testUser", "12345", "John", "Smith", "", "1967/06/07/" )
# print(m.read_all_admins())
# print(m.read_all_users())


# m.create_movie("Pirates of the caribbean", 120, "Meet Jack Sparrow and his fantastic adventures", "Gore Verbinski","Action", "AAA", "2003/06/28")
# m.create_movie("Avengers: Endgame", 170, "The Marvel heroes defeat the planet from Thanos", "Russo Brothers","Action", "B-12", "2019/04/26")
# m.create_movie("Avatar", 160, "Year 2154. Pandora is a planet with life and a new culture but humans are destroying it.", "James Cameron", "Action", "B-15", "2009/12/18")
# m.create_movie("Titanic", 130, "Jack and Rose come from different economic classes but they fall in love in the Titanic", "James Cameron", "Drama", "B-15", "1997/12/19")
# m.create_movie("Minions", 90, "The history of the adorable minions come before meeting Gru.", "Pierre Coffin", "Comedy", "AAA", "2015/06/11")
# print(m.read_all_movies())


# m.create_hall("A-1", "XE Experience", 20, 30)
# m.create_hall("A-2", "3D", 19, 28)
# m.create_hall("B-3", "regular", 22, 32)
# m.create_hall("B-4", "regular", 22, 32)
# print(m.read_all_halls())

# m.create_schedule(1,"B-3", '2020/05/28', '16:00')
# m.create_schedule(1,"B-3", '2020/05/28', '18:00')
# m.create_schedule(1,"B-3", '2020/05/28', '20:30')
# m.create_schedule(2,"B-4", '2020/05/28', '16:30')
# m.create_schedule(2,"B-4", '2020/05/28', '20:00')
# m.create_schedule(2,"B-3", '2020/05/29', '20:00')
# print(m.read_all_schedules())

# m.create_seat(6, 'A', 1, 'Y')
# m.create_seat(6, 'A', 2, 'Y')
# m.create_seat(6, 'A', 3, 'Y')
# m.create_seat(7, 'A', 4, 'Y')
# m.create_seat(7, 'B', 1, 'Y')
# m.create_seat(7, 'B', 2, 'N')
# m.create_seat(8, 'B', 3, 'Y')
# m.create_seat(10, 'B', 4, 'N')
# print(m.read_all_seats())

# m.create_ticket(25, 'testUser',67)
# m.create_ticket(26, 'testUser',50)
# m.create_ticket(27, 'testUser',50)
# print(m.read_all_tickets())

c.start()
# v.error('terminal')
# seats = m.read_seat_schedule(17)
# for s in seats:3

#     print(s)
# v.user_show_hall(seats)
# v.start()
# print(m.read_seat_id(17, 'O', 2)[0])
# r = m.user_login('testUser', '12345')
# r = m.read_user('testUser')

# c.create_schedule()
# c.user_buy_ticket()


# m.delete_all_tables()
# m.close_db()