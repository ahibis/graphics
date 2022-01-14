from turtle import *

def setWindowSize(width, height):
	reset()
	hideturtle()
	setup(width, height)
	setworldcoordinates(0, 0, width, height)
	

def move_to(x, y):
	penup()
	goto(x, y)

def line_to(x2, y2):
	x1 = xcor()
	y1 = ycor()
	move_to(x1, y1)
	pendown()
	goto(x2, y2)

def line(x1, y1, x2, y2):
	move_to(x1, y1)
	pendown()
	goto(x2, y2)

#парметры по умолачанию
width=60
leafWidth=10
leafHight=15
count=4;
fullWidth=width*count*1.2+50;
fullHight=width+100;
'''
#вводимые параметры
fullWidth=int(input("введите ширину сцены="));#ширина сцены
fullHight=int(input("введите высоту сцены="));#высота сцены
width=int(input("введите размер цветка="));#размер цветка
leafWidth=int(input("введите шириниу лиспестка="));#ширина липестка
leafHight=int(input("введите высоту липестка="));#высота липестка
count=int(input("введите колличество цветков="));#кол-во цветков
'''
setWindowSize(fullWidth,fullHight);
def drawLeaf(x,y,mx=1,my=1):#функция рисования вертикального листка с координатами (x,y) и коэффициэтами mx,my 
	move_to(x,y);#переходим на начальные координаты
	begin_fill();#начинаем рисование
	x+=leafWidth*mx;#сдвигаемся по x на ширину листка
	line_to(x,y);#рисуем линию
	y-=leafHight*my;#сдвигаемся на высоту листка
	line_to(x,y);#рисуем линию
	x-=leafWidth*mx;#сдвигаемся на ширину листка по x и y
	y+=leafWidth*my;
	line_to(x,y);#рисуем линию
	end_fill()#закрашиванм

def drawLeafH(x,y,mx=1,my=1):#функция рисования горизонтального листка с координатами (x,y) и коэффициэтами mx,my 
	move_to(x,y);
	begin_fill();
	y+=leafWidth*my;
	line_to(x,y);
	x-=leafHight*mx;
	line_to(x,y);
	y-=leafWidth*my;
	x+=leafWidth*mx;
	line_to(x,y);
	end_fill()

def box(x,y,width):#функция рисования квадрата на координатах x,y
	move_to(x,y);
	begin_fill();
	x+=width;
	line_to(x,y);
	y-=width;
	line_to(x,y);
	x-=width;
	line_to(x,y);
	end_fill()

def line(x,y,width):#рисование черных полос
	move_to(x,y);
	begin_fill();
	x+=width;
	line_to(x,y);
	y-=fullHight//10;
	line_to(x,y);
	x-=width;
	line_to(x,y);
	end_fill()

def drawFlower(x,y):#рисование цветка
	dx=(width-2*leafWidth)//3;#высчитываем размер между липестками
	#рисуем липестки
	drawLeaf(x+dx,y)
	drawLeaf(x+width-dx,y,-1,1)
	drawLeafH(x+width,y-dx,1,-1)
	drawLeafH(x+width,y-width+dx,1,1)
	drawLeaf(x+width-dx,y-width,-1,-1)
	drawLeaf(x+dx,y-width,1,-1)
	drawLeafH(x,y-width+dx,-1,1)
	drawLeafH(x,y-dx,-1,-1)
	#рисуем ценьр
	box(x+dx+leafWidth,y-dx-leafWidth,dx)

def drawRowOfFlowers(x=0,y=0):#функция рисующая ряд цветов
	for i in range(count):
		drawFlower(x,y)#рисуем цветок
		x+=width*1.2;#сдвигаемся на ширину цветка*1.2
hideturtle()
drawRowOfFlowers(0,fullHight//2+width//2);
line(0,fullHight,fullWidth);
line(0,16,fullWidth);
