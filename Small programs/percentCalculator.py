def getValue(x, z):
    y = x * z
    return y
def percent():
    print('Input percent ')
    y = float(input())
    return y/100

getPercent = percent()
while True:
    print('Input number ')
    to_getValue = input()
    if to_getValue == 'exit':
        break
    elif to_getValue == '%':
        getPercent = percent()
    else:
        getValue_result = getValue(float(to_getValue), getPercent)
        print(getValue_result)
