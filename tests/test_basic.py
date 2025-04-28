import ast
import sys
from astToolkit import Make, DOT, Be

def test_make_name():
	"""Test basic Make functionality."""
	name_node = Make.Name(id="test_var")
	assert isinstance(name_node, ast.Name)
	assert name_node.id == "test_var"

def test_dot_access():
	"""Test DOT accessor functionality."""
	name_node = Make.Name(id="test_var")
	assert DOT.id(name_node) == "test_var"

def test_be_checker():
	"""Test Be type checking functionality."""
	name_node = Make.Name(id="test_var")
	assert Be.Name(name_node) is True
	assert Be.Call(name_node) is False

def test_python_version_compatibility():
	"""Verify compatibility with expected Python version."""
	assert sys.version_info >= (3, 10)
