from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import Image, ImageDraw

player_1 = True
player_2 = False
turn = True

player_1_draws = []
player_2_draws = []

count_player_1 = 0
count_player_2 = 0

lable_player_1 = "Player 1 = " + str(count_player_1)
lable_player_2 = "Player 2 = " + str(count_player_2)

qd_count = 0

#create the window
janela = Tk()

#draw images
x = Image.new( 'RGB', (110,110), "black")
pixels = x.load() 

for i in range(x.size[0]):   
	if(i > 20) and (i < 90):
	    for j in range(x.size[1]):
	    	if(i == j) or (i + j == 110):
	    	    pixels[i,j] = (255, 255, 255) 

x.save("x.gif")


o = Image.new( 'RGB', (110,110), "black") 

draw_circle = ImageDraw.Draw(o)
draw_circle.ellipse((10, 10, 100, 100), outline="white")

o.save("o.gif")

empty = Image.new( 'RGB', (110,110), "black") 

empty.save('empty.gif')

x_image = PhotoImage(file="x.gif")
o_image = PhotoImage(file="o.gif")
empty_image = PhotoImage(file="empty.gif")



# Restart
def bt_initiate(botao):
	game_over("Restart")
	set_label_player_1["text"] = "Player 1 = 0"
	set_label_player_2["text"] = "Player 2 = 0"


#draw Xs and Os
def draw_player(qd):
	global turn, x_image, o_image, empty_image, player_1_draws, player_2_draws
	if(turn):
		if((qd["text"] not in player_1_draws) and (qd["text"] not in player_2_draws)):
			qd["image"] = x_image
			qd["width"] = 100
			qd["height"] = 100
			player_1_draws.append(qd["text"])
			turn = not turn
			track_draws()
	else:
		if((qd["text"] not in player_1_draws) and (qd["text"] not in player_2_draws)):
			qd["image"] = o_image
			qd["width"] = 100
			qd["height"] = 100
			player_2_draws.append(qd["text"])
			turn = not turn
			track_draws()


#keep track of x and o drawned
def track_draws():
	global player_1_draws, player_2_draws, qd_count, count_player_1, count_player_2

	qd_count = qd_count + 1	
	if(('qd1' in player_1_draws) and ('qd2' in player_1_draws) and ('qd3' in player_1_draws)):
		game_over("Player 1")
	elif(('qd4' in player_1_draws) and ('qd5' in player_1_draws) and ('qd6' in player_1_draws)):
		game_over("Player 1")
	elif(('qd7' in player_1_draws) and ('qd8' in player_1_draws) and ('qd9' in player_1_draws)):
		game_over("Player 1")
	
	
	elif(('qd1' in player_1_draws) and ('qd4' in player_1_draws) and ('qd7' in player_1_draws)):
		game_over("Player 1")
	elif(('qd2' in player_1_draws) and ('qd5' in player_1_draws) and ('qd8' in player_1_draws)):
		game_over("Player 1")
	elif(('qd3' in player_1_draws) and ('qd6' in player_1_draws) and ('qd9' in player_1_draws)):
		game_over("Player 1")


	elif(('qd1' in player_1_draws) and ('qd5' in player_1_draws) and ('qd9' in player_1_draws)):
		game_over("Player 1")
	elif(('qd7' in player_1_draws) and ('qd5' in player_1_draws) and ('qd3' in player_1_draws)):
		game_over("Player 1")


	elif(('qd1' in player_2_draws) and ('qd2' in player_2_draws) and ('qd3' in player_2_draws)):
		game_over("Player 2")
	elif(('qd4' in player_2_draws) and ('qd5' in player_2_draws) and ('qd6' in player_2_draws)):
		game_over("Player 2")
	elif(('qd7' in player_2_draws) and ('qd8' in player_2_draws) and ('qd9' in player_2_draws)):
		game_over("Player 2")


	elif(('qd1' in player_2_draws) and ('qd4' in player_2_draws) and ('qd7' in player_2_draws)):
		game_over("Player 2")
	elif(('qd2' in player_2_draws) and ('qd5' in player_2_draws) and ('qd8' in player_2_draws)):
		game_over("Player 2")
	elif(('qd3' in player_2_draws) and ('qd6' in player_2_draws) and ('qd9' in player_2_draws)):
		game_over("Player 2")


	elif(('qd1' in player_2_draws) and ('qd5' in player_2_draws) and ('qd9' in player_2_draws)):
		game_over("Player 2")
	elif(('qd7' in player_2_draws) and ('qd5' in player_2_draws) and ('qd3' in player_2_draws)):
		game_over("Player 2")


	elif(qd_count == 9):
		print(qd_count)
		game_over("Draw")
		

