# AWS Lambda Function Project - Masking Social Security Numbers

This project is an implementation of an AWS Lambda function that retrieves data from an AWS RDS instance, masks the Social Security Numbers (SSNs) in the data based on a key file stored in an S3 bucket, and returns the masked data as a JSON object.

## Project Components

This project consists of the following components:

- An AWS RDS instance with a MySQL database containing a `PersonSSN` table with SSNs to be masked.
- An S3 bucket containing a `key.txt` file with a mapping of SSN digits to be masked.
- An AWS Lambda function implemented in Python that retrieves data from the `PersonSSN` table, masks the SSNs based on the `key.txt` file, and returns the masked data as a JSON object.

## Project Workflow

The workflow of this project is as follows:

1. The AWS Lambda function is triggered by an event, such as an API Gateway request.
2. The function retrieves the database connection details from environment variables set in the AWS Lambda configuration.
3. The function retrieves the SSN masking key from the `key.txt` file in the S3 bucket using the AWS SDK for Python (Boto3).
4. The function retrieves the data from the `PersonSSN` table in the RDS instance using the PyMySQL library.
5. The function masks the SSNs in the data using the SSN masking key.
6. The function returns the masked data as a JSON object.

## Setting up the Project

To set up this project, follow these steps:

1. Create an AWS RDS instance with a MySQL database containing a `PersonSSN` table with SSNs to be masked. Note down the database host, port, name, username, and password.
2. Create an S3 bucket containing a `key.txt` file with a mapping of SSN digits to be masked.
3. Create an AWS Lambda function with the following settings:
   - Runtime: Python 3.9
   - Execution role: Choose an existing role with the necessary permissions to access the RDS instance and S3 bucket.
   - Environment variables:
     - `DATABASE_HOST`: The hostname of the RDS instance.
     - `DATABASE_PORT`: The port number of the RDS instance.
     - `DATABASE_NAME`: The name of the database in the RDS instance.
     - `DATABASE_USER`: The username for accessing the RDS instance.
     - `DATABASE_PASSWORD`: The password for accessing the RDS instance.
   - Function code: Copy and paste the Python code from the `lambda_function.py` file in this repository.
   - Handler: `lambda_function.lambda_handler`
   - Timeout: 30 seconds
4. Test the function by invoking it with a test event and verifying that it returns the masked data as expected.

## Flowchart

Here is a flowchart that describes the workflow of this project:

![image](https://user-images.githubusercontent.com/31472256/234401243-df1d8f9b-f625-43aa-8c09-db1d113c9030.png)
