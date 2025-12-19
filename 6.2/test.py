file = open("6.2/spotify.csv")
junk = file.readline()

drake_data = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])

for danceability in drake_data:
	for i in range(len(drake_data)):
		smallest_score = drake_data[i]
		smallest_index = i

		for j in range(i + 1, len(drake_data)):
			if drake_data[j] < smallest_score:
		
				drake_data[smallest_index], drake_data[i] = drake_data[i], drake_data[smallest_index]

				for x in range(5):
					print(str(danceability[0]))



