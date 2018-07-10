#encoding=utf-8

import sys
sys.path.append('./TFIDF_baseline/')

from cutWords import *
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence

def run_prediction(input_file_path, output_file_path):
    # 读入训练集
    file_obj = FileObj(r"./TFIDF_baseline/dataSet/trainQuestions.txt")  
    train_sentences = file_obj.read_lines()
   

    # 读入测试集
    file_obj = FileObj(input_file_path)   
    test_sentences = file_obj.read_lines()


    # 分词工具，基于jieba分词，并去除停用词
    seg = Seg()

    # 训练模型
    ss = SentenceSimilarity(seg)
    ss.set_sentences(train_sentences)
    ss.TfidfModel()         # tfidf模型

    # 测试集
    right_count = 0
    
    file_result=open(output_file_path,'w')
    with open("./TFIDF_baseline/dataSet/trainAnswers.txt",'r',encoding = 'utf-8') as file_answer:
        line = file_answer.readlines()
           
    for i in range(0,len(test_sentences)):
        top_15 = ss.similarity(test_sentences[i])
        
        '''
        for j in range(0,len(top_15)):
            answer_index=top_15[j][0]
            answer=line[answer_index]
            file_result.write(str(top_15[j][1])+'\t'+str(answer))
        file_result.write("\n")
        '''
        file_result.write(line[top_15[0][0]]+'\n')
        
    file_result.close() 
    file_answer.close()
    
