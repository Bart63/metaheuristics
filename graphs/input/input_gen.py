import random
import os.path

current_path = os.path.dirname(os.path.realpath(__file__))

vertices = 1000
path = os.path.join(current_path, "1.txt")
f = open(path, "w")
f.write(str(vertices)+'\n')
for i in range(0, vertices-1):
    f.write(f"{i} {i+1}"+'\n')
f.write("q\n")
f.write("0\n")
f.write(f"{vertices-1}")
f.close()

vertices = 2000
path = os.path.join(current_path, "2.txt")
f = open(path, "w")
f.write(str(vertices)+'\n')
for i in range(0, vertices-1):
    f.write(f"{i} {i+1}"+'\n')
f.write("q\n")
f.write("0\n")
f.write(f"{vertices-1}")
f.close()

vertices = 1000
first_limit = vertices//10
second_limit = vertices//2
path = os.path.join(current_path, "3.txt")
f = open(path, "w")
f.write(str(vertices)+'\n')
for i in range(0, first_limit):
    f.write(f"{0} {i+1}"+'\n')

for i in range(first_limit, second_limit):
    f.write(f"{random.randint(1, first_limit)} {i+1}"+'\n')

for i in range(second_limit, vertices-1):
    f.write(f"{random.randint(first_limit+1, second_limit)} {i+1}"+'\n')

f.write("q\n")
f.write("0\n")
f.write(f"{vertices-1}")
f.close()

vertices = 2000
first_limit = vertices//10
second_limit = vertices//2
path = os.path.join(current_path, "4.txt")
f = open(path, "w")
f.write(str(vertices)+'\n')
for i in range(0, first_limit):
    f.write(f"{0} {i+1}"+'\n')

for i in range(first_limit, second_limit):
    f.write(f"{random.randint(1, first_limit)} {i+1}"+'\n')

for i in range(second_limit, vertices-1):
    f.write(f"{random.randint(first_limit+1, second_limit)} {i+1}"+'\n')

f.write("q\n")
f.write("0\n")
f.write(f"{vertices-1}")
f.close()

vertices = 2000
first_limit = vertices//10
second_limit = vertices//3
third_limit = vertices//1.5
path = os.path.join(current_path, "5.txt")
f = open(path, "w")
f.write(str(vertices)+'\n')
for i in range(0, first_limit):
    f.write(f"{0} {i+1}"+'\n')

for i in range(first_limit, second_limit):
    f.write(f"{random.randint(1, first_limit)} {i+1}"+'\n')

for i in range(first_limit, second_limit):
    f.write(f"{random.randint(1, first_limit)} {i+1}"+'\n')

for i in range(second_limit, vertices-1):
    f.write(f"{random.randint(first_limit+1, second_limit)} {i+1}"+'\n')

f.write("q\n")
f.write("0\n")
f.write(f"{vertices-1}")
f.close()