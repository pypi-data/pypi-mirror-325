from pygt3x.reader import FileReader


# Read raw data and calibrate
# Dump to pandas data frame
with FileReader("AI3_CLE2B21130054_2017-06-02.gt3x") as reader:
    df = reader.to_pandas()
    print(df.head(5))
    print(df.count())
