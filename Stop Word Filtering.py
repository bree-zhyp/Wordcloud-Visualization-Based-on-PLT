import os  
import argparse

parser = argparse.ArgumentParser(description='Stop Word Filtering')  
parser.add_argument('output_file', type=str, help='Path to the output Excel file')  
args = parser.parse_args()  

# 指定要读取的文件夹路径  
folder_path = 'stopwords'  
  
# 指定输出文件的路径  
output_file = args.output_file  
  
# 初始化一个空集合来存储所有的词  
word_set = set()  
  
# 遍历文件夹内的所有文件  
for filename in os.listdir(folder_path):  
    if filename.endswith('.txt'):  
        # 拼接文件的完整路径  
        file_path = os.path.join(folder_path, filename)  
          
        # 打开文件并读取内容  
        with open(file_path, 'r', encoding='utf-8') as file:  
            for line in file:  
                # 移除每行两端的空白字符，包括换行符  
                word = line.strip() 
                # 将词添加到集合中  
                word_set.add(word)  

# 对停止词集合中的词进行排序  
sorted_words = sorted(word_set)  

# 将集合中的词写入到输出文件中  
with open(output_file, 'w', encoding='utf-8') as outfile:  
    for word in sorted_words:  
        outfile.write(word + '\n')  
  
print(f"Stop words have been sorted and written to {output_file}")