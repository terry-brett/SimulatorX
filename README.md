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

## Installation

1. Clone Repo
```
    git clone https://github.com/ama-yash/SimulatorX.git
    cd SimulatorX
```

2. Install the Dependencies

```
    pip install -r requirements.txt
```

3. Start the local server

```
    python manage.py runserver
```
### Using Facial Recognition System
The Facial Recognition consists of three models: Age Model, Gender Model, and Ethnicity Model. Due to size constraints, the user is first required to download those models from Google Drive.

Download [Age Model](https://drive.google.com/file/d/1-NnO9GiRVAvugq4Oc5XE2Ezoj596oB56/view?usp=sharing)

Download [Ethnicity Model](https://drive.google.com/file/d/1-Dz-kjs2ny5pRshXzfrA-7tWvPNm3mN6/view?usp=sharing)

Download [Gender Model](https://drive.google.com/file/d/1-VfamgvLQf1ClHfhia5oMMvK19ICTDSD/view?usp=sharing)

Once downloaded, make sure the name of age, ethnicity, and gender models are named as 'age-model.h5', 'eth-model.h5', and 'gen-model.h5' respectively.

Next step is to place these models in an appropriate location. These models should be placed in 'static-only' folder which could be found in '/simulatorx/static/'.

Note that if Tensorflow is not configured with local system GPU, the facial recogntion system might take a considerable amount of time for operations. In these cases, alternative options should be preferred.
## Datasets
For testing the accuracy of software, the result produced by SIS simulation on Westminster Population using COVID-19 Auto Simulation was tested with real NHS data of Westminster which could be found in CSV format in datasets file. The COVID-19 infection and recovery parameters used by the software can also be found in the same path. 
### Sources Of Parameters
Age-specific Infection Rates: https://www.nature.com/articles/s41591-020-0962-9

White Ethnic Group Infection and Recovery Rates: https://upcommons.upc.edu/bitstream/handle/2117/330579/SEIRmodelCOVID19.pdf?sequence=1&isAllowed=y

Asian Ethnic Group Infection Rate: https://www.sciencedirect.com/science/article/pii/S096007792030446X

Asian Ethnic Group Recovery Rate: https://www.researchgate.net/profile/Md-Islam-477/publication/340604406_COVID-19_Epidemic_Compartments_Model_and_Bangladesh/links/5ea9356292851cb26762fdc7/COVID-19-Epidemic-Compartments-Model-and-Bangladesh.pdf

Black Ethnic Group Infection and Recovery Rates: https://www.sciencedirect.com/science/article/pii/S0048969720324761

## Contact For Queries
For any query related to the software, please proceed to mail at yash.soni5999@gmail.com
