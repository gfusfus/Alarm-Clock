from datetime import datetime
import time
import webbrowser


def main():
    now = datetime.now()
    print ("Welcome to the ultimate alarm clock!")
    print ("The current time is: "+ '%s:%s' % (now.hour, now.minute))
    chosen_time = input("When would you like to wakeup (please write your chosen time in HH:MM format)?")
    time_len = len(chosen_time)
    chosen_hour, chosen_minute =  chosen_time.split(":")
    chosen_hour = int (chosen_hour)
    chosen_minute = int (chosen_minute)
    var_time_check = time_check(chosen_time, time_len, chosen_hour, chosen_minute)
    while var_time_check == False:
        chosen_time = input("Please enter your chosen time again in HH:MM format")
        var_time_check = time_check(chosen_time, time_len, chosen_hour,chosen_minute)
    print ("You chose to wake up at "+chosen_time)
    link = get_link()
    var_link_check = link_check(link)
    while var_link_check == False:
        print("Please re-enter your chosen link from YouTube.com. After pasting the link press space and after it enter.")
        link = input("Link: ")
        var_link_check = link_check(link)
    print("Alright, we are ready to go! Good night.")
    now_hour = now.hour
    now_minute = now.minute
    while chosen_hour != now_hour or chosen_minute != now_minute:
        time.sleep(0.5)
        now = datetime.now()
        now_hour = now.hour
        now_minute = now.minute
    webbrowser.open_new(link)
    print("Time to wake up!")

def time_check(chosen_time, time_len,chosen_hour, chosen_minute):
    if time_len != 5:
        return False
    if chosen_time[2] != ":":
        return False
    if chosen_hour < 0 or chosen_hour > 24:
        return False
    if chosen_minute < 0 or chosen_minute > 60:
        return False
    else:
        return True


def get_link():
    print("After choosing wakeup time, it is time to choose with what song (or other video) you would like to wake up with.")
    print("Please paste your chosen video link from YouTube.com. After pasting the link, please press space and after it click entetr.")
    link = input
    return link()


def link_check(link):
    if link[0:24] != "https://www.youtube.com/":
        return False
    return True


if __name__ == "__main__":
    main()
