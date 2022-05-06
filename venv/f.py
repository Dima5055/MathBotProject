import random
termins = {"медиана": "― отрезок, соединяющий вершину треугольника с серединой противоположной стороны.",
           "биссектриса": "— луч, исходящий из вершины угла и делящий этот угол на два равных угла."}
values = []
r = termins.values()
for j in r:
    values.append(j)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

f = random.choice(values)
print(f)
n = input()
while n != get_key(termins, f):
    n = input()