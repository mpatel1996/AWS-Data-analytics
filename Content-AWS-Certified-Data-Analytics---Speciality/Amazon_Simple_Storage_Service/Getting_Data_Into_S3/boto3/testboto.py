import boto3

s3Client = boto3.client(
    's3',
    aws_access_key_id='ASIA4C4IIOIYHBVZJE7Z',
    aws_secret_access_key='ECwak+6eQ5qJAmybBjkPqEJqv1hjqbaBhvxF3mpe',
    aws_session_token='IQoJb3JpZ2luX2VjENr//////////wEaCXVzLWVhc3QtMSJGMEQCIDM5Q/ZgUw4tvXbxPQHwMNm5d5suT7xsOoks8l+yYPEnAiA658e9LB7dtH54bday0OT8auEI+x3ZD7G/MNoFHm9cfSrrAQgzEAAaDDgzMDgyNTA2NzA1NiIMqnlNzFaSIWO2I5ZqKsgBwYeFOAcg1ifGzUWj5Ex/05He26ox4f6mfjnnd471NFA9ExIRDAkDeMwsgmnKFOUsXYnJZNuljaCo4QtgOpJmzPkzzsckLIXjkeLG6MrK8GbqYoWwqaHhE7umaAS4RzeNScAv2gxPAx79ICXL7H/2aTsCDSkIp1rqp578Af4U2o7+s1SxpIgkh7g/I/dm55FpNR5ieCq99ucxtiHw3hXdnYZ5zrsh8AcMq0teNpS5aSkoyAn285xCxrkK+xxgvi7pSJG2oxQc/Xgw3Z6tpAY6mQHZG82j7c9JTxtYJzHVKPpwRj4kC17xD9c0NIUyVd1IpJ6//EAvmER2JZ9zdcR7QEVBRtOXFk854uFNTN3cG7iFlYJ5ZGpgHow3wd7i1vxwQTfWKA9MwvSJ+k4Fq/xHbqo9yVAydJwmuDIc/mBOB76Yhpwsk6OHR3p/U2wDZ6IJ3aqczs4QZgVGSYGIVZgse1KR2KVSxCtp8GM='
)

s3 = boto3.resource(
    's3',
    aws_access_key_id='ASIA4C4IIOIYHBVZJE7Z',
    aws_secret_access_key='ECwak+6eQ5qJAmybBjkPqEJqv1hjqbaBhvxF3mpe',
    aws_session_token='IQoJb3JpZ2luX2VjENr//////////wEaCXVzLWVhc3QtMSJGMEQCIDM5Q/ZgUw4tvXbxPQHwMNm5d5suT7xsOoks8l+yYPEnAiA658e9LB7dtH54bday0OT8auEI+x3ZD7G/MNoFHm9cfSrrAQgzEAAaDDgzMDgyNTA2NzA1NiIMqnlNzFaSIWO2I5ZqKsgBwYeFOAcg1ifGzUWj5Ex/05He26ox4f6mfjnnd471NFA9ExIRDAkDeMwsgmnKFOUsXYnJZNuljaCo4QtgOpJmzPkzzsckLIXjkeLG6MrK8GbqYoWwqaHhE7umaAS4RzeNScAv2gxPAx79ICXL7H/2aTsCDSkIp1rqp578Af4U2o7+s1SxpIgkh7g/I/dm55FpNR5ieCq99ucxtiHw3hXdnYZ5zrsh8AcMq0teNpS5aSkoyAn285xCxrkK+xxgvi7pSJG2oxQc/Xgw3Z6tpAY6mQHZG82j7c9JTxtYJzHVKPpwRj4kC17xD9c0NIUyVd1IpJ6//EAvmER2JZ9zdcR7QEVBRtOXFk854uFNTN3cG7iFlYJ5ZGpgHow3wd7i1vxwQTfWKA9MwvSJ+k4Fq/xHbqo9yVAydJwmuDIc/mBOB76Yhpwsk6OHR3p/U2wDZ6IJ3aqczs4QZgVGSYGIVZgse1KR2KVSxCtp8GM='
)

putMessage = b'Hi! I came from Boto3!' # this is in Binary form 

# put_object
# Simple put request to send an item to the S3 bucket into boto3put.txt file.
# response = s3Client.put_object(
#     Body = putMessage,
#     Bucket = 'bototestupload',
#     Key = 'boto3put.txt'
# )

toCopy = {
    'Bucket': 'bototestupload',
    'Key': 'boto3put.txt'
}

re = s3.meta.client.copy(toCopy, 'bototestupload', 'copy.txt')
print(re)