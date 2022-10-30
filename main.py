from tkinter import *
from tkinter.messagebox import *
import random

btn = {}

WIN_COLOR = '#40FF00'
TIE_COLOR = '#FFFF00'

PLAYER1_MARK = '\u274C'  # "X"  \u274C
PLAYER2_MARK = '\u2B55'  # "O"  \u2B55

PLAYER_TURN = True

board = {1: '', 2: '', 3: '',
         4: '', 5: '', 6: '',
         7: '', 8: '', 9: ''}


def isAvailable(board, pos):
    if board.get(pos):
        return False
    return True


def isFull(board):
    for i in range(1, 10):
        if isAvailable(board, i):
            return False
    return True


def isWin_for_computer_moves(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True

    if board[7] == board[4] == board[1] == mark:
        return True
    if board[8] == board[5] == board[2] == mark:
        return True
    if board[9] == board[6] == board[3] == mark:
        return True

    if board[7] == board[5] == board[3] == mark:
        return True
    if board[9] == board[5] == board[1] == mark:
        return True
    else:
        return False


def isWin(board, mark):
    if board[1] == board[2] == board[3] == mark:
        btn[1]['bg'] = WIN_COLOR
        btn[2]['bg'] = WIN_COLOR
        btn[3]['bg'] = WIN_COLOR
        return True
    if board[4] == board[5] == board[6] == mark:
        btn[4]['bg'] = WIN_COLOR
        btn[5]['bg'] = WIN_COLOR
        btn[6]['bg'] = WIN_COLOR
        return True
    if board[7] == board[8] == board[9] == mark:
        btn[7]['bg'] = WIN_COLOR
        btn[8]['bg'] = WIN_COLOR
        btn[9]['bg'] = WIN_COLOR
        return True

    if board[7] == board[4] == board[1] == mark:
        btn[7]['bg'] = WIN_COLOR
        btn[4]['bg'] = WIN_COLOR
        btn[1]['bg'] = WIN_COLOR
        return True
    if board[8] == board[5] == board[2] == mark:
        btn[8]['bg'] = WIN_COLOR
        btn[5]['bg'] = WIN_COLOR
        btn[2]['bg'] = WIN_COLOR
        return True
    if board[9] == board[6] == board[3] == mark:
        btn[9]['bg'] = WIN_COLOR
        btn[6]['bg'] = WIN_COLOR
        btn[3]['bg'] = WIN_COLOR
        return True

    if board[7] == board[5] == board[3] == mark:
        btn[7]['bg'] = WIN_COLOR
        btn[5]['bg'] = WIN_COLOR
        btn[3]['bg'] = WIN_COLOR
        return True
    if board[9] == board[5] == board[1] == mark:
        btn[9]['bg'] = WIN_COLOR
        btn[5]['bg'] = WIN_COLOR
        btn[1]['bg'] = WIN_COLOR
        return True
    else:
        return False


def computer_choice():
    global copy_of_board

    for i in range(1, 10):
        copy_of_board = board.copy()
        if isAvailable(copy_of_board, i):
            copy_of_board[i] = PLAYER2_MARK
            if isWin_for_computer_moves(copy_of_board, PLAYER2_MARK):
                return i

    for i in range(1, 10):
        copy_of_board = board.copy()
        if isAvailable(copy_of_board, i):
            copy_of_board[i] = PLAYER1_MARK
            if isWin_for_computer_moves(copy_of_board, PLAYER1_MARK):
                return i

    if isAvailable(copy_of_board, 5):
        return 5

    for i in range(10):
        copy_of_board = board.copy()
        move = random.choice([7, 9, 1, 3])
        if isAvailable(copy_of_board, move):
            return move

    for i in range(10):
        copy_of_board = board.copy()
        move = random.choice([8, 6, 2, 4])
        if isAvailable(copy_of_board, move):
            return move


def tie():
    btn[1]['bg'] = TIE_COLOR
    btn[2]['bg'] = TIE_COLOR
    btn[3]['bg'] = TIE_COLOR
    btn[4]['bg'] = TIE_COLOR
    btn[5]['bg'] = TIE_COLOR
    btn[6]['bg'] = TIE_COLOR
    btn[7]['bg'] = TIE_COLOR
    btn[8]['bg'] = TIE_COLOR
    btn[9]['bg'] = TIE_COLOR


def computer():
    c = computer_choice()
    if isAvailable(board, c):
        board[c] = PLAYER2_MARK
        btn[c].config(text=PLAYER2_MARK, state=DISABLED)
        if isWin(board, PLAYER2_MARK):
            showinfo('Tic Tac Toe', f'Player 2:"{PLAYER2_MARK}" won the game.')
        else:
            if isFull(board):
                tie()
                showinfo('Tic Tac Toe', 'The game is tie!!')


def btn_clicked(pos):
    if isAvailable(board, pos):
        board[pos] = PLAYER1_MARK
        btn[pos].config(text=PLAYER1_MARK, state=DISABLED)
        if isWin(board, PLAYER1_MARK):
            showinfo('Tic Tac Toe', f'Player 1:"{PLAYER1_MARK}" Won the game.')
        else:
            if isFull(board):
                tie()
                showinfo('Tic Tac Toe', 'The game is tie!!')
            else:
                computer()


def btn_clicked_pvp(pos):
    global PLAYER_TURN
    if PLAYER_TURN:
        if isAvailable(board, pos):
            board[pos] = PLAYER1_MARK
            btn[pos].config(text=PLAYER1_MARK, state=DISABLED)
            if isWin(board, PLAYER1_MARK):
                showinfo('Tic Tac Toe', f'Player 1:"{PLAYER1_MARK}" Won the game.')
            else:
                if isFull(board):
                    tie()
                    showinfo('Tic Tac Toe', 'The game is tie!!')
                else:
                    PLAYER_TURN = False
                    playerO.config(fg='red')
                    playerX.config(fg='black')

    else:
        if not PLAYER_TURN:
            if isAvailable(board, pos):
                board[pos] = PLAYER2_MARK
                btn[pos].config(text=PLAYER2_MARK, state=DISABLED)
                if isWin(board, PLAYER2_MARK):
                    showinfo('Tic Tac Toe', f'Player 2:"{PLAYER2_MARK}" Won the game.')
                else:
                    if isFull(board):
                        tie()
                        showinfo('Tic Tac Toe', 'The game is tie!!')
                    else:
                        PLAYER_TURN = True
                        playerX.config(fg='red')
                        playerO.config(fg='black')


def new_game():
    for i in board:
        board[i] = ''
    try:
        playerX.config(fg='red')
        playerO.config(fg='black')
    except NameError:
        pass
    finally:
        btn[1].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[2].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[3].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[4].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[5].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[6].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[7].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[8].config(text='', state=NORMAL, bg='#F0F0F0')
        btn[9].config(text='', state=NORMAL, bg='#F0F0F0')


main = Tk()
main.title('TIC TOC TOE')
main.iconbitmap('images/tic-tac-toe.ico')
w, h = 470, 500
s_w = (main.winfo_screenwidth() // 2 - (w // 2))
s_h = (main.winfo_screenheight() // 2 - (h // 2))
main.geometry(f'{w}x{h}+{s_w}+{s_h}')


# main.resizable(False, False)


def screen1():
    global frame1
    frame1 = Frame(main)
    frame1.pack(expand=True, fill='both')

    label1 = Label(frame1, text='Tic Tac Toe', font=('Bahnschrift SemiCondensed', 60, 'bold'))
    label1.pack(side='top', pady=(10, 0))

    btn1 = Button(frame1, width=15, text='P vs C', font=('Bahnschrift SemiCondensed', 20, 'bold'), command=screen2)
    btn2 = Button(frame1, width=15, text='P vs P', font=('Bahnschrift SemiCondensed', 20, 'bold'), command=screen3)
    btn3 = Button(frame1, width=15, text='Exit', font=('Bahnschrift SemiCondensed', 20, 'bold'), command=main.quit)

    btn1.pack(anchor='center', pady=(90, 0))
    btn2.pack(anchor='center', pady=5)
    btn3.pack(anchor='center')


def screen2():
    frame1.pack_forget()

    def back():
        new_game()
        frame2.pack_forget()
        screen1()

    frame2 = Frame(main)
    frame2.pack(expand=True, fill='both')

    f_title = Frame(frame2)
    f_title.pack(side='top', fill='x')

    player1 = Label(f_title, text=f'Player1 {PLAYER1_MARK}', font=('Bahnschrift SemiCondensed', 20))
    player2 = Label(f_title, text=f'Player2 {PLAYER2_MARK}', font=('Bahnschrift SemiCondensed', 20))
    player1.pack(anchor='nw', side='left', pady=(5, 0))
    player2.pack(anchor='ne', side='right', pady=(5, 0))

    f_board = Frame(frame2, bg='gray')
    f_board.pack(anchor='center', padx=31, pady=(30, 10), expand=True, fill='both')

    for x in range(0, 3):
        f_board.rowconfigure(x, weight=1)
        f_board.columnconfigure(x, weight=1)

    btn[1] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(1))
    btn[2] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(2))
    btn[3] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(3))
    btn[4] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(4))
    btn[5] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(5))
    btn[6] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(6))
    btn[7] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(7))
    btn[8] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(8))
    btn[9] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked(9))

    btn[7].grid(row=0, column=0, sticky=NSEW)
    btn[8].grid(row=0, column=1, sticky=NSEW)
    btn[9].grid(row=0, column=2, sticky=NSEW)
    btn[4].grid(row=1, column=0, sticky=NSEW)
    btn[5].grid(row=1, column=1, sticky=NSEW)
    btn[6].grid(row=1, column=2, sticky=NSEW)
    btn[1].grid(row=2, column=0, sticky=NSEW)
    btn[2].grid(row=2, column=1, sticky=NSEW)
    btn[3].grid(row=2, column=2, sticky=NSEW)

    f_bottom = Frame(frame2)
    f_bottom.pack(side='bottom', fill='x')

    b_btn = Button(f_bottom, width=7, text='Back', font=('Bahnschrift SemiCondensed', 20), command=back)
    r_btn = Button(f_bottom, width=7, text='Restart', font=('Bahnschrift SemiCondensed', 20), command=new_game)
    b_btn.pack(side='left', pady=(0, 5), padx=(5, 0))
    r_btn.pack(side='right', pady=(0, 5), padx=(0, 5))


