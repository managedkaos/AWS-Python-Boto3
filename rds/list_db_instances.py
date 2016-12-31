#!/usr/bin/env python
# a script to list rds instances

# import the boto3 library
import boto3

# create an rds client
rds = boto3.client('rds')

try:
    # get all of the db instances
    dbs = rds.describe_db_instances()

    # for each db, print some details
    for db in dbs['DBInstances']:
        print ("%s@%s:%s") % (
            db['MasterUsername'], 
            db['Endpoint']['Address'], 
            db['Endpoint']['Port'])

except Exception as error:
    print error