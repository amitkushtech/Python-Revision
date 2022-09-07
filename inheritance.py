class Hotel:
    def __init__(self, name, address, totalfloor):
        self.name = name
        self.address = address
        self.totalfloor = totalfloor

    def star(self, star):
        print("The hotel is ", star, " star.")


class Room(Hotel):
    def __init__(self, room, name, address, totalfloor):
        Hotel.__init__(self, name, address, totalfloor)
        self.totalroom = room

    def price(self):
        print("The price is 5000")


rm = Room(23, "Elite", "KTM", 12)
print(rm.totalroom)
print(
    "The hotel name is ",
    rm.name,
    " total floor ",
    rm.totalfloor,
    " and address is",
    rm.address,
)
rm.price()
rm.star(4)


# rm.Hotel("High 5", "KTM", 34)
# rm.star(4)
