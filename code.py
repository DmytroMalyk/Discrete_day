'''discrete day module'''

import random
import time

def prime(fn):
    '''decorator'''
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class Routine:
    '''class for recreating the day'''

    def __init__(self) -> None:

        self.hour = 7
        self.study_time = 0

        self.start = self._awake()

        self.sleep = self._sleep()
        self.eat = self._eat()
        self.study = self._study()
        self.workout = self._workout()
        self.procrastinate = self._procrastinate()

        self.state = self.start

    @prime
    def _awake(self):
        '''method for starting the day'''
        while True:

            coef = yield
            prints("You woke up, it's 7 am in the morning")

            if coef < 4:
                prints("But it's weekends, so you sleep for a couple more hours")
                self.hour += 3
                prints('zzz...')
                prints("Now it's 10 am")

            prints("It's time to get something to eat now!")
            self.state = self.eat

    @prime
    def _sleep(self):
        '''sleeping method'''
        while True:

            _ = yield
            prints('zzz...')

            break

    @prime
    def _procrastinate(self):
        '''wasting time with a fancy name'''
        while True:

            _ = yield
            prints('You ended up scrolling on a social media for an hour')
            self.hour += 1

            if self.study_time < 4:
                prints('The deadlines are pushing, you need to study now!')
                self.state = self.study

            if self.hour == 8:
                prints("It's time for a workout!")
                self.state = self.workout

    @prime
    def _eat(self):
        '''eating method'''
        while True:

            coef = yield
            prints('*chewing')
            self.hour += 1

            if coef in (1, 2):
                prints("It's time for a workout!")
                self.state = self.workout

            if 3 <= coef <= 6 and self.study_time < 4:
                prints("It's time to study now!")
                self.state = self.study

            if coef >= 7:
                prints('You were feeling a little bit down so you ended up procrastinating')
                self.state = self.procrastinate

    @prime
    def _study(self):
        '''studying method'''
        while True:

            coef = yield
            prints('You are studying hard')
            self.hour += 1

            if coef < 4:
                prints('You were feeling a little bit down so you ended up procrastinating')
                self.state = self.procrastinate

            if self.hour == 8:
                prints("It's time for a workout!")
                self.state = self.workout

            if self.study_time < 4:
                prints("You need to study more")
                self.state = self.study

            prints("It's time for a workout!")
            self.state = self.workout

    @prime
    def _workout(self):
        '''workout method'''
        while True:

            _ = yield
            prints('You are working out')
            self.hour += 2

            prints('Now the day ended and you are going back to sleep')
            self.state = self.sleep

    def send(self, action):
        '''method for sending'''
        try:
            self.state.send(action)
        except StopIteration:
            return

def prints(text: str):
    '''function for slowly printing out the text'''
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    time.sleep(0.02)
    print()


def initiate():
    '''initiates the inout amount of ours of the day'''

    day = Routine()
    for _ in range(12):
        num = random.randint(1, 10)
        day.send(num)

    prints('The day ended.')

if __name__ == "__main__":
    initiate()
