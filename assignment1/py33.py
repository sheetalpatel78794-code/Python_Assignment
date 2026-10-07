length_garden= 30
breadth_garden = 20

area_garden = length_garden*breadth_garden

length_path1 = 20
breadth_path1 = 3

area_path1 = length_path1*breadth_path1

length_path2 = 30
breadth_path2 = 4

area_path2 = length_path2*breadth_path2

twice_area = breadth_path1*breadth_path2
area_occupied = area_path1+area_path2-twice_area

free_area = area_garden-area_occupied

print(f"The usable area of the garden {free_area}")
