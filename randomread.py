def main():
    readrandom = True
    while(readrandom):
        while(True):
            try:
                randomread = open('randomnum.txt', 'r') #handle exceptions
                print("List of random numbers in randomnum.txt: ")
                print(randomread.read())
                count = 0
                for line in open('randomnum.txt', 'r'): #why doesn't it work if I put for line in randomread?
                    count = count + 1
                print("Random number count:", count)
                randomread.close()
                break
            except FileNotFoundError:
                print("You need a randomnum.txt file to run this program.")
                break
            else:
                break
        break

main()
