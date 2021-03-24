# Q - quality; KT - kids ticket; TT - teenagers ticket; AT - adults ticket; T - total.

print('Сколько билетов желаете приобрести?')
Q = int(input())
print('Пожалуйста,уточните количество детей младше 18 лет')
KT = int(input())
print('Пожалуйста, уточните количество подростоков от 18 до 25 лет')
TT = int(input())
print('Пожалуйста, уточните количество взрослых ')
AT = int(input())
Q = KT+TT+AT
if Q > 3:
    T = 0.9*(KT*0+TT*990+AT*1390)
    print('Итого к оплате', T, 'руб.')
else:
    T = KT*0+TT*990+AT*1390
    print('Итого к оплате', T, 'руб.')