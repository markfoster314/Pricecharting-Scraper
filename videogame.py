class VideoGame:
    def __init__(self, title, console, loose_price, complete_price, new_price):
        self.title = title
        self.console = console
        self.loose_price = loose_price
        self.complete_price = complete_price
        self.new_price = new_price

    def getTitle(self):
        return self.title

    def getConsole(self):
        return self.console

    def getLoosePrice(self):
        return self.loose_price

    def getCompletePrice(self):
        return self.complete_price

    def getNewPrice(self):
        return self.new_price

    def __repr__(self):
        return (
            f"Title: {self.title}\n"
            f"Console: {self.console}\n"
            f"Loose: ${self.loose_price}\n"
            f"Complete: ${self.complete_price}\n"
            f"New: ${self.new_price}\n"
        )
