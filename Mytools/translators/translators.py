import requests
from re import search,compile
import execjs
from json import loads
from color import Colored

class Translator:
    result = str
    
    #*翻译接口
    def translator(self,context:str)->str:
        pass
    
    # *单词的查询接口
    def word_translator(self,word:str,part:'part of speech'=True,
                        synonyms=False,antonym=False,example=False):
        pass

    @classmethod
    def context_input(cls)->str:
        return input('请输入查询的单词:')
    
    
class GoogleTranslator(Translator):
    __headers = {
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-Hans-CN,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'cookie':'_ga=GA1.3.109609342.1586679922; NID=204=smkzALs4_20pfLxMBF7VJWK7LivaM4QPxGxKYivIDAvSsNDWUGiUoebtJTAJEn0rmAg8IGA9RL3HCWUyJeDTr3WeYsDxQLHnCMlka_f-jaq45m70vbQr6MhRaR-nqE6Zlp1uSGAtMu-FBkkTPLbN4jFahcUiZ6gCrbcz0mTNLkM; _gid=GA1.3.1741967395.1589608844; 1P_JAR=2020-5-16-11',
        'referer':'https://translate.google.cn/',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',
    }
    red = compile(r'<b>([a-zA-z]+?)</b>')
    clor = Colored()
    
    # *获取google翻译的内部实现
    def __get_res(self,keyword:str)->str:
        from google_index import str_
        tk = search(r'=(.*)',execjs.compile(str_).call('sM',keyword))[1]
        url = f'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&otf=2&ssel=0&tsel=0&kc=1&tk={tk}&q={keyword}'
        res = requests.get(url,headers=self.__headers)
        res.encoding = 'utf-8'
        return loads(res.text)
    
    #*翻译接口
    def translator(self,context=None):
        if not context:
            self.result = self.__get_res(super().context_input())[0][0][0]
            return self.result
        if isinstance(context,str):
            self.result = self.__get_res(context)[0][0][0]
            return self.result
        else:
            raise ValueError('context must be a str.')
            
    #*word的翻译
    def word_translator(self,word:str=None,synonyms=True,example=False):
        if not word:
            word = super().context_input()
        elif not isinstance(word,str):
            raise ValueError('word must be a str Obj')
            
        str_list = self.__get_res(word)
        level1 = str_list[0]
        print('+'+'-'*60+'+')
        print(level1[0][0],end=' ')
        print(level1[0][1],end=' ')
        print(level1[1][2])#*拼音       
        if synonyms:
            level2 = str_list[1]
            level3 = str_list[11]
        else:
            level3 = level2 = []
        if example:
            level4 = str_list[13][0]
        else:
            level4 = []

        #*近义词    
        if len(level2) == 2:
            print('词性: ',end='')
            print(level2[0][0])
            print('近义词: ',end='')
            for each in level2[0][1]:
                print(each,end=' ')
            print()
            print('词性: ',end='')
            print(level2[1][0])
            print('近义词: ',end='')
            for each in level2[1][1]:
                print(each,end=' ')
        elif len(level2) == 1:
            print('词性: ',end='')
            print(level2[0][0])
            print('近义词: ',end='')
            for each in level2[0][1]:
                print(each,end=' ')
        
        print()#*短语
        if level3:
            print('+'+'-'*30 + '短语' + '-'*30 + '+')
            if len(level3) == 2:
                print('词性: ',end='')
                print(level3[0][0])
                
                for each in level3[0][1][0][0]:
                    print(each,end=' /')
                print()
                print('词性: ',end='')
                print(level3[1][0])
                
                for each in level3[1][1][0][0]:
                    print(each,end=' /')
            elif len(level3) == 1:
                print('词性: ',end='')
                print(level3[0][0])
                
                for each in level3[0][1][0][0]:
                    print(each)

        #*例句
        if level4:
            print()
            print('+'+'-'*30 + '例句' + '-'*30 + '+')
            for each,i in zip(level4,range(1,len(level4)+1)):
                x,y,z = self.heightlight(each[0])
                print(f'{i}.',x+y+z)
                # print(f'{x}.',each[0])
            print('+'+'-'*30 + '-'*30 + '+')


    def heightlight(self,word:str):
        '''d <b>love</b> me for'''
        re_ = self.red.search(word)
        w_list = word.split(re_[0])
        # re_2 = red.sub(re_,word)
        return w_list[0],self.clor.red(re_[1]),w_list[-1]



            
if __name__ == "__main__":
    GoogleTranslator().word_translator('word',example=True)