import random
import csv

def randomization():
    a = random.randint(-1000 , 1000)
    return(a)

def random_arguments():
    q = [0] * 3
    i = 0
    while i < 3:
       q[i] = randomization()
       i += 1
    return(q)

def bufer_writing(counter: int):
    i = 0
    buff = open("bufer.txt", "w")
    while i < counter:
        buff.write(str(random_arguments()) + '\n')
        i += 1
    buff.close()
    return

def bufer_writing_in_list(counter):
    i = 0
    myData = []
    while i < counter:
        myData.append(random_arguments())
        i += 1
    return myData

def list_to_csv(data):
    file = open('base.csv', 'a+', newline ='')
    with file:   
       write = csv.writer(file)
       write.writerow(data)
    return

