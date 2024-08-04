import json
import math
from enemies.entity import entity
from utilities.dice import xd6, xd20

class hero(entity):
    def __init__(self, name, at, pa, ini_param: tuple, tp: tuple, lep, mu, ge, ko, mr, rs, eisern):
        super().__init__(name, at, pa, ini_param, tp, lep, mu, ge, ko, mr, rs)
        self.eisern: bool = eisern
        self.wound_count = 0

    
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
    
    def receive_damage(self, value: int):
        """
        Receive damage, under consideration of armor. Also adds wounds, if applicable
        @param value: the TP to be added
        """
        if value is None:
            return

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
