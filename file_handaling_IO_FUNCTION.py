file = open("demo1.txt",'w')
file.write("I am Learning JavaScript and \nIam after learning dsa in python by apna college")
file.close()

file = open("demo1.txt",'r')
a = file.read()
print(a)
file.close()

file = open("demo.txt",'r')
a = file.readline()
print(a)
file.close()

file = open("demo1.txt",'a')
file.write("Iam Joining Masters after that")
file.close()

file = open("demo1.txt",'r+') # overwrites from starting
file.write("Akash")
print(file.read())
file.close()

file = open("demo1.txt",'w+') # it clears all the previous data
print(file.read())
file.write("Abc is alphabets")
file.close()

file = open("demo1.txt",'a+') # it clears all the previous data
print(file.read())
file.write("Abc is alphabets")
file.close()


with open("histroy.txt",'r') as f:
    data = f.read()
    print(data)

with open("histroy.txt",'w') as f:
    f.write("I am learning Python")

################################ to delete something file
import os
os.remove("histroy.txt")

with open("practice.txt",'w') as a:
    a.write("Hi everyone one\nwe are learning file I/O\nusing java\nI like Programming in java.")

with open("practice.txt",'r+') as f:
    data = f.read()
new_data = data.replace("java","Python")
print(new_data)

with open("practice.txt",'w') as p:
    p.write(new_data)

with open("practice.txt",'r') as ak:
    data = ak.read()
    if(data.find("learoning") != -1): # another way to write if("learning" in data)
        print("It exict in the paragraph")
    else:
        print("It is not in the paragraph")

def check_for_line():
    word = "learoning"
    data = True
    line_no = 1
    with open("practice.txt",'r') as ak:
        while data:
            da = ak.readline()
            if(word in da):
                print(line_no)
                return
            line_no +=1
    return -1

print(check_for_line())

count = 0
with open("practice.txt",'r') as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if data[i] == ",":
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    nums  = data.split(",")
    for val in nums:
        if (int(val))% 2 ==0:
            count +=1
print(count)
