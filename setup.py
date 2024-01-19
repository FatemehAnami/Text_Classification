import setuptools

# For representing Readme file in case of publishing library 
with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text_Classification"
AUTHOR_USER_NAME = "FatemehAnami"
SRC_REPO = "Text_Classification"
AUTHOR_EMAIL = "fatemeh.anami@gmail.com"
    
setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A Python End To End Text Classification Project",
    long_description= long_description,
    long_description_content = "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "BUG Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"": "src"},
    packages = setuptools.find_packages(where = "src")
)    
