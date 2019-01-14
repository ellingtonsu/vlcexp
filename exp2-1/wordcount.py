from pyspark import SparkContext

sc = SparkContext()
# Step 1.
# Read text file to RDD
tf = sc.textFile("textfile")
#print tf.collect()

# Step 2.
# Read and split each line by " "
wc = tf.flatMap(lambda line: line.split(" "))
#print wc.collect()

# Step 3. 
# Read and output key-value pair (word, 1)
wc = wc.map(lambda word: (word, 1))
#print wc.collect()

# Step 4. 
# Sum up the values of the (word, 1) pairs 
# which have the same key  
wc = wc.reduceByKey(lambda a, x: a+x)
print wc.collect()
