class AcceptablePrice:
    def __init__(self, tomato, cucumber):
        self.tomato = tomato
        self.cucumber = cucumber

    @staticmethod
    def full_price_check(price: int):
        if price > 10000:
            print('Please, describe the purchase and its purpose!')
        else:
            print('The price is available!')

    @classmethod
    def count_sale_price(cls, initial_tom_price, tom_sale, initial_cuc_price, cuc_sale):
        tomato = initial_tom_price * tom_sale / 100
        cucumber = initial_cuc_price * cuc_sale / 100
        return cls(tomato, cucumber)

    def calculate(self):
        if self.cucumber < 100:
            print('Cucumber price is available)')
        else:
            print('Cucumber price is not available(')
        if self.tomato < 150:
            print('Tomato price is available)')
        else:
            print('Tomato price is not available(')

def buy_or_not(manufacture_date: float):
    if manufacture_date > 03.12:
        class Buy():
            print('Buy!')
    else:
        class DontBuy():
            print('Dont buy!')

AcceptablePrice.full_price_check(555)
check_1 = AcceptablePrice.count_sale_price(350, 50, 100, 20)
check_1.calculate()
buy_or_not(01.02)
