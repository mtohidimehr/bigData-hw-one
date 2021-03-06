# -*- coding: utf-8 -*-
"""bigData-HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aJXpkvDAuhetd1-5gmJo2CRs8tFXEAQN
"""

!wget https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz
!tar -xvzf spark-3.2.1-bin-hadoop3.2.tgz
!pip install findspark
import os
os.environ["SPARK_HOME"]= "/content/spark-3.2.1-bin-hadoop3.2"
import findspark
findspark.init()

bookList = ['In Search of Lost Time' , 'Nineteen Eighty Four' , 'The Lord of the Rings' ,'Pride and Prejudice','The Grapes of Wrath',
            'To Kill a Mockingbird','Jane Eyre','Wuthering Heights','A Passage to India','Lord of the Flies',
            'Hamlet','A Bend in the River','The Great Gatsby','The Catcher in the Rye','The Bell Jar',
            'Brave New World','The Diary of a Young Girl','Don Quixote','The Bible','The Canterbury Tales',
            'The Quiet American','Birdsong','Money','Harry Potter and the Deathly Hallows','Harry Potter and the Order of the Phoenix',
            'Harry Potter And The Prisoner Of Azkaban','Harry Potter and the Half-Blood Prince','Moby Dick','The Wind in the Willows','His Dark Materials',
            'Anna Karenina','Alice Adventures in Wonderland','Rebecca','On the Road','Heart of Darkness',
            'The Way We Live Now','The Stranger','The Color Purple','Life of Pi','Frankenstein',
            'War of the Worlds','Stories of Ernest Hemingway','Gulliver Travels','A Christmas Carol','Robinson Crusoe',
            'Catch-22','The Count of Monte Cristo','Memoirs of a Geisha','The Divine Comedy','The Picture of Dorian Gray']

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('App1').getOrCreate()
rdd = spark.sparkContext.parallelize(bookList)

rdd.filter(lambda x: bookList[19] in x).collect()

rdd.map(lambda x: x.upper()).collect()

rdd.groupBy(lambda x: x[0]).map(lambda x:(x[0],list(x[1]))).sortBy(lambda x: x[0]).collect()

from pyspark import SparkContext
sc = spark.sparkContext
RddText = sc.textFile("Input")
wordCounts = RddText.flatMap(lambda line: line.split()).map(lambda word:(word, 1)).reduceByKey(lambda a,b:a+b)
list(wordCounts.collect())

"""# New Section"""