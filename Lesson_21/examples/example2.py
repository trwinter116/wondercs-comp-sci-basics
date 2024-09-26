# %%
class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """

        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def increment(self, secs):
        pass

    def to_seconds(self):
        pass


# %%
tim1 = MyTime(11, 875, 30)
print(tim1)

# %%
# Pure function


def add_time(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds

    if s >= 60:
        m += 1
        s -= 60

    if m >= 60:
        h += 1
        m -= 60
    return MyTime(h, m, s)



# %%
current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 50, 0)
done_time = add_time(current_time, bread_time)
print(done_time)

# %%
# Modifier
# Rewrite for while


def increment(t, secs):
    t.seconds += secs

    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes += 1

    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1


# %%
increment(current_time, 500)
print(current_time)

# %%

# Implement increment as a method
current_time.increment(500)
print(current_time)

# %%

# Write a to_seconds method on the class
current_time_seconds = current_time.to_seconds()
print(current_time_seconds)


# %%
# Rewrite init to be based off total seconds
# hours = 3600 seconds

second_time = MyTime(0, 0, 9835)
print(second_time)


# %%
# Rewrite add_time function to take advantage of seconds

def add_time(t1, t2):
    total = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, total)


current_time = MyTime(9, 14, 30)
bread_time = MyTime(3, 50, 0)
done_time = add_time(current_time, bread_time)
print(done_time)

# %%
