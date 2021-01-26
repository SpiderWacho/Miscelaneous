#! python3
#Automatic search in maps a direction in the clipboard or in the command-line
import webbrowser, sys, pyperclip

#Check if command line argunments were passed

if len(sys.argv) > 1:
    adress = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()

#Launch maps

webbrowser.open('https://www.google.com.ar/maps/place/' + adress)



