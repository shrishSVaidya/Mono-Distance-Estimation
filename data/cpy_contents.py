import os

path = os.path.join(os.getcwd(), 'labels')

i= 0
for file in os.listdir(path):
    if file.startswith('val'):
        continue
    
    else:
        filename = os.path.join(path, file)
        print(filename)
        with open(filename, 'r') as input_file:
            contents = input_file.read()
        for y in range(1,6):
            new_file = file.split('.')[0] + f'_aug{y}.txt'
            new_filename = os.path.join(path, new_file)
            with open(new_filename, 'w') as output_file:
                output_file.write(contents)
    print('Done')

