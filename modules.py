# modules are:
# functions
# classes
# or other components
# helps break down code to reuse and read it



# import module as namespace
# can be specific about the module and namespace used
import helpers
helpers.display('Not a warning')

# import all into current namespace
# makes it easier to call directly
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')



# packages are just a public collection of modules
# python package index is searchable too
# reuse someone else's code! best code is something already written!
# pip is the installer

# # install an individual package
# pip install colorama

# # install from a list of  packages
# pip install colorama

# # requirements.txt
colorama
