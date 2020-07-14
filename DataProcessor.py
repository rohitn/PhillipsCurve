def load_data():

    f = open('data/data.csv')

    # create empty list
    inflation = []
    unemployment = []

    # infinite loop
    while True:
        # read a single line from file
        line = f.readline()
        # stops when the content is empty
        if len(line) == 0:
            break
        # split line by ','
        [inf, unemp] = line.split(',')
        # cast to float and append to the list
        inflation.append(float(inf))
        unemployment.append(float(unemp))

    # closes the file
    f.close()

    return inflation, unemployment

if __name__ == '__main__':
    inflation, unemployment = load_data()