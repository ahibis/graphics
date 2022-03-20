from turtle import *
def setWindowSize(width, height):
	screen = Screen()
	screen.setup(width, height)
	setworldcoordinates(0, 0, width, height)
	reset()
	hideturtle()

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

'''
функция рисующая квадрат
x,y - координаты
width- ширина квадрата
'''
def drawBox(x,y,width):
	move_to(x,y);
	begin_fill();
	x+=width;
	line_to(x,y);
	y-=width;
	line_to(x,y);
	x-=width;
	line_to(x,y);
	y+=width;
	line_to(x,y);
	end_fill()
'''
функция ряд квадратов
x,y  - координаты начала
width- ширина квадрата
count- количество квадратов
'''
def drawRowOfBoxs(x,y,width,count):#функция рисующующая count 
	for i in range(count):
		drawBox(x+i*width,y,width)
'''
функция рисующая цветок
x,y  - координаты центра цветка
width- ширина цветка
'''
def drawFlower(x,y,width):
	#сдвигаемся в начальный угол
	x-=width//2;
	y+=width//2;
	boxSize=width//5;#расчитываем ширину одного квадрата
	drawBox(x+boxSize*2,y,boxSize);
	y-=boxSize;#сдвигаемся на следующй слой
	drawRowOfBoxs(x+boxSize,y,boxSize,3);
	y-=boxSize;
	drawRowOfBoxs(x,y,boxSize,2);
	drawRowOfBoxs(x+boxSize*3,y,boxSize,2);
	y-=boxSize;
	drawRowOfBoxs(x+boxSize,y,boxSize,3);
	y-=boxSize;
	drawBox(x+boxSize*2,y,boxSize);
'''
функция рисующая нижнюю часть цветка
x,y  - координаты центра цветка
width- ширина цветка
'''
def drawDownPartFlower(x,y,width):
	x-=width//2;
	y+=width//2;
	boxSize=width//5;
	y-=boxSize*3;
	drawRowOfBoxs(x+boxSize,y,boxSize,3);
	y-=boxSize;
	drawBox(x+boxSize*2,y,boxSize);
'''
функция рисующая верхнюю часть цветка
x,y  - координаты центра цветка
width- ширина цветка
'''
def drawUpPartFlower(x,y,width):
	x-=width//2;
	y+=width//2;
	boxSize=width//5;
	drawBox(x+boxSize*2,y,boxSize);
	y-=boxSize;
	drawRowOfBoxs(x+boxSize,y,boxSize,3);
'''
функция рисующая конец цветка
x,y  - координаты центра цветка
width- ширина цветка
'''
def drawEndOfFlower(x,y,width):
	boxSize=width//5;
	x+=boxSize*1.5;
	y+=boxSize//2;
	drawBox(x,y,boxSize);
'''
функция рисующая начало цветка цветка
x,y  - координаты центра цветка
width- ширина цветка
'''
def drawStartOfFlower(x,y,width):
	boxSize=width//5;
	x-=boxSize*2.5;
	y+=boxSize//2;
	drawBox(x,y,boxSize);
'''
функция рисующая первый ряд цветков
x,y  - координаты начала ряда
width- ширина цветка
count- количество цветков
distance- расстояние между цветками
'''
def drawRowOfFlowers(x,y,flowerWidth,count,distance):
	for i in range(count):
		drawFlower(x,y,flowerWidth);
		x+=distance
	drawStartOfFlower(x,y,flowerWidth);
'''
функция рисующая второй ряд цветков(между цветками)
x,y  - координаты начала ряда
width- ширина цветка
count- количество цветков
distance- расстояние между цветками
'''
def drawRowOfFlowers2(x,y,flowerWidth,count,distance):
	drawEndOfFlower(x-distance,y,flowerWidth);
	for i in range(count):
		drawFlower(x,y,flowerWidth);
		x+=distance
'''
функция рисующая верхние части ряда цветков
x,y  - координаты начала ряда
width- ширина цветка
count- количество цветков
distance- расстояние между цветками
'''
def drawRowOfUpPartFlower(x,y,flowerWidth,count,distance):
	for i in range(count):
		drawUpPartFlower(x,y,flowerWidth);
		x+=distance
	
'''
функция рисующая нижние части ряда цветков
x,y  - координаты начала ряда
width- ширина цветка
count- количество цветков
distance- расстояние между цветками
'''
def drawRowOfDownPartFlower(x,y,flowerWidth,count,distance):
	for i in range(count):
		drawDownPartFlower(x,y,flowerWidth);
		x+=distance
'''
функция рисующая узор
x,y  - координаты начала ряда
flowerWidth- ширина цветка
count- количество цветков в ряду. 
Кол-во рядов высчитывается так, чтобы получился квадрат
distance- расстояние между цветками
'''
def drawRoomOfFlowers(x,y,flowerWidth,count,distance):
	#сдвигаемся на размеры для красивых рамок
	x+=flowerWidth;
	y-=flowerWidth//2;
	drawRowOfDownPartFlower(x,y,flowerWidth,count,distance)
	drawRowOfFlowers2(x+distance/2,y-distance/2,flowerWidth,count,distance)
	y-=distance
	for i in range(count-1):
		drawRowOfFlowers(x,y,flowerWidth,count,distance)
		drawRowOfFlowers2(x+distance/2,y-distance/2,flowerWidth,count,distance)
		y-=distance
	drawRowOfUpPartFlower(x,y,flowerWidth,count,distance)


#парметры по умолачанию(не влияют на результат)
flowerWidth=80;
count=2;
distance=flowerWidth*1.6;
roomWidth=500;
roomHight=500;
#вводимые параметры
roomWidth=int(input("введите ширину сцены="));#ширина сцены
roomHight=int(input("введите высоту сцены="));#высота сцены
flowerWidth=int(input("введите размер цветка="));#размер цветка
count=int(input("введите колличество цветков="));#кол-во цветков
distance=flowerWidth*1.6;#растояние между цветками, указываем как ширина цветка + 3 блока расстояния 
setWindowSize(roomWidth,roomHight);#устанавливаем размеры экрана
drawRoomOfFlowers(0,roomHight,flowerWidth,count,distance)#рисуем узор
input("нажмите любую клавишу, чтобы завершить программу");