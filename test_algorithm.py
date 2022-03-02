import pytest
import commonFunctions as cf
import os

input_folder=os.getcwd()+"\Input"

filename=[]
for i in os.listdir(input_folder):
    filename.append(input_folder+"\\"+i)

@pytest.mark.parametrize("filename", filename)
def test_validate_input(filename):
    cf.validate(filename)

@pytest.mark.parametrize("filename", filename)
def test_validate_output(filename):
    assert cf.consoleOutput(filename) == cf.happy_scenario(filename)

