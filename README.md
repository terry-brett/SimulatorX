# SimulatorX
## Introduction
SimulatorX is a web-application built on top of Django server. The software offers performing epidemiological simulations of infectious disease. It provides a novel approach towards epidemiological simulations. The data is at the core of its functions. The simulations are driven by data related to demography of population. It means biological features such as age, gender, and ethnicity of population are taken into consideration for driving the simulation. Facial recognition technology is embedded with the software to extract biological features (age, gender, and ethnicity) from face visuals. This version only supports images for facial recognition.
For simulation purposes, software supports three comparmental models: SI (Susceptible-Infected), SIS (Susceptible-Infected-Susceptible), and SIR (Susceptible-Infected-Recovered). Moreover, it offers using two networks: Static (Barabasi-Albert) and Temporal Activity Driven network.

For performing simulations, the software consists of two applications: COVID-19 Auto Simulation and Manual Simulation
### COVID-19 Auto Simulation
As the name suggests, this application is used to simulate COVID-19 on a community. The disease and graph parameters are pre-defined. Activity Driven network is used for simulation. The user is only required to provide demographic details about population and model parameters (model type, timesteps, and seeds). To generate a network containing nodes with biological attributes, the software provides three options: Create Manual Node where user is required to use form inputs to provide age, gender, and ethnicity data, Region-Based nodes where user is required to select an area/region to simulate and rest of the fields will be auto-populated, Facial Recognition where user is required to upload images and biological features will be automatically extracted from those images. After simulation, software also provides functionality to predict the probability of infection on an individual level by providing required inputs. After performing simulation, the results are visualized using different plots generated by software describing infection propagation in age groups, gender groups, and ethnic groups.

### Manual Simulation
Unlike COVID-19 Auto Simulation, the application provides complete flexibility to user for setting disease (infection rate and/or recovery rate) and graph (graph type, number of connections) parameters along with population and model parameters. The method for creating a network for simulation is same as COVID-19 Auto Simulation. After performing simulation, the results are visualized using different plots generated by software describing infection propagation in age groups, gender groups, and ethnic groups.

### Tools and Technologies
The backend of web-application is handled by Python Django framework while the frontend is designed using HTML5, Javacript, CSS, AJAX, and ChartJS. For graph/network operations, NetworkX library is used. VGG16 model architechture is used for developing facial recogntion system. KNN classifier is used for predicting the chance of catching COVID-19 on an individual level. Key libraries include Pandas, Numpy, Keras, Tensorflow, NetworkX, and sklearn.

### Installation

1. Clone Repo
```
    git clone https://github.com/ama-yash/SimulatorX.git
    cd SimulatorX
```

2. Install the Dependencies

```
    pip install -r requirements.txt
```