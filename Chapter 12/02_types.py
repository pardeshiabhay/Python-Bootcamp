from typing import List,Tuple,Dict,Union

#List of integers
numbers: List[int] = [1,2,3,4,5]

#Tuple of a string and am integer
person: Tuple[str, int] = ("Abhay", 22)

#Dictionary with string keys and integer values
scores: Dict[str, int] = {"Abhay": 22,"Bob":25}

#Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 1234 #also valid

print(numbers,person,scores,identifier)