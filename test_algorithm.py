import pytest
import commonFunctions as cf
import os

input_folder=os.getcwd()+"\Input"
output_folder=os.getcwd()+"\Output"
filenam=[]
for i in os.listdir(input_folder):
    filenam.append(input_folder+"\\"+i)

@pytest.mark.parametrize("filenam", filenam)
def test_validate_input(filenam):
    cf.validate(filenam)

@pytest.mark.parametrize("filenam", filenam)
def test_validate_output(filenam):
    assert cf.consoleOutput(filenam) == cf.happy_scenario(filenam)

