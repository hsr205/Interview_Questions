class Side:
    BUY = 1
    SELL = 2


# Create the custom exception
class NegativeBalanceError:
    pass

# Create the class TradeManager
# By default the init value for the balance will be 1000

class TradeManager:

    # create the constructor
    def __init__(self):
        pass

    # create handle_transaction
    def handle_transaction(self):
        pass
    # create update_balance
    def update_balance(self):
        pass
    # create update_pnl
    def update_pnl(self):
        pass
    # create update_position
    def update_postion(self):
        pass
    # create repr_position
    def repr_positon(self):
        pass
    # create repr_pnl
    def repr_pnl(self):
        pass
    # create repr_balance
    def repr_balance(self):
        pass
    # create set_balance
    def set_balance(self):
        pass

    # you will certainly need to overload a built-in function
    # # Probably the toString() method but could be wrong

def test_position_1():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    t2={'quantity' : 100, 'price' : 1.3, 'side' : Side.SELL, 'symbol' : 'USD/CAD'}
    tm1.update_position(t1)
    tm1.update_position(t2)
    print(tm1.repr_position())

def test_position_2():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    t2={'quantity' : 100, 'price' : 1.3, 'side' : Side.SELL, 'symbol' : 'EUR/USD'}
    tm1.update_position(t1)
    tm1.update_position(t2)
    print(tm1.repr_position())

def test_pnl_1():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    t2={'quantity' : 100, 'price' : 1.3, 'side' : Side.SELL, 'symbol' : 'EUR/USD'}
    tm1.update_pnl(t1)
    tm1.update_pnl(t2)
    print(tm1.repr_pnl())

def test_pnl_2():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    tm1.update_pnl(t1)
    print(tm1.repr_pnl())

def test_balance_1():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    tm1.update_balance(t1)
    print(tm1.repr_balance())

def test_balance_2():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    t2={'quantity' : 100, 'price' : 1.3, 'side' : Side.SELL, 'symbol' : 'EUR/USD'}
    tm1.update_balance(t1)
    tm1.update_balance(t2)
    print(tm1.repr_balance())

def test_balance_3():
    tm1=TradeManager()
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    tm1.update_balance(t1)
    print(tm1.repr_balance())


def test_transaction_1():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    t2={'quantity' : 100, 'price' : 1.3, 'side' : Side.SELL, 'symbol' : 'EUR/USD'}
    tm1.handle_transaction(t1)
    tm1.handle_transaction(t2)
    print(tm1)

def test_transaction_2():
    tm1=TradeManager(100000)
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    t2={'quantity' : 100, 'price' : 1.3, 'side' : Side.SELL, 'symbol' : 'EUR/USD'}
    t3 = {'quantity': 1000, 'price': 1.1, 'side': Side.BUY, 'symbol': 'USD/CAD'}
    t4 = {'quantity': 1000, 'price': 1.4, 'side': Side.SELL, 'symbol': 'USD/CAD'}

    tm1.handle_transaction(t1)
    tm1.handle_transaction(t2)
    tm1.handle_transaction(t3)
    tm1.handle_transaction(t4)

    print(tm1)

def test_balance_4():
    tm1=TradeManager()
    t1={'quantity' : 100, 'price' : 1.2, 'side' : Side.BUY, 'symbol' : 'EUR/USD'}
    tm1.update_balance(t1)
    tm1.set_balance(123)
    print(tm1.repr_balance())
    try:
        tm1.set_balance(-123)
    except NegativeBalanceError as e:
        print(e)


if __name__ == '__main__':
    func_name = input().strip()
    globals()[func_name]()
