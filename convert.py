import os
from ebooklib import epub
import chardet

def txt_to_epub(txt_folder, epub_folder):
    # 确保epub文件夹存在，如果不存在则创建
    if not os.path.exists(epub_folder):
        os.makedirs(epub_folder)

    # 遍历txt文件夹中的所有txt文件
    for txt_file in os.listdir(txt_folder):
        if txt_file.endswith('.txt'):
            # 读取txt文件内容
            # 尝试的编码列表
            encodings_to_try = ['utf-8', 'latin-1', 'gbk', 'gb2312', 'big5']  # 根据你的需要添加更多编码

            # 读取txt文件内容并尝试不同的编码
            with open(os.path.join(txt_folder, txt_file), 'rb') as f:
                raw_data = f.read()
                for encoding in encodings_to_try:
                    try:
                        txt_content = raw_data.decode(encoding)
                        break  # 如果成功解码，则跳出循环
                    except UnicodeDecodeError:
                        continue  # 如果解码失败，则尝试下一个编码

                # 如果所有尝试都失败，则使用空字符串作为文本内容
                else:
                    txt_content = ''

            # 如果txt_content为空，可以输出一条消息来通知用户
            if not txt_content:
                print(f"无法解码 {txt_file}，可能是因为它的编码无法被识别。")

            # 创建一个新的epub对象
            book = epub.EpubBook()

            # 设置epub标题
            book.set_title(os.path.splitext(txt_file)[0])

            # 创建一个新的章节并添加txt内容
            chapter = epub.EpubHtml(title='Chapter 1', file_name='chapter1.xhtml', lang='en')
            chapter.content = txt_content

            # 将章节添加到epub书籍中
            book.add_item(chapter)

            # 添加导航
            book.toc = (epub.Link('chapter1.xhtml', 'Introduction', 'intro'),)

            # 添加样式文件
            style = 'body { font-family: Times, Times New Roman, serif; }'
            nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
            book.add_item(nav_css)

            # 创建spine
            book.spine = ['nav', chapter]

            # 将epub文件保存到epub文件夹中
            epub_file = os.path.join(epub_folder, os.path.splitext(txt_file)[0] + '.epub')
            epub.write_epub(epub_file, book, {})

            print(f"{txt_file} 转换完成为 {os.path.basename(epub_file)}")

# 设置txt文件夹和epub文件夹的路径
txt_folder_path = r'F:\OneDrive\新建文件夹\电子书\其他\11精品'
epub_folder_path = r'F:\test'

# 转换txt到epub
txt_to_epub(txt_folder_path, epub_folder_path)
