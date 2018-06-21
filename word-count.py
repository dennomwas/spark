from pyspark import SparkConf, SparkContext

# initialize spark context
conf = SparkConf().setMaster('local').setAppName('wordcount')
sc = SparkContext(conf=conf)

# load the data file
input = sc.textFile('/Users/dennomwas/Documents/Projects/spark/Book.txt')

# create an RDD
words = input.flatMap(lambda x: x.split())

# Transform the RDD
word_count = words.countByValue()

# Display the word and count
for word, count in word_count.items():
    clean_word = word.encode('ascii', 'ignore')
    if clean_word:
        print(clean_word, count)
