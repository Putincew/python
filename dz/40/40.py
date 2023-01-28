import json
from random import choice


def get_person():
    name = ''
    tel = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)


    while len(tel) != 10:
        tel += choice(nums)


    person = {
        'name': name,
        'tel': tel
    }

    return person


def write_json(person_dict):
    num = ''
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = dict()

    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(num) != 10:
        num += choice(nums)

    data[num] = person_dict
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)

for i in range(5):
    write_json(get_person())