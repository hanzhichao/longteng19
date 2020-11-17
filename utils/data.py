import csv
import os
from config import DATA_DIR


def load_csv(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


if __name__ == '__main__':
    data = load_csv('users.csv')
    print(data)