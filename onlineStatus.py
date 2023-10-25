"""
"""
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count (statuses):
    counter = 0
    for value in statuses.values():
        if value == "online":
            counter += 1
    return counter
print(online_count(statuses))