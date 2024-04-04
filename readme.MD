# mLocust Development Tester
This is a shim for testing locustfiles for mLocust locally. This makes it easier and faster to test your code as you don't have to upload your changes and wait for mLocust to have finished deploying and restarting. Just upload & deploy the final version after you have verified it's fully working locally.

## Instructions
- Clone/Download & unzip this repo to a folder on your machine.
- Copy your locustfile to the same folder and remove any dashes and special characters from the filename (this complicates importing it).
- Edit `locust-tester.py`:
  - Change the connection string on line 4. Make sure to include the database and collection name, and any other variables using the `|` delimiter, just like you would in the mLocust UI.
  - Change the filename of your locustfile to import it on line 8.
  - Change the name of the task/function that you want to test on line 13.
- Install any of the dependencies that are defined in your `requirements.txt` locally using `pip3`.
- You can now test your locustfile by running `locust-tester.py`, e.g.:
  ```bash
  $ python3 locust-tester.py
  Host Param: mongodb+srv://<username>:<password>@<clustername>.<clusterhash>.mongodb.net/|db|coll|batch_size
  New request came in:
  - request_type: mlocust
  - name: bulk insert
  - response_time: 303.9121627807617
  - response_length: 0
  ```