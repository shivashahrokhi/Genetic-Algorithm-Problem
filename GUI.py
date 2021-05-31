import tkinter
from PIL import Image, ImageTk
from tkinter import Canvas, Button, Tk


class Interface:

    def __init__(self, level, solution):
        # Variables
        self.level = level
        self.solution = solution
        self.modified_level = level
        self.counter = -1
        self.item_size = 40
        self.starting_x = int(int(540 * 16 / 9) - int(400 * 16 / 9)) / 2
        self.starting_y = int(270)
        self.font = "Helvetica 16 bold italic"

        # Components
        self.root = Tk()
        self.canvas = Canvas(self.root, bg="skyblue", height=540, width=540 * 16 / 9)

        self.el1 = tkinter.Label(self.root, text=level[:self.counter], font=self.font)
        self.el2 = tkinter.Label(self.root, text=level[self.counter], font=self.font, bg='yellow')
        self.el3 = tkinter.Label(self.root, text=level[(self.counter + 1):], font=self.font)
        self.sl1 = tkinter.Label(self.root, text=solution[:self.counter], font=self.font)
        self.sl2 = tkinter.Label(self.root, text=solution[self.counter], font=self.font, bg='yellow')
        self.sl3 = tkinter.Label(self.root, text=solution[(self.counter + 1):], font=self.font)
        self.free_label1 = tkinter.Label(self.root, text="          ")
        self.free_label2 = tkinter.Label(self.root, text="          ")

        self.b = Button(self.root, text='NEXT', command=self.update_gui, font=self.font)

        # Images
        self.Lakitu = Image.open("Images\\Lakitu.png").resize((int(0.87 * self.item_size), self.item_size),
                                                              Image.ANTIALIAS)
        self.Goomba = Image.open("Images\\Goomba.png").resize((int(1.37 * self.item_size), self.item_size),
                                                              Image.ANTIALIAS)
        self.Dead_Goomba = Image.open("Images\\Dead Goomba.png").resize((int(1.37 * self.item_size), self.item_size),
                                                                        Image.ANTIALIAS)
        self.Mario = Image.open("Images\\Mario.png").resize((self.item_size, self.item_size),
                                                            Image.ANTIALIAS)
        self.Mario_Jumping = Image.open("Images\\Mario Jumping.png").resize((self.item_size, self.item_size),
                                                                            Image.ANTIALIAS)
        self.Unit = Image.open("Images\\Unit.png").resize((self.item_size, self.item_size),
                                                          Image.ANTIALIAS)
        self.Mushroom = Image.open("Images\\Mushroom.png").resize((self.item_size, self.item_size),
                                                                  Image.ANTIALIAS)
        self.Mario_Crouching = Image.open("Images\\Mario_Crouching.png").resize((self.item_size, self.item_size),
                                                                                Image.ANTIALIAS)
        self.Flag = Image.open("Images\\Flag.png").resize((3 * self.item_size, 3 * self.item_size),
                                                          Image.ANTIALIAS)
        self.Foreground = Image.open("Images\\Foreground.png").resize((int(540 * 16 / 9), 270 - self.item_size),
                                                                      Image.ANTIALIAS)

        # ImageTks
        self.L = ImageTk.PhotoImage(master=self.canvas, image=self.Lakitu)
        self.G = ImageTk.PhotoImage(master=self.canvas, image=self.Goomba)
        self.DG = ImageTk.PhotoImage(master=self.canvas, image=self.Dead_Goomba)
        self.M = ImageTk.PhotoImage(master=self.canvas, image=self.Mario)
        self.MJ = ImageTk.PhotoImage(master=self.canvas, image=self.Mario_Jumping)
        self.U = ImageTk.PhotoImage(master=self.canvas, image=self.Unit)
        self.MU = ImageTk.PhotoImage(master=self.canvas, image=self.Mushroom)
        self.MC = ImageTk.PhotoImage(master=self.canvas, image=self.Mario_Crouching)
        self.F = ImageTk.PhotoImage(master=self.canvas, image=self.Flag)
        self.FG = ImageTk.PhotoImage(master=self.canvas, image=self.Foreground)

        self.arrange_component()
        self.update_gui()
        self.root.mainloop()

    def arrange_component(self):
        self.canvas.pack()
        self.el1.pack(padx=0, pady=10, side=tkinter.LEFT)
        self.el2.pack(padx=0, pady=10, side=tkinter.LEFT)
        self.el3.pack(padx=0, pady=10, side=tkinter.LEFT)
        self.free_label1.pack(side=tkinter.LEFT)
        self.sl1.pack(padx=0, pady=10, side=tkinter.LEFT)
        self.sl2.pack(padx=0, pady=10, side=tkinter.LEFT)
        self.sl3.pack(padx=0, pady=10, side=tkinter.LEFT)
        self.free_label2.pack(side=tkinter.LEFT)
        self.b.pack(padx=0, pady=10, side=tkinter.LEFT)

    def update_canvas(self, part1, part2):
        # Clearing canvas
        self.canvas.delete("all")

        # Drawing items on the canvas
        for i in range(self.counter - part1, self.counter + part2):
            j = i if self.counter < 11 else i - self.counter + part1
            self.canvas.create_image(self.starting_x + j * self.item_size,
                                     self.starting_y + self.item_size, image=self.U)
            if self.level[i] == 'L':
                self.canvas.create_image(self.starting_x + j * self.item_size,
                                         self.starting_y - self.item_size + 10, image=self.L)
            elif self.level[i] == 'G':
                if self.counter >= i > 1 and self.solution[i - 2] == '1':
                    self.canvas.create_image(self.starting_x + j * self.item_size,
                                             self.starting_y, image=self.DG)
                else:
                    self.canvas.create_image(self.starting_x + j * self.item_size,
                                             self.starting_y, image=self.G)
            elif self.level[i] == 'M':
                if self.counter < i or i > 0 and self.solution[i - 1] == '1':
                    self.canvas.create_image(self.starting_x + j * self.item_size,
                                             self.starting_y, image=self.MU)

        # Drawing the flag when necessary
        if len(self.level) < 20 or part2 < 10:
            flag_location = 20 if len(self.level) > 20 else len(self.level)
            self.canvas.create_image(self.starting_x + flag_location * self.item_size, self.starting_y, image=self.F)
            self.canvas.create_image(self.starting_x + flag_location * self.item_size, self.starting_y + self.item_size,
                                     image=self.U)

        # Drawing the foreground
        self.canvas.create_image(int(270 * 16 / 9), 450, image=self.FG)

        # Drawing Mario
        if len(self.level) > 20:
            mario_location = self.counter if self.counter < 11 else 20 - part2
        else:
            mario_location = self.counter if self.counter < 11 else len(self.level) - part2
        if self.counter == len(self.level):
            if self.solution[self.counter - 1] == '1':
                self.canvas.create_image(self.starting_x + mario_location * self.item_size,
                                         self.starting_y - self.item_size, image=self.MJ)
            elif self.solution[self.counter - 1] == '2':
                self.canvas.create_image(self.starting_x + mario_location * self.item_size,
                                         self.starting_y + 5, image=self.MC)
            else:
                self.canvas.create_image(self.starting_x + mario_location * self.item_size,
                                         self.starting_y, image=self.M)
            self.b["state"] = "disabled"
        elif self.counter > 0 and self.solution[self.counter - 1] == '1':
            self.canvas.create_image(self.starting_x + mario_location * self.item_size,
                                     self.starting_y - self.item_size, image=self.MJ)
        elif self.counter > 0 and self.solution[self.counter - 1] == '2':
            self.canvas.create_image(self.starting_x + mario_location * self.item_size,
                                     self.starting_y + 5, image=self.MC)
        else:
            self.canvas.create_image(self.starting_x + mario_location * self.item_size,
                                     self.starting_y, image=self.M)

    def update_gui(self):
        self.counter += 1
        part2 = min(len(self.level) - self.counter, 20 - self.counter) if self.counter < 11 else \
            min(len(self.level) - self.counter, 10)
        part1 = 20 - part2 if len(self.level) > 20 else len(self.level) - part2
        self.el1['text'] = self.level[self.counter - part1: self.counter]
        self.el2['text'] = self.level[self.counter] if self.counter < len(self.level) else ""
        self.el3['text'] = self.level[self.counter + 1: self.counter + part2]
        self.sl1['text'] = self.solution[self.counter - part1: self.counter]
        self.sl2['text'] = self.solution[self.counter] if self.counter < len(self.level) else ""
        self.sl3['text'] = self.solution[self.counter + 1: self.counter + part2]
        self.update_canvas(part1, part2)
