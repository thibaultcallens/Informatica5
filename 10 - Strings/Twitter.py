
tweet = input('wat is de tweet?: ')

a = tweet.find('#')

for i in range(0, len(tweet)- 1):
    if tweet[i] == '#':
        na_hashtag = tweet[i::]
        volgende_spatie= na_hashtag.find(' ')
        hashtag = na_hashtag[1:volgende_spatie:]

        print(hashtag)