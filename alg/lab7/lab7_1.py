import re

data = {}

with open('data.txt', 'r') as f:
    for line in f:
        fio, year_birth, mark, year_car, gov_number = re.split('\s+', line.strip())
        data[ gov_number ] = {
            'fio': fio,
            'year_birth': int(year_birth),
            'mark': mark,
            'year_car': int(year_car)
        }

def search_by_surname(surname):
    result = []
    for key, value in data.items():
        if value['fio'].split()[0] == surname:
            result.append(value)
    return result

def search_by_mark(mark, year):
    result = []
    for key, value in data.items():
        if value['mark'] == mark and value['year_car'] <= year:
            result.append(value)
    return result

def search_by_mark_only(mark):
    result = []
    for key, value in data.items():
        if value['mark'] == mark:
            result.append(value)
    return result

def get_count_by_mark(mark):
    return len(search_by_mark_only(mark))

def get_youngest_by_mark(mark):
    youngest = None
    for value in search_by_mark_only(mark):
        if youngest is None or value['year_birth'] > youngest['year_birth']:
            youngest = value
    return youngest

def get_oldest_by_mark(mark):
    oldest = None
    for value in search_by_mark_only(mark):
        if oldest is None or value['year_birth'] < oldest['year_birth']:
            oldest = value
    return oldest

if __name__ == '__main__':
    print(search_by_surname('Петров'))
    print(search_by_mark('Ford', 2010))
    print(get_count_by_mark('Ford'))
    print(get_youngest_by_mark('Ford'))
    print(get_oldest_by_mark('Ford'))
