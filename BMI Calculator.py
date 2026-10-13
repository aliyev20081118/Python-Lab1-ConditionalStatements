a='y'
while a=='y':
      m=float(input('Enter weight: '))
      if m<=0:
            print('please,enter correct weight.')
            continue
      h=float(input('Enter height: '))
      if h<=0:
            print('please,enter correct height.')
            continue
      BMI=m/(h**2)
      if BMI<18.5:
           c='Underweight'
      elif BMI>=18.5 and BMI<25.0:
           c='Normal Weight'
      elif BMI>=25.0 and BMI<30.0:
           c='Overweight'
      else:
           c='Obese'
      print('BMI:',BMI)
      print('Category:',c)
      a=input('Do you want calculate again? (y/n): ')

      
