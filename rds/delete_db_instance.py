#!/usr/bin/env python
# a script to delete an rds instance

# import the sys and boto3 libraries
import sys
import boto3

# use the first argument to the script as the name
# of the instance to be deleted
db = sys.argv[1]

# create an rds client
rds = boto3.client('rds')

try:
    # delete the instance and catch the response
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db,
        SkipFinalSnapshot=True)

    # print the response if there are no exceptions
    print response

# if there is an exception, print the error message
except Exception as error:
    print error

