import argparse
import math


def find_highest_jolt(jolts:list):
    max_jolt = max(jolts)
    max_jolt_index = jolts.index(max_jolt)
    
    return [max_jolt, max_jolt_index]

def find_jolts(batteries:str):
    jolts = [int(char) for char in batteries]
    highest_number, highest_index = find_highest_jolt(jolts)
    
    if highest_index < (len(jolts)-1):
        remaining_jolts = jolts[highest_index+1:]
        second_highest, second_highest_index = find_highest_jolt(remaining_jolts)
    else:
        second_highest, second_highest_index = highest_number, highest_index
        jolts.pop(highest_index)
        highest_number, highest_index = find_highest_jolt(jolts)
        
    return int(str(highest_number) + str(second_highest))
    

def main():
    
    parser = argparse.ArgumentParser(description="Process file and starting value.")
    parser.add_argument('path', type=str, help='file path')
    args = parser.parse_args()
    
    sum = 0

    file_path = args.path

    with open(file_path, "r") as f:
        for line in f.readlines():
            jolt = find_jolts(line.strip())
    
            print(jolt)
            sum += jolt
    
    print(sum)
            
        
if __name__ == "__main__":
    main()
    
    
