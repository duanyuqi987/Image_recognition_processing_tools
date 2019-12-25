import os  
      
class BatchRename():  
      #  ''''' 
     #   批量重命名文件夹中的图片文件 
     
       # '''  
        def __init__(self):  
            #我的图片文件夹路径horse  
            self.path = '/home/duanyajun/图片/文件处理中心/2'
            self.path1 = '/home/duanyajun/图片/文件处理中心/3'
      
        def rename(self):  
            filelist1 = os.listdir(self.path)  
            total_num = len(filelist1)  
            i = 100000
            n = 6
            print(sorted(filelist1))
            filelist = sorted(filelist1)
            for item in filelist:  
                if item.endswith('.jpg'):  
                    n = 6 - len(str(i))  
                    src = os.path.join(os.path.abspath(self.path), item)  
                    dst = os.path.join(os.path.abspath(self.path1), str(0)*n + str(i) + '.jpg')  
                    try:  
                        os.rename(src, dst)  
                        print ('converting %s to %s ...' % (src, dst) ) 
                        i = i + 1  
                  
                    except:  
                        continue  
            print ('total %d to rename & converted %d jpgs' % (total_num, i)  )
      
if __name__ == '__main__':  
        demo = BatchRename()  
        demo.rename()  
