import json
import boto3

ENDPOINT_NAME = "jumpstart-dft-meta-textgeneration-l-20240306-195837" # replace with your endpoint name
InferenceComponentName = 'meta-textgeneration-llama-2-7b-f-20240306-195837' # replace with you model name
client = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    print(boto3.__version__)
    response = client.invoke_endpoint(
        EndpointName=ENDPOINT_NAME, InferenceComponentName=InferenceComponentName,
        ContentType="application/json",
        Body=event['body'],
        CustomAttributes="accept_eula: true"
    )
    response = response["Body"].read().decode("utf8")
    response = json.loads(response)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

