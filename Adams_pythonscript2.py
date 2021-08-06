
name = ( "Adams Habeeb" )
email = ( "habeebadams@gmail.com" )
slack_username = ( "@Adams" )
biostack = ( "Public health and Genomic epidemiology" )
twitter_handle = ( "@Mega_Adams" )
 
str1 = 'slack_username'
str2 = 'twitter_handle'
def hammingDist (str1 , str2) : 
   count = 0 
   for i in range(len(str1)): 
       if str1[i] != str2[i] : 
          count += 1 
   return count 
print(name,email,slack_username,biostack,twitter_handle, hammingDist( slack_username,twitter_handle), sep=',') 
