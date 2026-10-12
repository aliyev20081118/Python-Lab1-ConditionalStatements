c='y'
while c=='y':
    a=int(input('Enter your year: '))
    if a>2026 or a<1900:
        print("Please, enter correct year!!")
        continue
    z=['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep']
    b=a%12
    print('Your Chinese Zodiac sign is:',z[b])
    ans=input('Do you want check your Chinese Zodiac sign? (y/n): ')

    
