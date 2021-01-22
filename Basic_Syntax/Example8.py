num = 5
# if
if num == 10 :
    print("숫자는 10")
elif num < 5 :
    print("숫자는 5 미만")
else :
    print("숫자는 5이상")

print("==========================")
# for
for i in range(4) :
    print(f"for 문 - {i}")

print("==========================")
nums = [i+1 for i in range(5)]
print(nums)


print("==========================")
while num > 0:
    print(num, end ="\t")
    num -= 1
