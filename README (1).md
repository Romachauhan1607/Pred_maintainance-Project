# Nasa Aircraft Turbofan Jet Engine- Predictive_Maintenance

###

INTRODUCTION

Each data set is further divided into training and test subsets.There are three operational settings that have a substantial effect on engine performance. These settings are also included in the data. The data is contaminated with sensor noise.

The engine is operating normally at the start of each time series, and develops a fault at some point during the series. In the training set, the fault grows in magnitude until system failure. In the test set, the time series ends some time prior to system failure. The objective of the competition is to predict the number of remaining operational cycles before failure in the test set, i.e., the number of operational cycles after the last cycle that the engine will continue to operate. Also provided a vector of true Remaining Useful Life (RUL) values for the test data.

The data are provided as a zip-compressed text file with 26 columns of numbers, separated by spaces. Each row is a snapshot of data taken during a single operational cycle, each column is a different variable. The columns correspond to:
1) unit number
2) time, in cycles
3) operational setting 1
4) operational setting 2
5) operational setting 3
6) sensor measurement 1
7) sensor measurement 2
...
26) sensor measurement 26

.In this dataset the goal is to predict the remaining useful life (RUL) of each engine in the test dataset. RUL is equivalent of number of flights remained for the engine after the last datapoint in the test dataset

. The Remaining useful life metric has been calculated with a difference of the whole engine lif
cycle from the cycle that the engine has completed, with the help of this feature we are going to fit the dataset with different machine learning models.
The purpose of this research paper is to present a Flask app developed for the Predictive Maintenance of NASA turbofan engines. The app uses the best machine learning algorithm to analyze real-time data from the engines and predict when maintenance should be performed. The scope of the research paper includes a literature review of existing PdM techniques, a description of the methodology
used to develop the app, a presentation of the app's results, and a discussion of the implications of the app for Predictive Maintenance in the aviation industry.

### Objective
The objective of this project is to develop a machine learning model to predict the remaining useful life of aircraft turbofan engines. The Remaining Useful Life (RUL) is the amount of cycles an engine has left before it needs maintenance.

### created a environment
```
conda create -p venv python==3.9 -y
'''

### creating conda environment
'''

conda activate venv/
```
### Install all necessary libraries
```
pip install -r requirements.txt

To Add files to git 

''' 
git add . 

'''
Note : To ignore file or folder from git we can write name of file/folder in .gitignore file

### To check the git status

''' 
git status 
''' 

### To check all version maintained by git 

''' 
git log 
'''

### To create version/commit all changes by git 
''' 
git commit -m "message" 
'''

### To send version/changes to git

'''
 git push origin main

 '''
### To check Remote URL 

''' 
git remote -v 
'''

### To install setup.py

''' python setup.py install 
'''

## Research Paper

- [Research Paper](https://ntrs.nasa.gov/api/citations/20090029214/downloads/20090029214.pdf)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Run Locally

Clone the project

```bash
  git clone https://Romachauhan1607/Pred_maintainance-Project
```

## Code scaffolding
Run `model_training.py` to run the application apply model

## Optimizations

For performance improvement used hyperparameter optimization techniques (Grid search cv)

## Roadmap
- https://prnt.sc/yGLyW2h8iXhb


## Screenshots
![App Screenshot]
https://prnt.sc/qDvF-HHbh8JY
https://prnt.sc/YfcT6cNClY-1
https://prnt.sc/DaxC0-FF_0ZT
https://prnt.sc/nUQCqJr6OUHn
https://prnt.sc/P4rjM807zpj_
https://prnt.sc/mIMrdRu9R-mM

## Development server
Run `app.py` for a dev server. Navigate to http://127.0.0.1:5000/. The app will automatically reload if you change any of the source files.

## Tech
'''
**Client:** localhost

**Server:** Flask

## Deployment
To deploy this project 

```AWS Elasticbeanstalk

https://prnt.sc/Lg55Fl6MuHAx
 
```
## Demo
C:\Users\PC\Videos\Predict Maintenance - Google Chrome 2023-09-27 01-06-20.mp4

## Build
Run `python setup.py install` to build the project. The build artifacts will be stored in the `dist/` directory. 

## Running end-to-end tests
Run `application.py` to execute the end-to-end tests 

http://predictive-env-1.eba-5bwnxpqm.ap-south-1.elasticbeanstalk.com/

http://predictive-env-1.eba-5bwnxpqm.ap-south-1.elasticbeanstalk.com/predict

## Support

For support,ayushgandhi904@gmail.com,miqbal303@gmail.com or join our Slack channel.
