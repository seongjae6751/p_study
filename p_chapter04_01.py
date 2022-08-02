# Chapter04-01
# 시퀀스형
# 컨테이너(container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형(str, bytes, bytearray, array.array, memorryview))
# 가변(list, bytearray, array.array, memorryview)
# 불변(tuple, str, bytes)

# 지능형 리스트(Comprehending lists)
chars = '+-)(*&^%$#@!'
code_lists1 = []

for s in chars:
    # 유니코드 리스트
    code_lists1.append(ord(s))

print(code_lists1)

# Comprehending Lists -> append로 넣는거보다 속도 우세
code_lists2 = [ord(s) for s in chars]

print(code_lists2)

# Comprehending lists = Map , Filter
code_lists3 = [ord(s) for s in chars if ord(s) > 40]
code_lists4 = list(filter(lambda x: x >40, map(ord, chars)))

print(code_lists1)
print(code_lists2)
print(code_lists3)
print(code_lists4)
print([chr(s) for s in code_lists1])
print([chr(s) for s in code_lists2])
print([chr(s) for s in code_lists3])
print([chr(s) for s in code_lists4])

print()
print()

# Generator 생성 -> 연속된 값을 사용할때 메모리 사용을 줄여줌
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars) # 제너레이터는 []이 아니라 ()
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist()) # array를 리스트로 변환

print()
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()

# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)


# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])
