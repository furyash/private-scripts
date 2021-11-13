import os
filenames = next(os.walk("."), (None, None, []))[2]
filenames = [x for x in filenames if x[0] == 'l']

file = open('contents.txt', 'r+')
new_filenames = []
for line in file:
    new_filenames.append(line[:-1] + ".mp4")
print(new_filenames)

for i in range(79):
    if os.path.isfile(new_filenames[i]):
        print(new_filenames[i] + " already exists.")
    os.rename(filenames[i], new_filenames[i])
