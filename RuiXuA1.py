"""
Replace the contents of this module docstring with your own details
Name: Rui Xu
Date started: 10/12/2020
GitHub URL: https://github.com/LuxDRK/RuiXuA1
"""

in_file = open("movies.csv", "r+")
movie_list = [data.split(",") for data in in_file]
movie_data = movie_list
for i in range (0,len(movie_list)):
    movie_data[i][1] = int(movie_data[i][1])
    if movie_data[i][3] == 'u\n':
        movie_data[i][3] = 'u'
    elif movie_data[i][3] == 'w\n':
        movie_data[i][3] = 'w'
movie_data = sorted(movie_data, key=lambda x: (x[1], x[0]))
in_file.close()

def menu():
    print("Menu:")
    print("L - List movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")
    menu_choose = input(">>> ")
    if menu_choose in ['L','l','A','a','W','w','Q','q']:
        menu_choose = menu_choose.lower()
    else:
        print("Invalid menu choice")
        menu()
    if menu_choose == 'l':
        list(movie_data)
    elif menu_choose == 'a':
        add()
    elif menu_choose == 'w':
        unwatched = 0
        for i in range(0, len(movie_data)):
            if movie_data[i][3] in ['u']:
                unwatched = unwatched + 1
        if unwatched == 0:
            print('No more movies to watch!')
            menu()
        else:
            print('Enter the number of a movie to mark as watched')
            watch(movie_data)
    elif menu_choose == 'q':
        out_print(movie_data)

def length_check(column):
    var_length = 0
    for i in range (0,len(movie_data)):
        if len(movie_data[i][column]) > var_length:
            var_length = len(movie_data[i][column])
    return var_length

def list(movie_data):
    movie_data = sorted(movie_data, key=lambda x: (x[1], x[0]))
    unwatched = 0
    for i in range (0,len(movie_data)):
        xxx = " "
        if movie_data[i][3] in ['u','u\n']:
            xxx = "*"
            unwatched = unwatched + 1
        print(" {}. {} {:{}} - {:4} ({})".format(i,xxx,movie_data[i][0],length_check(0),movie_data[i][1],movie_data[i][2]))
    print("{} movies watched, {} movies still to watch".format(len(movie_data)-unwatched,unwatched))
    menu()

def watch(movie_data):
    movie_data = sorted(movie_data, key=lambda x: (x[1], x[0]))
    movie_watch = input('>>> ')
    if movie_watch.lstrip('-').isdigit() is True:
        if int(movie_watch) < 0:
            print('Number must be >= 0')
            watch(movie_data)
        elif int(movie_watch) >= len(movie_data):
            print('Invalid movie number')
            watch(movie_data)
        else:
            if movie_data[int(movie_watch)][3] in ['u','u\n']:
                print('{} from {} watched'.format(movie_data[int(movie_watch)][0],movie_data[int(movie_watch)][1]))
                movie_data[int(movie_watch)][3] = 'w'
            else:
                print('You have already watched {}'.format(movie_data[int(movie_watch)][0]))
    else:
        print('Invalid input; enter a valid number')
        watch(movie_data)
    menu()

def title():
    add_title = input('Title: ')
    while add_title == '' or add_title.isspace():
        add_title = input('Input can not be blank\nTitle: ')
    return add_title

def year():
    add_year = input('Year: ')
    tag = False
    while tag is False:
        if add_year.lstrip('-').isdigit() is True:
            if int(add_year) < 0:
                add_year = input('Number must be >= 0\nYear: ')
            else:
                tag = True
        else:
            add_year = input('Invalid input; enter a valid number\nYear: ')
    return add_year

def category():
        add_category = input('Category: ')
        while add_category == '' or add_category.isspace():
            add_category = input('Input can not be blank\nCategory: ')
        return add_category

def add():
    movie_add=[]
    movie_add.append(title())
    movie_add.append(int(year()))
    movie_add.append(category())
    movie_add.append('u')
    print('{} ({} from {}) added to movie list'.format(movie_add[0],movie_add[2],movie_add[1]))
    movie_data.append(movie_add)
    menu()

def out_print(movie_data):
    movie_data = sorted(movie_data, key=lambda x: (x[1], x[0]))
    out_file = open("movies.csv","w+")
    for i in range (0,len(movie_data)):
        for j in range (0,3):
            print('{},'.format(movie_data[i][j]), end="", file=out_file)
        if i == len(movie_data)-1:
            print(format(movie_data[i][3]), end="", file=out_file)
        else:
            print('{}'.format(movie_data[i][3]), file=out_file)
    print('{} movies saved to movies.csv\nHave a nice day :)'.format(len(movie_data)))
    out_file.close()

def main():
    print("Movies To Watch 1.0 - by <Rui Xu>")
    print(len(movie_data),"movies loaded")
    menu()

main()