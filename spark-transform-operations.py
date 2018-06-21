from pyspark import SparkConf, SparkContext

# initialize spark context
conf = SparkConf().setMaster('local').setAppName('wordcount')
sc = SparkContext(conf=conf)


# ReduceByKey Transformation
# Spark RDD reduceByKey function merges the values for each key using an associative reduce function
rdd = sc.parallelize([("a", 1), ("b", 1), ("a", 1),
                      ("a", 1), ("b", 1), ("b", 1), ("b", 1), ("b", 1)], 3)

new_rdd = rdd.reduceByKey(lambda x, y: x + y)
results = new_rdd.collect()
print(results)


# Filter Transformation
# Spark RDD filter function returns a new RDD containing only the elements that satisfy the filter criteria applied.
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
filter_rdd = rdd.filter(lambda x: x % 2 == 0)
filter_results = filter_rdd.collect()
print(filter_results)


# Map Transformation
# Spark RDD map function returns a new RDD by applying a function to all elements of source RDD
rdd = sc.parallelize(["spark", "rdd", "example",  "sample", "example"], 2)
map_rdd = rdd.map(lambda x: (x, 1))
map_results = map_rdd.collect()
print(map_results)

map_rdd2 = rdd.map(lambda x: (x, len(x)))
map_results2 = map_rdd2.collect()
print(map_results2)


# flatMap Transformation
# Spark RDD flatMap function returns a new RDD by:
# ---> Applying a function to all elements of this RDD,
# ---> Flattening the results.
rdd = sc.parallelize(["spark rdd example", "sample example"], 2)

# NB: NOTE THE DIFFERENCE
# Transformation with Map applied
map_rdd3 = rdd.map(lambda x: x.split(' '))
map_results3 = map_rdd3.collect()
print(map_results3)

# Transformation with flatMap applied
flatmap_rdd = rdd.flatMap(lambda x: x.split(' '))
flatmap_results = flatmap_rdd.collect()
print(flatmap_results)

# groupBy Transformation
# Spark RDD groupBy function returns an RDD of grouped items.
# the new RDD is made up of a KEY (which is a group) and list of items of that group (in a form of Iterator)
rdd = sc.parallelize(["Joseph", "Jimmy", "Tina", "Thomas",
                      "James", "Cory", "Christine", "Jackeline", "Juan"], 3)

group_rdd = rdd.groupBy(lambda name: name[0])
print([(name[0], [i for i in name[1]]) for name in group_rdd.collect()])

# reduce Transformation
# Spark RDD reduce function reduces the elements of this RDD using the specified commutative and associative binary operator
# It accepts a function which accepts two arguments and returns a single element
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)

reduced_rdd = rdd.reduce(lambda x, y: x + y)
print(reduced_rdd)

# WIDE OPERATIONS => data shuffling may happen across the partitions.
# NARROW OPERATIONS =>do not distribute the data across the partitions
