import asyncio
from alicat import FlowController
import time #Don't know if I actually need this yet, figured I would import it just in case

gas_settings = {
    "A": {"gas": "C2H2", "setpoint": 0.0, "unit": "SLPM"},
    "B": {"gas": "H2", "setpoint": 0.0, "unit": "SLPM"},
    "C": {"gas": "O2", "setpoint": 0.0, "unit": "SLPM"},
    "D": {"gas": "N2", "setpoint": 0.0, "unit": "SLPM"},
}

async def get():
    #Establish connections with mass flow controllers A, B, and C
    for unit in ['A', 'B', 'C']:
        async with FlowController(address = 'COM3', unit = unit) as mfc:
            print(await mfc.get())

async def change_rate(unit, setpoint):
    #Changes flow rate based on user input from GUI
    async with FlowController(address = 'COM3', unit = unit) as mfc:
        #if gas not in 
        #create if loop to check if gas is in a user inputed gas list. Make gas list in GUI so that user can choose gasses
        await mfc.set_flow_rate(setpoint) # In units of SLPM
        print(f'Set to {setpoint} SLPM for controller {unit}')
        await asyncio.sleep(1) #allows for time in between update so that excpetion isn't thrown for moving too fast

async def zero():
    controller = ['A', 'B', 'C']
    for unit in ['A', 'B', 'C']:
        async with FlowController(address = 'COM3', unit = unit) as mfc:
            x = mfc.set_flow_rate(0.0)
            await x
            if unit := 0.0:
                print(f'{unit} failed to reset to 0.0')
            else:
                print('All controllers reset to 0.0 SLPM') #continues to loop 3 times, figure out later after user input list

if __name__ == '__main__':
    #Global settings for the flow controllers
    asyncio.run(get())
    asyncio.run(change_rate(unit='A', setpoint = 0.0))
    asyncio.run(change_rate(unit='B', setpoint = 0.0))

#This works but figure out how to get this connected to GUI???

# SET EVERYTHING BACK TO 0.0 SLPM AT THE END OF THE DAY, TURN OFF CHEMICAL SUPPLY