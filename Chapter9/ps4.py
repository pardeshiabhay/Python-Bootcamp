word = "Donkey"

with open("ps4.txt", "r") as f:
    content = f.read()
    
contentNew = content.replace(word, "######")

with open("ps4.txt", "w") as f:
    f.write(contentNew)