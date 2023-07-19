import csv
from roots_of_quation import roots_of_quation
import math
import json
def print_data(func):
    ii = 0
    bufff = []
    with open('base.csv') as f:
          reader = csv.reader(f)
          data = list(reader)
    while ii < 1000:
       aaa = data[ii]
       bufff.append(func(float(aaa[0]),float(aaa[1]),float(aaa[2])))
       ii +=1
    with open("base.json", "w") as write_file:
       json.dump(bufff, write_file)
@print_data
def roots_of_quation(a: float, b: float, c: float):
    d = float(b**2 - 4*a*c)
    answer = [None]*2
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2 * a)
        x2 = (-b - math.sqrt(d))/(2 * a)
        answer[0] = x1
        answer[1] = x2
        return(answer)
    if d == 0:
        x1 = 0
        x2 = 0
        answer[0] = x1
        answer[1] = x2
        return(answer)
    if d < 0:
        return(answer)
   
    roots_of_quation()