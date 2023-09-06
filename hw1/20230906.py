# 請求用戶輸入身高和體重
height = float(input("糗輸入你的身高(公尺):"))
weight = float(input("糗輸入你的體重(公斤):"))

# 使用公式來計算BMI
BMI = weight/(height**2)

# 顯示計算得到的BMI值
print(f"您的BMI是:{BMI:.2f}")
