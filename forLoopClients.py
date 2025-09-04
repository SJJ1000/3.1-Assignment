client_file = open("clients.txt", 'r')

clientNo = 1

for client in client_file:
    print(f"{clientNo}. {client.rstrip('\n')}")
    clientNo += 1
