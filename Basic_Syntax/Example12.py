import pickle

# profile = open("profile.pickle", "wb")
# info = {"name":"Kim", "age":29, "hobby":["book", "sleep", "run"]}
# print(info)
# pickle.dump(info, profile)
# profile.close()


# profile = open("profile.pickle", "rb")
# info = pickle.load(profile)
# print(info)
# print(info["name"])
# print(info["hobby"])
# profile.close()


with open("profile.pickle", "rb") as profile:
    print(pickle.load(profile))


with open("text2.txt", "w", encoding="utf8") as text2:
    text2.write("open text2\n")
    text2.write("save text2\n")
    text2.write("close text2")




