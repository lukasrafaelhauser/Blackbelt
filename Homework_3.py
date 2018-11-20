#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:51:28 2018

@author: l-r-h
"""

#%%

class Student:
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
        
        
class Master:
    
    master_students = []   
    def __init__(self, name):
        self.name = name               
    def add_list_students(self, list_students):
        self.master_students += list_students      
    def print_student(self):
        for student in self.master_students:      
            print(student.name + " is a "+ student.age + " years old student of the " + student.master + " masters program")      
         
master = Master("master")

list_students = [
    Student("Alejandro", "Meneses", "27", "MCSBT"),
    Student("Agata", "Kaczmarek", "31","MDBI"),
    Student("Anastasia", "Lasunina", "25", "MDBI"),
    Student("Anikken", "Barstad Gjeruldsen", "27", "MDBI"),
    Student("Arthur", "Maroquene-Froissart","23", "MCSBT"), 
    Student("Candela", "Noya", "24", "MDBI"),
    Student("Daniil", "Osipov", "21", "MDBI"),
    Student("David", "Barrero Gonzalez", "31", "MCSBT"),
    Student("Edem", "Francois", "28", "MCSBT"),
    Student("Felix ", "Fastrich", "23", "MDBI"),
    Student("Eduardo", "Paraja", "23", "MDBI"),
    Student("Florian", "Diegruber", "25", "MCSBT"),
    Student("Hannah", "Oldorf", "23", "MCBT"),
    Student("Isabella", "Rosenthal", "27", "MDBI"),
    Student("Javier", "Fernandez", "24", "MCSBT"),
    Student("Lukas", "Hauser", "28","MDBI"),
    Student("Leila", "Tazi", "27", "MCSBT"),
    Student("Laura", "Kageneck", "23", "MCSBT"),
    Student("Monica", "Alvarenga","28", "MDBI"),
    Student("Natalie", "Cedeno", "26", "MDBI"),
    Student("Octavio", "Ramírez", "28", "MDBI"),
    Student("Tancredi", "Bernard", "21", "MCSBT"),
    Student("Yasmine", "Lyagoubi", "23", "MDBI"),
    Student("Zineb", "Mezzour","22","MCSBT")
]


master.add_list_students(list_students)

master.print_student()

#%%