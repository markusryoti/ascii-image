*** Settings ***
Documentation   Test ascii image is generated as an HTML page
Resource        Global.robot
Library         BuiltIn

*** Test Cases ***
HTML image is created
  Remove old image
  Create image
  Image should exist