from test import test


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
        seconds_time = self.to_seconds()
        seconds_time += secs

        self.hours = seconds_time // 3600
        remaining_time = seconds_time % 3600
        self.minutes = remaining_time // 60
        self.seconds = remaining_time % 60

    def to_seconds(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def between(self, lower_bound, upper_bound):
        return lower_bound.to_seconds() <= self.to_seconds() < upper_bound.to_seconds()

    def __gt__(self, time2):
        return self.to_seconds() > time2.to_seconds()


# Exercise 1:
# Write a Boolean method "between" that takes two MyTime objects, t1 and t2, as
# arguments, and returns True if the invoking object falls between the two times.
# Assume t1 <= t2, and make the test closed at the lower bound and open at the upper
# bound, i.e. return True if t1 <= obj < t2.
t1 = MyTime(4, 6, 17)
t2 = MyTime(5, 8, 47)
t3 = MyTime(8, 28, 0)
test(t2.between(t1, t3))
test(not t3.between(t1, t2))

# Exercise 2:
# Overload the __gt__ operator so that instead of having to write "if t1.after(t2): ..."
# we can use the more convenient "if t1 > t2 : ..."
test(not t1 > t2)
test(t3 > t2)

# Exercise 3:
# Rewrite "increment" as a method using our seconds logic.
t1.increment(-20)
test_time = MyTime(4, 5, 57)
test((t1.hours == test_time.hours) and (t1.minutes == test_time.minutes) and (t1.seconds == test_time.seconds))
