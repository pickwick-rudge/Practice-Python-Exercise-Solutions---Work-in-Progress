'''Exercise 22: Read from File

This little program reads a .txt file and then counts instances of each name in
the file, and then prints the results to the screen'''

def main():
    names_list = [] #Initialize an empty list and empty counter variables for the names
    darthcount = 0
    lukecount = 0
    leacount = 0

    #'with open' is more efficient because it doesn't require a .close() function, and it takes up fewer lines
    with open('nameslist.txt', 'r') as open_file:
        for name in open_file:
            name = name.rstrip() #Unless an argument is passed into rstrip(), it defaults to eliminating whitespace
            if name not in names_list:
                names_list.append(name)

            if name == 'Darth':
                darthcount += 1
            elif name == 'Luke':
                lukecount += 1
            elif name == 'Lea':
                leacount += 1

    print(names_list)
    print('darthcount =', darthcount, 'lukecount =', lukecount, 'leacount = ', leacount)

if __name__ == '__main__':
    main()
