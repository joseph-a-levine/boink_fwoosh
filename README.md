# World 3 simulation code

To run `run_world3.py` file it is required to load the pysd librairy available here: https://pysd.readthedocs.io/en/master/basic_usage.html
Python version : 3.6
    
WARNING: 
To avoid initialization issues a modification in the library is needed  : https://github.com/swhatelse/pysd/commit/dc6288b477056ac5f2af0cac215d233009858bac
    
    
## Outputs
The output is 3 graphs representing the state of the system between 1900 and 2100:
* the state of the world
* the level of life
* the human impact on the planet

This choice of different classes is based on the book 'Limits to Growth' - 2004
    
  The file `world3_scenario1.py` (launched by default) is the implementation of the World3 model when is was actualized in 2004.
  It simulates the scenario 1 called by the author Business-As-Usual.
  
  The others scenarios ares available in the folder `scenarii`. (run run_world3.py scenario_number)
  All scenarios and the modifications related are described here : https://reference.wolfram.com/system-modeler/libraries/SystemDynamics/SystemDynamics.WorldDynamics.World3.html
    