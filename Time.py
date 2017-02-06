from datetime import datetime
from datetime import timedelta



class MarsTime:
    def __init__(self):
        # Sim Start is May 3rd, 2040
        self.worldTime = datetime.strptime("20240503000000", '%Y%m%d%H%M%S')
        self.sols = 0.0

    def updateSimTime(self, seconds):
        self.worldTime = self.worldTime + timedelta(0, seconds)
        self.sols += float(seconds)/(24*60*60*60)

    def isNight(self):
        night = True
        md = (self.worldTime)
        if md.hour > 6 and md.hour < 18:
            night = False
        return night

gMarsTime = MarsTime()


def main():
    gMarsTime.updateSimTime(seconds=60)
    print(gMarsTime.sols)


if __name__ == '__main__':
    main()
