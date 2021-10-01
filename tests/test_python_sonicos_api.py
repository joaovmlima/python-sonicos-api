from sonicos_api import __version__
from sonicos_api import sonicOS as snwl

address = 'https://192.168.168.168:6443'
user = 'admin'
password = 'password'

def testLogin():
    response = snwl.fwLogin(address, user, password, False)
    assert response['status']['success'] == True

def testCommit():
    response = snwl.commitChanges(address, False)
    assert response['status']['success'] == True

def testGetCFSProfiles():
    response = snwl.getCFSProfiles(address, False)
    assert 'content_filter' in response

def testGetCFSList():
    response = snwl.getCFSLists(address, False)
    assert 'content_filter' in response

def testGetSpecificCFSList():
    response = snwl.getSpecificCFSList(address, 'Allowed Default', False)
    assert 'content_filter' in response

def testLogout():
    response = snwl.fwLogout(address, False)
    assert response['status']['success'] == True