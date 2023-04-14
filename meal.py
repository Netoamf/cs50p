def main():
    user_input = input("What time is it? ")

    time = convert(user_input)
    
    if time >= 7 and time <=8:
        print("breakfast time")
    elif time >=12 and time <=13:
        print("lunch time")
    elif time >=18 and time <=19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    new_minute: float(minutes) / 60
    return float(hours) + round(new_minute,2)
    
if __name__ == "__main__":
    main()