from utilities.dice import xd6, d20
from utilities.formatting import roll_tuple_to_string

class entity:
    
    def __init__(self, name, at, pa, ini_param: tuple, tp: tuple, lep, mu, ge, ko, mr, rs):
        self.name:str = name
        self.at: int = at
        self.pa: int = pa
        self.ini_param: tuple = ini_param # tuple containing number of d6s on index 0, and base ini on index 1
        self.ini: int = self.ini_roll()
        self.tp: tuple = tp # tuple containing number of d6s on index 0, and base tp on index 1
        self.lep: int = lep
        self.max_lep: int = lep
        self.mu: int = mu
        self.ge: int = ge
        self.ko: int = ko
        self.mr: int = mr
        self.rs: int = rs
        self.turn: bool = False

    @classmethod
    def dummy(cls):
        return cls("Dummy", 1, 1, (1, 1), (1, 1), 1, 1, 1, 1, 1, 1)

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
        Receive damage, under consideration of armor. 
        @param value: the TP to be added
        """
        if value is None:
            return
        
        damage = value - self.rs
        if damage < 0:
            damage = 0
        self.lep -= damage

    def regenerate(self):
        return

    def set_ini(self, value):
        """
        Set the initiative value manually, so that players can roll themselves
        """
        self.ini = value