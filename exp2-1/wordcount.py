from pyspark import SparkContext

sc = SparkContext()
# Step 1. Read text file to RDD
text_file = sc.textFile("textfile")
#print text_file.collect()

# Step 2. Read and split each line by " "
counts = text_file.flatMap(lambda line: line.split(" "))
#print counts.collect()

# Step 3. Read and output key-value pair (word, 1) for each word
counts = counts.map(lambda word: (word, 1))
#print counts.collect()

# Step 4. If the keys of any two key-value pairs are the same, sum up their values
counts = counts.reduceByKey(lambda a, x: a+x)
print counts.collect()