def game_over(player):
	global player_1_draws, player_2_draws, qd_count, qd1, qd2, qd3, qd4, qd5, qd6, qd7, qd8, qd9, count_player_2, count_player_1, turn
	if(player == "Draw"):
		mensagem = messagebox.showinfo("Draw!", "Draw")
	elif(player =="Restart"):
		mensagem = messagebox.showinfo("Restarting!", "Restarting!")
		count_player_1 = 0
		count_player_2 = 0
		turn = True
	else:
		mensagem = messagebox.showinfo("Win!", player + " won!")
		if(player == "Player 1"):
			turn = True
		else:
			turn = False

	player_2_draws = []
	player_1_draws = []
	qd1["image"] = empty_image
	qd2["image"] = empty_image 
	qd3["image"] = empty_image 
	qd4["image"] = empty_image 
	qd5["image"] = empty_image 
	qd6["image"] = empty_image 
	qd7["image"] = empty_image 
	qd8["image"] = empty_image 
	qd9["image"] = empty_image 
	qd_count = 0
	update_score(player)
	draw_quadrants()

# update score
def update_score(player):
	global lable_player_1, lable_player_2, count_player_1, count_player_2, set_label_player_1, set_label_player_2
	
	if(player == "Player 1"):
		count_player_1 = count_player_1 + 1
		lable_player_1 = "Player 1 = " + str(count_player_1)
		set_label_player_1["text"] = lable_player_1

	elif(player == "Player 2"):
		count_player_2 = count_player_2 + 1
		lable_player_2 = "Player 2 = " + str(count_player_2)
		set_label_player_2["text"] = lable_player_2


#create buttons
bt_restart = Button(width="5", height="3", text="RESTART")

#set the buttons
bt_restart.pack(side=RIGHT)
bt_restart["command"] = partial(bt_initiate, bt_restart)

#print score
set_label_player_1 = Label(text = lable_player_1, font=16)
set_label_player_1.pack(anchor=CENTER)

set_label_player_2 = Label(text = lable_player_2, font=16)
set_label_player_2.pack(anchor=CENTER)


#create canvas
bg = Canvas(janela, width=360, height=360, bg="black")
bg.pack(side=LEFT)

#draw quadrants
def draw_quadrants():
	global  qd1, qd2, qd3, qd4, qd5, qd6, qd7, qd8, qd9, bg
	qd1 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd1")
	qd1["command"] = partial(draw_player, qd1)
	qd1["image"] = empty_image
	qd1.place(x=14, y=14)
	qd1.config(highlightbackground="black")

	qd2 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd2")
	qd2["command"] = partial(draw_player, qd2)
	qd2["image"] = empty_image
	qd2.place(x=126, y=14)
	qd2.config(highlightbackground="black")

	qd3 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd3")
	qd3["command"] = partial(draw_player, qd3)
	qd3["image"] = empty_image
	qd3.place(x=236, y=14)
	qd3.config(highlightbackground="black")


	qd4 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd4")
	qd4["command"] = partial(draw_player, qd4)
	qd4["image"] = empty_image
	qd4.place(x=14, y=126)
	qd4.config(highlightbackground="black")

	qd5 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd5")
	qd5["command"] = partial(draw_player, qd5)
	qd5["image"] = empty_image
	qd5.place(x=126, y=126)
	qd5.config(highlightbackground="black")

	qd6 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd6")
	qd6["command"] = partial(draw_player, qd6)
	qd6["image"] = empty_image
	qd6.place(x=236, y=126)
	qd6.config(highlightbackground="black")


	qd7 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd7")
	qd7["command"] = partial(draw_player, qd7)
	qd7["image"] = empty_image
	qd7.place(x=14, y=238)
	qd7.config(highlightbackground="black")

	qd8 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd8")
	qd8["command"] = partial(draw_player, qd8)
	qd8["image"] = empty_image
	qd8.place(x=126, y=238)
	qd8.config(highlightbackground="black")

	qd9 = Button(bg, width=100, height=100, activebackground="black", borderwidth=0, text="qd9")
	qd9["command"] = partial(draw_player, qd9)
	qd9["image"] = empty_image
	qd9.place(x=236, y=238)
	qd9.config(highlightbackground="black")


#draw horizontal lines
bg.create_line(15, 125, 345, 125, fill="white")
bg.create_line(15, 235, 345, 235, fill="white")

#draw vertical lines
bg.create_line(125, 15, 125, 345, fill="white")
bg.create_line(235, 15, 235, 345, fill="white")


draw_quadrants()

#modify the window
janela.title("Tic Tac Toe")
janela.geometry("440x500")


#kick off the event loop
janela.mainloop()