def screen3():
    global playerX, playerO
    frame1.pack_forget()

    def back():
        new_game()
        frame3.pack_forget()
        screen1()

    frame3 = Frame(main)
    frame3.pack(expand=True, fill='both')

    f_title = Frame(frame3)
    f_title.pack(side='top', fill='x')

    playerX = Label(f_title, text=f'Player1 {PLAYER1_MARK}', font=('Bahnschrift SemiCondensed', 20), fg='red')
    playerO = Label(f_title, text=f'Player2 {PLAYER2_MARK}', font=('Bahnschrift SemiCondensed', 20))
    playerX.pack(anchor='nw', side='left', pady=(5, 0))
    playerO.pack(anchor='ne', side='right', pady=(5, 0))

    f_board = Frame(frame3, bg='gray')
    f_board.pack(anchor='center', padx=31, pady=(30, 10), expand=True, fill='both')

    for x in range(0, 3):
        f_board.rowconfigure(x, weight=1)
        f_board.columnconfigure(x, weight=1)

    btn[1] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(1))
    btn[2] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(2))
    btn[3] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(3))
    btn[4] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(4))
    btn[5] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(5))
    btn[6] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(6))
    btn[7] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(7))
    btn[8] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(8))
    btn[9] = Button(f_board, borderwidth=1, font="Constantia 20", command=lambda: btn_clicked_pvp(9))

    btn[7].grid(row=0, column=0, sticky=NSEW)
    btn[8].grid(row=0, column=1, sticky=NSEW)
    btn[9].grid(row=0, column=2, sticky=NSEW)
    btn[4].grid(row=1, column=0, sticky=NSEW)
    btn[5].grid(row=1, column=1, sticky=NSEW)
    btn[6].grid(row=1, column=2, sticky=NSEW)
    btn[1].grid(row=2, column=0, sticky=NSEW)
    btn[2].grid(row=2, column=1, sticky=NSEW)
    btn[3].grid(row=2, column=2, sticky=NSEW)

    f_bottom = Frame(frame3)
    f_bottom.pack(side='bottom', fill='x')

    b_btn = Button(f_bottom, width=7, text='Back', font=('Bahnschrift SemiCondensed', 20), command=back)
    r_btn = Button(f_bottom, width=7, text='Restart', font=('Bahnschrift SemiCondensed', 20), command=new_game)
    b_btn.pack(side='left', pady=(0, 5), padx=(5, 0))
    r_btn.pack(side='right', pady=(0, 5), padx=(0, 5))


screen1()

main.mainloop()
