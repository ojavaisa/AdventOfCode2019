# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:42:48 2019

@author: Olli

--- Day 1: The Tyranny of the Rocket Equation ---

--- Part Two ---

During the second Go / No Go poll, the Elf in charge of the Rocket Equation 
Double-Checker stops the launch sequence. Apparently, you forgot to include 
additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, 
round down, and subtract 2. However, that fuel also requires fuel, and that 
fuel requires fuel, and so on. Any mass that would require negative fuel should
instead be treated as if it requires zero fuel; the remaining mass, if any, is 
instead handled by wishing really hard, which has no mass and is outside the 
scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, 
treat the fuel amount you just calculated as the input mass and repeat the 
process, continuing until a fuel requirement is zero or negative. 

What is the sum of the fuel requirements for all of the modules on your 
spacecraft when also taking into account the mass of the added fuel? (Calculate
the fuel requirements for each module separately, then add them all up at the 
end.)

Module masses (input values) are saved in file input.txt

"""

import numpy as np
mass = np.loadtxt('input.txt')

total = 0
for x in mass:
    temp = x
    fuel = 0
    while temp > 0:
        total += fuel
        fuel = np.floor(temp/3)-2
        temp = fuel
        
print(int(total))
