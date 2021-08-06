
name = 'Rhoda Kolo'
email = 'rhodakolo@gmail.com'
slackId = '@Rhoda-K'
biostack = 'genomics'
twitter = '@rekiaya_'

S1 = '@Rhoda-K'
S2 = '@rekiaya_'
def  hamming_distance (s1 , s2) :
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] :
            count += 1
    return count

print(name,email,slackId,biostack,twitter, hamming_distance( '@Rhoda-K','@rekiaya'), sep=',')



