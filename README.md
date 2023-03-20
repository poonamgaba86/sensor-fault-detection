# sensor-fault-detection
Problem Statement:= 

The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

Solution Proposed:


In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

Tech Stack Used :--


1.Python
2.FastAPI
3.Machine learning algorithms
4.Docker
5.MongoDB


Steps to run project

1.open command prompt, reach to location where you want to keep project

2. write this command :- git clone https://github.com/poonamgaba86/sensor-fault-detection.git

3.open the project in Visual studio

4.open terminal then choose command prompt

5. create environment:-  conda create -p ./sens_env_name

6.conda activate ./sens_env_name

7.pip install -r requirements.txt

8. python main.py

9. localhost:8080
