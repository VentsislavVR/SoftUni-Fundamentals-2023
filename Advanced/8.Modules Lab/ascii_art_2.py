from pyfiglet import Figlet

def print_art(msg):
    figlet = Figlet(font="isometric4")
    ascii_art = figlet.renderText(f"{msg}")
    print(ascii_art)

msg = input("Choose your words:  ")
print_art(msg)