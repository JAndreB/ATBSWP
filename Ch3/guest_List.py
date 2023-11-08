guests = ['Michail Bakunin', 'Norbert Weiner', 'Stafford Beer']

print(f"Hello {guests[0].title()}, would you like to come to dinner?")
print(f"Hello {guests[1].title()}, would you like to come to dinner?")
print(f"Hello {guests[2].title()}, would you like to come to dinner?")

print(f"Apparently {guests[1].title()} cannot make it...")
guests[1] = "Iain M. Banks"

print(f"Hello {guests[0].title()}, would you like to come to dinner?")
print(f"Hello {guests[1].title()}, would you like to come to dinner?")
print(f"Hello {guests[2].title()}, would you like to come to dinner?")

print(f"Thank you all for responding, I have found a bigger table and therefore will be inviting more guests!")

guests.insert(0, "Lucy Parsons")
guests.insert(1, "Lula")
guests.append("Vrollint")

print(f"Hello {guests[0].title()}, would you like to come to dinner?")
print(f"Hello {guests[1].title()}, would you like to come to dinner?")
print(f"Hello {guests[2].title()}, would you like to come to dinner?")
print(f"Hello {guests[3].title()}, would you like to come to dinner?")
print(f"Hello {guests[4].title()}, would you like to come to dinner?")
print(f"Hello {guests[5].title()}, would you like to come to dinner?")

print("Unfortunatley the table will not be here in time some of you cannot come")
popped = guests.pop()
print(f"Unfortunately {popped.title()} will not be able to attend.")
popped = guests.pop()
print(f"Unfortunately {popped.title()} will not be able to attend.")
popped = guests.pop()
print(f"Unfortunately {popped.title()} will not be able to attend.")
popped = guests.pop()
print(f"Unfortunately {popped.title()} will not be able to attend.")

print(guests)

print(f"Hello {guests[0].title()}, would you still like to come to dinner?")
print(f"Hello {guests[1].title()}, would you still like to come to dinner?")

del guests[0]
del guests[0]
print(guests)