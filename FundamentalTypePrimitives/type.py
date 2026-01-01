from typing import Type

class CharlieBrownCharacter:
    def __init__(self, name: str):
        self._name = name
    
def makeCharacter(cls: Type[CharlieBrownCharacter], name: str):
    return cls(name)

character1 = makeCharacter(CharlieBrownCharacter, "Snoopy")
print(character1._name) # Snoopy

def makeCharacterV2(cls: type[CharlieBrownCharacter], name: str):
    return cls(name)

character2 = makeCharacterV2(CharlieBrownCharacter, "Linus")
print(character2._name) # Linus