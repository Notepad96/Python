print("person1", "person2","person3", sep=" vs. ")

import sys
print("person1", "person2","person3", file=sys.stdout)
print("person1", "person2","person3", file=sys.stderr)

text = "abcd"
print(text.ljust(10), text.rjust(10), sep="|")

text2 = "1234"
print( text2.zfill(10) )

print("============================")


# 오른쪽 정렬, 10자리, 빈공간
print("{0: >10}".format(1234) )
print("{0: >+10}".format(1234))
print("{0: >+10}".format(-1234))

# 왼쪽 정렬, 10자리, 빈공간 -
print("{0:-<+10}".format(1234))
print("{0:-<10}".format(1234))

# 3자리 마다 , 찍어 표시
num = 11111111111111
print("{0:,}".format(num))
print("{0:+,}".format(num))
print("{0:+,}".format(-num))

print("{0:Z>+25,}".format(num))

print("============================")

print("{0:f}".format(8/3))
print("{0:.3f}".format(8/3))
 

