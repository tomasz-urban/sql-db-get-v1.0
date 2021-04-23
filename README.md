# sql-db-get
### Getting data from two databases on different servers using Python and SQL statements.

## DATA INFO:
First database stores data with maximum and minimum download speed for every user id. Second database stores data about download and upload speed usage for every user id collected periodically. 

The aim of this project is to get the data from two databases located on two different servers. An output is a CSV file with the information that joins the data from those databases. That information will be gathered periodically using time schedule. Files will be stored in the format of: YYYY-MM-DD_HH-MM-SS_AM/PM).csv in the folder provided by the file_path.
The result CSV file gathers: user id, download-sum and upload-sum columns which holds the sums of exceeding download and upload speed cases.

## COMMENTS:

This version is `provided with or without scheduler`. To use scheduler follow instructions in point `3.`. The scheduler is set to execute script every Sunday at 8:00AM. To change scheduling EDIT `sql_db_get.py` follow instructions on `https://schedule.readthedocs.io/en/stable/` and change the `scheduler()` module.

## INSTRUCTIONS:

1. Install packages using:
    `pip install -r requirements.txt` for Python 2
    or
    `pip3 install -r requirements.txt` for Python 3

2. Update the `input_data.py` with the information about databases:

    * db_name - name of the database
    * db_user - database username (used for authentication)
    * db_password = database password used to authenticate
    * db_host - database host address (defaults to UNIX socket if not provided)
    * db_port - connection port number (defaults to 5432 if not provided)

    * file_path - the destination folder

3. Run `sql_db_get.py` file to execute script.
    * To run script without scheduler use: 
    `python sql_db_get.py run_now` for Python 2
    or
    `python3 sql_db_get.py run_now` for Python 3

    * To run script with scheduler use:
    `python sql_db_get.py scheduler` for Python 2
    or
    `python3 sql_db_get.py scheduler` for Python 3


