long_brick = 25/100
wide_brick = 10/100
thick_brick = 7.5/100

volume_brick = long_brick*wide_brick*thick_brick

long_wall = 20
wide_wall = 2
thick_wall = 0.75

volume_wall = long_wall*wide_wall*thick_wall

total_cost = ((volume_wall/volume_brick)/1000)*900

print(f"The total cost of make the wall is {total_cost} rs")

