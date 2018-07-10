#! /usr/bin/python
# -*- coding: utf-8 -*-

import re


class TextPreProcessor(object):

    def __init__(self):
        pass

    @staticmethod
    def clean_text(text):
        """
        Clean text
        :param text: the string of text
        :return: text string after cleaning
        """
        '''
        # punctuation
        text = re.sub(r"\+", " + ", text)
        text = re.sub(r"'", " ", text)
        text = re.sub(r"-", " - ", text)
        text = re.sub(r"/", " / ", text)
        text = re.sub(r"\\", " \ ", text)
        text = re.sub(r"=", " = ", text)
        text = re.sub(r"\^", " ^ ", text)
        text = re.sub(r":", " : ", text)
        text = re.sub(r"\.", " . ", text)
        text = re.sub(r",", " , ", text)
        text = re.sub(r"\?", " ? ", text)
        text = re.sub(r"!", " ! ", text)
        text = re.sub(r"\"", " \" ", text)
        text = re.sub(r"&", " & ", text)
        text = re.sub(r"\|", " | ", text)
        text = re.sub(r";", " ; ", text)
        text = re.sub(r"\(", " ( ", text)


        # punctuation
        text = re.sub(r".", "  ", text)
        text = re.sub(r"'", " ", text)
        text = re.sub(r"-", " - ", text)
        text = re.sub(r"/", " / ", text)
        text = re.sub(r"\\", " \ ", text)
        text = re.sub(r"=", " = ", text)
        text = re.sub(r"\^", " ^ ", text)
        '''


        text = re.sub(r"#E-s", " <EMO> ", text)
        text = re.sub(r"\[数字x]", "00000000000000000000", text)
        text = re.sub(r"\[ORDERID_[0-9]+]", " <ORD> ", text)
        text = re.sub(r"\[金额x]", " <MON> ", text)
        text = re.sub(r"\[日期x]", " <DATE> ", text)
        text = re.sub(r"\[时间x]", " <TIME> ", text)
        text = re.sub(r"\[地址x]", " <ADDR> ", text)
        text = re.sub(r"\[组织机构x]", " <ORG> ", text)
        text = re.sub(r"\[电话x]", " <TEL> ", text)
        text = re.sub(r"\[姓名x]", " <NAME> ", text)
        text = re.sub(r"\[站点x]", " <SITE> ", text)
        text = re.sub(r"https://\[链接x]", " <LINK> ", text)
        text = re.sub(r"(https?|ftp|file|\[链接x])://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", " <LINK> ", text)
        text = re.sub(r"\[链接x]", " <LINK> ", text)
        text = re.sub(r"\[身份证号x]", " <IDC> ", text)
        text = re.sub(r"&nbsp;", " ", text)
        text = re.sub(r"00000000000000000000", " <NUM> ", text)



        # remove extra space
        # text = ' '.join(text.split())

        return text



if __name__ == '__main__':
    with open('./dataSet/devQuestions.txt', 'r') as input_file:
        lines = input_file.readlines()

    textPreProcessor = TextPreProcessor()

    with open('test.txt', 'w') as output_file:
        for line in lines:
            output_file.write(textPreProcessor.clean_text(line))
