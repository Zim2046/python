SELECT * FROM burgers_schema.burgers;
SELECT * FROM burgers_schema.restaurants;
INSERT INTO restaurants (name)
VALUES ("Happy Time Burgers"), 
("Fun Time Burgers"),
("What did I just Eat");

INSERT INTO burgers (name, bun, meat, calories, restaurant_id)
VALUES ("The destroyer", "Sesame Seed", "Mystery", 1400, 3),
("Tofu Delight", "Pretzel", "Tofu", 300, 2),
("Creamy Chicken", "Lettuce", "Creamed Chicken", 1000, 2),
("Gut Buster", "Crispy Ramen Noodles", "Spicey Beef", 700, 3),
("The Omen", "Fire", "Turkey", 400, 2),
("The TeurDucken", "White Bread", "Turkey and Duck", 1500, 2);

SELECT * FROM restaurants
LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id
WHERE restaurants.id = 1;