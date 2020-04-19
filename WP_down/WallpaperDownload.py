#!/usr/local/bin/python3
#encoding:utf-8
import requests
from ahttp import get,run
import asyncio
from aiofiles import open as ay_open
# from os.path import isdir,mkdir
from os import mkdir
from os.path import isdir



class WallpaperDownload:
    
    def requests_interface(self,page:int,cate:str)->None:
        """request the json_interface and return the json data for img_url
        
        Arguments:
            page {int} -- the pageNum for download
            cate {str} -- the cate of img for downloading
        
        Returns:
            str -- json data
        """
        num = page*12
        url = 'https://bird.ioliu.cn/v2?'
        params = {
            'url':'http://wallpaper.apc.360.cn/index.php?c=WallPaper',
            'start':f'{num}',
            'count':'12',
            'from':'360chrome',
            'a':'getAppsByCategory',
            'cid':f'{cate}',
        }
        res = requests.get(url,params=params)
        print(res.status_code)
        return res.json()['data']


    def downloa_img(self,page:int,cate:str)->bytes:
        """after getting the urls for downloading,create the tasks for loop,
        yield the name consititutes of its url ,the img_bytes and img_tag
        
        Arguments:
            page {int} -- [pageNum for downloading]
            cate {str} -- [img_cate]
                
        Yields:
            url -- [for name]
            bytes -- [img_bytes]
            tag -- [img_tag]
        """
        datas = self.requests_interface(page,cate)
        urls = [x['url'] for x in datas]
        tasks = [get(x) for x in urls]
        resluts = run(tasks)
        for each,tach in zip(resluts,datas):
            tag = tach['tag'][-5:]
            if not isdir(tag):
                mkdir(tag)
            yield str(each.url)[-15:],each.content,tag
            print(str(each.url),each.status)
        

    async def save(self,bits:bytes,name:str,tag:str)->None:
        """
        asynchronously save the imgs
        """
        async with ay_open(f'{tag}/{name}','wb') as fp:
                await fp.write(bits)
                print('finished!')
            
        
    def main_(self,page:str,catagory:str)->None:
        """The main function for run the events loop
        
        Arguments:
            page {str} -- img_page for downlia_img
            catagory {str} -- img_cate for downloa_img
        """
        loop = asyncio.get_event_loop()
        coros = [self.save(y,x,t) for x,y,t in self.downloa_img(page,catagory)]
        tasks = [asyncio.ensure_future(x) for x in coros]
        res = asyncio.gather(*tasks)
        loop.run_until_complete(res)
        print('='*100)
        
    
    
    def run_(self,startpage:int,endpage:int,catagory:str)->None:
        for x in range(startpage,endpage+1):
            print(x)
            self.main_(x,catagory)

    
    
    def for_download(self):
        """the outside interface for main project
        """
        start,end,cate = self.select()
        self.run_(start,end,cate)
        
    @classmethod
    def select(cls):
        CATE_STR = r"""
        "4K":"36",
        "美女":"6",
        "爱情":"30",
        "风景":"9",
        "小清新":"15",
        "动漫":"26",
        "明星":"11",
        "宠物":"14",
        "游戏":"5",
        "汽车":"12",
        "时尚":"10",
        "月历":"29",
        "影视":"7",
        "节日":"13",
        "军事":"22",
        "体育":"16",
        "BABY秀":"18",
        "文字":"35"
        """
        print(CATE_STR)
        category = input("你想要什么样的壁纸,输入编号")
        start,end = map(int,input("从那一页到那一页?").split())
        return start,end,int(category)


    
# if __name__ == "__main__":
#     downloader = WallpaperDownload()
#     start,end,cate = downloader.select()
#     downloader.run_(start,end,cate)

    