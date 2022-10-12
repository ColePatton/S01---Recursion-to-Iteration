#-------------------------------
#
# CC1 Formative #4 - Your own Recursion
#
# Cole Patton
#
# A quite simple program but I think I did pretty good thinking this one up for just getting back into
# Thonny, since trying to remember how to do everything has been kind of sucky );
#
#-------------------------------
import time

# My defined Function for counting out the numbers in a digit
def count_numbers(number):
    if number > 0:
        for digits in range(number): #I use a For Loop here to do this too :D
            print(digits)
            time.sleep(0.4) #I just like to add time.sleep so that it prints out a bit slower making it easier to watch
        
        count_numbers(number-1)

#------Main Code Here------#
count_numbers(6)