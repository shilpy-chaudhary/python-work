lucky_numbers = [2,3,5,7,8,97]
friends = ["kevin", "jim","oscar","truss"]

friends[1]= "mike"
print(friends[0])
print(friends[0:2])

friends.extend(lucky_numbers)

friends.append("creed")

friends.insert(1,"kelly")

friends.remove("oscar")

friends.clear()

friends.pop()

print(friends)
