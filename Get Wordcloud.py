import wordcloud
import argparse  
  
parser = argparse.ArgumentParser(description='Get Wordcloud')  
parser.add_argument('input_file', type=str, help='Path to the input text file')  
parser.add_argument('wordcloud_file', type=str, help='Path to the output wordcloud file')  
args = parser.parse_args()  
  
# 接收分词统计后的字符数据，并生成词云对象  
wordcloud_text = args.input_file  
# wc = wordcloud.WordCloud(font_path='simhei.ttf', background_color='black', max_words=30, width=800, height=400, margin=2).generate(wordcloud_text)  
wc = wordcloud.WordCloud(  
    font_path='simhei.ttf',             # 使用支持中文的字体  
    background_color='white',           # 设置背景色为黑色  
    max_words=30,                       # 最多显示的词语数量  
    width=800,                          # 词云的宽度  
    height=400,                         # 词云的高度  
    margin=2,                           # 词语间距  
    colormap='viridis'                  # 使用viridis颜色映射，也可以选择其他颜色映射  
).generate(wordcloud_text)  

# 保存词云图片  
wc.to_file(args.wordcloud_file)  
print(f"Stop words have been sorted and written to {args.wordcloud_file}")


