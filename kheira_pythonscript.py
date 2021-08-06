
import hashlib

def hamming_distance(slack,twitter):
    return sum(c1 != c2 for c1, c2 in zip(slack, twitter))





name= 'Kheira Lakhdari,'
email= 'kirabasma12@gmail.com,'
slack= '@Kheira,'
biostack= 'Software development / Data science,'
twitter= '@Kheira,'



print (name, email, slack, biostack, twitter, hamming_distance(slack,twitter))

