from dataclasses import dataclass
import random

@dataclass
class Ship:
    x_start: int
    y_start: int
    x_end: int
    y_end: int
    type: str
    pos: str


class Ships:
    def __init__(self):
        self.ships_objs = list()
        self.generate()
    
    def generate(self, amount_3d=0, amount_2d=2, amount_1d=3):
        for i in range(amount_3d):
            self.ships_objs.append(self.__generate_3d_ship())
        
        for i in range(amount_2d):
            self.ships_objs.append(self.__generate_2d_ship())
        
        for i in range(amount_1d):
            self.ships_objs.append(self.__gererate_1d_ship())

    def get_by_pos(self, x: int, y: int):
        for inx, ship in enumerate(self.ships_objs):
            if ship.x_start <= x <= ship.x_end and ship.y_start <= y <= ship.y_end:
                return (inx, ship)
            
    def __overlap(self, x_start: int, y_start: int, x_end: int, y_end: int) -> bool:
        for ship in self.ships_objs:
            if (ship.x_start - 1 <= x_start <= ship.x_end + 2) and (ship.y_start - 1 <= y_start <= ship.y_end + 2) and (ship.x_start - 1 <= x_end <= ship.x_end + 2) and (ship.y_start - 1 <= y_end <= ship.y_end + 2):
                return True
        return False
    
    def __generate_3d_ship(self):
        pass
    
    def __generate_2d_ship(self) -> Ship:
        while True:
            x_start = random.randint(0, self.size)
            y_start = random.randint(0, self.size)
            pos = random.choice('h', 'v')
            
            if 'h':
                if (x_start <= self.size - 2):
                    x_end = x_start + 1
                else:
                    x_start -= 1
                    x_end = x_start + 1
            else:
                if (y_start <= self.size - 2):
                    y_end = y_start + 1
                else:
                    y_start -= 1
                    y_end = y_start + 1
            
            if not(self.__overlap(x_start, y_start, x_end, y_end)):
                break
        return Ship(x_start, y_start, x_end, y_end, '2d', pos)
    
    def __gererate_1d_ship(self) -> Ship:
        while True:
            x_start = random.randint(0, self.size)
            y_start = random.randint(0, self.size)
            pos = 'h'
            if not(self.__overlap(x_start, y_start, x_start, y_start)):
                break
        return Ship(x_start, y_start, x_start, y_start, '1d', pos)
