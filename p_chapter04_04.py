# Chapter04-02
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소르로 많은 데이터를 관리
# Dict -> key 중복 허용x, Set -> 중복 허용x
# Dict 및 Set 심화

# imutable Dict

from types import MappingProxyType
d = {'key1' : 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 불가
# d_frozen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'value2'
print(d)

print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')

print(s1)

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis
print('-------')
print(dis('{10}'))
print('-------')
print(dis('set(10)'))

# 지능형 집합(Comprehending Set)

print('-------')

from unicodedata import name

print({name(chr(i), '') for i in range(0,256)})

