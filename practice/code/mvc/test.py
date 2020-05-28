# from model.model import Model
# from view.view import View
from controller.controller import Controller


# m = Model()
# v = View()
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

# m.create_hall("A-1", "XE Experience", 20, 20)
# m.create_hall("A-2", "3D", 19, 28)
# m.create_hall("B-3", "regular", 22, 15)
# m.create_hall("B-4", "regular", 22, 15)
# print(m.read_all_halls())



c.start()



# m.delete_all_tables()
# m.close_db()