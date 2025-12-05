import argparse
import math

def turn_dial(direction:str, value:int, current_value:int):
    # check how many times it would go one revolution
    x_rotations = math.floor(value / 100)
    
    if x_rotations > 0:
        value -= 100 * x_rotations
        
    if direction == "L":
        if (current_value - value) < 0 and current_value != 0:
            x_rotations += 1
        
        current_value = (current_value - value) % 100
    else:
        if (current_value + value) > 100 and current_value != 0:
            x_rotations += 1
        
        current_value = (current_value + value) % 100
    
    if  current_value == 0:
        x_rotations += 1
    
    return [current_value, x_rotations]

def main():
    
    parser = argparse.ArgumentParser(description="Process file and starting value.")
    parser.add_argument('start_pos', type=int, help='starting position of dial')
    parser.add_argument('path', type=str, help='file path')
    args = parser.parse_args()

    current_value = args.start_pos
    file_path = args.path
    count_zeros = 0
    
    # go through each line and find direction to turn, count number of revolutions passed 0 or landing on 0
    with open(file_path, "r") as f:
        for line in f.readlines():
            result = turn_dial(line[0], int(line[1:]), current_value)
        
            count_zeros += result[1]
            current_value = result[0]
                
    print("count", count_zeros)
    
if __name__ == "__main__":
    main()
    
    
