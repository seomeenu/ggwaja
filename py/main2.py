asdf = input()

index = "꽈콰꿍콸콱불라자짜꽊"
special_chars = " !@#$%^&*()-+?_=,<>/."

output = ""
cache = ""
for i in asdf:
    if i in special_chars:
        output += i
    else:
        if i != "블":
            cache += str(index.find(i))
        else:
            output += chr(int(cache))
            cache = ""
print(output)