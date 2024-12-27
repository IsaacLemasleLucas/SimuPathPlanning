import Map
import Robot
    
if __name__ == "__main__":
    my_map = Map.Map(15,20)
    snoopy = Robot.Robot(my_map, 3, 4)
    spot = Robot.Robot(my_map,3,2)
    my_map.printMap()
    snoopy.go_up(my_map)
    print("\n\n")
    my_map.printMap()
    snoopy.go_up(my_map)
    print("\n\n")
    my_map.printMap()
    spot.go_right(my_map)
    print("\n\n")
    my_map.printMap()
    snoopy.go_up(my_map)
    print("\n\n")
    my_map.printMap()
    