filename = 'exam1_learning_python.txt'

### 1. 파일을 읽고 그대로 출력하는 것

with open(filename) as file_object:
    line = file_object.read()
    replaced_line = line.replace('python', 'C++')
    print(replaced_line)

### 2. with문 안에서 for문을 사용해서 하나씩 읽기
string_strip = ''
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        string_strip += line.replace('python', 'C++').strip()
print(string_strip)

### 3. 리스트에 저장하고 with문 밖에서 출력하는 방법

line_list = []
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        replaced_line = line.replace('python', 'C++')
        line_list.append(replaced_line)

print(line_list)
