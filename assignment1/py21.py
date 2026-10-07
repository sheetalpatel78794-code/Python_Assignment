length_brick = 15
breadth_brick = 8
heigth_brick = 5

bricks_volume = length_brick*breadth_brick*heigth_brick

length_wall = 15
breadth_wall = 10
heigth_wall = 8

wall_volume = length_wall*breadth_wall*heigth_wall

no_brick = wall_volume/bricks_volume

print(f"No of bricks are required for the wall {no_brick}")



