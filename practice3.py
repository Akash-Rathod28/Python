#Q1

lst = [1, 2, 3, 4, 5]
print(len(lst))
print(lst[0])
print(lst[-1])

#Q2

lst = []
for i in range(5):
    num = int(input("Enter number: "))
    lst.append(num)
print(lst)

#Q3

nums = [10, 20, 30, 40, 50]
mid = len(nums) // 2
print(nums[mid])
print(sum(nums))

#Q4 (without max/min)

nums = [10, 2, 45, 7, 19]

max_val = nums[0]
min_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Max:", max_val)
print("Min:", min_val)

#Q5

nums = [1, 2, 3, 4, 5, 6]
even = []

for n in nums:
    if n % 2 == 0:
        even.append(n)

print(even)

#Q6 (reverse without slicing)

nums = [1, 2, 3, 4, 5]
rev = []

for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])

print(rev)

#Q7 (remove duplicates)

nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique)

#Q8

nums = [1, -2, 0, 4, -5, 0]

pos = neg = zero = 0

for n in nums:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)

#Q9 (second largest, no sort)

nums = [10, 20, 4, 45, 99]

first = second = -1

for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print("Second largest:", second)

#Q10

a = [1, 2, 3]
b = a
b.append(4)
print(a)

#Q11

person = {"name": "Akash", "age": 22, "city": "Pune"}
print(person.keys())
print(person.values())

#Q12

name = input("Enter name: ")
marks = int(input("Enter marks: "))

student = {"name": name, "marks": marks}
print(student)

#Q13

student = {"name": "Akash", "marks": 85}
student["grade"] = "A"

print(student)

#Q14

data = {"name": "Akash", "marks": 85}

if "age" in data:
    print("Key exists")
else:
    print("Key not found")
#Q15

student = {"name": "Akash", "marks": 85, "city": "Pune"}

for key, value in student.items():
    print(key, ":", value)

#Q16 (character frequency)

s = "hello"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)

#Q17

data = {"a": 10, "b": 25, "c": 15}

max_key = max(data, key=data.get)
print(max_key)

#Q18

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = d1 | d2
print(merged)

#Q19

lst = ["a", "b", "c"]
d = {}

for i in lst:
    d[i] = 1

print(d)

#Q20

dict1 = dict()
dict2 = {}
