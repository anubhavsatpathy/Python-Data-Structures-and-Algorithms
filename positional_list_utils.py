import positional_list_adt
import random

class CardHand:

    class _Card:

        __slots__ = "_suit","_number"

        def __init__(self, suit, number):

            self._suit = suit
            self._number = number

    def __init__(self):

        self._hand = positional_list_adt.PositionalList()
        self._suit_markers = {
            "diamonds" : None,
            "hearts" : None,
            "spades" : None,
            "clubs" : None
        }
        self._suit_counts = {
            "diamonds": 0,
            "hearts": 0,
            "spades": 0,
            "clubs": 0
        }

    def add_card(self,suit, number):

        if self._suit_markers[suit.lower()] == None:
            pos = self._hand.add_last(self._Card(suit,number))
            self._suit_markers[suit.lower()] = pos
            self._suit_counts[suit.lower()] += 1
        else:
            pos = self._hand.add_after(self._Card(suit,number),self._suit_markers[suit.lower()])
            self._suit_markers[suit.lower()] = pos
            self._suit_counts[suit.lower()] += 1

    def find_pos(self, suit, number):

        walk =self._hand.first()

        while walk != None and walk.element()._suit != suit and walk.element()._number !=number:
            walk = self._hand.after(walk)

        return walk

    def play_card(self,suit,number):
        pos = self.find_pos(suit, number)

        if pos == None:
            raise ValueError("This card is not in this hand")
        else:
            if self._suit_counts[suit.lower()] == 1:
                self._suit_markers[suit.lower()] = None
                self._hand.delete(pos)
            else:
                self._hand.delete(pos)

    def __iter__(self):

        for i in self._hand:
            yield (i._suit,i._number)

    def all_of_suit(self, suit):

        walk = self._suit_markers[suit.lower()]
        for i in range(self._suit_counts[suit.lower()]):
            yield (walk.element()._suit,walk.element()._number)
            walk = self._hand.before(walk)

class FavoritesList:

    class _Song:

        __slots__ = "_name","_id","_count"

        def __init__(self, name, identifier, count = 1):

            self._name = name
            self._id = identifier
            self._count = count

        def __str__(self):

            return self._name

    def __init__(self):

        self._fav_list = positional_list_adt.PositionalList()

    def __len__(self):

        return len(self._fav_list)

    def find_pos(self,identifier):

        walk = self._fav_list.first()

        while walk != None and walk.element()._id != identifier:
            walk = self._fav_list.after(walk)

        return walk

    def move_up(self,position):

        if position != self._fav_list.first():
            walk = self._fav_list.before(position)
            if position.element()._count > walk.element()._count:
                while walk != self._fav_list.first() and self._fav_list.before(walk).element()._count < position.element()._count:
                    walk = self._fav_list.before(walk)
                self._fav_list.add_before(position.element(),walk)
                self._fav_list.delete(position)


    def access(self, identifier, name):

        p = self.find_pos(identifier)
        if p == None:
            self._fav_list.add_last(self._Song(name, identifier))
        else:
            p.element()._count+=1
            self.move_up(p)

    def top_k(self,k):

        if k <= 0 or k > len(self):
            raise ValueError("k should be in the range [1,len(favourites)")
        else:
            walk = self._fav_list.first()
            for i in range(k):
                yield (walk.element()._name,walk.element()._count)
                walk = self._fav_list.after(walk)

    def remove(self, identifier):

        position = self.find_pos(identifier)
        if position == None:
            raise ValueError("No such song found in favorites")
        else:
            self._fav_list.delete(position)

    def __str__(self):

        if len(self) == 0:
            return ""
        else:
            return "".join(str(self._fav_list))




if __name__ == "__main__":

    playlist =[
        "Wish you were here",
        "High Hopes",
        "Hey You",
        "Dream On",
        "Crazy",
        "Hysteria",
        "When Love and Hate Collide",
        "Dazed and Confused",
        "Since Ive been loving you",
        "Kashmir",
        "Black Dog",
        "Stairway to heaven",
        "Hotel Carlifornia",
        "Love will keep us alive",
        "November Rain"
    ]

    favs = FavoritesList()

    for i in range(1000):
        name = random.choice(playlist)
        identifier = playlist.index(name)
        favs.access(identifier, name)

    for i in favs.top_k(10):
        print(i)

    print("_____________________________________________________________________________________________")

    h = CardHand()

    suits = ["diamonds", "hearts", "spades", "clubs"]
    hand = []
    for i in range(10):
        suit = random.choice(suits)
        number = random.randint(1,13)
        if (suit,number) not in hand:
            h.add_card(suit,number)
            hand.append((suit,number))

    for k in h:
        print(k)

    hand = [i for i in h]

    for j in range(5):
        card = random.choice(hand)
        print("Played" + str(card))
        h.play_card(card[0],card[1])

    for k in h:
        print(k)

    diamonds = [k for k in h.all_of_suit("diamonds")]
    print(diamonds)







