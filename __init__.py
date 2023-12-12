# complycat/__init__.py

# Import necessary modules/classes to make them available when someone imports your package
from .compliance_checker import ComplianceChecker
# Add more imports as needed

# Define what should be imported when someone uses 'from complycat import *'
__all__ = [
    'ComplianceChecker',
    # Add more classes/functions as needed
]
