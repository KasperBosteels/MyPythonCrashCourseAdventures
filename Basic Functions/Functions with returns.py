def city_country(city,country):
    return f"{city} {country}"

cities = [{'city':"Brussels",'country':'Belgium'},{'city':"Paris",'country':'France'},{'city':"Kiev","country":"Ukraine"}]

for city in cities:
   result = city_country(city['city'],city['country'])
   print(result)

def make_album(author,title,songs=None):
    new_album =  {'author':author,'title':title,'songs':songs}
    return new_album

result = make_album("Gorillaz","the now now")
print(result)
result = make_album("Gorillaz","the now now",["2001","feel good inc.","plastic beach"])
print(result)

active = True
while active:
    active = input("Make a new Album [y,n]: ") == "y"
    if active == False:
        break
    author= input("Authors name: ")
    title = input ("Album title: ")
    addSong = input("Does this album have songs [y/n]: ") == "y"
    songs = []
    while addSong:
        song = input("Song name: ")
        if song == "stop":
            break
        songs.append(song)
    new_album = make_album(author,title,songs)
    print(new_album)
