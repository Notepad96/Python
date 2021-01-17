myList = [50, 30, 10, 70, 10]
myList2 = ["가나다", "라마바", "사아자"]

print("=================리 스 트================")
print(myList)
print(myList2)
print(myList[0])


print("\n=================삽 입================")
myList.append("abc")    # 숫자 리스트의 문자열 넣기 가능
print(myList)
myList2.append("abc")   # 맨 뒤에 새 원소 넣기
print(myList2)


print("\n=================삭 제================")
print(myList.pop())
print(myList)


print("\n=================기 타================")
print(myList.count(10))     # 10의 개수

myList.sort()               # 오름차순 정렬
print(myList)

myList.sort(reverse=True)   # 내림차순 정렬
print(myList)

myList.extend(myList2)      # 리스트 뒤에 추가
print(myList)
