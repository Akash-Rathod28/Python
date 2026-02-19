#1
lst = [1, 2, 3, 4, 5]
print(lst)
print(len(lst))
print(lst[0])
print(lst[-1])

#2
t = ("apple", "banana", "cherry")
print(t[0])
print(t[1])
print(t[2])

#3
lst = []
for _ in range(3):
    lst.append(int(input()))
print(lst)

#4
nums = [10, 20, 30, 40, 50]
print(nums[1:4])
print(nums[-3:])

#5
lst = [1, 2, 3, 4]
lst.append(5)
lst.insert(2, 99)
lst.remove(3)
print(lst)

#6
lst = []
for _ in range(5):
    lst.append(int(input()))

print(max(lst))
print(min(lst))
print(sum(lst))

#7
data = [1, 2, 3, 4, 5]
copy_data = data
copy_data[0] = 100
print(data)
print(copy_data)

#8
t = (1, 2, 3)
lst = list(t)
lst[1] = 99
t = tuple(lst)
print(t)

#9
lst = [1, 2, 3, 4, 5, 6]
for n in lst:
    if n % 2 == 0:
        print(n)

#10
lst = [1, -2, 0, 5, -7, 0]
pos = neg = zero = 0

for n in lst:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)

#11
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#12
a = [1, 3, 5]
b = [2, 4, 6]
final = a + b
final.sort()
print(final)

#13
t = (1, 2, 3)
try:
    t[0] = 10
except TypeError as e:
    print(e)

#14
t = (10, 20, 30, 20, 40, 20)
print(t.count(20))
print(t.index(20))

#15
t = tuple(map(int, input().split()))
num = int(input())

if num in t:
    print("Exists")
else:
    print("Does not exist")

#16
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print(unique)

#17
lst = [10, 20, 30, 40, 50]
first = second = -1

for n in lst:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print(second)

#18
lst = ["akash", "chatgpt", "python"]
t = tuple(len(s) for s in lst)
print(t)

#19
nested = [1, 2, [3, 4, 5], 6]
print(nested[2][1])
nested[2][1] = 99
print(nested)

#20
t = (1, 2, 3, 4, 5)
lst = list(t)
lst = [x for x in lst if x % 2 != 0]
t = tuple(lst)
print(t)




