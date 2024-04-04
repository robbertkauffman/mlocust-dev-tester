# Change below to your connection string. Make sure to include the database and 
# collection name, and any other variables using the *|* delimiter, just like 
# you would in the mLocust UI.
CONNSTRING = "mongodb+srv://<username>:<password>@<clustername>.<clusterhash>.mongodb.net/|db|coll|batch_size"

# Change below to the filename of your locustfile.
# If filename includes a dash, either remove or change to underscore
from locustfiles.query import MetricsLocust

locust = MetricsLocust(CONNSTRING)

# Change below to the name of the task/function that you want to test
locust._async_find_random()