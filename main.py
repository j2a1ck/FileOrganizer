import os
from typee import file

location = input("enter your directory: ")

os.mkdir(location + "/Document")
os.mkdir(location + "/Picture")
os.mkdir(location + "/Video")
os.mkdir(location + "/Compressed")
os.mkdir(location + "/Audio")

for i in os.listdir(location):
    x = os.path.splitext(i)[1]

    if x in file["Document"]:
        os.rename(location + "/" + i, location + "/Document/" + i)
    elif x in file["Picture"]:
        os.rename(location + "/" + i, location + "/Picture/" + i)
    elif x in file["Video"]:
        os.rename(location + "/" + i, location + "/Video/" + i)
    elif x in file["Compressed"]:
        os.rename(location + "/" + i, location + "/Compressed/" + i)
    elif x in file["Audio"]:
        os.rename(location + "/" + i, location + "/Audio/" + i)


print("completed")
