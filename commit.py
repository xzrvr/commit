import os

ip = int(input("how many times u wanna commit? \n"))
autoPush = input("autopush when committed? (y/n) \n")

for i in range(ip):
	os.system(f'git commit --allow-empty -m "commit {i}"')	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')
