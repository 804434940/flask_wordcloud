# -*- coding:utf-8 -*-

import jieba
from wordcloud import WordCloud
from scipy.misc import imread,imsave

test_text = '''浙江大学（Zhejiang University），简称“浙大”，坐落于“人间天堂”杭州。前身是1897年创建的求是书院，是中国人自己最早创办的新式高等学校之一。1928年更名为国立浙江大学。中华民国时期，浙江大学在竺可桢老校长的带领下，崛起为民国最高学府之一，被英国科学史家李约瑟誉为“东方剑桥”，迎来了浙大百年历史中最辉煌的时期。竺可桢老校长因其历史贡献，成为了浙大校史中最伟大的人，并为浙大确立了“求是”校训和文言文《浙江大学校歌》。
浙江大学直属于中华人民共和国教育部，是中国著名顶级学府之一，是中国“学科最齐全”、“学生创业率最高”的大学，是首批7所“211工程”、首批9所“985工程”重点建设的全国重点大学之一，是九校联盟、世界大学联盟、环太平洋大学联盟的成员，入选“珠峰计划”、“2011计划”、“111计划”[1-3]  ，教育部首批“卓越法律人才教育培养计划”[4]  、“卓越工程师教育培养计划”[5]  、“卓越医生教育培养计划”、“卓越农林人才教育培养计划”改革试点高校。[6-7] 
截至2016年12月，学校有紫金港、玉泉、西溪、华家池、之江、舟山、海宁7个校区，占地面积4265678㎡，校舍总建筑面积2575983㎡，图书馆藏量693.5万册。学校有7个学部，36个专业学院（系），2个中外合作办学学院、7家附属医院。有一级学科国家重点学科14个，二级学科国家重点学科21个。有全日制在校学生48762人，其中硕士研究生15092人，博士研究生9537人；留学生6237人，其中学位生3498人。'''

sw_path = './utils/stop_words.txt'

class word_spliter():
    def __init__(self,text,stop_path = sw_path):
        self.text = text
        self.stop_word = stop_path

    def get_stopword(self):
        stopwords = {}.fromkeys([line.rstrip() for line in open(self.stop_word, encoding='utf-8')])
        return stopwords

    def text_wash(self):
        self.text = self.text.encode(encoding="utf-8",errors='ignore').decode("utf-8")
        # print(self.text)
        return self.text

    def split_word(self):
        seq = ''
        sw_words = self.get_stopword()
        text = self.text_wash()
        segs = jieba.cut(text,cut_all=False)
        for seg in segs:
            if seg not in sw_words:
                seq = seq + seg +" "
        return seq


class wordclouder():
    # get parameter
    def __init__(self,text,image):
        self.text = text
        self.imag = image

    # generate picture
    def word_cloud(self):
        mask_image = imread(self.imag,flatten=False)
        word_pic = WordCloud(
            font_path='msyh.ttc',
            background_color='white',
            mask=mask_image
        ).generate(self.text)
        imsave(self.imag,word_pic)


# sp_word = word_spliter(test_text)
# text = sp_word.split_word()
# g_word = wordclouder(text,'./static/pic/mask.jpg')
# g_word.word_cloud()