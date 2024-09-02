#Attempted to make a menu for the program, but it doesn't work as intended.
#Using pystray as a reference: https://pypi.org/project/pystray/
#Also using one of my other programs as a reference: https://github.com/T-Kalv/Tasp-Talia-/releases/tag/v1.0.0-beta
import os
import pystray
import PIL.Image
import les_dames

image = PIL.Image.open("les dames icon.png")

def on_clicked(icon, item):
    if str(item) == "Les_Dames":#Runs les_dames program
        #run les_dames.py
        les_dames.main()
    elif str(item) == "Ai Les_Dames":#Runs Ai les_dames program
        #run les_dames_ai.py
        les_dames.main()

    elif str(item) == "Exit":#Exits the program
        icon.stop()


icon = pystray.Icon("Les Dames", image, menu=pystray.Menu(#Allows user to run the program in the taskbar tray
    pystray.MenuItem("Les Dames", on_clicked),
    pystray.MenuItem("AI Les Dames", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))
icon.run()





















