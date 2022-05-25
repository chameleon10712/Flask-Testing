import pytest
import sys
import os

from flask.helpers import get_root_path

#alvin
def test_get_root_path_mod_PC_TTT():
    mod = sys.modules.get("pytest")
    assert os.path.dirname(os.path.abspath(mod.__file__)) == get_root_path("pytest")
    
def test_get_root_path_mod_PC_FFF():
    assert os.getcwd() == get_root_path("")

def test_get_root_path_mod_CC_TTT():
    mod = sys.modules.get("pytest")
    assert os.path.dirname(os.path.abspath(mod.__file__)) == get_root_path("pytest")
    
def test_get_root_path_mod_CC_FFF():
    assert os.getcwd() == get_root_path("")
    
def test_get_root_path_mod_CACC_TTT():
    
    mod = sys.modules.get("pytest")
    assert os.path.dirname(os.path.abspath(mod.__file__)) == get_root_path("pytest")
    

def test_get_root_path_mod_CACC_TTF():
    assert os.getcwd() == get_root_path("static")#just a folder not package, no __init__.py
    

def test_get_root_path_mod_CACC_FFF():
    assert os.getcwd() == get_root_path("")

#oceane
def test_get_root_path_import_name_CACC_TTT():
    assert os.getcwd() == get_root_path("module_not_exists")

def test_get_root_path_import_name_CACC_TFT():
    _main = os.path.abspath(str(sys.modules['__main__'].__file__))
    assert os.path.dirname(_main)== get_root_path("__main__")

def test_get_root_path_import_name_CACC_TFT():
    assert os.getcwd()== get_root_path("__init__")


