# Q.11: Demonstrate all file modes (r, w, a, r+, w+, a+)

# 1. 'w' mode: Write only (creates file or overwrites)
with open("demo.txt", "w") as f:
    f.write("Hello World\n")

# 2. 'r' mode: Read only
with open("demo.txt", "r") as f:
    print("r mode :", f.read())

# 3. 'a' mode: Append only
with open("demo.txt", "a") as f:
    f.write("Appended line\n")

# 4. 'r+' mode: Read and write (file must exist)
with open("demo.txt", "r+") as f:
    print("r+ mode read :", f.read())
    f.write("Added via r+\n")

# 5. 'w+' mode: Write and read (overwrites existing file)
with open("demo.txt", "w+") as f:
    f.write("Fresh content via w+\n")
    f.seek(0)  # Move cursor back to start to read
    print("w+ mode read :", f.read())

# 6. 'a+' mode: Append and read
with open("demo.txt", "a+") as f:
    f.write("Appended via a+\n")
    f.seek(0)  # Move cursor back to start to read
    print("a+ mode read :\n" + f.read())