# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def a_ski(character):
    # Use a breakpoint in the code line below to debug your script.
    print(chr(character), end='')  # Press Ctrl+F8 to toggle the breakpoint.


def read_fichier(name):
    fichier = open(name, 'r')
    for line in fichier:
        for word in line.split():
            a_ski(int(word))
    fichier.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_fichier('enigmes\Enigme1.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
