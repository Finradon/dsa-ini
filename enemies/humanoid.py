import json
from utilities.dice import xd6, d20
from utilities.formatting import roll_tuple_to_string
import math

class humanoid:
    
    def __init__(self, name, at, pa, ini_param: tuple, tp: tuple, lep, mu, ge, ko, mr, rs):
        self.name:str = name
        self.at: int = at
        self.pa: int = pa
        self.ini_param: tuple = ini_param # tuple containing number of d6s on index 0, and base ini on index 1
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

    # classmethods to directly create template enemies
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

    # json import classmethod
    @classmethod
    def from_json(cls, file: str):
        json_data = json.loads(file)
        return cls(
            json_data["Name"],
            json_data["AT"],
            json_data["PA"],
            (
                json_data["INI"]["W6"],
                json_data["INI"]["Basis"]
            ),
            (
                json_data["TP"]["W6"],
                json_data["TP"]["Basis"]
            ),
            json_data["LeP"],
            json_data["MU"],
            json_data["GE"],
            json_data["KO"],
            json_data["MR"],
            json_data["RS"]
        )


    def tp_roll(self) -> int:
        """
        Roll for damage
        @return: TP value
        """
        return xd6(self.tp[0]) + self.tp[1]

    def ini_roll(self):
        """
        Roll for initiative
        """
        return xd6(self.ini_param[0]) + self.ini_param[1]
    
    def attack_roll(self) -> str:
        """
        Roll on the attack value, create a tuple from the results and format them
        @return: string representation of the roll
        """
        res = d20()

        if res <= self.at:
            success = True
        else: 
            success = False

        res_tuple = (res, success, self.tp_roll())
        return roll_tuple_to_string(res_tuple)
    
    def parry_roll(self) -> str:
        """
        Roll on the parry value, create a tuple from the results and format them
        @return: string representation of the roll
        """
        res = d20()

        if res <= self.pa:
            success = True
        else: 
            success = False

        res_tuple = (res, success)
        return roll_tuple_to_string(res_tuple)
    
    def receive_damage(self, value: int):
        """
        Receive damage, under consideration of armor. Also adds wounds, if applicable
        @param value: the TP to be added
        """
        if value is None:
            pass

        damage = value - self.rs
        if damage < 0:
            damage = 0
        self.lep -= damage

        nr_wounds = math.floor((damage-1)/self.ko)
        for _ in range(nr_wounds):
            self.add_wound()

    def add_wound(self):
        """
        Add a wound, automatically reduce appropriate values
        """
        self.wound_count += 1
        self.at -= 3
        self.pa -= 3
        self.ini -= 3
        self.ge -= 3
    
    def remove_wound(self):
        """
        Remove a wound, if at least one exists
        """
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
