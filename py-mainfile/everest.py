import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkfont
import pygame
import json
import random
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x300")#643x360
root.title("Everest")
root.iconbitmap('images/icon.ico')
root.resizable(0,0) 
root.itemlist = ["Oxygen mask", "Rope", "Climbers"]
global math_btn_clk
fd_t = 'ocr a extended'


import pygame
import sys
import threading

pygame.mixer.init()



imagemain = Image.open("images/mountain.jpg")
imagemain = imagemain.resize((500, 300), Image.Resampling.LANCZOS)

image = Image.open("images/mountain_wt.jpg")
image = image.resize((500, 300), Image.Resampling.LANCZOS)

image_sh = Image.open('images/mountain_sh.jpg')
image_sh= image_sh.resize((500,300), Image.Resampling.LANCZOS)

default_font = tkfont.nametofont("TkDefaultFont")
fd_t = 'ocr a extended'
default_font.config(family=fd_t, size=12, weight="bold")

def reset_grid():
    container = root
    for widget in container.grid_slaves():
        widget.destroy()
    
    for i in range(container.grid_size()[0]):
        container.columnconfigure(i, weight=0)
        container.grid_columnconfigure(i, weight=0)
    for j in range(container.grid_size()[1]):
        container.rowconfigure(j, weight=0)
        container.grid_rowconfigure(i, weight=0)

def back():
    pass

def update_label(label, text):
    label.config(text=text)


