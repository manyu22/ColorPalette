# -*- coding: utf-8 -*-
import Image
import sys
import os
import math
import ImageDraw
import ImageFont
 
path=os.getcwd()
dirList=os.listdir(path+"/input")
step=input("enter size of each grid  ")
method=input("enter the method\n1 for average \n2 for precise\n")
for infile in dirList:
    l=r=u=b=0
    box=(l,u,r,b)
    im=Image.open(path+"/input/"+infile)
    f, e = os.path.splitext(infile)
    A=im.load()
    s=im.size
 
    im2=Image.new("RGBA",s,"#FFFFFF")
    step=50
 
    while step>min(s[0],s[1]):
      print "step size cannot be greater than image dimension "
      step=input("enter size of each grid  ")
    if step%2==1:
      step=step-1
    offset=int(math.ceil(step/2))
    x=y=offset
    colorlist=[]
    count=0
    colorsum=[0,0,0]
    if method==2:
      while x<s[0]:
          y=offset
          while y<s[1]:
            count+=1
            color=A[x,y]
            colorsum[0]+=color[0]
            colorsum[1]+=color[1]
            colorsum[2]+=color[2]
            colorlist.append(color)
            box=(x-offset,y-offset,x+offset,y+offset)
            y=y+step
            im2.paste(color,box)
          x=x+step
      im2.save(path+"/color_precise/"+f,"JPEG",quality=100)
 
    elif method==1:
      d1=int(math.ceil(s[0]/float(step)))
      d2=int(math.ceil(s[1]/float(step)))
      out=im.resize((d1,d2),Image.ANTIALIAS)
      A2=out.load()
      x1=y1=0
      while x1<d1:
          r=r+step
          l=r-step
          while y1<d2:
            count+=1
            color=A2[x1,y1]
            colorsum[0]+=color[0]
            colorsum[1]+=color[1]
            colorsum[2]+=color[2]
            colorlist.append(color)
            b=b+step
            u=b-step
            box=(l,u,r,b)
            im2.paste(color,box)
            y1=y1+1
          x1=x1+1
          y1=0
          b=u=0
      im2.save(path+"/color_average/"+f,"JPEG",quality=100)