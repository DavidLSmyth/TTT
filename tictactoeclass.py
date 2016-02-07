from tkinter import *
import time
import random
import webbrowser

class TicTacToe:

    #userscore and computer score class variables
    def __init__(self, parent): #start
        #init should initialise the the game 
        self.parent=parent
        self.parent.resizable(width=FALSE,height=FALSE)
        self.parent.title("TicTacToe")
        self.parent.configure(bg="black")
        self.difficulty=StringVar(self.parent)
        self.difficulty.set("hard")
        self.optionmenu=OptionMenu(root, self.difficulty, "easy","hard")
        self.optionmenu.configure(bg="khaki")
        self.optionmenu.grid(row=3, column=2)

        self.scoreboard_text=StringVar(root)
        self.user_score=0
        self.computer_score=0
        self.scoreboard_text.set("User score= "+str(self.user_score)+"  Computer score= "+str(self.computer_score))
        self.leaderboard=Label(self.parent, textvariable=self.scoreboard_text)
        self.leaderboard.grid(row=3, column=0, columnspan=2)
        self.reset_Button=Button(root, command=self.reset, text="Click to reset!")
        self.reset_Button.configure(bg="burlywood2")
        self.reset_Button.grid(row=4, column=0,columnspan=3)
        self.winnerLabelText=StringVar(self.parent)
        self.gameNo=1
        self.winnerLabelText.set('Game 1')
        self.winnerLabel=Label(self.parent, textvariable=self.winnerLabelText)
        self.winnerLabel.configure(bg='khaki')
        self.winnerLabel.grid(row=5, column=1)
        self.start()

    def start(self):
        self.user_turns=[]
        self.computer_turns=[]
        self.available_tiles=[1,2,3,4,5,6,7,8,9]
        self.buttons1=["button1","button2","button3","button4","button5","button6","button7","button8","button9"]
        self.used_tiles=[]
        self.clicked_buttons=[]
        button1=Button(self.parent, height=5,width=10,bg="gold3")
        button1.grid(row=0, column=0)
        button1.config(highlightbackground="black")
        button2=Button(self.parent, height=5, width=10,bg="gold3")
        button2.grid(row=0, column=1)
        button2.config(highlightbackground="black")
        button3=Button(self.parent, height=5, width=10, bg="gold3")
        button3.grid(row=0, column=2)
        button3.config(highlightbackground="black")
        button4=Button(self.parent, height=5, width=10,bg="gold3")
        button4.grid(row=1, column=0)
        button4.config(highlightbackground="black")
        button5=Button(self.parent, height=5, width=10,bg="gold3")
        button5.grid(row=1, column=1)
        button5.config(highlightbackground="black")
        button6=Button(self.parent, height=5, width=10,bg="gold3")
        button6.grid(row=1, column=2)
        button6.config(highlightbackground="black")
        button7=Button(self.parent, height=5, width=10,bg="gold3")
        button7.grid(row=2, column=0)
        button7.config(highlightbackground="black")
        button8=Button(self.parent,height=5, width=10,bg="gold3")
        button8.grid(row=2, column=1)
        button8.config(highlightbackground="black")
        button9=Button(self.parent, height=5, width=10,bg="gold3")
        button9.grid(row=2, column=2)
        button9.config(highlightbackground="black")
        self.buttons=[button1,button2, button3,button4,button5,button6,button7,button8,button9]
       
        L_1=Label(self.parent, text="X", font=("Times",14),bg="blue")
        L_2=Label(self.parent, text="X",font=("Times", 14),bg="blue")
        L_3=Label(self.parent, text="X",font=("Times", 14),bg="blue")
        L_4=Label(self.parent, text="X",font=("Times", 14),bg="blue")
        L_5=Label(self.parent, text="X",font=("Times", 14), bg="blue")
        L_6=Label(self.parent, text="X",font=("Times", 14),bg="blue")
        L_7=Label(self.parent, text="X",font=("Times", 14),bg="blue")
        L_8=Label(self.parent, text="X",font=("Times", 14),bg="blue")
        L_9=Label(self.parent, text="X", font=("Times", 14),bg="blue")

        self.xlabels=[L_1,L_2,L_3,L_4,L_5,L_6,L_7,L_8,L_9]

        oL_1=Label(self.parent, text="O", font=("Times",14),bg="yellow")
        oL_2=Label(self.parent, text="O",font=("Times", 14),bg="yellow")
        oL_3=Label(self.parent, text="O",font=("Times", 14),bg="yellow")
        oL_4=Label(self.parent, text="O",font=("Times", 14),bg="yellow")
        oL_5=Label(self.parent, text="O",font=("Times", 14),bg="yellow")
        oL_6=Label(self.parent, text="O",font=("Times", 14),bg="yellow")
        oL_7=Label(self.parent, text="O",font=("Times", 14),bg="yellow")
        oL_8=Label(self.parent, text="O",font=("Times", 14),bg="yellow")
        oL_9=Label(self.parent, text="O", font=("Times", 14),bg="yellow")

        self.olabels=[oL_1,oL_2,oL_3,oL_4,oL_5,oL_6,oL_7,oL_8,oL_9]
      
        self.button_row={"button1":0,"button2":0,"button3":0,"button4":1,"button5":1,"button6":1,"button7":2, "button8":2, "button9":2}
        self.button_col={"button1":0,"button2":1,"button3":2,"button4":0,"button5":1,"button6":2,"button7":0,"button8":1, "button9":2}
        i=1
        for button in self.buttons:
            button.my_name="button"+str(i)
            i+=1
        for button in self.buttons:
            button.bind("<Button-1>", self.user_turn)
        
    def reset(self):
        self.gameNo+=1
        self.winnerLabelText.set('Game '+str(self.gameNo))
        for button in self.buttons:
            button.grid_forget()   
        self.start()
        if self.user_turn_T_F=="TRUE":
            self.computer_turn(self.available_tiles)

    def end_game(self,winner):
        if winner=="draw":
            self.winnerLabelText.set('Draw game!')
            time.sleep(1)
            self.reset()
        if winner=="comp":
            webbrowser.open("https://www.youtube.com/watch?v=YgSPaXgAdzE")
            self.computer_score+=1
            self.scoreboard_text.set("User score= "+str(self.user_score)+"  Computer score= "+ str(self.computer_score))
            time.sleep(1)
            self.reset()
        if winner=="user":
            webbrowser.open("https://www.youtube.com/watch?v=04854XqcfCY")
            self.user_score+=1
            self.scoreboard_text.set("User score= "+str(self.user_score)+"  Computer score= "+str(self.computer_score))
            time.sleep(1)
            self.reset()

    def user_turn(self,event):
        #userturn handles when the user clicks on a tile when it's their choice
        self.user_turn_T_F="TRUE"
        self.user_turns.append(self.buttons1.index(event.widget.my_name)+1)
        self.hide_user_choice(event)
        self.available_tiles.remove(self.buttons1.index(event.widget.my_name)+1)
        if self.detectwinner(self.user_turns,"user")=="TRUE":
            pass
            
        else:
            if len(self.available_tiles)==0:
                time.sleep(1)
                self.end_game("draw")
            else:
                self.computer_turn(self.available_tiles)

    def hide_user_choice(self,event):
        #hideuserchoice displays the user's choice and hides the button the user selected
        event.widget.grid_forget()
        self.clicked_buttons.append(event.widget.my_name)
        self.xlabels[self.buttons1.index(event.widget.my_name)].grid(row=self.button_row[event.widget.my_name], column=self.button_col[event.widget.my_name], padx=30,pady=30)
        self.parent.update()

    def computer_turn(self,available_tiles):
        #computerturn allows the computer to choose a tile
        self.user_turn_T_F="FALSE"
        if self.difficulty.get()=="easy":
            print("easy")
            selection=random.choice(self.available_tiles)
        #medium code goes here, should prevent user if they get 2 in a row
        #needs work, should pick random tile instead of middle tile
        elif self.difficulty.get()=="hard":
            print("hard")
            if 5 in self.available_tiles:
                selection=5
            else:
                selection=self.defensive()

        self.available_tiles.remove(selection)
        self.hide_computer_selection(selection)

    def hide_computer_selection(self,selection):
        #hidecomputerselecion displays the computer's selection and hides the button it selected
        self.buttons[selection-1].grid_forget()
        self.computer_turns.append(selection)
        self.olabels[selection-1].grid(row=self.button_row[self.buttons[selection-1].my_name],column=self.button_col[self.buttons[selection-1].my_name],padx =30,pady=30)
        self.parent.update()
        self.detectwinner(self.computer_turns,"comp")
        if len(self.available_tiles)==0:
            self.end_game("draw")

    def defensive(self):
        #defensive gameplay algorithm
        win=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
        self.parent.update()
        for combo in win:
            if combo[0] in self.user_turns:
                if combo[1] in self.user_turns:
                    if combo[2] not in self.computer_turns:
                        return combo[2]
                elif combo[2] in self.user_turns:
                        if combo[1] not in self.computer_turns:
                            return combo[1]
            elif combo[1] in self.user_turns:
                if combo[2] in self.user_turns:
                    if combo[0] not in self.computer_turns:
                        return combo[0]
        else:
            return random.choice(self.available_tiles)

    def detectwinner(self, L, user_or_comp):
        #detectwinner detects if somebody has won the game
        win=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
        for combo in win:
            if combo[0] in L:
                if combo[1] in L:
                    if combo[2] in L:
                        if user_or_comp=="user":
                            self.winnerLabelText.set('Player wins!')
                            for i in combo:
                                self.xlabels[i-1].configure(bg="spring green")
                            self.parent.update()
                            
                            self.end_game("user")
                        if user_or_comp=="comp":
                            self.winnerLabelText.set('Computer wins!')
                            for i in combo:
                                self.olabels[i-1].configure(bg="spring green")
                            self.parent.update()
                            self.end_game("comp")
                        return "TRUE"

root=Tk()
ttc=TicTacToe(root)
root.mainloop()
