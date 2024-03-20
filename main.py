k1 = 1
k2 = 1.15
k3 = 1.35

m = None
h = None
l = None
k = None

# functions
def calculateQ():
    Q=k*m*l*lsh//100000
    print("Потраченные калории =", Q)

while m == None:
    try:
        m = int(input("Введите массу вашего тела (в килограммах): "))
    except ValueError:
        print("Введите число, а не строчку.")

while h == None:
    try:
        h = int(input("Введите рост вашего тела(в сантиметрах): "))
    except ValueError:
        print("Введите число, а не строчку.")

lsh = h//4+37
print("Интересный факт:", "Длина вашего шага составляет:", lsh)

while l == None:
    try:
        l = int(input("Введите кол-во пройденных шагов: "))
    except ValueError:
        print("Введите число, а не строчку.")



print("Для легкой прогулки: 1")
print("Для ходьбы с средней скорость: 2")
print("Для быстрой ходьбы: 3")
while k == None:
    try:
        k = int(input("Введите скорость шага: "))
        if k == 2:
            k = 1.15
        if k == 3:
            k = 1.35
    except ValueError:
        print("Введите число, а не строчку.")

calculateQ()
