#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from coder.crew import Coder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

assignment = 'Write a python program to calculate the fourier transform of a given signal.\
    The program should take a list of numerical values as input and return the Fourier transform as a list of complex numbers.\
        For testing, use the signal of an expoenential decay function defined as f(t) = e^(-t)*cos(2*pi*5*t) for t in the range of 0 to 1 with a step of 0.01.'
def run():
    """
    Run the crew.
    """
    inputs = {
        'assignment': assignment,
    }
    
    result = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)




