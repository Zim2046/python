class User():
    def __init__(self, height, weight, name, birthday) -> None:
        self.height = height
        self.weight = weight
        self.name = name
        self.birthday = birthday

    # Methods
    def say_hello(self):
        print(f'Hello, my name is Joe!')


joe = User(72, 220, "Joe", "3/3/90")
mary = User(66, 130, "Mary", "4/5/88")

print(joe)
