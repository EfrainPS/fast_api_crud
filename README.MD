# Welcome to this project!

### To run this project:

First, create a virtual environment whit venvironment

    `python -m venv name_of_environment`

Second, active you virtual environment

    **On windows**
        `name_of_environment\Scripts\activate.bat`

    **On unix or MacOS**
        `source name_of_environment/bin/activate`

Third, install all packages in requirements.txt file

    `pip install -r requirements.txt`

Fourth, run the project

    `uvicorn app.main:app --reload`

Fifth, enjoy and work.



Bonus! To generate a updated requirements.txt file. You should use

    `pip freeze > requirements.txt`