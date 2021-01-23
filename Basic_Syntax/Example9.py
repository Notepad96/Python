def hello():
    print("안녕하세요")

hello()
print("=================================")

def hello2(name = "이씨", age = 30):
    print(f"안녕하세요 {name} 님 = {age}살")

hello2("김씨", 28)
hello2()
hello2(age=34)
print("=================================")

def hello3(name, age, *names):
    print(f"안녕하세요 {name} 님 = {age}살")
    for m in names:
        print(f"같이 오신 분 : {m}")


hello3("김씨", 37, "이씨", "정씨", "호씨")




