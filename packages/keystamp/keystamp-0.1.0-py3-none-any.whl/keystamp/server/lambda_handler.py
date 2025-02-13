"""
Lambda handler for the Keystamp signing server.

This code needs to be moved over into the server package.
"""

import base64
import hashlib
import hmac
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, Optional


def generate_signature(data: Dict[str, Any], secret_key: bytes) -> str:
    """Generate a cryptographic signature for the data."""
    msg = json.dumps(data, sort_keys=True).encode()
    signature = hmac.new(secret_key, msg, hashlib.sha256).hexdigest()
    return signature


def validate_api_key(api_key: str) -> bool:
    """Validate the Keystamp API key."""
    # In production, this would validate against a proper key store
    valid_key = os.environ.get("KEYSTAMP_API_KEY")
    return api_key == valid_key


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """AWS Lambda handler for Keystamp signing server.

    Args:
        event: AWS Lambda event
        context: AWS Lambda context

    Returns:
        API Gateway response
    """
    try:
        # Extract request data
        body = json.loads(event.get("body", "{}"))
        headers = event.get("headers", {})

        # Validate API key
        api_key = headers.get("X-Keystamp-Key")
        if not api_key or not validate_api_key(api_key):
            return {
                "statusCode": 401,
                "body": json.dumps(
                    {
                        "error": "invalid_api_key",
                        "message": "Invalid or missing Keystamp API key",
                    }
                ),
            }

        # Extract request/response data to sign
        request_data = body.get("request", {})
        response_data = body.get("response", {})

        # Generate timestamp
        timestamp = datetime.now(timezone.utc).isoformat()

        # Prepare data bundle to sign
        data_to_sign = {
            "request": request_data,
            "response": response_data,
            "timestamp": timestamp,
        }

        # Sign the data
        secret_key = os.environ.get("KEYSTAMP_SIGNING_KEY", "test-key").encode()
        signature = generate_signature(data_to_sign, secret_key)

        # Return signed response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "X-Keystamp-Signature": signature,
                "X-Keystamp-Timestamp": timestamp,
            },
            "body": json.dumps(
                {
                    "signature": signature,
                    "timestamp": timestamp,
                    "request": request_data,
                    "response": response_data,
                }
            ),
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "internal_error", "message": str(e)}),
        }
