#!/usr/bin/env python
# a script to delete an rds instance

# import the sys and boto3 libraries
import sys
import boto3

# create an rds client
rds = boto3.client('rds')

db = sys.argv[1]

try:
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db,
        SkipFinalSnapshot=True)
    print response
except Exception as error:
    print error
