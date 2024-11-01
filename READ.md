### Install Poetry
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
    source ~/.zshrc

### Verify Poetry Installation
    poetry --version

### Install dependencies with pip
    pip install -r requirements.txt
    pip install --upgrade selenium
    pip install --upgrade -r requirements.txt
    # Update the requirements
    pip freeze > requirements.txt

    poetry init
    poetry add selenium pytest
    poetry install

### pip
    pip --version
    pip3 --version
    pip install --upgrade pip
    pip show selenium

### PyPI
[PyPI repository](https://pypi.org/)

    @pytest.fixture(scope="function")
    function
    class
    module
    session

### Reports
    ## Allure
    brew install allure
    #Activate Your Virtual Environment 
    source venv/bin/activate
    pytest --alluredir=allure-results
