import json
import math
from enemies.entity import entity
from utilities.dice import xd6, xd20

class demon(entity):
    def __init__(self, name, at, pa, ini_param: tuple, tp: tuple, lep, mu, ge, ko, mr, rs, regeneration=0):
        super().__init__(name, at, pa, ini_param, tp, lep, mu, ge, ko, mr, rs)
        self.regen = regeneration

    # classmethods to directly create template enemies
    @classmethod
    def quitslinga(cls):
        return cls("Quitslinga", 17, 12, (1, 14), (1, 5), 70+xd20(2), 12, 12, 13, 12, 4, 1)

    @classmethod
    def heshtoth(cls):
        return cls("Heshthot", 16, 10, (1, 12), (1, 4), 20, 14, 13, 14, 4, 2, 0)
    
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
            json_data["Regeneration"]
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

    def regenerate(self):
        """
        Regenerate LeP according to the regeneration feat (WdZ S. 234)
        """
        self.lep = self.lep + xd6(self.regen)
        if self.lep > self.max_lep:
            self.lep = self.max_lep