""" Simple example of using boto to return EC2 information"""

import boto3


class GetAwsInfo:
    def __init__(self):
        pass

    def run(self):
        self.show_ec2()
        self.show_rds()

    def show_ec2(self):
        print '----------------------'
        print 'Getting EC2 host list'

        client = boto3.client('ec2')

        res = client.describe_instances()['Reservations']
        for r in res:
            instances = r['Instances']
            for inst in instances:
                tags = inst['Tags']
                for tag in tags:
                    if tag['Key'] == 'Name':
                        print tag['Value']

    def show_rds(self):
        print '----------------------'
        print 'Getting RDS host list'
        client = boto3.client('rds')
        dbs = client.describe_db_instances()
        for db in dbs['DBInstances']:
            print db['Endpoint']['Address']

if __name__ == '__main__':
    GetAwsInfo().run()
