'''
Data extraction helpers
'''

from pathlib import Path


def safely_read_lines(path: str) -> list[str]:
    '''
    Common function to safely extract lines
    '''
    file_path = Path(path)
    if not file_path.exists():
        print(f"File {file_path} doesn't exist")
        return []
    with open(file_path, 'r', encoding="utf-8") as fh:
        lines = fh.readlines()
    return lines
