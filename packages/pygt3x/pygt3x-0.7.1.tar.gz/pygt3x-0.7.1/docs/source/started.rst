.. toctree::
   :maxdepth: 2
   :caption: Contents:

How to use PyGT3x ?
=======================

To read calibrated accelerometer data, you can use the code snippet below:

.. code-block:: python

    from pygt3x.reader import FileReader

    # Read raw data and calibrate, then export to pandas data frame
    with FileReader("FILENAME") as reader:
        was_idle_sleep_mode_used = reader.idle_sleep_mode_activated
        df = reader.to_pandas()
        print(df.head(5))


If your AGDC file contains temperature data, you can read it using:

.. code-block:: python

    from pygt3x.reader import FileReader

    with FileReader("FILENAME") as reader:
        df = reader.temperature_to_pandas()
        print(df.head(5))