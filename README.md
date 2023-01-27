# Problem Analysis and Software Design Proof of Technology Group 19
#### Emmanouil Kalostypis, Antonis Charalambous & Abi Raveenthiran

## Installation 
Download and unzip the main branch of this repository.\
Then, we recommend to use a virtual environment to install the required packages.\
If you don't want to use a virtual environment skip to [No virtual environment](#no-virtual-environment).

### Virtual environment
If you don't have pipenv installed yet, you can install it by running the following line in your terminal.
```python
pip install --user pipenv
```
Once you've successfully installed pipenv,  in the terminal, navigate to the PASD-POT-main folder you just unzipped.\
Now you can create a virtual environment by entering the following line in the terminal.
```python
pipenv shell
```
If you closed your terminal or virtual environment, navigate back to the folder again and start up the virtual environment using:
```python
pipenv shell
```

Now to install the required packages, enter the following line in the terminal:
```python
pipenv install -r requirements.txt
```

### No virtual environment
Navigate to the folder you created in the terminal and enter the following line:
```python
pip install -r requirements.txt
```

## Usage
In the terminal, navigate to the disruptive_delivery folder, where the manage.py file is.\
This folder should be in the root of the PASD-POT-main folder.\
Then enter the following line in the terminal to run the server:
```python
python manage.py runserver
```

Now you can access the web app in your browser with the link given in the terminal:\
Which should be at http://localhost:8000
