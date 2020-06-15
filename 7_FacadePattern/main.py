import Theater
import HomeTheaterFacade

if __name__ == "__main__":
    amp = Theater.Amplifier("Top-O-Line Amplifier")
    tuner = Theater.Tuner("Top-O-Line AM/FM Tuner", amp)
    dvd = Theater.DvdPlayer("Top-O-Line DVD Player", amp)
    cd = Theater.CdPlayer("Top-O-Line CD Player", amp)
    projector = Theater.Projector("Top-O-Line Projector", dvd)
    lights = Theater.TheaterLights("Theater Ceiling Lights")
    screen = Theater.Screen("Theater Screen")
    popper = Theater.PopcornPopper("Popcorn Popper")
    homeTheater = HomeTheaterFacade.HomeTheaterFacade(amp, tuner, dvd, cd, projector, screen, lights, popper)
    homeTheater.watchMovie("Raiders of the Lost Ark")
    homeTheater.endMovie()
