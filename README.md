The repository contains, analyzes the data for watchlists that comprise stocks and their prices; stock prices are also compared with the price at the previous day's closing bell.  
Hundreds of stocks were initially selected, included for analysis using a cloud, the Cloudera Big Data Platform, (Hortonworks) which supports Hadoop, Hadoop FS (hdfs fs; file system), 
Ambari portal (arranges the cloud software including Hadoop, Files Manager/Viewer, also including Zookeeper (Apache's Data Catalog), yarn (manager of the worker node and node manager cluster),  
Hive Sql et al query and visualization s/w (software).  Files are injested, transformed and loaded into the hadoop:  the files are cleaned for use in column stored data where the data type is 
enforced for use with aggregation (sum, data science, eg.), remove extrinsic data originally presented by the source, including commas, quotes and extra spaces in column names.  
PowerBI and Excel are used to clean data before injest.  PowerBI and Excel offer the advantage of using native functions to split data by comma to capture the needed symbol from 
fields from the Brokerage that encapsulate the name, symbol and full name; for the analysis this is too much data; data stored for this platform is delimtted by the tuple requirement
which is a python container of data, or collection.  Python tuples allow up to five column delimitted fields as we know.  *args, **kwargs were not used to expand the capacity to favor
multiple columns for analysis.  Moreover, the use of hadoop allows us to extract data columns individually.  This diverges from sql based database and database warehouses (oltp/OLAP) which
require retrieving and storing entire rows of data.  In other words were I interested in the price move of a stock over a period of time, the enduser would query only that column field, the price move
which captures that field and is associated with the key for that value (kvp (key-value pair), like the no sql schema syntax), the stock symbol.  For example the key value pair of aapl, 5%
is yielded from a table which shows stocks, stock symbol, price, price change, price change as percent, bid, ask, and date.  Big data clusters in other words process data that is
using multiple resources to simplify the data analytics without storing and retrieving and querying full records of data as a sql, row based file system or database would.
Files marked as .csv are cleaned files, files that were transformed for consistent data types, eg., number formats are used where the original record was provided as "general" or "string".
Calculations on "general" or "string" format require the casting to numeric, integer and real numbers for calculations including min,max, standard mean, std dev.  

The code which runs on the files is also contained and labeled as .py.  The python code is used to call hadoop map reduce jobs (mrjobs) that satisfies the requirement to query data not rows of
data.  The query for this study queries the data for a histogram.  Bins are marked as 5,4,3,2,1 ranking moves by percent.  a 5 rank is used to label the number of stocks that
made moves of 5 percent, for instance, or ranked higher than those which moved 4 (%). This study can be done at user discretion.  As investors we tend to analyze stocks on the
short, medium and long term which dates range from one week to several weeks to several months.  
