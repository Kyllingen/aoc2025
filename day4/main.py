import argparse
import math
    
positions = [(1,1), (1,0),(1,-1),(0,1), (0,-1), (-1,1),(-1,0), (-1,-1)]

def check_surrounding(x_pos:int, y_pos:int, map:list):
    ''' search the 8 positions around current index for @ and return count'''
    count = 0
    access = 0
    for i in positions:
        if count >= 4:
            break
        
        if (x_pos+i[0]) >= 0 and (x_pos+i[0]) < len(map[0]) and (y_pos+i[1]) >= 0 and (y_pos+i[1]) < len(map):
            marker = map[x_pos+i[0]][y_pos+i[1]]
            if marker == "@":
                count += 1
    
    if count < 4:
        access = 1
        
    return access

def traverse_map(map:list):
    '''iterate through the map'''
    total_access = 0
    x = 0
    y = 0
    for col in map:
        for row in col: 
            if row == "@":
                total_access += check_surrounding(x, y, map)
            y += 1
            
        x += 1
        y = 0
            
    return total_access    

def main():
    
    parser = argparse.ArgumentParser(description="Process file and starting value.")
    parser.add_argument('path', type=str, help='file path')
    args = parser.parse_args()
    
    sum = 0

    file_path = args.path
    
    map = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            map.append( line.strip())

    total_acess = traverse_map(map)
    print(total_acess)
        
if __name__ == "__main__":
    main()
    
    
