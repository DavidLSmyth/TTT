from tkinter import *
import time
import random
import webbrowser

root = Tk()
root.title("Tic Tac Toe")
root.configure(bg="black")
global variable
variable=StringVar(root)
variable.set("hard")
optionmenu=OptionMenu(root,variable,"easy","hard")
optionmenu.configure(bg="khaki")
optionmenu.grid(row=3,column=2)

scoreboard_text=StringVar(root)
user_score=0
computer_score=0
scoreboard_text.set("User score= "+str(user_score)+"  Computer score= "+ str(computer_score))
leaderboard=Label(root, textvariable=scoreboard_text)
leaderboard.grid(row=3,column=0,columnspan=2)

def start():
    global user_turns
    user_turns=[]
    global computer_turns
    computer_turns=[]
    global available_tiles
    available_tiles=[1,2,3,4,5,6,7,8,9]
    global buttons1
    buttons1=["button1","button2","button3","button4","button5","button6","button7","button8","button9"]
    used_tiles=[]
    global clicked_buttons
    clicked_buttons=[]
    global user_turn_T_F
    button1=Button(root, height=5,width=10,bg="gold3")
    button1.grid(row=0, column=0)
    button1.config(highlightbackground="black")
    button2=Button(root, height=5, width=10,bg="gold3")
    button2.grid(row=0, column=1)
    button2.config(highlightbackground="black")
    button3=Button(root, height=5, width=10, bg="gold3")
    button3.grid(row=0, column=2)
    button3.config(highlightbackground="black")
    button4=Button(root, height=5, width=10,bg="gold3")
    button4.grid(row=1, column=0)
    button4.config(highlightbackground="black")
    button5=Button(root, height=5, width=10,bg="gold3")
    button5.grid(row=1, column=1)
    button5.config(highlightbackground="black")
    button6=Button(root, height=5, width=10,bg="gold3")
    button6.grid(row=1, column=2)
    button6.config(highlightbackground="black")
    button7=Button(root, height=5, width=10,bg="gold3")
    button7.grid(row=2, column=0)
    button7.config(highlightbackground="black")
    button8=Button(root,height=5, width=10,bg="gold3")
    button8.grid(row=2, column=1)
    button8.config(highlightbackground="black")
    button9=Button(root, height=5, width=10,bg="gold3")
    button9.grid(row=2, column=2)
    button9.config(highlightbackground="black")
    global buttons
    buttons=[button1,button2, button3,button4,button5,button6,button7,button8,button9]
   
    L_1=Label(root, text="X", font=("Times",14),bg="blue")
    L_2=Label(root, text="X",font=("Times", 14),bg="blue")
    L_3=Label(root, text="X",font=("Times", 14),bg="blue")
    L_4=Label(root, text="X",font=("Times", 14),bg="blue")
    L_5=Label(root, text="X",font=("Times", 14), bg="blue")
    L_6=Label(root, text="X",font=("Times", 14),bg="blue")
    L_7=Label(root, text="X",font=("Times", 14),bg="blue")
    L_8=Label(root, text="X",font=("Times", 14),bg="blue")
    L_9=Label(root, text="X", font=("Times", 14),bg="blue")
    global xlabels
    xlabels=[L_1,L_2,L_3,L_4,L_5,L_6,L_7,L_8,L_9]

    oL_1=Label(root, text="O", font=("Times",14),bg="yellow")
    oL_2=Label(root, text="O",font=("Times", 14),bg="yellow")
    oL_3=Label(root, text="O",font=("Times", 14),bg="yellow")
    oL_4=Label(root, text="O",font=("Times", 14),bg="yellow")
    oL_5=Label(root, text="O",font=("Times", 14),bg="yellow")
    oL_6=Label(root, text="O",font=("Times", 14),bg="yellow")
    oL_7=Label(root, text="O",font=("Times", 14),bg="yellow")
    oL_8=Label(root, text="O",font=("Times", 14),bg="yellow")
    oL_9=Label(root, text="O", font=("Times", 14),bg="yellow")
    global olabels
    olabels=[oL_1,oL_2,oL_3,oL_4,oL_5,oL_6,oL_7,oL_8,oL_9]
    global button_row
    global button_col
    button_row={"button1":0,"button2":0,"button3":0,"button4":1,"button5":1,"button6":1,"button7":2, "button8":2, "button9":2}
    button_col={"button1":0,"button2":1,"button3":2,"button4":0,"button5":1,"button6":2,"button7":0,"button8":1, "button9":2}
    i=1
    for button in buttons:
        button.my_name="button"+str(i)
        i+=1
    for button in buttons:
        button.bind("<Button-1>", user_turn)

