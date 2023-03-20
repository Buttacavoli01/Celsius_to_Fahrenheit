import matplotlib.pyplot as plt
import math


def temp_converter(a, b) :
    deg = chr(176)
    b = str(b.lower())
    if b == 'c':
        print( str(a) + deg + 'C ' + 'is equal to ' + str((a * 9/5) + 32) + deg + "F")
    elif b == 'f':
        print(str(a) + deg + 'C ' + 'is equal to ' + str((a-32) * 5/9) + deg + 'C')

#temp_converter(0, "f")

def graph_ratio():
    x = 0
    y = 0
    celc_arr = []
    f_arr = []

    while x <= 100:
        tmp_f = x * 9/5 + 32
        celc_arr.append(round(tmp_f, 2))
        x += 1
    while y <= 212:
        tmp_c = y - 32 * 5/9
        f_arr.append(tmp_c)
        y += 1

    #print(celc_arr)

    fig, ax = plt.subplots(figsize=(30, 18))
    ax.plot(celc_arr, linestyle='--', marker='*', color='r', label='line with marker')

    plt.legend()
    ax.set_title('Ratio between conversion of Celsius to Fahrenheit')
    plt.xticks(range(0, 102, 1))
    plt.yticks(range(30, 214, 2))
    plt.grid()
    plt.xlabel("Degrees in Celsius")
    plt.ylabel('Degrees In Fahrenheit')
    plt.savefig('Ratio_Change.png')
    plt.show()

    total = sum(celc_arr)
    opposite = math.sin(30 * math.pi/180) * total
    adjacent = math.cos(30 * math.pi/180) * total



graph_ratio()
