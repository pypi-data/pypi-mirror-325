#
#     from pyspark.sql.functions import col, udf
#     from pyspark.ml.linalg import VectorUDT
#
#
# if __name__ == "__main__":
#     # Initialize Spark
#     spark = SparkSession.builder \
#         .appName("FindSplitsExample") \
#         .master("local[*]") \
#         .getOrCreate()
#     sc = spark.sparkContext
#
#     # Example data: each Instance has (features, label, weight)
#     # Let's assume feature 0 is continuous and feature 1 is categorical (unordered)
#     data = [
#         Instance(features=[1.0, 'A'], label=0.0, weight=1.0),
#         Instance(features=[1.0, 'A'], label=1.0, weight=1.0),
#         Instance(features=[2.0, 'B'], label=1.0, weight=1.0),
#         Instance(features=[2.0, 'B'], label=0.0, weight=1.0),
#         Instance(features=[2.0, 'C'], label=1.0, weight=1.0),
#         Instance(features=[3.5, 'C'], label=1.0, weight=1.0),
#         Instance(features=[3.5, 'D'], label=0.0, weight=1.0),
#         Instance(features=[3.5, 'D'], label=1.0, weight=1.0),
#     ]
#     input_rdd = sc.parallelize(data)
#
#     # Define the parameters
#     num_features = 2
#     is_continuous = [True, False]  # Feature 0 is continuous, Feature 1 is categorical
#     is_unordered = [False, True]   # Feature 0 is not categorical, Feature 1 is unordered
#     max_splits_per_feature = [2, 2]  # Allow up to 2 splits per feature
#     max_bins = 32
#     total_weighted_examples = float(len(data))  # Assuming all weights are 1
#     seed = 42
#
#     # Get splits
#     splits = find_splits(
#         input_rdd=input_rdd,
#         num_features=num_features,
#         is_continuous=is_continuous,
#         is_unordered=is_unordered,
#         max_splits_per_feature=max_splits_per_feature,
#         max_bins=max_bins,
#         total_weighted_examples=total_weighted_examples,
#         seed=seed
#     )
#
#     print(splits)
#     # Print the splits
#     for fidx, feature_splits in enumerate(splits):
#         if is_continuous[fidx]:
#             print(f"Feature {fidx} (Continuous) splits:")
#             for s in feature_splits:
#                 print(f"  Threshold = {s.threshold}")
#         else:
#             print(f"Feature {fidx} (Categorical) splits:")
#             for s in feature_splits:
#                 print(f"  Categories = {s.categories}")
#             if not feature_splits:
#                 print("  No splits found.")
#
#     # # Stop Spark
#     # spark.stop()
#
#     # Show the first 5 rows of input_rdd
#     for row in input_rdd.take(5):
#         print(row)
#
#     # prompt: import the iris data set and create a dataset by duplicating it ten times. load it into a pyspark rdd. create another column features containing the feature vector of each row
#
#     import pandas as pd
#     from pyspark.ml.linalg import Vectors
#
#
#
#     # Load the iris dataset (replace with your actual path if needed)
#     try:
#         iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
#     except Exception as e:
#         print(f"Error loading Iris dataset: {e}")
#         # Handle the error appropriately (e.g., exit, use a local file)
#         exit(1)
#
#     # Rename columns
#     iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
#
#     # Duplicate the DataFrame ten times
#     iris_duplicated = pd.concat([iris_df] * 10, ignore_index=True)
#
#     # Convert pandas DataFrame to PySpark DataFrame
#     spark_df = spark.createDataFrame(iris_duplicated)
#
#
#     feature_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
#     @udf(returnType=VectorUDT())
#     def create_vector(sepal_length, sepal_width, petal_length, petal_width):
#         return Vectors.dense([sepal_length, sepal_width, petal_length, petal_width])
#
#     spark_df = spark_df.withColumn('features', create_vector(*[col(c) for c in feature_cols]))
#
#     # Show the first 5 rows
#     spark_df.show(5)
#
#     # Convert the PySpark DataFrame to an RDD
#     iris_rdd = spark_df.rdd
#
#     # Show the first 5 elements of the RDD
#     iris_rdd.take(5)
#
#     # Define the parameters
#     num_features = 4
#     is_continuous = [True, True, True, True]  # Feature 0 is continuous, Feature 1 is categorical
#     is_unordered = [False, False, False, False]   # Feature 0 is not categorical, Feature 1 is unordered
#     max_splits_per_feature = [10, 10, 10, 10]  # Allow up to 2 splits per feature
#     max_bins = 32
#     total_weighted_examples = float(len(data))  # Assuming all weights are 1
#     seed = 42
#
#     # Get splits
#     splits = find_splits(
#         input_rdd=iris_rdd,
#         num_features=num_features,
#         is_continuous=is_continuous,
#         is_unordered=is_unordered,
#         max_splits_per_feature=max_splits_per_feature,
#         max_bins=max_bins,
#         total_weighted_examples=total_weighted_examples,
#         seed=seed
#     )
#
#     print(splits)
#     # Print the splits
#     for fidx, feature_splits in enumerate(splits):
#         if is_continuous[fidx]:
#             print(f"Feature {fidx} (Continuous) splits:")
#             for s in feature_splits:
#                 print(f"  Threshold = {s.threshold}")
#         else:
#             print(f"Feature {fidx} (Categorical) splits:")
#             for s in feature_splits:
#                 print(f"  Categories = {s.categories}")
#             if not feature_splits:
#                 print("  No splits found.")