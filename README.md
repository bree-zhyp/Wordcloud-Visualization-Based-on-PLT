# 自然语言处理：中文分词、词性分析及可视化

使用分词工具 (哈工大 PLT) 对五个文档分别进行分词和词性标注，对分词结果去除停止词并进行词频统计，分别列出十六大到二十大报告全文中词频最高的 30 个名词及其词频，最后使用词云可视化工具 Wordcloud 分别对每一个文档中出现频率最高的 30 个名词进行词云的可视化展示。

## 作者

- [ZhangYupeng](https://github.com/SYSU-Zhangyp)

## 压缩包内容  

本压缩包包含了作业项目所需的一些文件、文档或数据，下面是关于这个压缩包的详细介绍。 
- **/dataset**：用于存储项目的数据集
- **/ltp-main**：武汉大学 LTP 分词系统源代码  
- **/output**：文件夹存储输出文件
- **/output/Full Text Annotation**：全文分词标注结果  
- **/output/Text Annotation after Stop Word Filtering**：过滤停止词词频统计结果
- **/small**：ltp 模型文件  
- **/stopwords**：停止词的数据集  
- **Tokenization and POS Tagging.py**：分词与词性标注 python 文件  
- **Stop Word Filtering.py**：停止词过滤 python 文件  
- **Word frequency analysis.py**：词频统计 python 文件  
- **Get Wordcloud.py**：词云生成 python 文件  
- **main.py**：主函数 (直接运行这个文件即可)

## 运行环境

操作系统：Windows 11 Version 23H2

Python版本：Python 3.11.4 ('base':conda)

## Python 程序依赖库  
  
要运行本程序，你可能需要安装以下Python库：  
   
1. **Pandas**: 提供数据结构和数据分析工具。    
2. **Openpyxl**: 与 Excel 文件进行交互，可以写入数据。  
3. **Argparse**: 用于编写命令行接口。  
  
你可以使用pip（Python的包管理工具）来安装这些依赖项。打开你的命令行工具，并输入以下命令：  
  
```bash  
pip install pandas openpyxl argparse
```
## 运行代码

整个任务都已封装好，只需要调用主函数即可执行。调用前请确保output/Full Text Annotation 文件夹中没有文件，否则可能会出现重复计算的错误。
```bash  
python main.py
```

## 结果展示
### 十六大报告词云
![十六大](output/Wordcloud/wordcloud_十六大报告.png)
### 十七大报告词云
![十七大](output/Wordcloud/wordcloud_十七大报告.png)
### 十八大报告词云
![十八大](output/Wordcloud/wordcloud_十八大报告.png)
### 十九大报告词云
![十九大](output/Wordcloud/wordcloud_十九大报告.png)
### 二十大报告词云
![二十大](output/Wordcloud/wordcloud_二十大报告.png)

## 参考使用

  
- [武汉大学 LTP 分词系统](https://github.com/HIT-SCIR/ltp)：武汉大学自然语言处理实验室开发的分词系统，提供了丰富的中文自然语言处理功能。



