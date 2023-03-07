import matplotlib.pyplot as plt
import math


def temp_converter(a, b) :
    deg = chr(176)
    b = str(b.lower())
    if b == 'c':
        print( str(a) + deg +  'C ' +  'is equal to ' + str((a * 9/5) + 32) + deg + "F" )
    elif b == 'f':
        print( str(a) + deg + 'C ' +  'is equal to ' + str((a-32)  * 5/9 ) + deg + 'C')

#temp_converter(0, "f")

def graph_ratio():
    x = 0
    celc_arr = []

    while x <= 100:
        tmp_f = x * 9/5 + 32
        temp_diff = tmp_f - x
        celc_arr.append(round(temp_diff, 2))
        x += 1
    print(celc_arr)

    fig, ax = plt.subplots(figsize=(40, 24))
    ax.plot(celc_arr, linestyle='--', marker='*', color='r', label='line with marker')
    plt.legend()
    ax.set_title('Ratio between conversion of Celsius to Fahrenheit')
    plt.xticks(range(0, 101, 1))
    plt.yticks(range(30, 113, 1))
    plt.grid()
    plt.xlabel("degrees in Celsius")
    plt.ylabel('Rate of Change from C to F')
    plt.savefig('Ratio_Change.png')

    plt.show()
    total = sum(celc_arr)
    print(total)


#print(dict)

graph_ratio()