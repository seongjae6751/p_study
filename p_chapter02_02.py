# Chapter02-02
# 객체 지향 프로그래밍(OOD) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그래밍) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : SeongJae
    Date:2022.04.28
    """

    # 클래스 변수(모든 인스턴스가 굥유)
    car_count = 0


    def __init__(self, company, details):
        self._company_ = company
        self._details_ = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company_, self._details_)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company_, self._details_)

    def __del__(self):
        print('del?')
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'. format(id(self)))
        print('Car Detail Info : {} {}'. format(self._company_, self._details_.get('price')))

# Self 의미
car1 = Car('Ferrari', {'color' : 'White','horsepower' : 400,'price' : 8000})
car2 = Car('Bmw', {'color' : 'Black','horsepower' : 270,'price' : 5000})
car3 = Car('Audi', {'color' : 'Silver','horsepower' : 300,'price' : 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company_ == car2._company_)
print(car1 is car2)

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring
print(Car.__doc__)
print()

# 실행
car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)

# 에러
# Car.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

# 공유 확인
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))



















