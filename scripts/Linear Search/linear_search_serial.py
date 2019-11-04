import random

def linear_search(sequence, target):
    for index, item in enumerate(sequence):
        if(item == target):
            return index
    return None

sequence = random.sample(range(1000000), 1000000)
target = 12312
result = linear_search(sequence, target)
if result is not None:
    print('{} found at positions: {}'.format(target, result))
else:
    print('Not found')
