with open("poem.txt") as f:
    content = f.read()
    print(content)

    if "Special" in content:
        print("The word 'Special' is present in the file")
    else:
        print("Something went wrong!")