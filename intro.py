name = "Ayesha Saman Hawaldar"
email = "ayesh95_saman@yahoo.in"
slack_username = "@Ayesha"
biostack = "Vaccine informatics"

#Updated

twitter_handle = "@Ash95Saman"
str1 = "@Ayesha"
str2 = "@Ash95Saman"

from itertools import zip_longest
def hamming_dist(str1, str2):
  return sum(c1 != c2 for c1, c2 in zip_longest(str1, str2))

hamming_dist("@Ayesha", "@Ash95Saman")

print(name, email, slack_username, biostack, twitter_handle, hamming_distance, sep=',')
