import argparse
import math


def find_jolts(batteries:str):
    
    return 0

def main():
    
    parser = argparse.ArgumentParser(description="Process file and starting value.")
    parser.add_argument('path', type=str, help='file path')
    args = parser.parse_args()

    file_path = args.path

    with open(file_path, "r") as f:
        for line in f.readlines():
            jolt = find_jolts(line.strip())
    
            print(jolt)
        
if __name__ == "__main__":
    main()
    
    
