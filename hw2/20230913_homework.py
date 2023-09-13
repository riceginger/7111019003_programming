#%%
def circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    perimeter = 2 * pi * radius
    return area, perimeter

#%%
def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

#%%
def triangle(length1, length2, length3):
    semiperimeter = (length1 + length2 + length3) / 2
    area = (semiperimeter * (semiperimeter - length1) * (semiperimeter - length2) * (semiperimeter - length3)) ** (1/2)
    perimeter = length1 + length2 + length3
    return area, perimeter

#%%
def main(function):
    while function != '4':
        if function == '1':
            radius = int(input("請輸入半徑："))
            area, perimeter = circle(radius)
            print(f"面積：{area}, 周長：{perimeter}")
        elif function == '2':
            length = int(input("請輸入矩形的長："))
            width = int(input("請輸入矩形的寬："))
            area, perimeter = rectangle(length, width)
            print(f"面積：{area}, 周長：{perimeter}")
        elif function == '3':
            length1 = int(input("請輸入三角形第一邊的長："))
            length2 = int(input("請輸入三角形第二邊的長："))
            length3 = int(input("請輸入三角形第三邊的長："))
            
            if length1 + length2 > length3 and length2 + length3 > length1 and length1 + length3 > length2:
                area, perimeter = triangle(length1, length2, length3)
                print(f"面積：{area}, 周長：{perimeter}")
            else:
                print("三角形不成立")
        
        print()
        print("請選擇一個幾何形狀（或退出程式）：")
        print("1. 圓形（需要半徑）")
        print("2. 矩形（需要長和寬）")
        print("3. 三角形（需要三邊長度）")
        print("4. 退出程式")
        function = input("請輸入 1 / 2 / 3 / 4：")

#%%
if __name__ == '__main__':
    print("請選擇一個幾何形狀（或退出程式）：")
    print("1. 圓形（需要半徑）")
    print("2. 矩形（需要長和寬）")
    print("3. 三角形（需要三邊長度）")
    print("4. 退出程式")
    function = input("請輸入 1 / 2 / 3 / 4：")
    
    main(function)
    