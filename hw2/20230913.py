#%% 這個函數接收一個名字做為參數，然後返回一個問候語
def greet(name):
    return f"你好, {name}!"

#%% 這個函數接收一個名字做為參數，然後返回一個問候語
def calculate_area(radius):
    pi = 3.14159
    return pi * radius ** 2

#%%
def main():
    name = input("請輸入你的名字：")
    print(greet(name))
    
    for i in range(3):
        while True:
            radius_str = input(f"請輸入圓的半徑(您還有{3-i}次機會) ：")
            
            if radius_str.lower() == '退出':
                print("感謝使用，再見！")
                return
            
            radius = float(radius_str)
            
            if radius > 0:
                area = calculate_area(radius)
                print(f"圓的面積是：{area}")
                break
            else:
                print("半徑不能是負數或零！請再試一次。")

#%%
if __name__ == '__main__':
    main()