"""
text_file = open("text.txt", "w", encoding="utf8")
print("text open", file=text_file)
print("text save", file=text_file)
print("text close", file=text_file)
text_file.close()
"""

"""
text_file = open("text.txt", "a", encoding="utf8")
print("==========", file=text_file)
text_file.write("text save2")
text_file.close()
"""

text_file = open("text.txt", "r", encoding="utf8")
# print(text_file.read())

# print(text_file.readline(), end="")
# print(text_file.readline(), end="")

for t in text_file.readlines():
    print(t, end="")

text_file.close()

