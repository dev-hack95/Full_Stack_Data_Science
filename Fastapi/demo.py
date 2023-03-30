from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("demo").master("spark://spark-master:7077").getOrCreate()

print(spark)