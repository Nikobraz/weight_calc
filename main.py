sex = input('Введите пол(1 - мужской, 2 - женский): ')
height = input('Введите рост в сантиметрах: ')

if sex == '1':
  base_weight = 50.0
  increment_weight = 2.45
elif sex == '2':
  base_weight = 45.0
  increment_weight = 2.3
else:
  print('Используются параметры по умолчанию(Пол: м, Рост: 186)')
  base_weight = 50.0
  increment_weight = 2.45
  height = 186.0

weight = round(((float(height) - 152.4)/2.54*increment_weight) + base_weight, 2)
sprint_weight = weight-weight*2.5/100
barrier_weight = weight-weight*6/100
middle_weight = weight-weight*12/100
long_weight = weight-weight*15/100
print('Идеальный вес обычного человека: ' + str(weight))
print('Идеальный вес спринтера: ' + str(round(sprint_weight, 2)))
print('Идеальный вес барьерщика: ' + str(round(barrier_weight, 2)))
print('Идеальный вес бегуна на средние дистанции: ' + str(round(middle_weight, 2)))
print('Идеальный вес марафонца: ' + str(round(long_weight, 2)))
input('Press Enter to exit')
