# First database stores data with maximum and minimum download speed for every user id.
# First database info (place the data within the quotes):

db1_name = ""
db1_user = ""
db1_password = ""
db1_host = ""
db1_port = ""

db1_sql_query = """
         SELECT assignmentid, down_max, up_max FROM "public"."user_info"
      """

# Second database stores data about download and upload speed usage for every user id collected periodically.
# Second database info (place the data within the quotes):

db2_name = ""
db2_user = ""
db2_password = ""
db2_host = ""
db2_port = ""

db2_sql_query = """
         SELECT assignmentid, down, up FROM "public"."trafficstats"
      """

# Destination folder info (place the data within the quotes):

file_path = ""
