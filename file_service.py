from datetime import datetime
import configuration as conf


def save_file(sum_df):
    """
    Sets the format of datetime. Collects file path from configuration file
    and saves it to the CSV file with current data and time.
    """
    date = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    file_path = conf.file_path
    saved_file = sum_df.to_csv(f'{file_path}{date}.csv')
    return saved_file
