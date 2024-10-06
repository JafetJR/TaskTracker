#from functions_to_control import list_of_functions
#from functions.Functions import *
import sys
import os

#from functions.Functions import *
#sys.path.append(os.path.abspath('./functions'))
#from functions.Functions import *

path = os.path.abspath( os.path.join(os.path.dirname(__file__), '..', 'functions') )
sys.path.append( path )
from Functions import *

#import Functions

def Options(values):
    if values[1] == 'add':
        return add(values[2])
    
    if values[1] == 'update':
        return update(values[2], values[3])
    
    if values[1] == 'delete':
        return delete_task(values[2])
    
    if values[1] == 'mark-in-progress':
        return mark_options(values[2], 'in-progress')
    
    if values[1] == 'mark-done':
        return mark_options(values[2], 'done')
    
    if values[1] == 'list':
        return list_by_status() if len(values) == 2 else list_by_status(values[2])

    print("Invalid option. See you!")
    #options_to_select[values[1]]

option = sys.argv
Options( option )
