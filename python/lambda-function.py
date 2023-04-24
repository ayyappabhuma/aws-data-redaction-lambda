import sys
import pymysql
import pandas as pd
import boto3
import csv
import os

sys.path.append('/opt')

host = os.environ.get('DATABASE_HOST')
port = os.environ.get('DATABASE_PORT')
database_name = os.environ.get('DATABASE_NAME')
username = os.environ.get('DATABASE_USER')
password = os.environ.get('DATABASE_PASSWORD')


def lambda_handler(event, context):
    # Retrieve data from the database
    conn = pymysql.connect(user=username, password=password, host=host, port=port, database=database_name)

    query = 'SELECT * FROM PersonSSN'
    df = pd.read_sql(query, conn)

    s3 = boto3.client('s3')

    bucket_name = 'bucket4keyfile'
    file_name = 'key.txt'

    response = s3.get_object(Bucket=bucket_name, Key=file_name)

    file_content = response['Body'].read().decode('utf-8')
    reader = csv.reader(file_content.split('\n'), delimiter='\t')
    key_dict = {row[0]: row[1] for row in reader if len(row) == 2}

    # function for masking the digits in a ssn based on a mapping
    def replace_digits(ssn):
        return ''.join(key_dict.get(digit, digit) for digit in str(ssn))

    new_df = df.copy()
    new_df['SSN'] = new_df['SSN'].apply(replace_digits).to_frame()

    # Convert the dataframe to a JSON object
    json_data = new_df.to_json(orient='records')
    print(new_df)

    # Return the JSON object
    return {
        'statusCode': 200,
        'body': json_data
    }
