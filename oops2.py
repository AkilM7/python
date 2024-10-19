class Theatre:
    ticket = 120
    name = "PVR Cinemas"
    
    
    def __init__(self, movie_name, screen_time):
        self.cinema_name = movie_name
        self.show_time = screen_time

    def watch(self):
        print("Watching", self.cinema_name)


    
screen1 = Theatre("Vettaiyan",630)
screen2 = Theatre("Lubber Pandhu",700)
screen3 = Theatre("Goat", 730)

screen3.watch()


#also give as

class Theatre:
    ticket = 120
    name = "PVR Cinemas"

#Constructor
    def __init__(self, movie_name, screen_time):
        self.movie_name = movie_name
        self.screen_time = screen_time

    def watch(self):
        print("Watching", self.movie_name)


    
screen1 = Theatre("Vettaiyan",630)
screen2 = Theatre("Lubber Pandhu",700)
screen3 = Theatre("Goat", 730)

screen3.watch()
