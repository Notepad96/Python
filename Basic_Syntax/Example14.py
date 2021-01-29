try:
    print("나누기 하기")
    num1 = int(input("첫번 째? "))
    num2 = int(input("두번 째? "))
    print(f"{num1} + {num2} = {num1/num2}")
except ValueError:
    print("숫자를 입력하시오!!")
except ZeroDivisionError as err:
    print(err)
except:
    print("에러가 발생했습니다.")

print("=======================================")

class NumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("10이하의 수끼리 더하기 하기")
    num1 = int(input("첫번 째? "))
    num2 = int(input("두번 째? "))
    if num1 >= 10 or num2 >= 10:
        raise NumberError(f"num1 = {num1}, num2 = {num2}")
    print("실행 못해버리고 넘어감")
except ValueError:
    print("잘못된 입력값!!")
except NumberError as err:
    print("잘못된 숫자값!!")
    print(err)
finally:
    print("종료되었습니다.")



