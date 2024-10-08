import json
import math
from enemies.entity import entity

class melee_fighter(entity):
    def __init__(self, name, at, pa, ini_param: tuple, tp: tuple, lep, mu, ge, ko, mr, rs, eisern):
        super().__init__(name, at, pa, ini_param, tp, lep, mu, ge, ko, mr, rs)
        self.eisern: bool = eisern
        self.wound_count = 0

    # classmethods to directly create template enemies
    @classmethod
    def bandit(cls):
        return cls("Bandit", 14, 10, (1, 10), (1, 3), 30, 12, 12, 13, 4, 2, False)

    @classmethod
    def orc(cls):
        return cls("Ork", 15, 10, (1, 12), (1, 5), 35, 14, 13, 14, 3, 2, True)
    
    @classmethod
    def orc_chief(cls):
        return cls("Ork-Häuptling", 19, 14, (1, 18), (2, 4), 45, 16, 14, 16, 5, 3, True)

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
            json_data["RS"],
            json_data["Eisern"]
        )
    
    def receive_damage(self, value: int, tp: bool):
        """
        Receive damage, under consideration of armor. Also adds wounds, if applicable
        @param value: the TP to be added
        """
        if value is None:
            return

        sp_correction = 0
        if not tp:
            sp_correction = self.rs

        damage = value - self.rs + sp_correction
        if damage < 0:
            damage = 0
        self.lep -= damage

        if self.eisern:
            eisern = 2
        else:
            eisern = 0
            
        nr_wounds = math.floor((damage-1)/(self.ko + eisern))
        for _ in range(nr_wounds):
            self.add_wound()

        if self.lep <= 0:
            self.name = self.name + "☠️"

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
                "Eisern": self.eisern,
                "Wunden": self.wound_count
                }
        
        return data
    