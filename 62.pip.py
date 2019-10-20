# 62 . Python PIP

"""
# PIP is a package manager for Python packages, or modules if you like.
# Note: If you have Python version 3.4 or later, PIP is included by default.
# Package? A package contains all the files you need for a module.
    Modules are Python code libraries you can include in your project
# Downloading a package is very easy:
    // Open the command line interface and tell PIP to download the package you want.
    // Navigate your command line to the location of Python's script directory, and type the
    // following: pip install [name of package]
# Once the package is installed, it is ready to use. Import the "camelcase" package into your project.
# Use the uninstall command to remove a package
    // following: pip uninstall [name of package]
# Use the list command to list all the packages installed on your system.
    // following: pip list
"""

import camelcase as cc

c = cc.CamelCase()
text = "this method capitalizes the first letter of each word"
print(c.hump(text))
