def lambda_handler(event, context):
    previous_result = event["result"]
    return {
        "body": f"{previous_result}_RESULT"
    }
