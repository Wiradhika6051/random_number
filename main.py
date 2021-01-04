from tkinter import *
import random

root = Tk()
root.title("Random Number Generator")
root.iconbitmap("random_number.ico")

#Function
def randomize(minimum,maximum):
    """
    Procedure to show the randomized number between a maximum and minimum value inclusively(both points included)
    using randint() function in random module and show the result to the screen
    """
    #Get the random number
    number = random.randint(minimum,maximum)
    #Show the result
    result["text"] = "Hasil:"+str(number)

def clear():
    """
    Function to clear the input entry and the result number
    """
    lower.delete(0,END)
    upper.delete(0,END)
    result["text"] = "Hasil:"


#Widget
#Judul
title = Label(root,text="Random Number Generator")
#Input prompt
lower_bound = Label(root,text="Batas Bawah:")
upper_bound = Label(root,text="Batas Atas:")
#Input box
lower = Entry(root)
upper = Entry(root)
#Button
roll_button = Button(root,text="ROLL",command=lambda:randomize(int(lower.get()),int(upper.get())))
clear_button = Button(root,text="CLEAR",command=clear)
#Result
result = Label(root,text="Hasil:")
#Grid
title.grid(row=0,column=0,columnspan=2)
lower_bound.grid(row=1,column=0)
upper_bound.grid(row=1,column=1)
lower.grid(row=2,column=0)
upper.grid(row=2,column=1)
roll_button.grid(row=3,column=0)
clear_button.grid(row=3,column=1)
result.grid(row=4,column=0)
#Main Loop
root.mainloop()