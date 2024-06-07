class Auction:
    def __init__(self):
        self.item = 2025
        self.highest_bid = 0
        self.highest_bidder = None

    def place_bid(self, username, bid):
        if bid > self.highest_bid:
            self.highest_bid = bid
            self.highest_bidder = username
            return True
        return False
