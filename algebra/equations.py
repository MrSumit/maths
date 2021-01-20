import errors
from typing import Dict, Union

class Variable: 
    def __init__(self, name: str, degree: Union[int, float] = 1, sign = +1):
        if not type(degree) in [int, float]:
            raise TypeError(f'invalid type {str(type(real_number)).split()[1][:-1]} for parameter \'degree\' of object \'Variable\'.')
        if not sign in [1, -1]:
            raise errors.InvalidSign("parameter 'sign' of object 'Variable' takes only (+1/-1) as it's argument.")
        vrns = [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123) if chr(x) != 'e']
        if name in vrns:
            self.name = name
            self.degree = degree
            self.sign = sign
        else:
            raise ValueError(f'invalid value \'{name}\' for parameter \'name\' of object \'Variable\'.')
    
    def __str__(self):
        return (f'({self.name})' if self.degree == 1 else f'({self.name}^{self.degree})') if self.sign == 1 else (f'({str(self.sign)[0]+self.name})' if self.degree == 1 else f'({str(self.sign)[0]+self.name}^{self.degree})')
        return 

    def __repr__(self):
        return str(self)

class Constant: 
    def __init__(self, real_number: Union[int, float]):
        if not isinstance(real_number, (int, float)):
            raise TypeError(f'invalid type {str(type(real_number)).split()[1][:-1]} for parameter \'real_number\' of object \'Constant\'.')
        else: self.const = real_number

    def __str__(self):
        return f'({self.const})'

    def  __repr__(self):
        return str(self)


class Factor:
    def __init__(self, term):
        pass



class Term:
    def __init__(self, **tokens: Dict[Union[Variable, Constant], Union[Constant, Variable]]):
        self.coefficient = coefficient
        self.variable = variable
    #factor
    #coefficient

    def __str__(self):
        return ( f'({self.coefficient.const}{self.variable.name}^{self.variable.degree})' if self.variable.degree != 1 else f'({self.coefficient.const}{self.variable.name})' ) if self.variable.sign == '+' else f'({-1*self.coefficient.const}{self.variable.name}^{self.variable.degree})' if self.variable.degree != 1 else f'({-1*self.coefficient.const}{self.variable.name})'

    def __repr__(self):
        return str(self)

class Expression: pass

class Function(Exception): 
    def __init__(self, Expression):
        self.expn = Exception

    @classmethod
    def ln(cls, expression):pass
        

