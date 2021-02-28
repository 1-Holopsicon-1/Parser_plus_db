import sqlite3

def main():
    sc = sqlite3.connect('data.sqlite')
    cursor = sc.cursor()
    sc.close()
if __name__ == '__main__':
    main()

