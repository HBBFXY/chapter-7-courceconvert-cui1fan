# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容import keyword

# 读取random_int.py文件
with open('random_int.py', 'r') as f:
    content = f.readlines()

# 处理每一行内容
processed_lines = []
for line in content:
    new_line = []
    for word in line.split():
        if keyword.iskeyword(word):
            new_line.append(word)
        else:
            new_line.append(word.upper())
    processed_lines.append(' '.join(new_line) + '\n')

# 将处理后的内容保存到新文件，例如new_random_int.py
with open('new_random_int.py', 'w') as f:
    f.writelines(processed_lines)自行完成
