class 사람:
    def __init__(self, 이름):
        self.이름 = 이름
        print('안녕하세요.')
    def 작별인사(self):
        print(f'{self.이름} 안녕히 가세요.')

person1 = 사람("홍길동")
person1.작별인사()


class 자식(사람):
    def __init__(self, 이름, 나이):
        super().__init__(이름)
        self.나이 = 나이
        print(f'{self.나이}살이에요.')

child1 = 자식("홍길동", 20)