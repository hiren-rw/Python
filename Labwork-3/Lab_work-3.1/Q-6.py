fruits = "apple,banana,grapes".split(",")
print("List :", fruits)

words = ["Python", "is", "awesome"]
print("Joined sentence :", " ".join(words))

multiline = "Line 1\nLine 2\nLine 3"
for line in multiline.splitlines():
    print(line)
