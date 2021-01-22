def hello():
    print("안녕하세요")

def hello2(name = "이씨", age = 30):
    print(f"안녕하세요 {name} 님 = {age}살")

hello()

hello2("김씨", 28)
hello2()
hello2(age=34)