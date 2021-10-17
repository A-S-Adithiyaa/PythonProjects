import random


date = ["1/2/2003", "13/2/2003", "31/12/2009", "12/7/2020", "1/11/2002", "11/5/2018", "4/4/2016"]
job = ["a Police", "a CBI", "an Employee", "a Postman", "a Teacher", "a Businessman", "a Robber"]
name = ["Liam", "Noah", "Oliver", "Olivia", "Emma", "Ava", "Sophia"]
another_name = ["Amelia", "Isabella", "Mia", "Elijah", "William", "James", "Benjamin"]
place = ["Tokyo, Japan", "Delhi, India", "Shanghai, China", "Sao Paulo, Brazil", "Beijing, China", "Mumbai, India", "Osaka, Japan"]

print("It was on " + random.choice(date) + ", that " + random.choice(job) + " named " + random.choice(name) + ", saw " + random.choice(another_name) + " stealing a valuable gem, soon the officials of " + random.choice(place) + " was contacted and the gem was returned to its original owner.")