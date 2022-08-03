from collections import defaultdict
from dataclasses import dataclass, field


def main():
    order = TradingStrategy(quantity=1, price=10, side='buy')
    order2 = TradingStrategy(quantity=5, price=50, side='sell')
    order3 = TradingStrategy(quantity=10, price=100, side='buy')

    order_struct = OrderStruct(quantity=order.quantity, price=order.price, side=order.side)

    print(order_struct)

    # test_add_method = order_struct.add_to_dict(order2)
    # test_add_method2 = order_struct.add_to_dict(order3)
    # print(test_add_method2)

    # test_list = [order, order2, order3]
    # test_dict = {}
    # test_keys = [1, 2, 3]
    #
    # for i in range(len(test_keys)):
    #     test_dict[test_keys[i]] = test_list[i]
    #
    # print(test_dict)

    # order_manager = OrderManager(order)
    # print(f'orders: {order_manager.handle_order_from_ts()}')
    # print(f'orders: {order_manager.add_order(order2)}')
    # print(f'orders: {order_manager.add_order(order3)}')


@dataclass
class TradingStrategy:
    quantity: int
    price: int
    side: str


@dataclass()
class OrderStruct:
    quantity: int
    price: int
    side: str
    order_id: int = 1
    state: str = 'new'

    @property
    def get_dict(self) -> dict:
        result = {self.order_id: [self.quantity, self.price, self.side, self.state]}
        return result

    # def add_to_dict(self, order):
    #     # result = self.get_dict
    #     result = {}
    #     order_id = self.order_id + 1
    #     result.update({order_id: [order.quantity, order.price, order.side, self.state]})
    #     return result


@dataclass
class OrderManager:
    trading_strategy: TradingStrategy
    test_dict: dict = field(default_factory=dict)
    # order_id: int = 1
    state: str = 'new'

    def handle_order_from_ts(self) -> dict:
        orders_dict = self.create_orders_dict(order_id=self.get_order_id, trading_strategy=self.trading_strategy)
        return orders_dict

    def create_orders_dict(self, order_id: int, trading_strategy: TradingStrategy) -> dict:
        self.test_dict = {order_id: [trading_strategy.quantity,
                                     trading_strategy.side,
                                     trading_strategy.price,
                                     self.state]}
        return self.test_dict

    def add_order(self, trading_strategy: TradingStrategy) -> dict:
        orders_dict = self.handle_order_from_ts()
        order_id = self.get_order_id + 1
        orders_dict.update({order_id: [trading_strategy.quantity,
                                       trading_strategy.side,
                                       trading_strategy.price,
                                       self.state]})
        return orders_dict

    @property
    def get_order_id(self):
        return 1

    def handle_order_from_market(self, order):
        return


if __name__ == '__main__':
    main()
