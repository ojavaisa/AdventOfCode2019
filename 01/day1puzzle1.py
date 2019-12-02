# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:31:45 2019

@author: Olli

--- Day 1: The Tyranny of the Rocket Equation ---

--- Part One ---

Santa has become stranded at the edge of the Solar System while delivering 
presents to other planets! To accurately calculate his position in space, 
safely align his warp drive, and return to Earth in time to save Christmas, 
he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each 
day in the Advent calendar; the second puzzle is unlocked when you complete the
 first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to 
find the fuel required for a module, take its mass, divide by three, round 
down, and subtract 2.

The Fuel Counter-Upper needs to know the total fuel requirement. To find it, 
individually calculate the fuel needed for the mass of each module (your puzzle
input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your 
spacecraft?

Module masses (input values) are saved in file input.txt

"""
import numpy as np
mass = np.loadtxt('input.txt')

temp = [np.floor(x/3)-2 for x in mass]
print(int(sum(temp)))