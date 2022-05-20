import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.glamour = 10
        self.eat = 100
    def to_study(self):
        print("time to study")
        self.progress +=5
        self.gladness -=3
        self.glamour -= 5
    def to_sleep(self):
        print("time to sleep")
        self.gladness +=3
    def to_chill(self):
        self.gladness +=5
        self.progress -= 1
    def to_shop(self):
        self.gladness += 10
        self.progress -= 0.2
        self.glamour += 10
    def to_eat(self):
        self.gladness += 10
        self.progress -= 0.2
    def to_work(self):
        self.gladness -= 0.5
        self.glamour -= 5
    def is_alive(self):
        if self.progress < -2.5:
            print("Cast out...")
            self.alive = False
            print("Fail")
        elif self.gladness < 0:
            print("Depression")
            self.alive = False
            print("Fail")
        elif self.progress >25:
            print("Passed Externally")
            self.alive = False
        elif self.glamour > 50:
            print("Passed Externally, trener fell in love with U")
            self.alive = False
        elif self.glamour < 0:
            print("U suicided")
            print("Fail")
            self.alive = False
        elif self.eat < 5:
            print("U poor, you are hungry")
            print("Fail")
            self.alive = False


    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Glamour = {self.glamour}")
        print(f"eat = {self.eat}")

    def live(self, day):
        day = "Day" + str(day) + 'of'+ self.name+"live"
        print(f"{day:=^50}")
        live_cube = random.randint(1,5)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_eat()
        elif live_cube == 5:
            self.to_shop()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
