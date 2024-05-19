import os
import shutil


def rename_zip_to_epub(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.epub'):
                zip_file_path = os.path.join(foldername, filename)
                epub_file_path = os.path.join(
                    foldername, filename[:-4] + '.zip')
                shutil.move(zip_file_path, epub_file_path)
                print(f'Renamed {zip_file_path} to {epub_file_path}')


# 指定根文件夹
root_folder = 'F:\OneDrive\新建文件夹\电子书\漫画\mz精品'
rename_zip_to_epub(root_folder)
