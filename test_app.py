from app import app

def test_home():
    ## Funtion/file name we have to start with 'test' inorder to allow the pytest library to find out the test use cases here.
    response = app.test_client().get("/") ## We are going to get from the home page. (app will give u response)

    assert response.status_code==200 ## This indicates that this is a successful request
    assert response.data == b"Hello World!" ## One type of test case i m trying to check
    ## pytest will automatically find out test cases by looking for the file name and function name starting with test.