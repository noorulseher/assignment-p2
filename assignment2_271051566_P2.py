
#cinemaBookingsystem
import pickle
class SystemAdministrator:
    def __init__(self):
        self.movies={}
        self.screens={}
        self.timeslots={}

    def create_movie_listing(self, movie_title, available_seats):
        self.movies[movie_title]=available_seats

    def create_screen(self, screen_number):
        self.screens[screen_number]=[]

    def allocate_timeslot(self, screen_number, timeslot):
        if screen_number in self.screens:
            self.timeslots[screen_number]=timeslot
        else:
            print("this screen number does not avaliable.")

    def save_data(self):
        with open("cinema_data.pickle","wb") as file:
            pickle.dump((self.movies, self.screens, self.timeslots), file)

    def load_data(self):
        with open("cinema_data.pickle","rb") as file:
            self.movies, self.screens, self.timeslots = pickle.load(file)

class User:
    def __init__(self,username):
        self.username = username

    def select_movie(self,movie_title):
        print(f"{self.username} this is the selected movie title {movie_title}.")

    def choose_seats(self,seats):
        print(f"{self.username} choose seats you want for the movie:{seats}")

    def initiate_reservation(self):
        print(f"{self.username} initiated reservation of the coustomer")

class Movie:
    def __init__(self,title,available_seats):
        
        self.title=title
        self.available_seats=available_seats if isinstance(available_seats, list) else []
        self.bookings =[]

    def update_available_seats(self,booked_seats):
        for seat in booked_seats:
            if seat in self.available_seats:
                self.available_seats.remove(seat)

    def record_booking(self,user,selected_seats):
        self.bookings.append((user, selected_seats))

class Screen:
    def __init__(self,screen_number):
        self.screen_number=screen_number

class Timeslot:
    def __init__(self,start_time,end_time):
        self.start_time=start_time
        self.end_time=end_time

class BookingDetails:
    def __init__(self, user, movie, date, time, selected_seats):
        self.user=user
        self.movie=movie
        self.date=date
        self.time=time
        self.selected_seats=selected_seats
        self.booking_id=self.generate_booking_id()

    def generate_booking_id(self):
      return f"BOOKING{BookingDetails.counter}"


BookingDetails.counter=1235
    
booking_admin=SystemAdministrator()
booking_admin.create_movie_listing("The Conjuring:The devil mede me do it", 100)
booking_admin.create_screen(1)
booking_admin.allocate_timeslot(1, Timeslot("5:00", "8:00"))
booking_admin.save_data()


booking_admin.load_data()
print(booking_admin.movies)
print(booking_admin.screens)
print(booking_admin.timeslots)

coustomer= User("fatima")
coustomer.select_movie("The Conjuring:The Devil made me do it")
coustomer.choose_seats(["seat3","seat4"])
coustomer.initiate_reservation()


avengers_movie = Movie("The  Conjuring:The devil made me do it", 100)
avengers_movie.update_available_seats(["seat3", "seat4"])
avengers_movie.record_booking(coustomer,["seat3", "seat4"])

booking_details = BookingDetails(coustomer, avengers_movie, "7-5-24", "5:00", ["seat3", "seat4"])
print("this is the coustomer booking id:", booking_details.booking_id)









         


          


    

     

        










    
