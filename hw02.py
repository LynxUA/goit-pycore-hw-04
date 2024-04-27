'''
Cat parsing module
'''

from data import safely_read_lines


def get_cats_info(path: str) -> dict:
    '''
    Returns cat infos based on the provided file
    '''
    lines = safely_read_lines(path)
    cat_infos = []
    for i, line in enumerate(lines):
        cat_info_line = line.strip().split(",")
        if len(cat_info_line) != 3 or not cat_info_line[2].isdigit():
            print(f"Incorrect cat info for the line {i},\
 the line should have 3 components, and the last one should be integer (age)")
        else:
            cat_infos.append({"id": cat_info_line[0],
                     "name": cat_info_line[1], 
                     "age": cat_info_line[2]})
    return cat_infos

def main():
    '''
    Main function
    '''
    print(get_cats_info("task2-testfile.txt"))
    print(get_cats_info("task123-testfile.txt"))

if __name__ == "__main__":
    main()
