class Point:
   def move(self):
      print("Move")
   
   def draw(self):
      print("Draw")
      
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)
point1.draw()

point2 = Point()
point2.x = 15
print(point2.x)