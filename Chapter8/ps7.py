def rem(l, word):
    n=[]
    for i in l:
        if not(i == word):
            n.append(i.strip(word))
    return n

l = ["Abhay", "Abhishek", "Abhimanyu", "Ab"]
print(rem(l,"Ab"))