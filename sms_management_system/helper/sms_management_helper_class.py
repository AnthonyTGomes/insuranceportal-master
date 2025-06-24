# smsapi/class/sms_client.py
import json
from django.conf import settings
import requests


from common.common_class.util import _response
from sms_management_system.helper.model_class import SendSMSRequest

API_URL = "https://corpsms.banglalink.net/bl/api/v1/smsapigw/"
HEADERS = {"Content-Type": "application/json"}

def send_sms_request(request: SendSMSRequest):
    try:
        payload = {
            "username": settings.BULKSMS_CONFIG["USERNAME"],
            "password": settings.BULKSMS_CONFIG["PASSWORD"],
            "apicode": settings.BULKSMS_CONFIG["APICODE"],
            "msisdn": request.msisdn,
            "countrycode": settings.BULKSMS_CONFIG["COUNTRY_CODE"],
            "cli": settings.BULKSMS_CONFIG["CLI"],
            "messagetype": "1",
            "message": request.message,
            "clienttransid": request.clienttransid,
            "bill_msisdn": settings.BULKSMS_CONFIG["BILL_MSISDN"],
            "tran_type": settings.BULKSMS_CONFIG["TRAN_TYPE"],
            "request_type": settings.BULKSMS_CONFIG["REQUEST_TYPE"],
            "rn_code": settings.BULKSMS_CONFIG["RN_CODE"],
        }

        response = requests.post(API_URL, json=payload, headers=HEADERS)

        if response.status_code == 200:
            resp_data = response.json()
            return _response("success", "SMS sent successfully", resp_data)
        else:
            print("Payload:", json.dumps(payload, indent=2))
            print("Result:", response)
            return _response("failed", f"HTTP Error: {response.status_code}", response.text)

    except Exception as ex:
        return _response("error", str(ex))
