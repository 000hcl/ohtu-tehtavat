*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  sout  password0
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  sout  password1
    Output Should Contain  User with username sout already exists

Register With Too Short Username And Valid Password
    Input Credentials  ii  abcd1234
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  oms  abc1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  oms  password
    Output Should Contain  Password can't contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  sout  abcd1234
    Input New Command