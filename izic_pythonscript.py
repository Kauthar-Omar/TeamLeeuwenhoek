name = 'Isaac Omolayo'
email = 'iomolayo2541@gmail.com'
slack_username = '@izic'
biostack = 'Data analysis/Software Development'
twitter_handle = '@izic_temi'

def hammingDist(str1, str2):
    i = 0
    count = 0
    if len(str1) == len(str2):
        while(i < len(str1)):
            if(str1[i] != str2[i]):
                count += 1
            i += 1
        return count
    else:
        return('0')
    
hamming_distance = hammingDist(slack_username,twitter_handle)

print(name+","+email+","+slack_username+","+biostack+","+twitter_handle+","+hamming_distance)
