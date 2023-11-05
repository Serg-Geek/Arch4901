from abc import ABC, abstractmethod
from random import randint, random




class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class Silver(IGameItem):
    def open(self):
        print('Silver!')


class Bronze(IGameItem):
    def open(self):
        print('Bronze!')


class Platinum(IGameItem):
    def open(self):
        print('Platinum!')


class Titanium(IGameItem):
    def open(self):
        print('Titanium!')


class Iron(IGameItem):
    def open(self):
        print("Iron")


class Bitcoin:
    def open(self):
        print("Bitcoin!!!")


class IronGenerator(ItemFabric):
    def create_item(self):
        return Iron()


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()


class TitaniumGenerator(ItemFabric):
    def create_item(self):
        return Titanium()

class PlatinumGenerator(ItemFabric):
    def create_item(self):
        return Titanium()


class BitcoinGenerator(ItemFabric):
    def create_item(self):
        return Bitcoin()


if __name__ == '__main__':
    rewards = [GoldGenerator(), GemGenerator(), SilverGenerator(), IronGenerator()]
    gem_count = 0
    gold_count = 0
    sil_count = 0
    iron_count = 0
    titan_count = 0
    bitcoin_count = 0
    platinum_count = 0
    for i in range(100):
        num = randint(0,100)
        if num <= 1:
            reward = GemGenerator().create_item()
            gem_count += 1
        elif 1 < num <= 3:
            reward = GoldGenerator().create_item()
            gold_count += 1
        elif 3 < num <= 19:
            reward = SilverGenerator().create_item()
            sil_count += 1
        elif 19 < num <= 42:
            reward = TitaniumGenerator().create_item()
            titan_count += 1
        elif 42 < num <= 61:
            reward = BitcoinGenerator().create_item()
            bitcoin_count += 1
        elif 61 < num <= 80:
            reward = PlatinumGenerator().create_item()
            platinum_count += 1

        else:
            reward = IronGenerator().create_item()
            iron_count += 1
        reward.open()
    print(f'gem выпало = {gem_count}, \n'
          f'gold выпало = {gold_count},\n'
          f'silver выпало =  {sil_count},\n'
          f'iron выпало = {iron_count}\n'
          f'bitcoin выпало = {bitcoin_count}\n'
          f'titanium выпало = {titan_count}\n'
          f'platinum выпало = {platinum_count}')
