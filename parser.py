
import os



path = "F:\\source\\123py"
os.chdir(path)

arr1 = []
arr_result = []
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            arr1.append(line)

for file in os.listdir():
    if file.endswith(".xml"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)
 
for i, line in enumerate(arr1):
    if "</Name>" in line and "Tag value" in arr1[i + 1]:
        tag = arr1[i + 1]
        tag = tag.split("\"")[1]
        name = line.replace(">", "$").replace("<", "$").split("$")[2]
        str_a = f"{name} = {tag}"
        arr_result.append(str_a)

for a in arr_result:
    count = 0
    for b in arr_result:
        if a == b:
            count += 1
            if count > 1:
                arr_result.remove(b)
                print("hui")

print("="*30)

for elem in arr_result:
    print(elem)
