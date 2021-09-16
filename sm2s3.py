import boto3

# Fetch secret from AWS SM
def get_secret(secretName):
    sm = boto3.Session().client('secretsmanager')
    return sm.get_secret_value(SecretId=secretName)['SecretString']

# Uplad content to S3
def uploadToS3 (bucket, path, content):
    s3 = boto3.Session().resource('s3')
    object = s3.Object(bucket, path)
    return object.put(Body=content)

# List of services/apps and environments
services = ['app1', 'app2']
environments = ['dev', 'staging', 'prod']

s3Bucket = 'envFiles'

for env in environments:
    for service in services:

        # Secret name is in format environment/service/env [dev/app1/env]
        secretName = env + '/' + service + '/env'

        # Environment file is on path bucket/environment/service.env [envFiles/dev/app1.env]
        s3Path = env + '/' + service + '.env'

        # Get secret and upload it to S3, write out status code of S3 upload
        s3Response = uploadToS3 (s3Bucket, s3Path, get_secret(secretName))
        print (env, service, s3Response['ResponseMetadata']['HTTPStatusCode'])