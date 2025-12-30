from typing import Literal

class PhoneBatterySetting:
    def __init__(self,mode: str):
        self._battery_mode = mode
    
    @property
    def battery_mode(self):
        return self._battery_mode
    
    @battery_mode.setter
    def battery_mode(self, mode: str):
        self._battery_mode = mode
        print(f'Phone battery has been changed to {mode}')

phone1 = PhoneBatterySetting("Default")
phone1.battery_mode = "Charlie Brown" #Phone battery has been changed to Charlie Brown (Not a battery mode)


BatterMode = Literal["Default", "Hybrid", "Saving"]

class PhoneBatterySettingV2:
    def __init__(self,mode: str):
        self._battery_mode = mode
    
    @property
    def battery_mode(self):
        return self._battery_mode
    
    @battery_mode.setter
    def battery_mode(self, mode: BatterMode):
        self._battery_mode = mode
        print(f'Phone battery has been changed to {mode}')

phone2 = PhoneBatterySettingV2("Default")
phone2.battery_mode = "Hybrid"

'''
phone2.battery_mode = "Charlie Brown"

error: Incompatible types in assignment (expression has type "Literal['Charlie Brown']", variable has type "Literal['Default', 'Hybrid', 'Saving']")  [assignment]
Found 1 error in 1 file (checked 1 source file)

'''

    
    