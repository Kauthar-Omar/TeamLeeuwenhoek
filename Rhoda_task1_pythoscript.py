
name = 'Rhoda Kolo'
email = 'rhodakolo@gmail.com'
slack_username = '@Rhoda-K'
biostack = 'genomics'
twitter_handle = '@rekiaya_'

  #To calculate hamming_distance
s1 = 'slack_username'
s2 = 'twitter_handle'
def  hamming_distance (s1 , s2) :
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] :
            count += 1
    return count

print(name,email,slack_username,biostack,twitter_handle, hamming_distance( 'slack_username','twitter_handle'), sep=',')



