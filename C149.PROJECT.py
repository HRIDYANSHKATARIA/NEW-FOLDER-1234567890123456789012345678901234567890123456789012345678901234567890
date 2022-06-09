from tkinter import *
import random
root = Tk()

root.title("WORDS")
root.geometry("400x500")

LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(LETTERS)

label_names = Label(root)


def WORD_CREATER():
    WORD_1 = random.randint(0,25)
    WORD_2 = random.randint(0,25)
   
    print(WORD_1,WORD_2)
    LETTERS_TO_PUT = LETTERS[WORD_1,WORD_2]
    print("THE WORD IS  "+LETTERS_TO_PUT)
    label_names["text"]="THE WORD IS "+ LETTERS_TO_PUT
    
   

btn1 = Button(root,text = "MAKE A WORD",command = WORD_CREATER)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)

label_names.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()