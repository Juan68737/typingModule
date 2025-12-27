
from typing import Annotated
from dataclasses import dataclass

class Animal:
    def __init__(self, name, metadata):
        self._name = name
        self.__metadata__ = metadata

animal = Animal(name = "Capybara", metadata=("They are big and cute", "They are very popular in Colombia"))

print(animal._name) #Capybara
print(animal.__metadata__) #('They are big and cute', 'They are very popular in Colombia')

Country = Annotated[str, "Must be valid country"]

@dataclass
class LargeAnimals:
    name: str
    country_of_origin: Country

capybara = LargeAnimals(name="Capybara", country_of_origin=("Colombia", "Panama"))
print(capybara.name) #Capybara
print(capybara.country_of_origin) #('Colombia', 'Panama')

from pydantic import BaseModel, Field


class CharlieBrownCharacters(BaseModel):
    #name: str = Field(min_length=3)
    name: Annotated[str, Field(min_length=3)]
    age: Annotated[int, Field(gt=0, lt=100)]


snoopy = CharlieBrownCharacters(name="snoopy", age=2)
print(snoopy.name)
print(snoopy.age)
