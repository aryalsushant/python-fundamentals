class Pizza:
    def _init_(self, size, toppings=None):
        #building a pizza of specified size and toppings
        self.size = size
        self.toppings = set()
        if toppings is not none:
            for topping in toppings:
                self.toppings.add(topping)

    def price(self):
        #calculating price of pizza based on size and toppings
        base_price ={'Small': 10.0, 'Medium': 12.0, 'Large': 14.0}
        p = base_price[self.size]
        for topping in self.toppings:
            p += 0.50
        return p
    

my_pizza = Pizza('Large', {'Garlic','Pepperoni'})
your_pizza = Pizza('Medium', {'Tomato', 'Avocado', 'chocolate'})

your_pizza.price()





