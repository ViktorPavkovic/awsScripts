
## AWS Scripts


#### AWS Secrets Manager to S3

<p>This Python script uses default boto3 profile to fetch AWS SM secrets file located under <em>environment</em>/<em>service</em>/env name and push it to S3 bucket located under envFiles/<em>envirnment</em>/<em>service.env</em>.<br>
It's made primarily for safe transfer of environment files for use in ECS tasks as it doesn't store the file anywhere during transfer.</p>

<p>Credentials can be easily adjusted by adding couple more variables if you don't have AWS CLI already configured.</p>

<p>Prerequisites:
<ul>
<li>Python3 with AWS SDK ( [boto3](https://github.com/boto/boto3) )
<li>Configured [AWS CLI v2](https://github.com/aws/aws-cli/tree/v2) (Key ID, Secret and region) or minor tweaks to the script
<li>IAM permission to fetch secret from Secret Manager
<li>IAM permission to put object in S3 bucket
</ul></p>