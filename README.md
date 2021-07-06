## run 
to run ``` python root.py <your-github-personal-access-token>```


## Overview 

root.py is a root file for application, it imports function from functions.py

root uses token to access github account for more than 60 reqeust per hour limit,the token is enviromental variable
main function in root call's get_* functions for user input.

get_repos and list_repos are logging repositories search history in /log directory 


## Docker

creating docker image by ``` docker run -ti --name noxx ``` <br>
login into docker hub ```docker login -u <username> ``` <br>
changing name to image for repo ``` docker tag noxx <username>/git-noxx ```<br>
pushing to repo ``` docker push <username>/git-noxx ```<br>
