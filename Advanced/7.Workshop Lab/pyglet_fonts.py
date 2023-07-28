from time import sleep
import pyfiglet

with open("pyfigletfonts.txt", "r") as file:
    fonts = file.read().splitlines()

for fonty in fonts:
    print("Testing font " + fonty)
    f = pyfiglet.Figlet(font=fonty, width=80)
    print(f.renderText('FooBar'))