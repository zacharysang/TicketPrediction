from pyspark.ml import Pipeline
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

PATH = './Traffic_Stops__drivers.csv'

#load the data
data = spark.read.format('csv').load(PATH)

# Convert Interview date to interview time

# Action taken column -> Citation | No Citation

# Address -> Road

# Address (Road) | Action Taken Id | Date (Time) | Vehicle Make | Vehicle Model | Vehicle Year | License Plate State | Sex | Race | Age range