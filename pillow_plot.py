from PIL import Image,ImageDraw
import random
import json
import ns

def creat_info(inf_file,long,mult):
    x=[]
    for i in range(long):
        x.append(1)
    x=list(map(lambda x:x*mult,x))
    with open(inf_file,'w') as file:
        json.dump(x,file)
    print('save success:'+inf_file)
    print('if color=False width*height='+str(long))
    if long%3==0:
        print('if color=True width*heigh='+str(long/3))
    else:
        print('not for color mode')

def creat_pic(inf_file,width,height,save_file,color=False):
    with open(inf_file,'r') as file:
        x=json.load(file)
    max_evalue=250-max(x)
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    if color==False:
        count = 0
        for i in range(height):
            for j in range(width):
                point = x[count+j] + random.randint(0,max_evalue)
                draw.point((j, i), fill=(point, point, point))
            count+=width
    else:
        count = 0
        for i in range(height):
            for j in range(width):
                star=count+j*3
                pointA = x[star] + random.randint(0,max_evalue)
                pointB = x[star+1] + random.randint(0, max_evalue)
                pointC = x[star+2] + random.randint(0, max_evalue)
                draw.point((j, i), fill=(pointA, pointB, pointC))
            count+=width*3
    image.save(save_file, quality=95)
    print('save picture:'+save_file+' color:'+str(color))


def pic_calns(pic_file,info_file,color=False):
    with open(info_file,'r') as file:
        x=json.load(file)
    im = Image.open(pic_file, 'r')
    width,height=im.size
    x_e=[]
    if color == False:
        for i in range(height):
            for j in range(width):
                x_e.append(im.getpixel((j, i))[0])
    else:
        for i in range(height):
            for j in range(width):
                    a, b, c = im.getpixel((j, i))
                    x_e.append(a)
                    x_e.append(b)
                    x_e.append(c)
    e=[x_e[i]-x[i] for i in range(len(x))]
    return ns.Fromltor(e)

#creat_info('information.json',1620,5)
#creat_pic('information.json',30,18,'pic_iscol.jpg',color=True)
nszhi=pic_calns(pic_file='pic_iscol.jpg',info_file='information.json',color=True)
print(nszhi)

