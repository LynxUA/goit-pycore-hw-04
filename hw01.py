'''
Salaries parsing module
'''

from data import safely_read_lines


def total_salary(path: str) -> tuple[int]:
    '''
    Returns total salary and avarage salary for the salaries in the provided
    '''
    lines = safely_read_lines(path)

    avg_salary = 0
    total_salary_val = 0
    salaries_len = len(lines)
    for line in lines:
        text_components = line.split(",")
        if len(text_components) > 0:
            try:
                total_salary_val += int(text_components[1])
            except ValueError:
                print(f"Please provide a valid salary for {text_components[0]}")
    if salaries_len != 0:
        avg_salary = total_salary_val / salaries_len
    return (avg_salary, total_salary_val)

def main():
    '''
    Main function
    '''
    print(total_salary("task1-testfile.txt"))
    print(total_salary("task123-testfile.txt"))

if __name__ == "__main__":
    main()
