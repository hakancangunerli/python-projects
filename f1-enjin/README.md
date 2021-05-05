# enjin <img src="https://img.shields.io/badge/Python-3.8.3-gree"> 


## info
gets a csv data and manipulates it to show you which engine suppliers provide what speed. 


 ## tech
- python (3.8.3)



## setup 

clone this project. 

suggest that you put all this project within a `venv` **BEFORE** you start running it , but it's your disk space after all :)))

make sure you have all the necessary components before trying to run the project, which could be accessed from `requirements.txt`. just install them all with the ``pip3 install -r requirements.txt`` command. 

after all the necessary components are installed, the only thing you have to do is to run `python3 data.py`

done! 

it'll read the csv data, which is gathered from ergast.com, gets constructor and time data ( in seconds) , does the math to fit into the hh:mm:ss format and then average them.

## todo
[ ] retrieve csv data 