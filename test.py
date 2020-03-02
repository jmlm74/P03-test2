# Created by jmlm at 20/02/2020-14:39 - test2
from models.map import Map
from models.position import Position
from models.hero import Hero
# to use : pytest test.py -v -s



def test_1():
    map = Map("ressource/map01.txt")
    assert len(map.start) == 1
    assert len(map.goal) == 1
    toto = Hero(map)
    toto.position = map.start[0]
    assert toto.position.getx == 0
    assert toto.position.gety == 0
    toto.move('left')  # outside the map
    assert toto.position.getx == 0
    assert toto.position.gety == 0
    toto.move('up')  # outside the map
    assert toto.position.getx == 0
    assert toto.position.gety == 0
    toto.move('right')  # in the wall
    assert toto.position.getx == 0
    assert toto.position.gety == 0
    toto.move('down')  # OK
    assert toto.position.getx == 1   # new x
    assert toto.position.gety == 0

    map.items.append(Position(5, 5))  # put an Item in the list
    len_items = len(map.items)
    toto.position = Position(4, 5)  # put the hero near the item
    toto.move('down')  # move onto the new items
    print('coucou {}'.format(toto.position))
    assert len_items == len(map.items) + 1  # the item  has been removed from the list


