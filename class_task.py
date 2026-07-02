

class iphoneclass:

    def __init__(self, model, price, version):
        self.model = model
        self.price = price
        self.version = version

    def Model(self):
        return self.model

    def Price(self):
        return self.price

    def Version(self):
        return self.version

    def Overall(self):
        return f"Model: {self.model}, Price: {self.price}, Version: {self.version}"


iphone = iphoneclass("iPhone 15 Pro", "₹1,34,900", "iOS 18")

print(iphone.Overall())