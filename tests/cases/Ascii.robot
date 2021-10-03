*** Settings ***
Documentation   Test ascii value generation from pixels
Resource        ../Global.robot
Library         BuiltIn

*** Test Cases ***
Pixel value 0 is scaled to 33
  Pixel value 0 should be scaled to 33

Pixel value 255 is scaled to 126
  Pixel value 255 should be scaled to 126

Pixel value 127 is scaled to 79
  Pixel value 127 should be scaled to 79

*** Keywords ***
Pixel value ${pixel} should be scaled to ${scaled}
  ${pixel_int_value} =    Convert To Integer    ${pixel}
  ${scaled_int_value} =   Convert To Integer    ${scaled}
  ${scaled} =   Get Ascii Value   ${pixel_int_value}
  Should Be Equal   ${scaled}   ${scaled_int_value}