def reset():
    for button in buttons:
        button.grid_forget()   
    start()
    global user_turn_T_F
    if user_turn_T_F=="TRUE":
        computer_turn(available_tiles)

def end_game(winner):
    time.sleep(1)
    if winner=="draw":
        print("draw game!")
        reset()
    if winner=="comp":
        webbrowser.open("https://www.youtube.com/watch?v=YgSPaXgAdzE")
        global computer_score
        global user_score
        computer_score+=1
        scoreboard_text.set("User score= "+str(user_score)+"  Computer score= "+ str(computer_score))
        print("computer wins!")
        reset()
    if winner=="user":
        webbrowser.open("https://www.youtube.com/watch?v=04854XqcfCY")
        user_score+=1
        scoreboard_text.set("User score= "+str(user_score)+"  Computer score= "+str(computer_score))
        print("player wins!")
        reset()

def user_turn(event):
    global user_turn_T_F
    user_turn_T_F="TRUE"
    user_turns.append(buttons1.index(event.widget.my_name)+1)
    hide_user_choice(event)
    available_tiles.remove(buttons1.index(event.widget.my_name)+1)
    if detectwinner(user_turns,"user")=="TRUE":
        pass
        
    else:
        if len(available_tiles)==0:
            time.sleep(1)
            end_game("draw")
        else:
            computer_turn(available_tiles)
        
def hide_user_choice(event):
    event.widget.grid_forget()
    clicked_buttons.append(event.widget.my_name)
    xlabels[buttons1.index(event.widget.my_name)].grid(row=button_row[event.widget.my_name], column=button_col[event.widget.my_name], padx=30,pady=30)
    root.update()

def defensive():
    win=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    root.update()
    for combo in win:
        if combo[0] in user_turns:
            if combo[1] in user_turns:
                if combo[2] not in computer_turns:
                    return combo[2]
            elif combo[2] in user_turns:
                    if combo[1] not in computer_turns:
                        return combo[1]
        elif combo[1] in user_turns:
            if combo[2] in user_turns:
                if combo[0] not in computer_turns:
                    return combo[0]
    else:
        return random.choice(available_tiles)
            
def computer_turn(available_tiles):
    global user_turn_T_F
    user_turn_T_F="FALSE"
    if variable.get()=="easy":
        selection=random.choice(available_tiles)
    #medium code goes here, should prevent user if they get 2 in a row
    #needs work, should pick random tile instead of middle tile
    elif variable.get()=="hard":
        if 5 in available_tiles:
            selection=5
        else:
             selection=defensive()
            
    #else:
    #if the user chooses the middle tile, pick a corner tile. If the user picks
    #another corner tile then continue with defensive strategy
    #if the computer goes first, execute the defensive strategy, if the user
    #doesn't have 2 in a row, then use an offensive strategy. this means either:
    #1) picking a 3 corner tiles if the user doesn't pick the middle
    #2)picking the middle tile and then corner tiles to trap the user
    #this ensures the computer never loses but perhaps doens't give the best
    #possible win rate
    #code goes here that never loses

    available_tiles.remove(selection)
    hide_computer_choice(selection)
    
def hide_computer_choice(selection):
    global computer_turns
    buttons[selection-1].grid_forget()
    computer_turns.append(selection)
    olabels[selection-1].grid(row=button_row[buttons[selection-1].my_name],column=button_col[buttons[selection-1].my_name],padx =30,pady=30)
    root.update()
    detectwinner(computer_turns,"comp")
    if len(available_tiles)==0:
        end_game("draw")

def detectwinner(L, user_or_comp):
    win=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    for combo in win:
        if combo[0] in L:
            if combo[1] in L:
                if combo[2] in L:
                    if user_or_comp=="user":
                        for i in combo:
                            xlabels[i-1].configure(bg="spring green")
                        root.update()
                        end_game("user")
                    if user_or_comp=="comp":
                        for i in combo:
                            olabels[i-1].configure(bg="spring green")
                        root.update()
                        end_game("comp")
                    return "TRUE"
                    
reset_Button=Button(root, command=reset, text="Click to reset!")
reset_Button.configure(bg="burlywood2")
reset_Button.grid(row=4, column=0,columnspan=3)
start()
root.mainloop()
