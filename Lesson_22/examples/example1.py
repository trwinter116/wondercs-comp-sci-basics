# %%
class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """

        total_seconds = (hrs * 3600) + (mins * 60) + secs
        self.hours = total_seconds // 3600
        remaining_time = total_seconds % 3600
        self.minutes = remaining_time // 60
        self.seconds = remaining_time % 60

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def increment(self, secs):
        self.seconds += secs

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, time2):
        total_seconds = self.to_seconds() + time2.to_seconds()
        return MyTime(0, 0, total_seconds)


# %%
t1 = MyTime(10, 55, 12)
t2 = MyTime(10, 48, 22)
t1.after(t2)


# %%
# Demonstrate operator overload
t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t1 + t2
print(t3)

# %%
