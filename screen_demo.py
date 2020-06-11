import lcddriver
import time

display = lcddriver.lcd()

try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        print("Write to display")
        display.lcd_display_string("Alexey Shanin", 1) # Write line of text to first line of display
        display.lcd_display_string("Artyom Sterstyuk", 2) # Write line of text to second line of display
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_display_string("Very important message", 1)  # Refresh the first line of display with a different message
	display.lcd_display_strinf("S dnyom Rossii", 2)
        time.sleep(2)                                     # Give time for the message to be read
        display.lcd_clear()                               # Clear the display of any data
        time.sleep(2)                                     # Give time for the message to be read

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Stop")
    display.lcd_clear()
