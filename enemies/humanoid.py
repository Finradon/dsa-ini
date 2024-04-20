from utilities.dice import xd6, d20

class humanoid:
    
    def __init__(self, name, at, pa, ini_param: tuple, tp: tuple, lep, mu, ge, ko, mr, rs):
        self.name:str = name
        self.at: int = at
        self.pa: int = pa
        self.ini_param: int = ini_param # tuple containing number of d6s on index 0, and base ini on index 1
        self.ini: int = self.ini_roll()
        self.tp: tuple = tp # tuple containing number of d6s on index 0, and base tp on index 1
        self.lep: int = lep
        self.mu: int = mu
        self.ge: int = ge
        self.mr: int = mr
        self.rs: int = rs
        self.ko: int = ko
        self.wound_count = 0

    def tp_roll(self) -> int:
        return xd6(self.tp[0]) + self.tp[1]

    def ini_roll(self):
        return xd6(self.ini_param[0]) + self.ini_param[1]
    
    def attack_roll(self) -> tuple:
        res = d20()

        if res <= self.at:
            suc = True
        else: 
            suc = False

        tp = self.tp_roll() # ToDo: maybe only return tp when succesful?
        return (res, suc, tp)
    
    def receive_damage(self, value: int):
        damage = value - self.rs
        self.lep -= damage

        if damage > self.ko:
            self.add_wound()

    def add_wound(self):
        self.wound_count += 1
        self.at -= 3
        self.pa -= 3
        self.ini -= 3
        self.ge -= 3
    
    def remove_wound(self):
        if self.wound_count > 0:
            self.wound_count -= 1
            self.at += 3
            self.pa += 3
            self.ini += 3
            self.ge += 3
