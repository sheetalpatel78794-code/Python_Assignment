long_path = 120
breadth_path = 2.4

long_brick = 24/100
breadth_brick = 15/100

area_brick = long_brick*breadth_brick
area_path = long_path*breadth_path
no_of_bricks = area_path/area_brick

print(f"The no of bricks required for path: {no_of_bricks}")