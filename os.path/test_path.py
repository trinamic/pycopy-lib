import sys

dir = "."
if "/" in __file__:
    dir = __file__.rsplit("/", 1)[0]

sys.path[0] = dir + "/os"
from path import *

assert split("") == ("", "")
assert split("path") == ("", "path")
assert split("/") == ("/", "")
assert split("/foo") == ("/", "foo")
assert split("/foo/") == ("/foo", "")
assert split("/foo/bar") == ("/foo", "bar")

assert splitdrive("/foo/bar") == ("", "/foo/bar")

assert join("a", "b") == "a/b"
assert join("a/", "b") == "a/b"
assert join("a", "/b") == "/b"

assert exists(dir + "/test_path.py")
assert not exists(dir + "/test_path.py--")

assert isdir(dir + "/os")
assert not isdir(dir + "/os--")
assert not isdir(dir + "/test_path.py")

assert isfile(__file__)
assert not isfile(dir)
