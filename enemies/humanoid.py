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
        self.turn: bool = False

    @classmethod
    def bandit(cls):
        return cls("Bandit", 14, 10, (1, 10), (1, 3), 30, 12, 12, 13, 4, 2)

    @classmethod
    def orc(cls):
        return cls("Ork", 15, 10, (1, 12), (1, 5), 35, 14, 13, 14, 3, 2)
    
    @classmethod
    def orc_chief(cls):
        return cls("Ork-Häuptling", 19, 14, (1, 18), (2, 4), 45, 16, 14, 16, 5, 3)
    
    @classmethod
    def dummy(cls):
        return cls("Dummy", 1, 1, (1, 1), (1, 1), 1, 1, 1, 1, 1, 1)

    @classmethod
    def from_json(cls, file: str):
        # ToDo: implement classmethod to create enemy from a json file
        raise NotImplementedError

    def tp_roll(self) -> int:
        return xd6(self.tp[0]) + self.tp[1]

    def ini_roll(self):
        return xd6(self.ini_param[0]) + self.ini_param[1]
    
    def attack_roll(self) -> str:
        res = d20()

        if res <= self.at:
            suc = ":white_check_mark:"
            tp = f"TP: {self.tp_roll()}"
        else: 
            suc = ":x:"
            tp = ""

        res_str = f'{suc}:{res} ' + tp
        return res_str
    
    def parry_roll(self) -> str:
        res = d20()

        if res <= self.pa:
            suc = ":white_check_mark:"
        else: 
            suc = ":x:"

        res_str = f'{suc}:{res}'
        return res_str
    
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

    def to_dict(self) -> dict:
        data = {"Name": self.name,
                "INI": self.ini,
                "LeP": self.lep,
                "AT": self.at,
                "PA": self.pa,
                "RS": self.rs,
                "MR": self.mr,
                "MU": self.mu,
                "GE": self.ge,
                "KO": self.ko,
                "Wunden": self.wound_count
                }
        
        return data
