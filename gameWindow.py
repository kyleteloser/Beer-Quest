import tkinter as tk
gInitialGeometery = "1400x800"

class GameWindow(tk.Frame):
    def __init__(self, root):
        self.mainFrame = tk.Frame.__init__(self, root)
        self.gameWindow = tk.LabelFrame(root, text="Game", borderwidth=2, cursor="cross_reverse",
                                       relief="sunken")
        self.root = root
        self.gameWindow.grid(row = 0, column=0)

    def updateUX(self):
        pass
       

def main():
    root = tk.Tk()
    root.geometry(gInitialGeometery)
    app = GameWindow(root)
    app.master.title("Beer Quest")
    app.updateUX()
    app.mainloop()
    root.quit()
   
   
if __name__ == "__main__":
    main()