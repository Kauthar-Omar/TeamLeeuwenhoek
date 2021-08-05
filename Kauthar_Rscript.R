#/usr/bin/env Rscript
library(DescTools)

name <- 'Kauthar Omar'
email <- 'kauthyomar@gmail.com'
slack_username <- '@Kauthar'
biostack <- 'genomics/transcriptomics'
twitter_username <- '@K__Omar'
hamming_distance <- StrDist(slack_username, twitter_username, method="hamming")

cat(name, email, slack_username, biostack, twitter_username, hamming_distance, sep = ',')
