#%%
from os import system, name
from math import log10
x = 1
o = -1
_ = 0
IMPASSE = -9999
PIECES_DICT = {
    1 : 'x',
    -1 : 'o',
    0 : '_',
    IMPASSE : 'none'
}

class GameBoard:
    SIZE = 14
    _data = []

    
    def __init__(self):
        self._data = [ [0 for i in range(self.SIZE)] for i in range(self.SIZE)]
    
    def get(self, x:int, y:int)->str:
        return self._data[self.SIZE-y][x-1]

    def set(self, x:int, y:int, piece:int)->bool:
        if x>self.SIZE or y>self.SIZE: return False
        if x<1 or y<1: return False
        elif self.get(x, y) != 0: return False
        self._data[self.SIZE-y][x-1] = piece
        return True

    def show(self)->None:
        add_padd = lambda n, m: ' '*(int(log10(m))-int(log10(n))) + str(n)
        print(' ' * int(log10(self.SIZE)) + 'Y')
        for y in range(self.SIZE):
            print(f"{add_padd(self.SIZE-y, self.SIZE)} ", end='')
            for x in range(self.SIZE):
                print(f"_{PIECES_DICT[self._data[y][x]]}_", end='')
                if x==self.SIZE-1: break
                print('|', end='')
            print()
        print("  ", end='')
        for x in range(self.SIZE):
            print(f' {x+1}' + ' '*(3-int(log10(self.SIZE))-int(log10(x+1)) ), end='')
        print(' X')
    
    def clear(self)->None:
        system('cls' if name == 'nt' else 'clear')

    def reset(self)->None:
        self.__init__(self)
        clear()

    def eval(self)->None:
        win = lambda x: -1 if x == -self.SIZE else 1 if x == self.SIZE else 0
        game_over = True
        for y in self._data:
            if _ in y: game_over = False
            state = win(sum(y)) 
            if(state!=0): return state
        for x in range(self.SIZE):
            _sum = 0
            for y in range(self.SIZE):
                _sum += self._data[y][x]
            state = win(_sum)
            if(state!=0): return state
        _sum = 0
        for xy in range(self.SIZE):
            _sum += self._data[xy][xy]
        state = win(_sum)
        if(state!=0): return state
        _sum = 0
        for xy in range(self.SIZE):
            _sum += self._data[self.SIZE-1-xy][xy]

        state = win(_sum)
        if(state!=0): return state
        if(game_over): return IMPASSE
        return 0


        
                
                        
#%%