from Board import GameBoard, PIECES_DICT, x, o
gb = GameBoard()
turn = 1
round_res = 0
while(1):
    gb.clear()
    gb.show()
    inp = input(f"It is {PIECES_DICT[turn]}'s turn, where would you like to place your piece? x y: ").strip().split(' ')
    if inp[0] == 'q': quit()
    if len(inp) != 2: continue
    if(not (inp[0]+inp[1]).isdigit()): continue
    x, y = int(inp[0]), int(inp[1])
    if(not gb.set(x, y, turn)): continue
    round_res = gb.eval()
    if(round_res!=0): break
    turn = -turn
gb.clear()
gb.show()
print(f"winner: {PIECES_DICT[round_res]}")
