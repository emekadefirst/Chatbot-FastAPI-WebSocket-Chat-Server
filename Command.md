To create virtual environment in python 
        python -m venv your-environmen-tname

To start virtual environment in python
        cd venv   --- change directory into the virtual environment folder 
        source ./Scripts/activate  --- This command starts the virtual environment
        cd ..    ---This command change directory out of your virtual enviromnet

To run the server 
        uvicorn main:app --reload