class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"


    def next_second(self):
        self.seconds = (self.seconds + 1) % (Time.max_seconds + 1)
        self.minutes = (self.minutes + (self.seconds == 0)) % (Time.max_minutes + 1)
        self.hours = (self.hours + (self.seconds == 0 and self.minutes == 0)) % (Time.max_hours + 1)

        # if self.seconds == Time.max_seconds + 1:
        #     self.seconds = 0
        #     self.minutes += 1
        #     if self.minutes == Time.max_minutes + 1:
        #         self.minutes = 0
        #         self.hours += 1
        #         if self.hours == Time.max_hours + 1:
        #             self.hours = 0
        return self.get_time()



time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())