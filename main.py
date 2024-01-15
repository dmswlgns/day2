while True:
    menu = input("1)화씨 -> 섭씨,2)섭씨 -> 화씨: ")
    if menu == '1':
        fahrenheit = float(input("화씨온도:"))
        print(f'섭씨온도는:{((fahrenheit-32.0)*5/9):.2f}')
    elif menu=='2':
        celsius = float(input("섭씨온도:"))
        print(f'화씨온도는:{((celsius * 9/5) +32):.2f}')
    elif menu=='3':
        break












