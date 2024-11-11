import customtkinter as ctk
from random import choice,choices,randint
from time import time
import os
from threading import Thread
from tkinter import messagebox
# Functions
def is_numer_only(ch):
    a = "0123456789"
    for i in ch:
        if i not in a:
            return False
    else : return True

def no_error():
    if not os.path.exists(save_entry.get()):
        messagebox.showerror("path error","Incorrect output Path")
        return False
    elif is_numer_only(nbr_entry.get())==False:
        messagebox.showerror("number","password count must be a number")
        return False
    elif is_numer_only(len_entry.get())==False:
        messagebox.showerror("number","password length must be a number")
        return False
    return True

def even_ch_event():
    if ulvar.get() == "on" and nuvar.get() =="on" and syvar.get()=="off" and llvar.get()=="off":
        ev.configure(state = "normal")
    else:
        ev.configure(state = "disabled")
        evvar.set("off")
def charset_event():
    if ccvar.get()=="on":  
        ul.configure(state = "disabled")
        ll.configure(state = "disabled")
        nu.configure(state = "disabled")
        sy.configure(state = "disabled")
        ev.configure(state = "disabled")
        charset_label.configure(state = "disabled")
        pwd_count_frame.pack_forget()
        pwd_count_label.pack_forget()
        nbr_entry.pack_forget()
        pwd_length_label.pack_forget()
        len_entry.pack_forget()
        save_frame.pack_forget()
        output_label.pack_forget()
        save_entry.pack_forget()
        save_button.pack_forget()
        generate_btn.pack_forget()
        state_label.pack_forget()

        custom_frame.pack(pady = (5,10))
        pwd_count_frame.pack(pady = 5)
        pwd_count_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
        nbr_entry.pack(side = ctk.LEFT)
        pwd_length_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
        len_entry.pack(side = ctk.LEFT,padx = (0,5))
        save_frame.pack(pady = 5)
        output_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
        save_entry.pack(side = ctk.LEFT,padx = 10)
        save_button.pack(side = ctk.LEFT,padx = 10)
        generate_btn.pack(pady = 10)
        state_label.pack(pady = 8)
    else:
        custom_frame.pack_forget()
        charset_label.configure(state = "normal")
        ul.configure(state = "normal")
        ll.configure(state = "normal")
        nu.configure(state = "normal")
        sy.configure(state = "normal")
        if(ulvar.get() == "on" and nuvar.get() =="on"):
            ev.configure(state = "normal")


def choose_dir():
    path = ctk.filedialog.askdirectory(title="Output path")
    if path:
        save_entry.delete(0,len(save_entry.get()))
        save_entry.insert(0,path)
def generate_ev(length)->str:
# generate uppercase alphanumeric passwords with even chances for numbers and letters(for personal use , i need it)
    passwrd:str = ""
    for i in range (length):
        number = randint(0,1)
        if number:
            passwrd+=choice(Nums)
        else:
            passwrd+=choice(Uletrs)
    return passwrd

def generate_gen(charset:str,length:int)->str:
# generate passwords with chances based on the lenght of each type on the charset (ik it sound unundestandable)
    return "".join(choices(charset,k=length))

def create_file(ev_chances:bool,file_name:str,chset:str,psw_count:int,length:int)->None:
    path = save_entry.get()
    if ev_chances and chset == Uletrs+Nums:
        with open(path+r'/'+file_name+".txt","w")as f:
            for i in range(psw_count):
                f.write(generate_ev(length)+"\n")
    else:
        with open(path+r'/'+file_name+".txt","w")as f:
            for i in range(psw_count):
                f.write(generate_gen(chset,length)+"\n")
def generate()->None:
    if no_error():
        charset = ""
        a = None
        if ccvar.get() == "on":
            charset = custom_entry.get()
            a = Thread(target=create_file, args=(False, "Wordlist", charset, int(nbr_entry.get()), int(len_entry.get())))
        else:
            if ulvar.get() == "on":
                charset += Uletrs
            if llvar.get() == "on":
                charset += Lletrs
            if nuvar.get() == "on":
                charset += Nums
            if syvar.get() == "on":
                charset += Symbols
            if evvar.get() == "on" and ev.cget("state") == "normal":
                a = Thread(target=create_file, args=(True, "Wordlist", charset, int(nbr_entry.get()), int(len_entry.get())))
            else:
                a = Thread(target=create_file, args=(False, "Wordlist", charset, int(nbr_entry.get()), int(len_entry.get())))
                
        if charset :
            if a :
                try :
                    state_label.configure(text=f"Progress: Working on it...", text_color="yellow")
                    start_time = time()
                    a.start()
                    def check_thread() :
                        if a.is_alive() :
                            root.after(100, check_thread)
                        else:
                            end_time = time()
                            state_label.configure(text=f"Progress: Done in {end_time - start_time:.2f} seconds!", text_color="#00FF00")
                    root.after(100, check_thread)
                    messagebox.showinfo("Done","Generated successfully !")
                    with open("assets/last.txt","w") as f :
                        f.write(save_entry.get())
                except Exception as e:
                    messagebox.showerror(title="Error", message=f"{e}")
        else:
            messagebox.showerror(title="Charset Error", message="You Must Have a Charset ! ")
