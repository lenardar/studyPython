import os


def rename_zip_to_epub(root_folder):
    # 遍历根文件夹及其所有子文件夹
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            # 检查文件是否以.zip结尾
            if filename.endswith('.webp'):
                # 构建旧文件路径和新文件路径
                old_file = os.path.join(foldername, filename)
                new_file = os.path.join(foldername, filename[:-4] + 'jpg')
                # 重命名文件
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} to {new_file}')


# 调用函数，传入根文件夹路径
root_folder_path = 'F:\OneDrive\新建文件夹\电子书\漫画\mz\[1111]\[hente]'
rename_zip_to_epub(root_folder_path)
