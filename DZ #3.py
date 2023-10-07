import os

folder_path = r'C:\Users\Вася\Desktop\DZ\papka'
files = os.listdir(folder_path)
# print(files)
file_list = []
for file in files:
    # print(file)
    with open(f'{folder_path}\{file}', 'r', encoding = 'utf8') as f:
        # print(f)
        file_lines = f.readlines()
        # print(file_lines)
        file_list.append([str(len(file_lines)), file, file_lines])
file_list.sort()
with open('DZ_3.txt','a',encoding="utf8") as l:
    for list in file_list:
        for elements in list:
            l.writelines(elements)
            l.write('\n')
        l.write('\n')
print(file_list)