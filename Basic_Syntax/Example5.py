dic = {2:"가나다", 3:"abc", 4:"zfd", 1: "바사자"}

print("=================사 전================")
print(dic)
print(dic[4])               # index로 접근
print(dic.get(5, "없음"))   # key가 없을 경우 기본값 반환
print(2 in dic)         # 해당 key 존재 여부 확인
print(6 in dic)         # 해당 key 존재 여부 확인


print("\n=================삽입, 삭제================")
dic["abc"] = 102    # 삽입
print(dic)
del dic[1]          # 삭제
print(dic)


print("\n=================확 인================")
print(dic.keys())       # Key 리스트
print(dic.values())     # Value 리스트

temp = list(dic.items())
print(temp[0][1])
