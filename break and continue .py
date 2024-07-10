for i in range (12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i , "=", 5 * i)


count = 0

while count <= 100:
    print (count)
    count += 1
    if count == 3:
        break


#simalirly we can use the continue in place of break
