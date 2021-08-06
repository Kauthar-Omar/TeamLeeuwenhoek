name ="Ajayi Grace"
email = "gracejeta08@gmail.com"
slack_user_name = "@grace"
biostack = "Genomics"
twitter_handle ="Gracy_ldn"
def hammingDist(str1, str2):
    i = 0
    count = 0
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
            i += 1
            return count
str1 = "SLACK USERNAME"
str2 = "TWITTER HANDLE"
print("NAME: "+name,"EMAIL: "+email,"SLACK USERNAME: "+slack_user_name,"BIOSTACK: "+biostack,"TWITTER HANDLE: "+twitter_handle,hammingDist(str1, str2))
