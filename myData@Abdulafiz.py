#project1
myData = { "name": "Abdulafiz Musa",
           "email": "musaabdulafiz@gmail.com",
           "slackUsername": "@Abdulafiz",
           "biostack": "Data Science",
           "twitterHandle": "@Abdulafiz_O" }

#print(myData["name"]+","+myData["email"]+","+myData["slackUsername"]+","+myData["biostack"])

#Hamming distance
str1 = myData["slackUsername"]
str2 = myData["twitterHandle"]
def hammingDist(str1, str2):
    i = 0
    count = 0
    while (i < len(str1)):
        if (str1[i] != str2[i]):
            count += 1
        i += 1
    return count

#updated output
print(myData["name"]+","+myData["email"]+","+myData["slackUsername"]+","+myData["biostack"]+","+
      myData["twitterHandle"]+","+str(hammingDist(str1, str2)))

