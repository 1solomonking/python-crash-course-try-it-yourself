#Dinner invitation of guest
friends_list = ['victoria', 'esther', 'elizabeth']

#Printing the invitation message to each of them
print("sending an invititionn message to all")
print(f" Hey {friends_list[0].title()}, I would like to specially invite you to my dinner.\n Hope you would attend :).")
print(f"\n Hey {friends_list[1].title()}, I would like to specially invite you to my dinner.\n Hope you would attend :).")
print(f"\n Hey {friends_list[2].title()}, I would like to specially invite you to my dinner.\n Hope you would attend :).")

#List of firends that won't attend the dinner
print("\nSending a message to the friend that won't attand the dinner party...")
print(f"{friends_list[2].title()} will be absent for the dinner part\n")
friends_list[2] = 'cheta'

#Printing the second set of invitation message to each of them
print("Sending the second set of invitation...")
print(f" Hey {friends_list[0].title()}, I would like to specially invite you to my dinner.\n Hope you would attend :).")
print(f"\n Hey {friends_list[1].title()}, I would like to specially invite you to my dinner.\n Hope you would attend :).")
print(f"\n Hey {friends_list[2].title()}, I would like to specially invite you to my dinner.\n Hope you would attend :).")

#Adding more guest to the dinner party list
friends_list.insert(0, 'motunrayo')
friends_list.insert(2, 'onyeka')
friends_list.append('tope')

#Inviting the everyone in the list
print("\n\nInviting everyone in the list informing them of the bigger table to contian everyone...")
print(f"\n Hey {friends_list[0].title()}, I would like to specially invite you to my dinner.\n I just got a a bigger table to accomodate everyone :).")
print(f"\n Hey {friends_list[1].title()}, I would like to specially invite you to my dinner.\n I just got a a bigger table to accomodate everyone :).")
print(f"\n Hey {friends_list[2].title()}, I would like to specially invite you to my dinner.\n I just got a a bigger table to accomodate everyone :).")
print(f"\n Hey {friends_list[3].title()}, I would like to specially invite you to my dinner.\n I just got a a bigger table to accomodate everyone :).")
print(f"\n Hey {friends_list[4].title()}, I would like to specially invite you to my dinner.\n I just got a a bigger table to accomodate everyone :).")
print(f"\n Hey {friends_list[5].title()}, I would like to specially invite you to my dinner.\n I just got a a bigger table to accomodate everyone :).")

#Adding a line that state you can only invite two people
print("I am sorry guys, something cameup and I can only invite two people")

#Popping out the invited guest
popped_friends = friends_list.pop(0)
print(f"\n I am sorry {popped_friends.title()}, I can't invite you to the dinner :(")
popped_friends = friends_list.pop(1)
print(f"\n I am sorry {popped_friends.title()}, I can't invite you to the dinner :(")
popped_friends = friends_list.pop(2)
print(f"\n I am sorry {popped_friends.title()}, I can't invite you to the dinner :(")
popped_friends = friends_list.pop()
print(f"\n I am sorry {popped_friends.title()}, I can't invite you to the dinner :(\n")

#Last invitation to the remaining guest
print(f"Hey {friends_list[0].title()} Hope to see you in the party\n")
print(f"Hey {friends_list[1].title()} Hope to see you in the party")

#Dinner party is over, cleaning the list
del friends_list[0]
del friends_list[0]

print(friends_list)