# global variables
Lletrs:str = "abcdefghijklmnopqrstuvwxyz"
Uletrs:str = Lletrs.upper()
Nums:str = "0123456789"
Symbols:str = ",;:!@-&_*."
length:int = 8
root = ctk.CTk()
root.title("Random Wordlist Generator")
root.resizable(False,True)
root.iconbitmap("./assets/logo.ico")
#title
title_lab = ctk.CTkLabel(root,text="Random Wordlist Generator",font=("",30))
title_lab.pack(pady = (10,20),padx = 20)
# radio variables
ulvar = ctk.StringVar(value="on")
nuvar = ctk.StringVar(value="off")
llvar = ctk.StringVar(value="off")
syvar = ctk.StringVar(value="off")
evvar = ctk.StringVar(value="off")
ccvar = ctk.StringVar(value="off")
# radio frame 
options_frame = ctk.CTkFrame(root)
options_frame.pack(pady = 5,padx = 20)
############
charset_label = ctk.CTkLabel(options_frame,text="Charset : ",font=("",15))
charset_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
ul = ctk.CTkCheckBox(options_frame,text="A-Z",variable=ulvar, onvalue="on", offvalue="off",command=even_ch_event)
ul.pack(side = ctk.LEFT,padx = 10,pady = 5)
ll = ctk.CTkCheckBox(options_frame,text="a-z",variable=llvar, onvalue="on", offvalue="off",command=even_ch_event)
ll.pack(side = ctk.LEFT,padx = 10,pady = 5)
nu = ctk.CTkCheckBox(options_frame,text="0-9",variable=nuvar, onvalue="on", offvalue="off",command=even_ch_event)
nu.pack(side = ctk.LEFT,padx = 10,pady = 5)
sy = ctk.CTkCheckBox(options_frame,text="Symbols",variable=syvar, onvalue="on", offvalue="off",command=even_ch_event)
sy.pack(side = ctk.LEFT,padx = 10,pady = 5)
ev = ctk.CTkCheckBox(options_frame,text="Even-Chances",state="disabled",variable=evvar, onvalue="on", offvalue="off")
#ev.pack(side = ctk.LEFT,padx = 10,pady = 5)
cc = ctk.CTkCheckBox(options_frame,text="Custom charset",variable=ccvar, onvalue="on", offvalue="off",command=charset_event)
cc.pack(side = ctk.LEFT,padx = 10,pady = 5)
#############
custom_frame = ctk.CTkFrame(root)
custom_label = ctk.CTkLabel(custom_frame,text="Custom charset : ")
custom_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
custom_entry = ctk.CTkEntry(custom_frame,placeholder_text="example : abcd1234@.?",width=150)
custom_entry.pack(side = ctk.LEFT,padx = 10,pady = 5)
#############
pwd_count_frame = ctk.CTkFrame(root)
pwd_count_frame.pack(pady = 5)
pwd_count_label = ctk.CTkLabel(pwd_count_frame,text="Number of passwords : ",font=("",15))
pwd_count_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
nbr_entry = ctk.CTkEntry(pwd_count_frame,placeholder_text=100000)
nbr_entry.insert(0,"100000")
nbr_entry.pack(side = ctk.LEFT)
#############
pwd_length_label = ctk.CTkLabel(pwd_count_frame,text="Length of each password : ",font=("",15))
pwd_length_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
len_entry = ctk.CTkEntry(pwd_count_frame,placeholder_text=8,width=40)
len_entry.insert(0,"8")
len_entry.pack(side = ctk.LEFT,padx = (0,5))
#############
save_frame = ctk.CTkFrame(root)
save_frame.pack(pady = 5)
output_label = ctk.CTkLabel(save_frame,text="Output : ",font=("",15))
output_label.pack(side = ctk.LEFT,padx = 10,pady = 5)
save_entry = ctk.CTkEntry(save_frame,placeholder_text="Choose an output folder",width=400)
if os.path.isfile("assets/last.txt"):
    with open("assets/last.txt","r") as f:
        save_entry.insert(0,f.read())
save_entry.pack(side = ctk.LEFT,padx = 10)
save_button = ctk.CTkButton(save_frame,text="Choose output folder",command=choose_dir)
save_button.pack(side = ctk.LEFT,padx = 10)
generate_btn = ctk.CTkButton(root,text="Generate",command=generate)
generate_btn.pack(pady = 10)
state_label = ctk.CTkLabel(root,text=f"Progress : {None}",font=("",15),text_color="#00FF00")
state_label.pack(pady = 8)

def main() ->None:
    root.mainloop()
if __name__=="__main__":
    main()