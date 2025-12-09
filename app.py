import json
from calculator import add, subtract, multiply


def lambda_handler(event, context):
    # We’ll take inputs from query parameters: ?a=2&b=3&op=add
    params = event.get("queryStringParameters") or {}

    try:
        a = int(params.get("a"))
        b = int(params.get("b"))
        op = params.get("op", "add")
    except (TypeError, ValueError):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid or missing parameters (a, b, op)"})
        }

    if op == "add":
        result = add(a, b)
    elif op in ("sub", "subtract"):
        result = subtract(a, b)
    elif op in ("mul", "multiply"):
        result = multiply(a, b)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid operation. Use add/sub/mul"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"result": result})
    }
