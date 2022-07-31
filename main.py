import tkinter as tk

tf=True
movecount=0
result="no result"
# result options: "no result" \ "tie" \"x wins" \ "o wins"


# zmiana True na False i vice versa
def change_truthness(func_tf):
    global tf
    # true-> false
    if func_tf==True:
        func_tf=False 
        tf=func_tf

        # false -> true
    elif func_tf==False:
        func_tf=True
        tf=func_tf



# sprawdzanie wygranej
def check_winning(a1,a2,a3,b1,b2,b3,c1,c2,c3,result):

    # deklarowanie lini zwyciestw
    vert1=[a1,a2,a3]
    vert2=[b1,b2,b3]
    vert3=[c1,c2,c3]
    hor1 =[a1,b1,c1]
    hor2 =[a2,b2,c2]
    hor3 =[a3,b3,c3]
    diag1=[a1,b2,c3]
    diag2=[a3,b2,c1]
    all_lines=[vert1,vert2,vert3,hor1,hor2,hor3,diag1,diag2]
    # przechodzenie przez kazda z "lini zwyciestw"
    for xd in all_lines:
        # i patrzenie czy x wygrywa
        if xd[0]["text"]=='x' and xd[1]["text"]=='x'and xd[2]["text"]=='x':
            result="x wins"
            return(result)
        # oraz czy o wygrywa
        elif xd[0]["text"]=='o' and xd[1]["text"]=='o'and xd[2]["text"]=='o':
            result="o wins"
            return(result)                    
    #czy jest remis    
    if result == "no result" and movecount == 9:
        result="tie"
        return(result)
    # lub czy wszystko jest normalnie
    else:
        result = "no result"
        return(result)
         

def change_symbol(cell,mv,a1,a2,a3,b1,b2,b3,c1,c2,c3):
    # sprawdzaczy jest pusty text zeby nie mozna bylo zmieniac juz zaznaczonych
    if cell['text'] == "":
        global movecount
        global result

        # jak jest True to x
        if tf==True:
            cell['text']="x"
            change_truthness(tf)
            mv=mv+1
            movecount=mv

        # a jak jest False to o
        elif tf==False:
            cell['text']="o"
            change_truthness(tf)
            mv=mv+1
            movecount=mv

        

        # sprawdzanie wygranej
        # (zrob tak zeby wysakiwaly popupy i niszczyl sie window)
        print (check_winning(a1,a2,a3,b1,b2,b3,c1,c2,c3,result))













# creating window i zdefiniowanie wymirow
window =tk.Tk ()
window.rowconfigure(2, minsize=10, weight=1)
window.columnconfigure(2, minsize=250, weight=1)
window.geometry("245x245")
window.maxsize(240,245)
window.minsize(240,245)

# tworzenie buttonow
a1= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(a1,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
a1.grid(row=0,column=0,sticky="nesw")

b1= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(b1,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
b1.grid(row=0,column=1,sticky="nesw")

c1= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(c1,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
c1.grid(row=0,column=2,sticky="nsw")

a2= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(a2,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
a2.grid(row=1,column=0,sticky="nesw")

b2= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(b2,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
b2.grid(row=1,column=1,sticky="nesw")

c2= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(c2,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
c2.grid(row=1,column=2,sticky="w")

a3= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(a3,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
a3.grid(row=2,column=0,sticky="nw")

b3= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(b3,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
b3.grid(row=2,column=1,sticky="n")

c3= tk.Button(text="",height=5,width=10,command=lambda:change_symbol(c3,movecount,a1,a2,a3,b1,b2,b3,c1,c2,c3))
c3.grid(row=2,column=2,sticky="nw")



window.mainloop()





