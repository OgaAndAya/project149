from tkinter import*
import random

root=Tk()
root.title("Random Words with Alphabets'")
root.geometry("500x500")


alpha_list= list= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(list)
random_no1= random.radiant(1,26)
random_no2= random.radiant(1,26)
random_no3= random.radiant(1,26)
random_no4= random.radiant(1,26)
random_no5= random.radiant(1,26)

random_alpha1= alpha_list
random_alpha2= alpha_list
random_alpha3= alpha_list
random_alpha4= alpha_list
random_alpha5= alpha_list

def random_number():
    random_no= random.randint(0,25)
    print(random_no)
    random_word= list[random_no]
    print("Your Combined Word is: "+ random_word)
    
btn=Button(root,text= "What is your Random Word?", command= random_number)
btn.place(relx=0.5, rely=0.5, anchor= CENTER)

root.mainloop()