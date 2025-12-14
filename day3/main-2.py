import argparse
import math


def scan_range(count:int, jolts:list, start_index:int):
    None

def scan_best_range(jolts:list, index:int, max_result:int):
    count = 0
    result = -1
    while count >= 0 and count < 13:
        None #TODO
        

def find_jolts(batteries:str):
    jolts = [int(char) for char in batteries]
    end_index = len(jolts) - 12
    for i in range(0, end_index):
        sum = scan_best_range(jolts[i:], i, -1)
    

def main():
    
    parser = argparse.ArgumentParser(description="Process file and starting value.")
    parser.add_argument('path', type=str, help='file path')
    args = parser.parse_args()
    
    sum = 0

    file_path = args.path

    with open(file_path, "r") as f:
        for line in f.readlines():
            jolt = find_jolts(line.strip())
    
            #print(jolt)
            #sum += jolt
    
    print(sum)
            
        
if __name__ == "__main__":
    main()
    
    
