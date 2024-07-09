import re


def optimize_txt_format(filename):
    # 尝试使用的编码列表
    encodings = ['gb18030', 'utf-8', 'utf-16',
                 'gbk', 'big5', 'gb2312', 'utf-16', 'utf-16', 'ascii']

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()
            # 如果没有异常，则跳出循环
            break
        except UnicodeDecodeError as e:
            print(f"Warning: {e}, trying next encoding")
            continue

    # 确认读取的行是否有效
    if not lines:
        print("Could not read the file with any encoding, exiting.")
        return

    optimized_lines = []
    for line in lines:
        if optimized_lines and re.search(r'[\u4e00-\u9fa5]$', optimized_lines[-1]):
            optimized_lines[-1] = optimized_lines[-1].rstrip() + line.lstrip()
        else:
            optimized_lines.append(line.strip())

    # 写入文件时，尝试与读取相同的编码列表
    for encoding in encodings:
        try:
            with open(filename, 'w', encoding=encoding) as file:
                for line in optimized_lines:
                    file.write(line + '\n')
            # 如果写入成功，则跳出循环
            break
        except Exception as e:
            print(f"Warning: {e}, trying next encoding")

    # 如果所有编码都失败，则报错
    if encoding == encodings[-1]:
        print("Could not write the file with any encoding, exiting.")


# 请确保路径正确，并且您有权限写入该文件
optimize_txt_format(r'C:/Users/86151/Desktop/【与爸爸的约定】【1-63】【作者：酒醉梦自醒】.txt')
