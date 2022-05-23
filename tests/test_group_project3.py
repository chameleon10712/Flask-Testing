import pytest
import sys
import os

from flask.helpers import get_root_path

def test_get_root_path_PC_TTT():
    
    mod = sys.modules.get("pytest")
    assert os.path.dirname(os.path.abspath(mod.__file__)) == get_root_path("pytest")
    
def test_get_root_path_PC_FFF():
    assert os.getcwd() == get_root_path("")

def test_get_root_path_CC_TTT():
    
    mod = sys.modules.get("pytest")
    assert os.path.dirname(os.path.abspath(mod.__file__)) == get_root_path("pytest")
    
def test_get_root_path_CC_FFF():
    assert os.getcwd() == get_root_path("")
    
    
def test_get_root_path_CACC_TTT():
    
    mod = sys.modules.get("pytest")
    assert os.path.dirname(os.path.abspath(mod.__file__)) == get_root_path("pytest")
    
def test_get_root_path_CACC_FFF():
    assert os.getcwd() == get_root_path("")