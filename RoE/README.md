# xchange <img src="https://img.shields.io/badge/Python-3.8.3-gree"> 


## info
using transferwise api data, it gives you the current USD/TRY exchange rate.
i need this cause it is constantly changing

### NOTE
you need your own api token for this. get one from [here](https://sandbox.transferwise.tech/register)

 ## tech
- python (3.8.3)



## setup 

clone this project. 

suggest that you put all this project within a `venv` **BEFORE** you start running it , but it's your disk space after all :)))

make sure you have all the necessary components before trying to run the project, which could be accessed from `requirements.txt`. just install them all with the ``pip3 install -r requirements.txt`` command. 

after all the necessary components are installed, the only thing you have to do is to run `python3 xchange.py`

done! 

it'll read the transferwise data, which is gathered from their api , gets  data ( in seconds) ,then give you the current info.

## todo
- [ ] make it pretty 
