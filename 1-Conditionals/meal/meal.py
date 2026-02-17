def main():
    time = input("What's the time? ")

    if convert(time) <= 8:
        print("Breakfast time")


#    elif 12 <= ConvertedTime <= 13:
#        print("Lunch Time")
#    elif 18 <= ConvertedTime <= 19:
#        print("Dinner Time")
#    else:
#        print("Nothing")


def convert(t):
    hours, minutes = time.split(":")
    t = int(hours) + (int(minutes) / 60)


main()
