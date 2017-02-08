#!/usr/bin/env python
# a script to create an rds instance

# import the boto3 library
import boto3

# create an rds client
rds = boto3.client('rds')

# use default settings for our db instance creation
# DBInstanceIdentifier must be unique to this account in this region
try:
    response = rds.create_db_instance(
        DBInstanceIdentifier='dbserver',
        MasterUsername='dbadmin',
        MasterUserPassword='abcdefg123456789',
        DBInstanceClass='db.t2.micro',
        Engine='mariadb',
        AllocatedStorage=5)
    
    # print the response if there are no exceptions
    print response

# if there is an exception, print the error message
except Exception as error:
    print error

