# SSD api test Solution

### Pre-requisites

- Install Dokcer for Desktop :  
  For windows : https://docs.docker.com/desktop/windows/install/
  For linux   : https://docs.docker.com/desktop/linux/install/
- Create folder to store the test report
  Ex :
   For windows: D:/report
   For linux :/report

### Docker image repository
https://hub.docker.com/repository/docker/flanker64/ssd-api-test

### To execute tests locally using docker:

```

docker container run --rm -v <directory to store the test report>:/app/output <IMAGE NAME> <TAG>

Replace <IMAGE NAME> flanker/ssd-api-test:V1
Replace <TAG> with any of the following values
  - smoketest
  - test
To run multiple tests seperate the <TAG> using comma

Ex :
  docker container run --rm -v <directory to store the test report>:/app/output <image name> test1,test2,test3

```


### To execute tests locally without docker

#### Install testing solution dependencies
From root project folder execute the following command: ```pip install -r requirements.txt```

#### To execute tests locally:
Execute the following command, by replacing \<TAG\> by any scenario tags you would like to execute:
```
behavex -t <TAG>

```

### Test report 
'''
 The test report file (report.html) will be stored in the directory you have mentioned while running the test. 
'''

### Testing solution documentation
As the testing solution consists of a wrapper (called BehaveX) on top of Python Behave, please take a look at the Behave documentation:
https://behave.readthedocs.io/en/stable/






