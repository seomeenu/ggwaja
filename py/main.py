asdf = input()

index = "꽈콰꿍콸콱불라자짜꽊"
special_chars = " !@#$%^&*()-+?_=,<>/.~:"

output = ""
for i in asdf:
    if i in special_chars:
        output += i
    else:
        asd = str(ord(i))
        res = ""
        for j in asd:
            res += index[int(j)]
        res += "블"
        output += res
        
print(output)