import boto3
# from botocore.exceptions import ClientError
import requests
import json

# Set up your SQS queue URL and boto3 client

sqs = boto3.client('sqs')
url = "https://sqs.us-east-1.amazonaws.com/440848399208/hdj3fw"

def get_message():

    # create the dictionary we will be using later 
    attributes = {} 

    try:
        for _ in range(20): 
        # Receive message from SQS queue. Each message has two MessageAttributes: order and word
        # You want to extract these two attributes to reassemble the message
            response = sqs.receive_message(
                QueueUrl=url,
                AttributeNames=[
                    'All'
                ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                    'All'
                ]
            )
            # Check if there is a message in the queue or not
            if "Messages" in response:
                # extract the two message attributes you want to use as variables
                # extract the handle for deletion later
                order = response['Messages'][0]['MessageAttributes']['order']['StringValue']
                word = response['Messages'][0]['MessageAttributes']['word']['StringValue']
                handle = response['Messages'][0]['ReceiptHandle']

                attributes[order] = word

                # Print the message attributes - this is what you want to work with to reassemble the message
                print(f"Order: {order}")
                print(f"Word: {word}")

            # If there is no message in the queue, print a message    
            else:
                print("No message in the queue") 
                break 


def sort_messages(): 
    try: 
        attributes_sorted = dict(sorted(attributes.items(), key=lambda item: item[0]))
        return attributes_sorted
    except Exception as e: 
        print(f"An error has occurred: {e}")  
    # Handle any errors that may occur connecting to SQS
    #except ClientError as e:
       # print(e.response['Error']['Message'])

                # (^ I had to comment this out to get the script to run) 

    # Trigger the function
if __name__ == "__main__": 
    get_message()  
    sort_messages() 
