def word_count(tweet):
    words = tweet.split()
    count = {}

    for word in words:
        word = word.lower()

        # Skip mentions and URLs
        if word.startswith('@') or word.startswith('http'):
            continue

        # Count words
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count

def main():
    tweet = "I'm tweeting about #Python! @pybites"
    print(word_count(tweet))
    print('Word count: ', sum(word_count(tweet).values()))

main()
