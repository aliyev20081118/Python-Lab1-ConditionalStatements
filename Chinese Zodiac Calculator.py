ans='y'
while ans=='y':
    a=int(input('Enter your year: '))
    z=['Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep']
    b=a%12
    print('Your Chinese Zodiac sign is:',z[b])
    ans=input('Do you want check your Chinese Zodiac sign? (y/n): ')

