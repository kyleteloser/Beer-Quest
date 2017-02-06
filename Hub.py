# Print statements
# start of the game
# where to print all the code

import time
import random

print("Welcome to Beer Quest a tavern/blacksmith style game")
print("")
time.sleep(0.1)





















def main():
    root = tk.Tk()
    root.geometry(gInitialGeometery)
    app = MarsGame(root)
    app.master.title(gGameName)
    app.updateUX()
    app.mainloop()
    root.quit()