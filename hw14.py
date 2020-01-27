#!/usr/bin/env python3.8
import pickle
import os

"""
    Создать сотрудника Mary, пользуясь классом
    Employee и перенести его в другую программу,
    используя модуль Pickle и файловую систему.
    Узнать про + и - модуля Pickle.
"""

class Employee:
    def __init__(self,name,phone,salary=10000):
        self.name = name
        self.phone = phone
        self.salary = salary
    def print_salary_info(self):
        print("Employee {} gets {} Rubles".format(self.name,self.salary))
    def add_salary(self,delta=5000):
        self.salary = self.salary+delta
    def add(self,other_empl):
        new_name = self.name + "&" + other_empl.name
        new_phone = str(round( (int(self.phone) + int(other_empl.phone))/2 ))
        new_salary = self.salary + other_empl.salary
        return Employee(new_name,new_phone,new_salary)
    def __del__(self):
        print(self.name+" is FIRED!!!")


def main():
    newpid = os.fork()
    if newpid == 0:                             # child
        a = Employee('First', 100)
        with open('temp/a.stored', 'wb') as f:
            pickle.dump(a, f)
        del(a)
    else:                                       # parent
        ret = os.wait()
        with open('temp/a.stored', 'rb') as f:
            b = pickle.load(f)
        if not isinstance(b, Employee):
            print('Error')
            return
        b.print_salary_info()
    return
    

if __name__ == "__main__":
    main()

"""
Плюсы:
* Компактное хранение 
Минусы:
* unsafe
"""