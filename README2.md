# Video

(LangChain Master Class For Beginners 2024)[https://www.youtube.com/watch?v=yF9kGESAi3M]

#  Install Poetry

    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

Copy Installation Path: Once the installation is complete, it will provide you with a path. Copy this path as you'll need to add it to your user environment variables.

    C:\Users\franc\AppData\Roaming\Python\Scripts


test poetry

        poetry --version

Install dépendances depuis le fichier pyproject.toml

    poetry install --no-root

Vérifier les configurations qui sont dans ~/.cache/pypoetry/virtualenvs/

    poetry config --list


start poetry

    poetry shell        

ctrl + shift + P : select interpreter path

choose : enter interpreter path 

enter path displayed after `start poetry` command