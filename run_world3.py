"""
    Script to launch the World3 model
    The output is 3 graphs representing the state of the system:
            - the state of the world
            - the level of life
            - the human impact on the planet
    This choice of different classes is based on the book 'Limits to Growth' - 2004
    
"""
import numpy as np
import matplotlib.pyplot as plt
import pysd
import sys

if len(sys.argv) < 2:
        print('usage: runs_world3.py <scenario_number>')
        print('if scenario_number is not filled, the scenario 1 will be launched')
        print('scenario_number needs to be between 1 and 10')
        scenario = 1
else:
    scenario = int(sys.argv[1])
    if scenario > 10:
        print('scenario_number needs to be between 1 and 10 scenario 1 will be launched')
        scenario = 1
        
total_years = np.arange(1900, 2100.5, 0.5)


world = [
    "population",
    "industrial_output",
    "nonrenewable_resources",
    "persistent_pollution",
    "food"
]

life = [
    "service_output_per_capita",
    "industrial_output_per_capita",
    "food_per_capita",
    "life_expectancy"
]

human =[
    "human_welfare_index",
    "human_ecological_footprint"
]

comp = [world, life, human]


for j in range(3):
    
    #reload  model for each run to avoid initialization issues
    w3 = pysd.load('scenarii/world3_scenario' + str(scenario) + '.py')
    
    #select the components according to the class
    components = comp[j]
    stocks = w3.run(return_columns = components,params = {'final_time':2100} )
    
    fig, ax = plt.subplots()
    
    #scaling the outputs such as all the studied parameters are normalized to 1
    scale = []
    for s in stocks.T.values:
        scale.append(1/max(s))
    stocks = stocks * scale
     
    #ploting
    ax.set_xlim([1900, 2100])
    stocks.plot(ax=ax)
    plt.grid(linestyle=':', linewidth=1)
    if j == 0:
        plt.suptitle('State of the World') 
        plt.show()
    elif j == 1:
        plt.suptitle('Material standard of living')
        plt.show()
    else:
        plt.suptitle('Human welfare and footprint')
        plt.show()

    

