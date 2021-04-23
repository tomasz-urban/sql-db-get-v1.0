import sys
import schedule
import time
import pandas as pd
import data_service as ds
import file_service as fs

pd.options.mode.chained_assignment = None


def run_all():
    if len(sys.argv) < 2:
        print("No argument given. Please use: 'scheduler' or 'run_now'. Check README file for more information.")
        sys.exit(1)

    input_arg = sys.argv[1]

    if input_arg == "scheduler":
        scheduler()
    elif input_arg == "run_now":
        query_setup()
    else:
        print("Wrong argument given. Please use: 'scheduler' or 'run_now'. "
              "Check README file for more information.")


def query_setup():
    """
    Runs all of the modules from data_service and file_service files.
    """
    df_1 = ds.db1_query()
    df_2 = ds.db2_query()
    df_3 = ds.merge_data(df_1, df_2)
    download_df = ds.download_sum_query(df_3)
    upload_df = ds.upload_sum_query(df_3)
    sum_df = ds.join_summary_data(download_df, upload_df)
    fs.save_file(sum_df)


def scheduler():
    """
    Executes query_setup() module at the given time schedule. Ran once it works until terminated.
    """
    schedule.every().sunday.at("8:00").do(query_setup)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    run_all()
