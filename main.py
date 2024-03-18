import subprocess  
  
def run_tokenization_and_POS_tagging(args):  
    # 运行分词和词性标注的python文件并传递参数 
    file = 'Tokenization and POS Tagging.py' 
    subprocess.run(['python', file] + args)   

def run_stop_word_filtering():
    # 运行停词统计的python文件
    file = 'Stop Word Filtering.py'
    stopwords_location = 'output/Text Annotation after Stop Word Filtering/stopwords.txt'
    subprocess.run(['python', file] + [stopwords_location])

def run_word_frequency_analysis(args):
    # 运行词频统计的python文件
    file = 'Word Frequency Analysis.py'
    subprocess.run(['python', file] + args)

# 文件路径地址，要修改文件只需要修改这部分的内容
# 修改十六大报告为二十大报告，只需要将所有地址中的"十六"改为"二十"即可
# 请注意，由于分词操作对excel文件进行追加写操作，如果要重新运行，
#    需要先删除output_location位置下存储的已经运行好的FTA_XXX报告全文.xlsx文件
#    否则所有词的数量都会增加一倍，导致统计次数不准确，但是不影响最后的词云结果
data_location = 'dataset/十六大报告全文.txt'
output_location = 'output/Full Text Annotation/FTA_十六大报告全文.xlsx'
result_loaction = 'output/Text Annotation after Stop Word Filtering/TA_SWF_十六大报告.xlsx'
wordcloud_location = 'output/Wordcloud/wordcloud_十六大报告.png'

# 设置传递的参数
args = [data_location, output_location]   
result_args = [output_location, result_loaction, wordcloud_location]

# 调用Python文件并传递参数  
run_tokenization_and_POS_tagging(args)
run_stop_word_filtering()
run_word_frequency_analysis(result_args)