from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = "Package permettant de generer un ensemble de fichiers et de fichier en fonction de la configuration voulu."
LONG_DESCRIPTION = "Il s'agit d'un package qui permet de generer un ensemble de fichiers et de fichier en fonction de la configuration voulu."

# Setting up
setup(
       # the name must match the folder name 'pyarcgen'
        name="pyarcgen", 
        version=VERSION,
        author="BILONG NTOUBA Célestin",
        author_email="bilongntouba.celestin@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            "pytz;python_version>='2022.1'",
            "typing;python_version>='3.7.4.3'",
            "asyncio;python_version>='3.4.3'",
            "jonschema;python_version>='0.0.9119'",
        ],
        
        keywords=['python', 'hivi', 'pyarcgen', 'generator'],
        classifiers= [
            # "Headless CMS :: package :: Digibehive",
        ]
)