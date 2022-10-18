from os import system, name
from keyboard import is_pressed
from time import sleep

IMPASSE = -9999
PIECES = {
    1  : 'x',   'x' :  1,
    -1 : 'o',   'o' : -1,
    0  : '_',   '_' :  0,
    IMPASSE : 'none'
}
turn = 1

class GameBoard:
    _data = []
    _selection_x, _selection_y = 0, 0
    INPUT_SLEEP = 0.1
    SIZE = 6

    fore_message = ''
    aft_message = ''

    

    def _cartesian_to_arr_indexes(self, x: int, y: int):
        return x-1, self.SIZE-y
    
    def __init__(self):
        """use a generator expression to initialize each square for board of size SIZE to the char '_' """
        self._data = [ [PIECES['_'] for i in range(self.SIZE)] for i in range(self.SIZE)]
    
    def get(self, x: int, y: int, is_cartesian: bool = True) -> str:
        """returns the selected square from the board interpreted as a cartesian coordinate plane, with the square closest to the origin being (1, 1)"""
        if is_cartesian: x, y = self._cartesian_to_arr_indexes(x, y)
        return self._data[y][x]

    def set(self, x: int, y: int, piece: int, is_cartesian: bool = True) -> bool:
        """sets a piece on the board according to cartesian interpretation of the board"""
        
        if is_cartesian: x, y = self._cartesian_to_arr_indexes(x, y)

        if ( 
            (x>self.SIZE or y>self.SIZE) or # a given coordinate is too big
            (x<0 or y<0) or # a given coordinate is too small 
            (self.get(x, y, False) != 0) # the space is occupied
            ): return False
        
        self._data[y][x] = piece
        return True

    def show(self) -> None:
        """Outputs the board"""
        olen = lambda n=self.SIZE: len(str(n)) # Python has no builtin to find the length of an integer's digits
        add_padding = lambda n, m=self.SIZE: ' '*( olen(m) - olen(n) ) + str(n) # adds padding corresponding to the olen(larger_n) - olen(n)
        square_is_selected = lambda x, y: y == self._selection_y and x == self._selection_x

        print(self.fore_message)#add_padding('Y'))
        for y in range(self.SIZE):
            print(f"{ add_padding(self.SIZE - y) } ", end='')

            for x in range(self.SIZE):
                print( f"{'[' if square_is_selected(x, y) else ' '}{ PIECES[ self._data[y][x] ]}", end=']' if square_is_selected(x, y) else ' ')

            print()
        print(self.aft_message)
    

    def clear(self) -> None:
        system('cls' if name == 'nt' else 'clear')

    def reset(self) -> None:
        self.__init__(self)
        self.clear()

    def refresh(self) -> None:
        self.clear()
        self.show()

    def eval(self) -> None:
        win = lambda x: -1 if x == -self.SIZE else 1 if x == self.SIZE else 0
        game_over = True
        for y in self._data:
            if 0 in y: game_over = False
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

    def get_user_selection(self) -> tuple[int, int]:

        while not is_pressed('enter'):
            if is_pressed('q'): quit()
            
            if ( is_pressed("a") or is_pressed("left_arrow") ) and self._selection_x - 1 >= 0:
                self._selection_x -= 1
                self.refresh()
                sleep(self.INPUT_SLEEP)

            elif ( is_pressed("d") or is_pressed("right_arrow") ) and self._selection_x + 1 < self.SIZE:
                self._selection_x += 1
                self.refresh()
                sleep(self.INPUT_SLEEP)

            if ( is_pressed("s") or is_pressed("down_arrow") ) and self._selection_y + 1 < self.SIZE:
                self._selection_y += 1
                self.refresh()
                sleep(self.INPUT_SLEEP)

            elif ( is_pressed("w") or is_pressed("up_arrow") ) and self._selection_y - 1 >= 0:
                self._selection_y -= 1
                self.refresh()
                sleep(self.INPUT_SLEEP)

        sleep(self.INPUT_SLEEP)
        return self._selection_x, self._selection_y
