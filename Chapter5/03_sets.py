#no repition allowed in sets
# e=set() #dont use s={} as it will create an empty dict

# s={1,2,4,5,5,5,}
# print(s)
# s.add(55)
# print(s)
# s.remove(2)
# print(s)

#union intersection

s={1,2,4,5}
s1={7,8,9,100,1}

print(s.union(s1))
print(s.intersection(s1))