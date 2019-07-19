from pyfiglet import figlet_format as fig
from termcolor import colored

message = input("What message do you want to print? ")
color = input("What color? ")

result = fig(message)
if color in ("red", "green", "yellow", "blue", "magenta", "cyan", "white"):
    result = colored(result, color)
    print(result)
else:
    result = colored(result, "red")
    print(result)
