import json
import base64
import requests
from collections import OrderedDict

headers = OrderedDict(
        [('Accept', 'application/json'),
            ('Content-Type', 'application/json'),
            ('Accept-Encoding', 'application/json'),
            ('charset', 'UTF-8')
         ])

def isSuccessStatus(status_code):
    return (status_code >= 200 and status_code < 300)

def fwLogin(fwAddress: str, fwUser: str, fwPassword: str, verifySSLCert: bool):
    # make credentials base64 encoded
    credentials = fwUser+":"+fwPassword
    credentials = bytes(credentials, 'utf-8')
    encode = base64.b64encode(credentials)
    encode = str(encode, 'utf-8')

    url = f"{fwAddress}/api/sonicos/auth"
    payload = ""
    headers = OrderedDict(
        [('Authorization', f'Basic {encode}'),
            ('Accept', 'application/json'),
            ('Content-Type', 'application/json'),
            ('Accept-Encoding', 'application/json'),
            ('charset', 'UTF-8')
         ])

    response = requests.request("POST", url, data=payload, headers=headers, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response) 
    return response

def fwLogout(fwAddress: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/auth"
    payload = ""

    response = requests.request("DELETE", url, data=payload, headers=headers, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response

def configMode(fwAddress: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/config-mode"
    payload = ""
    response = requests.request("POST", url, headers=headers, data=payload, verify=verifySSLCert)
    response = response.json()
    response = json.dumps(response).loads(response)

    return response

def commitChanges(fwAddress: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/config/pending"
    payload = ""
    response = requests.request("POST", url, headers=headers, data=payload, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response

def getCFSProfiles(fwAddress: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/content-filter/profiles"

    response = requests.request("GET", url, headers=headers, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response

def getCFSLists(fwAddress: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/content-filter/uri-list-objects"
    payload = ""
    response = requests.request("GET", url, headers=headers, data=payload, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response

def getSpecificCFSList(fwAddress: str, cfsListName: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/content-filter/uri-list-objects/name/{cfsListName}"
    payload = ""
    response = requests.request("GET", url, headers=headers, data=payload, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response

def insertIntoCFSList(fwAddress: str, cfsName: str, uri: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/content-filter/uri-list-objects"
    payload = {"content_filter": {"uri_list_object": [
        {
            "name": cfsName,
                    "uri": [{"uri": uri}]
        }
    ]}}

    response = requests.request("PUT", url, json=payload, headers=headers, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response

def removeFromCFS(fwAddress: str, cfsName: str, uri: str, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/content-filter/uri-list-objects"

    payload = {"content_filter": {"uri_list_object": [
                {
                    "name": cfsName,
                    "uri": [{"uri": uri}]
                }
            ]}}

    response = requests.request("DELETE", url, json=payload, headers=headers, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response

def getFwInfo(fwAddress, verifySSLCert: bool):
    url = f"{fwAddress}/api/sonicos/administration/global"

    payload = ""
    response = requests.request("GET", url, headers=headers, data=payload, verify=verifySSLCert)
    if (isSuccessStatus):
        response = response.text
        response = json.loads(response)
    return response.json()