import customtkinter as ctk
from random import choice,choices,randint
from time import time
# global variables
starting_time = time()
Lletrs:str = "abcdefghijklmnopqrstuvwxyz"
Uletrs:str = Lletrs.upper()
Nums:str = "0123456789"
Symbols:str = ",;:!@-&_*."
length:int = 8
root = ctk.CTk()
root.title("Random Wordlist Generator")
# Functions

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

def create_file(ev_chances:bool,file_name:str,chset:str,psw_count:int)->None:
    if ev_chances and chset == Uletrs+Nums:
        with open(file_name+".txt","w")as f:
            for i in range(psw_count):
                f.write(generate_ev(length)+"\n")
    else:
        with open(file_name,"w")as f:
            for i in range(psw_count):
                f.write(generate_gen(chset,length)+"\n")

def main() ->None:
    pass
'''    finish = time()
    print(finish-starting_time)'''
if __name__=="__main__":
    main()
    