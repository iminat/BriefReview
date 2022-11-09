# Task 4
# The following table lists the sound level in decibels for several common noises.
# Noise	        Decibel Level
# Jackhammer	130 dB
# Gas Lawnmower	106 dB
# Alarm Clock	70 dB
# Quite Room	40 dB
# Write a program that reads a sound level in decibels from the user.
# If the user enters a decibel level that matches one of the noises in the table
# then your program should display a message containing only that noise.
# If the user enters a number of decibels between the noises listed
# then your program should display a message indicating which noises the value is between.
# Ensure that your program also generates reasonable output for a value smaller than the quietest noise in the table,
# and for a value larger than the loudest noise in the table.
sound_level = int(input())
if sound_level == 130:
    print('Jackhammer')
elif 130 > sound_level > 106:
    print('The sound level is between Jackhammer and Gas Lawnmower')
elif sound_level == 106:
    print('Gas Lawnmower')
elif 106 > sound_level > 70:
    print('The sound level is between Gas Lawnmower and Alarm Clock')
elif sound_level == 70:
    print('Alarm Clock')
elif 70 > sound_level > 40:
    print('The sound level is between Alarm Clock and Quite Room')
elif sound_level == 40:
    print('Quite Room')
elif sound_level < 40:
    print('The sound level is less than Quite Room')
elif sound_level > 130:
    print('The sound level is more than Jackhammer')