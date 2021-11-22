*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  abc
    Set Password  abcd1234
    Confirm Password  abcd1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  abcd1234
    Confirm Password  abcd1234
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  sauce
    Set Password  ae1
    Confirm Password  ae1
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  sauce
    Set Password  1234abcd
    Confirm Password  2345abcd
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  abcd
    Set Password  abcd1234
    Confirm Password  abcd1234
    Submit Credentials
    Register Should Succeed
    Log Out From Welcome Page
    Set Username  abcd
    Set Password  abcd1234
    Submit Log In Info
    Main Page Should Be Open

Login After Failed Registration
    Set Username  sauce
    Set Password  1234abcd
    Confirm Password  2345abcd
    Submit Credentials
    Register Should Fail With Message  Passwords don't match
    Go To Login Page
    Set Username  sauce
    Set Password  1234abcd
    Submit Log In Info
    Login Should Fail With Message  Invalid username or password


*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${confirm}
    Input Text  password_confirmation  ${confirm}

Create User And Go To Register Page
    Create User  new  password3
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Log Out From Welcome Page
    Go To Ohtu Page
    Click Button  Logout
    Login Page Should Be Open

Submit Log In Info
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}