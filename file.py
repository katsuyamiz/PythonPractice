my_file = open('test.txt')
read_file = my_file.read()
print(read_file)

my_file.seek(0)
read_file_2 = my_file.readlines()
print(read_file_2)

my_file.close()

with open('test.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)



with open('test.txt', mode='r') as my_file:
    contents = my_file.read()

with open('test_2.txt', mode='r') as my_new_file_2:
    contents = my_new_file_2.read()
    print(contents)

with open('test_2.txt', mode='a') as my_new_file_2:
    my_new_file_2.write('hi5')
with open('test_2.txt', mode='r') as my_new_file_2:
    print(my_new_file_2.read())

with open('ddfdfdfdfd.txt', mode='w') as f:
    f.write('I created this file')
with open('ddfdfdfdfd.txt', 'r') as f:
    print(f.read())





