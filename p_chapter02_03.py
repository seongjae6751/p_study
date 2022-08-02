# Chapter02-01
# 객체 지향 프로그래밍(OOD) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그래밍) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : SeongJae
    Date:2022.04.28
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 굥유)
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)


    # Instance Method
    def get_price(self):
        return 'Before Car price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # Class Method
    @classmethod
    def raise_price(cls, per):
        cls.price_per_raise
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased!')

    # Static Method
    @staticmethod # 클래스의 속성이나 함수를 이용하지 않을때 사용?
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'Ok! This car is {}'.format(inst._company)
        return 'Sorry. This car is not Bmw'

    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'. format(id(self)))
        print('Car Detail Info : {} {}'. format(self._company, self._details.get('price')))

# Self 의미
car1 = Car('Ferrari', {'color' : 'White','horsepower' : 400,'price' : 8000})
car2 = Car('Bmw', {'color' : 'Black','horsepower' : 270,'price' : 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보 -> 이런식으로 직접 가져오는거 좋지 않음
print(car1._details.get("price"))
print(car2._details['price'])

# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 인스턴스 호출(스테이틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

# 클래스 호출(스테이틱)
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))