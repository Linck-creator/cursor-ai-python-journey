print("Hello, Cursor")

# Loop over the numbers 0 through 4 and print each one
for i in range(5):
    print(i)

# Open a text file and read its entire contents.
# `with` closes the file automatically when this block ends — no f.close() needed.
with open("message.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
print(f.closed)  # True: the file is already closed after the `with` block
