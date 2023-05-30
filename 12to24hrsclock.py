

'''

Converting 12 hrs time to 24 hours 
'''


def main():
    user_input = input("Enter time in a hour:minute:second format : ")
    print(convert(user_input))

def convert(time):
    if time[-2:] == 'AM' and time[2:] == '12': # checking if its 12 am
        return '00' + time[2:-2] # converting 12 am to 00:00:00
    elif time[-2:] == 'AM': # removing the am if its below 12. What I mean is that if its like 8:00 in the morning we remove the am and return 8:00
        return time[:-2] # returning the same time, just removing the am
    elif time[2:]=='PM' and time[2:] == '12': # checking if its is 12 pm
        return time[:-2] # removing pm and returning just 12
    else:
        return str((int(time[:2]) +12)) + time[2:-2]  # removing the pm and changing it to 24 hrs, like if its 3pm making it 15 pm


main()