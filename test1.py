import os

folderPath = 'F:\MTU\PythonScripts\AILabs\MLLabs\imdb_data\data\\trainSmall\pos'
listing = os.listdir(folderPath)

# Loop through all the files in the folder and collect the words of all files
for file in listing:
    # open file for reading
    f = open(folderPath + '\\' + file, "r", encoding="utf8")

    # read file and split the contents
    allWords = f.read().split()

    wordCount = len(allWords)

    print('Word Count in file: ', file, ' is :', wordCount)

    # close the file
    f.close()
