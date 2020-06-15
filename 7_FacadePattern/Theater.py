class Amplifier :
    def __init__(self, description) :
        self.description = description

    def on(self) :
        print('{} on'.format(self.description))

    def off(self) :
        print('{} off'.format(self.description))

    def setStereoSound(self) :
        print('{} stereo mode on'.format(self.description))

    def setSurroundSound(self) :
        print('{} surround sound on (5 speakers, 1 subwoofer)'.format(self.description))

    def setVolume(self, level) :
        print('{} setting volume to {}'.format(self.description, str(level)))

    def setTuner(self, tuner) :
        print('{} setting tuner to {}'.format(self.description, str(self.dvd)))
        self.tuner = tuner

    def setDvd(self, dvd) :
        print('{} setting DVD player to {}'.format(self.description, str(self.dvd)))
        self.dvd = dvd

    def setCd(self, cd) :
        print('{} setting cd player to {}'.format(self.description, str(self.cd)))
        self.cd = cd

    def __str__(self) :
        return self.description

class CdPlayer :
    def __init__(self, description, amplifier) :
        self.description = description
        self.amplifier = amplifier

    def on(self) :
        print("{} on".format(self.description))

    def off(self) :
        print("{} off".format(self.description))

    def eject(self) :
        self.title = None
        print("{} eject".format(self.description))

    def play(self, **kwargs) :
        if kwargs['title'] :
            self.title = title
            self.current_track = 0
            print('{} playing "{}"'.format(self.description, self.title))
        if kwargs['track'] :
            if self.title :
                self.current_track = kwargs['track']
                print('{}  playing track {}'.format(self.description, str(self.current_track))
            else :
                print("{} can't play track {}, no cd inserted".format(self.description, str(self.current_track)))

    def stop(self) :
        self.current_track = 0
        print("{} stopped".format(self.description))

    def pause(self) :
        self.current_track = 0
        print('{} pause "{}"'.format(self.description, self.title))

    def __str__(self) :
        return self.description

class DvdPlayer :
    def __init__(self, description, amplifier) :
        self.description = description
        self.amplifier = amplifier

    def on(self) :
        print("{} on".format(self.description))

    def off(self) :
        print("{} off".format(self.description))

    def eject(self) :
        self.movie = None
        print("{} eject".format(self.description))

    def play(self, **kwargs) :
        if kwargs['movie'] :
            self.movie = movie
            self.current_track = 0
            print('{} playing "{}"'.format(self.description, self.movie))
        if kwargs['track'] :
            if self.movie :
                self.current_track = kwargs['track']
                print('{}  playing track {} of {}'.format(self.description, str(self.current_track), str(self.movie))
            else :
                print("{} can't play track {}, no dvd inserted".format(self.description, str(kwargs['track'])))

    def stop(self) :
        self.current_track = 0
        print('{} stopped {}'.format(self.description, self.movie))

    def pause(self) :
        self.current_track = 0
        print('{} pause "{}"'.format(self.description, self.movie))

    def setTwoChannelAudio(self) :
        self.current_track = 0
        print('{} set two channel audio'.format(self.description))

    def setSurroundAudio(self) :
        self.current_track = 0
        print('{} set surround audio'.format(self.description))

    def __str__(self) :
        return self.description

class PopcornPopper :
    def __init__(self, description) :
        self.description = description

    def on(self) :
        print("{} on".format(self.description))

    def off(self) :
        print("{} off".format(self.description))

    def pop(self) :
        print("{} popping popcorn!".format(self.description))

    def __str__(self) :
        return self.description

class Projector :
    def __init__(self, description, dvdPlayer) :
        self.description = description
        self.dvdPlayer = dvdPlayer

    def on(self) :
        print("{} on".format(self.description))

    def off(self) :
        print("{} off".format(self.description))

    def wideScreenMode(self) :
        print("{} in widescreen mode (16x9 aspect ratio)".format(self.description))

    def tvMode(self) :
        print("{} in tv mode (4x3 aspect ratio)".format(self.description))

    def __str__(self) :
        return self.description

class Screen :
    def __init__(self, description) :
        self.description = description

    def up(self) :
        print("{} going up".format(self.description))

    def down(self) :
        print("{} going down".format(self.description))

    def __str__(self) :
        return self.description

class TheaterLights :
    def __init__(self, description) :
        self.description = description

    def on(self) :
        print("{} on".format(self.description))

    def off(self) :
        print("{} off".format(self.description))

    def dim(self, level) :
        print("{} dimming to {}%".format(self.description, str(level)))

    def tvMode(self) :
        print("{} in tv mode (4x3 aspect ratio)".format(self.description))

    def __str__(self) :
        return self.description
