from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#-----------------------UI_Setup--------------------------------

random_dictionary={}
words_data=pandas.read_csv("french_words.csv")
to_learn=words_data.to_dict('records')





#reading words from csv 

def creating_word():
  
  global random_dictionary , flip_timer
  window.after_cancel(flip_timer)#for solving the bug of running without counting the time
  random_dictionary=random.choice(to_learn)
  french_word=random_dictionary['French']
  canvas.itemconfig(lang,text="French",fill="black")
  canvas.itemconfig(word,text=f"{french_word}",fill="black")
  canvas.itemconfig(canvas_image,image=flash_card)
  window.after(3000,func=flip_card)#after 3 seconds , make this function



#flip card

def flip_card():
    
  
    
    canvas.itemconfig(lang,text="English",fill="white")
    canvas.itemconfig(word,text=random_dictionary["English"],fill="white")
    canvas.itemconfig(canvas_image,image=back_card)


def is_known():
  to_learn.remove(random_dictionary)
  data=pandas.DataFrame(to_learn)
  data.to_csv("words_to_learn.csv")
  creating_word()








window=Tk()
window.title("Flashy")
window.config(padx=30,pady=30,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)



  


#canvas and card

canvas=Canvas(width=400,height=500)

#flash card
flash_card=PhotoImage(file="card_front.png")
canvas_image=canvas.create_image(200,400,image=flash_card)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

# flipped card 

back_card=PhotoImage(file="card_back.png")




#contents

lang=canvas.create_text(190,270,text="Title",font=("Ariel",20,"italic"))
word=canvas.create_text(190,350,text="Word",font=("Ariel",30,"bold"))

canvas.grid(column=0,row=0,columnspan=2)


#buttoms


right_image=PhotoImage(file="right.png")
wrong_image=PhotoImage(file="wrong.png")

right_click=Button(image=right_image,highlightthickness=0,command=is_known)
right_click.grid(column=1,row=1)

wrong_click=Button(image=wrong_image,highlightthickness=0,command=creating_word)
wrong_click.grid(column=0,row=1)

#showing the card at the start

creating_word()



window.mainloop()