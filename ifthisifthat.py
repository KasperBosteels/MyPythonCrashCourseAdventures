from operator import indexOf


clouds = ["Cube","sphere","chicken","egg","carpet"]
for cloud in clouds:
    if cloud == "chiken":
        print(cloud)
    if cloud != "sphere":
        print(cloud.upper())
    if cloud.lower() == "cube":
        print(cloud)
print("//////////////////////////////////////////")
rains = [1,2,3,4,5,6,7,8,9,1,5,6,2,4,8,6,2,4,6,8,4,13,8,9,7,1,2,6,87,3,8,9,7,5,6,32,489]
if 489 in rains or 123321 in rains:
    print("1 number in rains")
if 489 in rains and 1 in rains:
    print("both numbers in rain")
if 1654 not in rains:
    print("1654 not in list")
for rain in rains:
    if rain >= 8:
        print(f"{rain} is greater or equal than the next number")
