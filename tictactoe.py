from Board import GameBoard, PIECES, turn
gb = GameBoard()
round_res = 0
while(round_res==0):
    gb.fore_message = f"It is {PIECES[turn]}'s turn"
    gb.refresh()


    while(True):
        x, y = gb.get_user_selection()
        if gb.set(x, y, turn, False): break

    round_res = gb.eval()
    if(round_res!=0): break
    turn = -turn

gb.clear()
gb.show()
print(f"winner: {PIECES[round_res]}")
