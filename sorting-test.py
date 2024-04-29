import boto3
# from botocore.exceptions import ClientError
import requests
import json

# create an array of dict entries and feed into sort messages 

test = {3: 'hard', 1: 'coding', 0: 'wow', 2: 'is'} 

def sort_messages(): 
    try: 
        test_sorted = dict(sorted(test.items(), key=lambda item: item[0]))
        return test_sorted
    except Exception as e: 
        print(f"An error has occurred: {e}")  
    # Handle any errors that may occur connecting to SQS
    #except ClientError as e:
       # print(e.response['Error']['Message'])

                # (^ I had to comment this out to get the script to run) 

    # Trigger the function
if __name__ == "__main__": 
    sorted_dic = sort_messages() 
    print(sorted_dic) 
