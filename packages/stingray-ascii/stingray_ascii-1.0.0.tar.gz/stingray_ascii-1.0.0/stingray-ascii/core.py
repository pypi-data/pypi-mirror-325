# core.py


# Import
from typing import Literal

from .exceptions import *

# Defuine functions
def print_mini_stingray_ascii(direction: Literal['left', 'right'] = 'left'):
    # Validate direction
    if direction not in ['left', 'right']:
        raise IncorrectDirection

    # Set result
    if direction == 'left':
        result = '◀--'
    else:
        result = '--▶'

    # Print result
    print(result)

def print_stingray_ascii(direction: Literal['left', 'right'] = 'left'):
    # Validate direction
    if direction not in ['left', 'right']:
        raise IncorrectDirection

    # Print stingray
    if direction == 'left':
        result = r'''    /\  
  |  \.  
 /     \  
|:      >------  
 \     /  
  |  /'  
    \/  '''
    else:
        result = r'''           /\
         ./  |
        /     \
------<      :|
        \     /
         '\  |
           \/'''

    # Print result
    print(result)