import os
# import old file names
filenames = os.listdir(".")
filenames = [x for x in filenames if x[0] == 'l']
#import new file names
file = open('contents.txt', 'r+')
new_filenames = []
for line in file:
    new_filenames.append(line[:-1] + ".mp4")
# rename it
for i in range(79):
    if os.path.isfile(new_filenames[i]):
        print(new_filenames[i] + " already exists.")
    os.rename(filenames[i], new_filenames[i])
