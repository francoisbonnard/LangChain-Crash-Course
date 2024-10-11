# Video

[LangChain Master Class For Beginners 2024](https://www.youtube.com/watch?v=yF9kGESAi3M)

[Where am I ?](https://youtu.be/yF9kGESAi3M?si=7YUPv2unz6PDkzYW&t=1251)

#  Install Poetry

    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

Copy Installation Path: Once the installation is complete, it will provide you with a path. Copy this path as you'll need to add it to your user environment variables.

    C:\Users\franc\AppData\Roaming\Python\Scripts

ou avec Powershell :
    
    $env:Path
    $env:Path += ";C:\Users\franc\AppData\Roaming\Python\Scripts"
    [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\franc\AppData\Roaming\Python\Scripts", [EnvironmentVariableTarget]::User)
    [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\103677\AppData\Roaming\Python\Scripts\", [EnvironmentVariableTarget]::User)



test poetry

        poetry --version

Install dépendances depuis le fichier pyproject.toml

    poetry install --no-root

Vérifier les configurations qui sont dans ~/.cache/pypoetry/virtualenvs/

    poetry config --list


start poetry

    poetry shell        

Retirer les liens bleus zigzag

    Spawning shell within C:\Users\103677\AppData\Local\pypoetry\Cache\virtualenvs\langchain-crash-course-AemLJ--Y-py3.11

ctrl + shift + P : select interpreter path

choose : enter interpreter path 

enter path displayed after `start poetry` command (see above sentence starting with : "Spawning")

Voir les packages

    poetry show
    poetry add dotenv


[More about Poetry](https://www.youtube.com/watch?v=Ji2XDxmXSOM)

# Explore different models

[Chat Model Documents](https://python.langchain.com/v0.2/docs/integrations/chat/)

# Firebase 

## AWS Amplify
L'équivalent de Firebase chez Amazon est AWS Amplify. AWS Amplify est une plateforme de développement d'applications proposée par Amazon Web Services (AWS) qui offre une gamme complète d'outils pour créer, déployer et gérer des applications web et mobiles. Comme Firebase, AWS Amplify simplifie le développement backend avec des services comme l'authentification, les API (REST et GraphQL), les bases de données (via AWS DynamoDB), le stockage de fichiers, et les notifications push. Amplify est entièrement intégré avec l'écosystème AWS, offrant aux développeurs la flexibilité et la puissance de la plateforme cloud d'AWS tout en permettant une scalabilité et une sécurité robustes pour leurs applications.

## Firestore
Firestore, ou Cloud Firestore, est une base de données NoSQL en temps réel proposée par Firebase. Elle est conçue pour stocker et synchroniser des données entre les applications web et mobiles à l'échelle mondiale. Les données dans Firestore sont organisées en collections et documents, où chaque document contient des paires clé-valeur et peut être structuré avec des types de données imbriqués.





