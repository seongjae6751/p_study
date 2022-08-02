# Chapter04-02
# 시퀀스형
# 컨테이너(container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형(str, bytes, bytearray, array.array, memorryview))
# 가변(list, bytearray, array.array, memorryview)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpaking

# b, a = a, b

print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x, y, rest)
x, y, i, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

# Mutable(가변) vs Imutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))

print()
print()

# sort vs sorted
# reverse, key = en, key = str.Lower, key = func.....

# sorted : 정렬 후 새로운 객체 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse = True))
print('sorted - ', sorted(f_list, key = len))
print('sorted - ', sorted(f_list, key=lambda x : x[-1])) # x[-1] 끝에 글자 기준으로 정렬
print('sorted - ', sorted(f_list, key=lambda x : x[-1], reverse = True))

print('sorted - ', f_list)

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse = True), f_list)
print('sort - ', f_list.sort(key = len), f_list)
print('sort - ', f_list.sort(key = lambda x : x[-1]), f_list)
print('sort - ', f_list.sort(key = lambda x : x[-1], reverse = True), f_list)

# List vs Array 적합 한 사용법
# 리스트 기반(List) : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반(Array) : 배열(리스트와 거의 호환)







