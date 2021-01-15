print("\n=============1==============")
text = """a
b
cd
efg"""
print(text)


print("\n=============2==============")
text = "가나다라마바사"
print(text)
print("0 1 2 3 4 5 6")

print(text[:5])     # 0 ~ 4
print(text[5:])     # 5 ~ end
print(text[3:5])    # 3 ~ 4
print(text[-3:-1])  # 인덱스 뒤에서부터 접근, 맨 뒤 -1
print(text[-3:])    # 인덱스 뒤에서부터 접근, 맨 뒤 -1
print(text[::-1])   # 뒤집기


print("\n=============3==============")
text = "Test TexT python"

print(text)
print(len(text))
print(text.lower())
print(text.upper()) 
print(text.replace("python", "Python"))


print("\n=============4==============")
index = text.index("T")             # "T"의 Index
print(index)
index = text.index("T", index + 1)  # "T"의 Index, index+1 위치부터 탐색
print(index)

print("\n=============5==============")
print(text.find("abc"))     # 인덱스 반환, 없으면 -1
# print(text.index("abc"))  # find와 달리 없으면 에러 발생

print(text.count("T"))      # T의 개수
print(text.split())         # 공백 기준으로 나누기
