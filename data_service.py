import psycopg2
import pandas as pd
import configuration as conf


def db1_query():
    """
    Makes connection to the first database using inputs from configuration.py (connection details, SQL query).
    Returns sorted DataFrame by the given id (column name).
    """
    conn = psycopg2.connect(database=conf.db1_name, user=conf.db1_user, password=conf.db1_password,
                            host=conf.db1_host, port=conf.db1_port)
    sql_query = pd.read_sql_query(conf.db1_sql_query, conn)
    df_1 = pd.DataFrame(sql_query)
    df_1.sort_values(by=['assignmentid'], inplace=True)
    return df_1


def db2_query():
    """
      Makes connection to the second database using inputs from configuration.py (connection details, SQL query).
      Returns sorted DataFrame by the given id (column label).
    """
    conn = psycopg2.connect(database=conf.db2_name, user=conf.db2_user, password=conf.db2_password,
                            host=conf.db2_host, port=conf.db2_port)
    sql_query = pd.read_sql_query(conf.db2_sql_query, conn)
    df_2 = pd.DataFrame(sql_query)
    df_2.sort_values(by=['assignmentid'], inplace=True)
    return df_2


def merge_data(df_1, df_2):
    """
    Merges data from DataFrames df_1 (from db1_query) and df_2 (from db2_query).
    Returns df_3 DataFrame merged on given id (column label).
    """
    merge_df = df_1.merge(df_2, on='assignmentid')
    df_3 = pd.DataFrame(merge_df)
    return df_3


def download_sum_query(df_3):
    """
    Extracts values from the df_3 DataFrame where download speed is equal or exceeds
    maximum download speed value. Creates a new column and drop unnecessary ones.
    In return it gives DataFrame with user id and download sum column which holds the sums
    of exceeding download speed cases.
    """
    download_data = df_3[(df_3['down'] >= df_3['down_max'])]
    download_data.loc[:, "down_sum"] = download_data["assignmentid"]
    new_column = download_data.pop("down_sum")
    download_data.insert(1, "down_sum", new_column)
    download_data.drop(['down_max', 'up_max', 'down', 'up'], axis=1, inplace=True)
    download_df = download_data.groupby('assignmentid').agg({'down_sum': 'count'})
    return download_df


def upload_sum_query(df_3):
    """
       Extracts values from the df_3 DataFrame where upload speed is equal or exceeds
       maximum upload speed value. Creates a new column and drop unnecessary ones.
       In return it gives DataFrame with user id and upload sum column which holds the sums
       of exceeding download speed cases.
    """
    upload_data = df_3[(df_3['up'] >= df_3['up_max'])]
    upload_data.loc[:, "up_sum"] = upload_data["assignmentid"]
    new_column = upload_data.pop("up_sum")
    upload_data.insert(1, "up_sum", new_column)
    upload_data.drop(['down_max', 'up_max', 'down', 'up'], axis=1, inplace=True)
    upload_df = upload_data.groupby('assignmentid').agg({'up_sum': 'count'})
    return upload_df


def join_summary_data(download_df, upload_df):
    """
    Joins download_df (DataFrame with sums of exceeding download speed cases) and upload_df
    (DataFrame with sums of exceeding upload speed cases) into one DataFrame.
    """
    join_sum_df = download_df.join(upload_df, on='assignmentid')
    sum_df = pd.DataFrame(join_sum_df)
    sum_df.fillna(0, inplace=True)
    return sum_df