def screen2():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f"music/btnklk.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.fadeout(500)
    x = random.randint(1, 4)
    print(x)
    pygame.mixer.music.load(f"music/bgs/{x}.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    reset_grid()
    for widget in root.winfo_children():
        widget.destroy()
    
    root.background_image2 = ImageTk.PhotoImage(image_sh)
    background_label2 = tk.Label(root, image=root.background_image2)
    background_label2.place(relheight=1, relwidth=1)
    
    shop_list = tk.Listbox(root, bg="lightblue",fg="black")
    shop_list.grid(row=0, 
                   column=0, 
                   padx=10, 
                   pady=10, 
                   sticky="nsew", 
                   rowspan=2,
    )
    def buy_item(listbox):
        values = listbox.curselection()
        if values:
            index = values[0]
            vals = listbox.get(index)
            val = vals.lower()
            with open('data/items.json', 'r') as f:
                x=json.load(f)
            if val in x['items']:
                with open('data/items.json', 'r') as f:
                    x=json.load(f)
            else:
                x['items'][val] = 0
                with open("data/items.json", "w") as file:
                    json.dump(x, file)
            print('AMOUNT IN ACC : ',x['items'][val])
            with open('database/userdata.json', 'r') as a:
                coins = json.load(a)
            with open('data/dt.json', 'r') as b:
                cost = json.load(b)
            try:
                print('COST OF PRDC : ', cost['items'][val])
            except:
                print('item not found')
            if coins['coins']['trash'] >= cost['items'][val]:
                x['items'][val] += 1
                print('Buyed')
                coins['coins']['trash'] -= cost['items'][val]
                with open('data/items.json', 'w') as j:
                    json.dump(x, j)
                with open('database/userdata.json', 'w') as k:
                    json.dump(coins, k)
                with open('database/userdata.json', 'r') as w:
                    coinup = json.load(w)
                lbl.configure(text=f"CURRENCY : {coinup['coins']['trash']}")
            elif coins['coins']['trash'] < cost['items'][val]:
                print('Don\'t have enough')


    for i in root.itemlist:
        shop_list.insert(tk.END, i)

    def on_item_click(event):
        selected_indices = shop_list.curselection()
        if selected_indices:
            selected_item = shop_list.get(selected_indices[0])
            selected_item = selected_item.lower()
            
        with open("data/dt.json", "r") as f:
            x = json.load(f)
            
        y = x['items'][selected_item]

        lbl2.config(text=f"COST : {y}")

        with open('database/userdata.json', 'r') as k:
            coins = json.load(k)
        
        if coins['coins']['trash'] < x['items'][selected_item]:
            print('yay')
            btn2.config(state="disabled")
        else:
            btn2.config(state="normal")



    shop_list.bind("<<ListboxSelect>>", on_item_click)


    btn2 = tk.Button(root, text="Buy", command=lambda: buy_item(shop_list), bg="#14FFEC", fg="white")
    btn2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    btn1 = tk.Button(root, text="Inventory", bg="#00a886", fg="white", command=lambda: inv_screen(), height=1)
    btn1.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    btn3 = tk.Button(root, text="Work ⚒", bg="#e3d095", fg="black", command=lambda: work_screen())
    btn3.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    lbl2 = tk.Label(root, )
    lbl2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    btn4 = tk.Button(root, text="Back", command=lambda: screen1(), bg="#ffb3ba", fg="black")
    btn4.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

    with open('database/userdata.json', 'r') as f:
        loads=json.load(f)

    lbl = tk.Label(root, text=f"CURRENCY : {loads['coins']['trash']}", bg="#dcedc1")
    lbl.grid(row=3, column=0, sticky="nsew", pady=10, padx=10)

    root.grid_columnconfigure(0, weight=1) 
  


def screen1():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f"music/btnklk.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.fadeout(500)
    x = random.randint(1, 4)
    print(x)
    pygame.mixer.music.load(f"music/bgs/{x}.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    reset_grid()
    for widget in root.winfo_children():
        widget.destroy()
    #background_image = ImageTk.PhotoImage(image)
    #background_label = tk.Label(root, image=background_image)

    root.background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=root.background_image)

    background_label.place(relwidth=1, relheight=1)

        
    play_but = tk.Button(root, text="Play ✨", bg="#C1EBC0", fg="black", command=lambda: play_menu())
    play_but.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")
    play_but2 = tk.Button(root, text="Shop ♥", bg="#F6CA94", fg="black", command=lambda: screen2())
    play_but2.grid(row=10, column=1, padx=5, pady=10)
    play_but3 = tk.Button(root, text="Work ⚒", bg="#CDABEB", fg="black", command=lambda: work_screen())
    play_but3.grid(row=10, column=2, padx=5, pady=10)
    about = tk.Button(root, text="About", bg="#FAFABE", fg="black", state="disabled")
    about.grid(row=10, column=3, padx=5, pady=10)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


def inv_screen():
    import random
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f"music/btnklk.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.fadeout(500)
    x = random.randint(1, 4)
    print(x)
    pygame.mixer.music.load(f"music/bgs/{x}.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)

    reset_grid()
    for widget in root.winfo_children():
        widget.destroy()
    root.background_image4 = ImageTk.PhotoImage(imagemain)
    background_label = tk.Label(root, image=root.background_image4)

    background_label.place(relwidth=1, relheight=1)


    lst = tk.Listbox(root, bg="#fbf8cc", fg="black")
    lst.grid(row = 0, column = 0, columnspan=1, rowspan=1, sticky="nsew", padx=10, pady=10)



    with open('data/items.json', 'r') as g:
        items = json.load(g)

    for i in items['items']:
        if items['items'][i] > 0:
            print(i, items['items'][i])
            lst.insert(tk.END, i)
    
    import random
    from tkinter import messagebox as mb
    def sell_itm():
            with open('data/items.json', 'r') as w:
                items = json.load(w)
            indc = lst.curselection()
            if indc:
                sellitm = lst.get(indc[0])
                sellitm = sellitm.lower()
            try:
                if items['items'][sellitm] > 0:
                    ded = random.randint(1, 5)
                    res = True#mb.askyesno(title="Sell?", message=f"Are You Sure, There will be a deduction of {ded} coins")
                    if res == True:
                        with open('data/dt.json', 'r') as g:
                            cost = json.load(g)
                        final_rt = cost['items'][sellitm] - ded
                        with open('data/items.json', 'r') as itms:
                            items = json.load(itms)
                        items['items'][sellitm] -= 1
                        with open('data/items.json', 'w') as j:
                            json.dump(items, j)
                        with open('database/userdata.json', 'r') as h:
                            coins = json.load(h)
                        coins['coins']['trash'] += final_rt
                        with open('database/userdata.json', 'w') as dump:
                            json.dump(coins, dump)
                        with open("data/items.json", "r") as f:
                            x = json.load(f)
                        with open("data/dt.json", "r") as w:
                            w = json.load(w)
                            
                        yz = w['items'][sellitm]
                            
                        y = x['items'][sellitm]
                        lbl0.config(text=f"IN BAG : \n{y}\n\nCOST : \n{yz}")
                        print('Ok Sold')
                        if items['items'][sellitm] == 0:
                            btn3.config(state="disabled")
                            lbl0.config(text="click on \nitem \nfor info")
                            try:
                                selected_index = lst.curselection()
                                if selected_index:
                                    lst.delete(selected_index)
                                    if lst.size() == 0:
                                        btn3.config(state="disabled")
                                        lbl0.config(text="Your \nInventory \nis empty")
                            except Exception as e:
                                print(f"Error: {e}")
                            

                    else:
                        print('process cancelled')
                else:
                    mb.showinfo(title="Out Of Stock!!", message="You Have no more left")
            except Exception as e:
                print(f'Err: {e}')

    lbl0 = tk.Label(root, text="click on \nitem \nfor info", width=10, bg="#b9fbc0")
    lbl0.grid(row=0, column=1, sticky='nsew', pady=10, padx=10)
    btn3 = tk.Button(root, text="Sell", command=lambda: sell_itm(), bg="#fb6f92")
    btn3.grid(row=2, column=0, sticky = 'nsew', padx=10, pady=10)
    btn = tk.Button(root, text="Back", command=lambda: screen2(), bg="#ffadad")
    btn.grid(row=2, column=1, sticky = 'nsew', padx=10, pady=10)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    if lst.size() == 0: 
        btn3.config(state="disabled")
        lbl0.config(text="Your \nInventory \nis empty")
    else: 
        btn3.config(state="normal")

    def on_item_click(event):
        selected_indices = lst.curselection()
        if selected_indices:
            selected_item = lst.get(selected_indices[0])
            selected_item = selected_item.lower()
            
        with open("data/items.json", "r") as f:
            x = json.load(f)
        with open("data/dt.json", "r") as w:
            w = json.load(w)
            
        yz = w['items'][selected_item]
            
        y = x['items'][selected_item]

        if x['items'][selected_item] != 0:
            btn3.config(state="normal")

        try:
            selected_index = lst.curselection()
            if selected_index:
                selected_it = lst.get(selected_index[0])
                selected_it = selected_item.lower()
            with open('data/items.json', 'r') as jh:
                iteminfo = json.load(jh)
            if iteminfo['items'][selected_it] == 0: 
                if selected_index:
                    lst.delete(selected_index)
                else:
                    print("No item selected.")
        except Exception as e:
            print(f"Error: {e}")

        lbl0.config(text=f"IN BAG : \n{y}\n\nCOST : \n{yz}")


    lst.bind("<<ListboxSelect>>", on_item_click)

    root.grid_columnconfigure(0, weight=1)


def work_screen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f"music/btnklk.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.fadeout(500)
    x = random.randint(1, 4)
    print(x)
    pygame.mixer.music.load(f"music/bgs/{x}.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    reset_grid()
    for widget in root.winfo_children():
        widget.destroy()
    root.background_image4 = ImageTk.PhotoImage(imagemain)
    background_label = tk.Label(root, image=root.background_image4)

    background_label.place(relwidth=1, relheight=1)    

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)


    label = tk.Label(root, text="Select A Job to Do ⚒", bg="#FFF6E3", fg = "black", height=1, width=42)
    label.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
    btn = tk.Button(root, text="Solve math Sums", command=lambda: solve_mth(), bg="#F9E400")
    btn.grid(row = 1, column=0, columnspan=2, sticky = 'ew', padx=10, pady=10)
    btn2 = tk.Button(root, text="Coming Soon..", bg="#A1D6B2")
    btn2.grid(row = 2, column=0, columnspan=2, sticky = 'ew', padx=10, pady=10)
    btn2.config(state='disabled')
    btn3 = tk.Button(root, text="Coming Soon..", bg="#A1D6B2")
    btn3.grid(row = 3, column=0, columnspan=2, sticky = 'ew', padx=10, pady=10)
    btn3.config(state="disabled")
    btn4 = tk.Button(root, text="Coming Soon..", bg="#A1D6B2")
    btn4.grid(row = 4, column=0, columnspan=2, sticky = 'ew', padx=10, pady=10)
    btn4.config(state="disabled")
    btn5 = tk.Button(root, text="Coming Soon..", bg="#A1D6B2")
    btn5.grid(row = 5, column=0, columnspan=2, sticky = 'ew', padx=10, pady=10)
    btn5.config(state="disabled")
    btn5 = tk.Button(root, text="Home \n(Go Back)", width=8, bg="#FFB38E", command=lambda: screen1())
    btn5.grid(row = 1, column=2, columnspan=2,rowspan=2, sticky = 'nsew', padx=10, pady=10)
    btn6 = tk.Button(root, text="Shop", width=8, bg="#8967B3", fg="black", command=lambda: screen2())
    btn6.grid(row=3, column=2, columnspan=2, sticky = 'nsew', padx=10, pady=10)
    with open('database/userdata.json', 'r') as f:
        coins = json.load(f)
    lbl6 = tk.Label(root, text=f"Coins :-\n{coins['coins']['trash']}", width=8, bg="#A2D2DF", fg="black")
    lbl6.grid(row=4, column=2, columnspan=2, rowspan=2, sticky = 'nsew', padx=10, pady=10)

def solve_mth():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f"music/btnklk.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.fadeout(500)
    x = random.randint(1, 4)
    print(x)
    pygame.mixer.music.load(f"music/bgs/{x}.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    def start_timer():
        global remaining_time
        remaining_time = 61
        update_timer()

    def update_timer():
        global remaining_time
        if remaining_time > 0:
            remaining_time -= 1
            clr = random.choice(["95D2B3","F1F8E8","729762","F0A8D0","295F98","8967B3", "FADFA1"
                                 "9BB0C1","D37676","E1AFD1","B784B7","F9EFDB","8967B3", "FFF7D4"])
            tmlbl.config(text=f"Time Left: {remaining_time} sec", bg=f"#{clr}")
            root.after(1000, update_timer)
        else:
            tmlbl.config(text="Time's up!", bg="#C1CFA1")
            btn.config(state="disabled", bg="#FFB0B0")
            opt.config(state="disabled", bg="#FFB0B0")
            opt2.config(state="disabled", bg="#FFB0B0")
            opt3.config(state='disabled', bg="#FFB0B0")
            opt4.config(state="disabled", bg="#FFB0B0")
            btn3.config(state="normal", bg="#C1CFA1")
            Entry.config(text="Go Back and Try Again", bg="#FFB0B0")

    def add_question():
        global math_btn_clk
        math_btn_clk = 0
        btn.config(bg="#C1CFA1")
        Entry.config(bg="#C1CFA1")
        opt.config(bg="#C6E7FF")
        opt2.config(bg="#C6E7FF")
        opt3.config(bg="#C6E7FF")
        opt4.config(bg="#C6E7FF")
        global answer
        choice = random.randint(1,5)
        num1 = random.randint(1, 100)
        num2 = random.randint(10, 100)
        if choice == 1:
            qst = num1 + num2
            txt = f"{num1} + {num2}"
        elif choice==2:
            qst = num1 * num2
            txt = f"{num1} * {num2}"
        elif choice==3:
            qst = num1 - num2
            txt = f"{num1} - {num2}"
        elif choice == 4:
            qst = num2 - num1
            txt = f"{num2} - {num1}"
        elif choice == 5:
            qst = num1*num1
            txt = f'{num1}*{num1}'

        answer = qst
        Entry.config(text=txt)

        incorrect_options = []
        while len(incorrect_options) < 3:
            wrong_answer = random.randint(qst - 10, qst + 10)
            if wrong_answer != qst and wrong_answer not in incorrect_options:
                incorrect_options.append(wrong_answer)


        options = incorrect_options + [answer]
        random.shuffle(options)
        global ans_bt
        ans_bt = options.index(answer)
        print(ans_bt)

        opt.config(text=options[0])
        opt2.config(text=options[1])
        opt3.config(text=options[2])
        opt4.config(text=options[3])
    def addquestionagain():
        global remaining_time
        add_question()
        remaining_time -= 10
        with open('database/userdata.json', 'r') as k:
            ld = json.load(k)
        if ld['coins']['trash'] >= 5:
            ld['coins']['trash'] -= 5
        else:
            messagebox.showerror(title="Out Of Coins!", message="You Need 5 coins to perform this function!")
        with open('database/userdata.json', 'w') as k:
            json.dump(ld, k)

    def check_ans():
        print(math_btn_clk)
        print(answer)
        options_1 = opt.cget('text')
        options_2 = opt2.cget('text')
        options_3 = opt3.cget('text')
        options_4 = opt4.cget('text')
        opts = [ options_1,options_2, options_3, options_4]
        ans = 0
        if math_btn_clk == 1:
            print('text', options_1)
            if int(options_1) == answer:
                ans = 1
                opt.config(bg="#C1CFA1")
            else:
                ans = 0
                opt.config(bg="#FFB0B0")
        elif math_btn_clk == 2:
            if int(options_2) == answer:
                ans = 1
                opt2.config(bg="#C1CFA1")
            else:
                ans = 0
                opt2.config(bg="#FFB0B0")
        elif math_btn_clk == 3:
            if int(options_3) == answer:
                ans = 1
                opt3.config(bg="#C1CFA1")
            else:
                ans = 0
                opt3.config(bg="#FFB0B0")
        elif math_btn_clk == 4:
            if int(options_4) == answer:
                ans = 1
                opt4.config(bg="#C1CFA1")
            else:
                ans = 0
                opt4.config(bg="#FFB0B0")
        else:
            print('ran')
        from time import sleep as wait
        if ans == 1:
            global remaining_time
            remaining_time += 5
            print('correct')
            with open('database/userdata.json', 'r') as f:
                ld = json.load(f)
            ld['coins']['trash'] += 10
            with open('database/userdata.json', 'w') as g:
                json.dump(ld, g)
            Entry.config(bg="#C1CFA1")
            root.after(200, add_question())
        else:
            print('wrong')
            with open('database/userdata.json', 'r') as f:
                ld = json.load(f)
            ld['coins']['trash'] -= 5
            with open('database/userdata.json', 'w') as g:
                json.dump(ld, g)
            from tkinter import messagebox
            remaining_time -= 5
            print("remaining time",remaining_time)
            messagebox.showwarning(title="Wrong!", message="Wrong Choice.")
            Entry.config(bg="#FFB0B0")
            root.after(200, add_question())

    def mthbtn1():
        global math_btn_clk
        math_btn_clk = 1
        check_ans()

    def mthbtn2():
        global math_btn_clk
        math_btn_clk = 2
        check_ans()

    def mthbtn3():
        global math_btn_clk
        math_btn_clk = 3
        check_ans()

    def mthbtn4():
        global math_btn_clk
        math_btn_clk = 4
        check_ans()

    reset_grid()
    root.background_image4 = ImageTk.PhotoImage(imagemain)
    background_label = tk.Label(root, image=root.background_image4)

    background_label.place(relwidth=1, relheight=1)   
    Entry = tk.Label(root, height=2)
    Entry.grid(row = 0, column=0, padx=10, pady=10, columnspan=3, sticky='ew')
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    qst = 1+1
    opt = tk.Button(root, text=f"Option 1", command=lambda: mthbtn1())
    opt.grid(row=1, column=0, sticky='we', padx=10, pady=10)
    opt2 = tk.Button(root, text=f"Option 2", command=lambda: mthbtn2())
    opt2.grid(row=2, column=0, sticky='we', padx=10, pady=10)
    opt3 = tk.Button(root, text=f"Option 3", command=lambda: mthbtn3())
    opt3.grid(row=3, column=0, sticky='we', padx=10, pady=10)
    opt4 = tk.Button(root, text=f"Option 4", command=lambda: mthbtn4())
    opt4.grid(row=4, column=0, sticky='we', padx=10, pady=10)
    tmlbl = tk.Label(root, text="Timer appears here", bg="#8967B3")
    tmlbl.grid(row=5, column=0, padx=10, pady=10, sticky='ew', columnspan=3)
    btn = tk.Button(root, text="New Question\n(-10 Seconds, -5coins)", command=lambda: addquestionagain(), bg="#C1CFA1", font=(fd_t, 10))
    btn.grid(row = 1, column = 2, columnspan=2, rowspan=2, sticky='nsew', padx=10, pady=10)
    btn3=tk.Button(root, text='Back', command=lambda: work_screen(), bg="#FFCF9D")
    btn3.grid(row = 4, column=2, padx=10, pady=10, sticky='ew')
    lblx = tk.Label(root, text="Crrct: +10 Coins, +5s\nWrng: -10 Seconds, -5coins", font=(fd_t, 10), bg="#F0C1E1")
    lblx.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")
    add_question()
    start_timer()

def play_menu():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f"music/btnklk.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.fadeout(500)
    x = random.randint(1, 4)
    print(x)
    pygame.mixer.music.load(f"music/bgs/{x}.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    reset_grid()
    root.background_image5 = ImageTk.PhotoImage(imagemain)
    background_label = tk.Label(root, image=root.background_image5)

    background_label.place(relwidth=1, relheight=1)   

    label = tk.Label(root, text="Select A Level", bg="#003161", fg="gold")
    label.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew")
    
    for col in range(3):
        root.columnconfigure(col, weight=1)
    
    with open('data/lvl.json', 'r') as k:
        lvldt = json.load(k)

    btn = tk.Button(root, text="Base Camp", state="normal", bg="#C1CFA1", command=lambda:base_camp())
    btn.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    btn2 = tk.Button(root, text="Camp I", command=lambda: camp_1_game())
    btn2.grid(row=1, column=1, padx=10, pady=10,sticky="nsew")

    btn3 = tk.Button(root, text="Camp II", command=lambda: camp_2_game())
    btn3.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

    btn4 = tk.Button(root, text="Camp III")
    btn4.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    btn5 = tk.Button(root, text="Camp IV")
    btn5.grid(row=2, column=1, padx=10, pady=10,sticky="nsew")

    btn6 = tk.Button(root, text="The Summit")
    btn6.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    if lvldt['base'] == 'True':
        btn2.config(state="normal", bg="#C1CFA1")
    else:
        btn2.config(state='disabled', bg="#FFB0B0")
    if lvldt['4'] == 'True':
        btn6.config(state="normal", bg="#C1CFA1")
    else:
        btn6.config(state='disabled', bg="#FFB0B0")
    if lvldt['3'] == 'True':
        btn5.config(state="normal", bg="#C1CFA1")
    else:
        btn5.config(state='disabled', bg="#FFB0B0")
    if lvldt['2'] == 'True':
        btn4.config(state="normal", bg="#C1CFA1")
    else:
        btn4.config(state='disabled', bg="#FFB0B0")
    if lvldt['1'] == 'True':
        btn3.config(state="normal", bg="#C1CFA1")
    else:
        btn3.config(state='disabled', bg="#FFB0B0")

    with open('data/dyk.json', 'r') as f:
        dykt = json.load(f)
    
    rndtxt = dykt['rndm'][random.randint(0,10)]

    label = tk.Label(root, text=f"Did you know?\n{rndtxt}", font=(fd_t, 10), width=10, padx=5, pady=5, bg="#173B45", fg="#FAB12F")
    label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew", rowspan=3, columnspan=2)
    root.rowconfigure(3, weight = 1)

    btnbk = tk.Button(root, text="Store", command=lambda: screen2(), bg="#CB9DF0")
    btnbk.grid(row=3, column=2, sticky='new', padx=10, pady=10)
    btnbk = tk.Button(root, text="Work", command=lambda: work_screen(), bg="#F7DCB9")
    btnbk.grid(row=3, column=2, sticky='ew', padx=10, pady=10)
    btnbk = tk.Button(root, text="Back", command=lambda: screen1(), bg="#CB80AB")
    btnbk.grid(row=3, column=2, sticky='sew', padx=10, pady=10)


import pygame
import sys

def base_camp_game():
    import pygame
    import random
    import sys
    from tkinter import messagebox

    with open('data/items.json', 'r') as xyz:
        need = json.load(xyz)
    if need['items']['climbers'] >= 2:
        if need['items']['rope'] >= 1:
            need['items']['rope'] -= 1
            need['items']['climbers'] -=2
            with open('data/items.json', 'w') as f:
                json.dump(need, f)
            pygame.init()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('music/coldsnowfall.mp3')
            pygame.mixer.music.play(loops=1)
        else:
            from tkinter import messagebox as mb
            mb.showerror(title="Work!",message='You Need A rope to play this mission')
            return False
    else:
        messagebox.showerror(title="Work!",
                             message="You need two climbers to play this mission"
        )
        return False

    WIDTH, HEIGHT = 800, 488
    FPS = 60
    GRAVITY = 0.2
    PLAYER_SPEED = 2
    JUMP_STRENGTH = -5

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Climb Base")
    imagexxy = pygame.image.load('images/icon.ico')
    pygame.display.set_icon(imagexxy)

    WHITE = (255, 255, 255)

    player_image = pygame.image.load("main_car.png").convert_alpha()
    ground_img = pygame.image.load("basecamp/platform.png").convert_alpha()
    background = pygame.image.load('basecamp/bgfym.png').convert()

    pathlst = ['main2.png', 'main3.png', 'main4.png', 'main5.png']

    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = player_image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.vel_y = 0
            self.on_ground = False

        def get_position_top(self):
            return self.rect.top 
        def get_position_x(self):
            return self.rect.x 
        def get_position_y(self):
            return self.rect.y 

        def update(self, platforms):
            if self.rect.top < 80 and self.rect.x < 100:
                with open('data/lvl.json', 'r') as x:
                    ifcmpl = json.load(x)
                ifcmpl['base'] = "True"
                with open('data/lvl.json', 'w') as x:
                    json.dump(ifcmpl, x)

            current_time = pygame.time.get_ticks() 
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y

            self.on_ground = False

            for platform in platforms:
                if pygame.sprite.collide_rect(self, platform) and self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                self.rect.x += PLAYER_SPEED

            if keys[pygame.K_SPACE] and self.on_ground:
                if True:
                    if self.on_ground:
                        with open('data/items.json', 'r') as f:
                            items = json.load(f)
                        if items["items"]["oxygen mask"] > 0: 
                            self.vel_y = JUMP_STRENGTH
                        if items["items"]["oxygen mask"] > 0: 
                            if items["items"]["oxygen mask"]>3:
                                x = random.randint(1,3)
                            elif items["items"]["oxygen mask"] <= 3:
                                x = 1
                            items["items"]["oxygen mask"] -= x
                            with open('data/items.json', 'w') as x:
                                json.dump(items, x)
                            self.last_jump_time = current_time
                        elif items["items"]["oxygen mask"] == 0:
                            from tkinter import messagebox
                            messagebox.showerror(title="O2 Over", message="Your O2 is Over")
                        else:
                            print("Sorry!")

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.vel_y = 0 
                self.on_ground = True

    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height, imgpathgv):
            super().__init__()
            platform_image = pygame.image.load(f"basecamp/{imgpathgv}").convert_alpha()
            self.image = pygame.transform.scale(platform_image, (width, height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Ground(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height):
            super().__init__()
            self.image = pygame.transform.scale(ground_img, (width, height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    player = Player(WIDTH // 2, HEIGHT - 150)
    all_sprites.add(player)
    import pygame
    font = pygame.font.SysFont("ocr a extended", 20)
    with open('data/items.json', 'r') as f:
        ld = json.load(f)
    load = ld['items']['oxygen mask']

    scoretext = font.render(f"O2: {load}", True, (255, 255, 255))

    groundx = Ground(0, HEIGHT - 20, WIDTH + 20, 50)
    floating1 = Platform(50, 400, 30, 30, random.choice(pathlst))
    floating2 = Platform(135, 360, 30, 30, random.choice(pathlst))
    floating3 = Platform(210, 320, 30, 30, random.choice(pathlst))
    floating4 = Platform(290, 320, 30, 30, random.choice(pathlst))
    floating5 = Platform(385, 300, 30, 30, random.choice(pathlst))
    floating6 = Platform(500, 290, 30, 30, random.choice(pathlst))
    floating7 = Platform(600, 325, 30, 30, random.choice(pathlst))
    floating8 = Platform(685, 300, 30, 30, random.choice(pathlst))

    floating9 = Platform(760, 265, 30, 30, random.choice(pathlst))
    floating10 = Platform(675, 175, 30, 30, random.choice(pathlst))
    floating11 = Platform(600, 130, 30, 30, random.choice(pathlst))
    floating12 = Platform(495, 130, 30, 30, random.choice(pathlst))
    floating13 = Platform(425, 170, 30, 30, random.choice(pathlst))
    floating14 = Platform(365, 140, 30, 30, random.choice(pathlst))
    floating15 = Platform(290, 190, 30, 30, random.choice(pathlst))
    floating16 = Platform(190, 175, 30, 30, random.choice(pathlst))

    floatingend = Platform(95, 100, 30, 30, random.choice(pathlst))

    all_sprites.add(groundx, floating1, floating2, floating3, floating4, floating5, floating6, floating7, floating8,floating9, floating10, floating11, floating12, floating13, floating14, floating15, floating16, floatingend)
    platforms.add(groundx, floating1, floating2, floating3, floating4, floating5, floating6, floating7, floating8,floating9, floating10, floating11, floating12, floating13, floating14, floating15, floating16, floatingend)

    clock = pygame.time.Clock()
    running = False

    running=True
    import time
    start_time = time.time()
    while running:
        elapsed_time = time.time() - start_time
        screen.blit(background, (0, 0))
        fl2 = pygame.font.SysFont("ocr a extended", 20)
        countdown = fl2.render(f"Time Left : {str(60-int(elapsed_time))}", True, (0,0,0))
        screen.blit(countdown, (620, 10))
        root.iconify()
        clock.tick(FPS)
        with open('data/lvl.json', 'r') as z:
            ifover = json.load(z)

        if ifover['base'] == "False":
            if  elapsed_time >= 60:
                countdown = fl2.render(f"Time Left : 0", True, (0,0,0))
                screen.blit(countdown, (620, 10))
                messagebox.showwarning(title="Time Up!", message="Your Time Is Up, Better luck next time.")
                reset_grid()
                play_menu()
                pygame.quit()
                root.deiconify()
                break
        elif ifover['base'] == "True":
            if  elapsed_time >= 60:
                messagebox.showinfo(title="Over!", message="You have completed this mission")
                reset_grid()
                play_menu()
                pygame.quit()
                root.deiconify()
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            with open('data/items.json', 'r') as f:
                ld = json.load(f)
            load = ld['items']['oxygen mask']
            font = pygame.font.SysFont("ocr a extended", 20)
            scoretext = font.render(f"O2: {load}", True, (255, 255, 255))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f"Click At: ({mouse_x}, {mouse_y})")
        screen.blit(scoretext, (10, 10))
        player.update(platforms)
        all_sprites.draw(screen)
        pygame.display.flip()
        if player.get_position_top() < 80 and player.get_position_x() < 100:
            with open('data/lvl.json', 'r') as x:
                ifcmpl = json.load(x)
            ifcmpl['base'] = "True"
            with open('data/lvl.json', 'w') as x:
                json.dump(ifcmpl, x)
            messagebox.showinfo(title="Over!", message="You have completed this mission")
            reset_grid()
            play_menu()
            pygame.quit()
            root.deiconify()
            break
    root.deiconify()
    pygame.quit()
    sys.exit()




def camp_1_gamex():
    import pygame
    import random
    import sys
    from tkinter import messagebox
    with open('data/items.json', 'r') as xyz:
        need = json.load(xyz)
    if need['items']['climbers'] >= 3:
        if need['items']['rope'] >= 2:
            need['items']['rope'] -= 2
            need['items']['climbers'] -=3
            with open('data/items.json', 'w') as f:
                json.dump(need, f)
            pygame.init()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('music/coldsnowfall.mp3')
            pygame.mixer.music.play(loops=1)
        else:
            from tkinter import messagebox as mb
            mb.showerror(title="Work!",message='You Need Two ropes to play this mission')
            return False
    else:
        messagebox.showerror(title="Work!",
                             message="You need three climbers to play this mission"
        )
        return False

    WIDTH, HEIGHT = 800, 488
    FPS = 60
    GRAVITY = 0.3
    PLAYER_SPEED = 2
    JUMP_STRENGTH = -6

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Climb Camp 1")
    imagexxy = pygame.image.load('images/icon.ico')
    pygame.display.set_icon(imagexxy)

    WHITE = (255, 255, 255)

    player_image = pygame.image.load("main_car.png").convert_alpha()
    ground_img = pygame.image.load("basecamp/platform.png").convert_alpha()
    background = pygame.image.load('basecamp/bgfym.png').convert()

    pathlst = ['main2.png', 'main3.png', 'main4.png', 'main5.png']

    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = player_image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.vel_y = 0
            self.on_ground = False

        def get_position_top(self):
            return self.rect.top 
        def get_position_x(self):
            return self.rect.x 
        def get_position_y(self):
            return self.rect.y 

        def update(self, platforms):
            if self.rect.top < 80 and self.rect.x < 100:
                with open('data/lvl.json', 'r') as x:
                    ifcmpl = json.load(x)
                ifcmpl['1'] = "True"
                with open('data/lvl.json', 'w') as x:
                    json.dump(ifcmpl, x)

            current_time = pygame.time.get_ticks() 
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y

            self.on_ground = False

            for platform in platforms:
                if pygame.sprite.collide_rect(self, platform) and self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rect.x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                self.rect.x += PLAYER_SPEED

            if keys[pygame.K_SPACE] and self.on_ground:
                if True:
                    if self.on_ground:
                        with open('data/items.json', 'r') as f:
                            items = json.load(f)
                        if items["items"]["oxygen mask"] > 0: 
                            self.vel_y = JUMP_STRENGTH
                        if items["items"]["oxygen mask"] > 0: 
                            if items["items"]["oxygen mask"]>3:
                                x = random.randint(1,5)
                            elif items["items"]["oxygen mask"] <= 5:
                                x = 1
                            items["items"]["oxygen mask"] -= x
                            with open('data/items.json', 'w') as x:
                                json.dump(items, x)
                            self.last_jump_time = current_time
                        elif items["items"]["oxygen mask"] == 0:
                            from tkinter import messagebox
                            messagebox.showerror(title="O2 Over", message="Your O2 is Over")
                        else:
                            print("Sorry!")

            if self.rect.left < 0:  # Left boundary
                self.rect.left = 0
            if self.rect.right > WIDTH:  # Right boundary
                self.rect.right = WIDTH
            if self.rect.top < 0:  # Top boundary
                self.rect.top = 0
            if self.rect.bottom > HEIGHT:  # Bottom boundary (optional)
                self.rect.bottom = HEIGHT
                self.vel_y = 0  # Stop falling if at the bottom
                self.on_ground = True

    class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height, imgpathgv):
            super().__init__()
            platform_image = pygame.image.load(f"basecamp/{imgpathgv}").convert_alpha()
            self.image = pygame.transform.scale(platform_image, (width, height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Ground(pygame.sprite.Sprite):
        def __init__(self, x, y, width, height):
            super().__init__()
            self.image = pygame.transform.scale(ground_img, (width, height))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    player = Player(235,420)
    all_sprites.add(player)
    import pygame
    font = pygame.font.SysFont("ocr a extended", 20)
    with open('data/items.json', 'r') as f:
        ld = json.load(f)
    load = ld['items']['oxygen mask']

    scoretext = font.render(f"O2: {load}", True, (255, 255, 255))

    groundx = Ground(0, HEIGHT - 20, WIDTH + 20, 50)
    floating1 = Platform(50, 400, 30, 30, random.choice(pathlst))
    floating2 = Platform(135, 350, 30, 30, random.choice(pathlst))
    floating3 = Platform(50, 275, 30, 30, random.choice(pathlst))
    floating4 = Platform(135, 230, 30, 30, random.choice(pathlst))
    floating5 = Platform(255, 280, 30, 30, random.choice(pathlst))
    floating6 = Platform(380, 315, 30, 30, random.choice(pathlst))
    floating7 = Platform(505, 350, 30, 30, random.choice(pathlst))
    floating8 = Platform(610, 315, 30, 30, random.choice(pathlst))

    floating9 = Platform(720, 300, 30, 30, random.choice(pathlst))
    floating10 = Platform(775, 210, 30, 30, random.choice(pathlst))
    floating11 = Platform(700, 130, 30, 30, random.choice(pathlst))
    floating12 = Platform(605, 70, 30, 30, random.choice(pathlst))
    floating13 = Platform(470, 170, 30, 30, random.choice(pathlst))
    floating14 = Platform(428, 99, 30, 30, random.choice(pathlst))
    floating15 = Platform(309, 149, 30, 30, random.choice(pathlst))
    floating16 = Platform(210, 110, 30, 30, random.choice(pathlst))

    floatingend = Platform(95, 100, 30, 30, random.choice(pathlst))

    all_sprites.add(groundx, floating1, floating2, floating3, floating4, floating5, floating6, floating7, floating8,floating9, floating10, floating11, floating12, floating13, floating14, floating15, floating16, floatingend)
    platforms.add(groundx, floating1, floating2, floating3, floating4, floating5, floating6, floating7, floating8,floating9, floating10, floating11, floating12, floating13, floating14, floating15, floating16, floatingend)

    clock = pygame.time.Clock()
    running = False

    running=True
    import time
    start_time = time.time()
    while running:

        elapsed_time = time.time() - start_time
        screen.blit(background, (0, 0))
        fl2 = pygame.font.SysFont("ocr a extended", 20)
        countdown = fl2.render(f"Time Left : {str(60-int(elapsed_time))}", True, (0,0,0))
        screen.blit(countdown, (620, 10))
        root.iconify()
        clock.tick(FPS)
        with open('data/lvl.json', 'r') as z:
            ifover = json.load(z)
        if player.get_position_top() < 80 and player.get_position_x() < 100:
            with open('data/lvl.json', 'r') as x:
                ifcmpl = json.load(x)
            ifcmpl['1'] = "True"
            with open('data/lvl.json', 'w') as x:
                json.dump(ifcmpl, x)
            messagebox.showinfo(title="Over!", message="You have completed this mission")
            reset_grid()
            play_menu()
            pygame.quit()
            root.deiconify()
            break
        if ifover['base'] == "False":
            if  elapsed_time >= 60:
                countdown = fl2.render(f"Time Left : 0", True, (0,0,0))
                screen.blit(countdown, (620, 10))
                messagebox.showwarning(title="Time Up!", message="Your Time Is Up, Better luck next time.")
                reset_grid()
                play_menu()
                pygame.quit()
                root.deiconify()
                break
        elif ifover['base'] == "True":
            if  elapsed_time >= 60:
                messagebox.showinfo(title="Over!", message="You have completed this mission")
                reset_grid()
                play_menu()
                pygame.quit()
                root.deiconify()
                break


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            with open('data/items.json', 'r') as f:
                ld = json.load(f)
            load = ld['items']['oxygen mask']
            font = pygame.font.SysFont("ocr a extended", 20)
            scoretext = font.render(f"O2: {load}", True, (255, 255, 255))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(f"Click At: ({mouse_x}, {mouse_y})")
        screen.blit(scoretext, (10, 10))
        player.update(platforms)
        all_sprites.draw(screen)
        pygame.display.flip()
    root.deiconify()
    pygame.quit()
    sys.exit()




def base_camp():
    pygame_thread = threading.Thread(target=base_camp_game)
    pygame_thread.start()

def camp_1_game():
    pygame_thread = threading.Thread(target=camp_1_gamex)
    pygame_thread.start()

def camp_2_game():
    messagebox.showinfo(title='Not Ready :)', message="This Level Is Not Yet Ready to be played,\nComing Soon..")

screen1()


root.mainloop()
