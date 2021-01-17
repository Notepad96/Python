tp = ("바자다", "카마나", "가나다")

# 튜플은 수정이 불가하며 따라서 삽입, 삭제가 불가하다.
print("\n=================튜 플================")
print(tp)
print(tp[1])
print(len(tp))              # 길이
print(tp.index("가나다"))   # Tuple에서 index


print("\n=================기 타================")
tp2 = tp * 3
print(tp2)


print("\n=================초기화================")
(v1, v2, v3) = ("q", "we", "rty")
v1 = "asdf"
print(v1, v2, v3)

