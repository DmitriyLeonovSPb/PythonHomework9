
import math
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