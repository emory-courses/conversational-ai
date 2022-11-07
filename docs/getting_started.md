# Getting Started

## Python

* Install [Python 3.11.x](https://www.python.org/downloads/).
* Lower versions of Python may not be compatible to this course.

## Git Repository

* Login to [GitHub](https://github.com) (create an account if you do not have one). 
* Create a new repository called `conversational-ai` and make it **private**.
* From the `[Settings]` menu, add the instructors as collaborators of this repository.
  * Jinho Choi: [`jdchoi77`](https://github.com/jdchoi77)
  * Talyn Fan: [`talynfan`](https://github.com/talynfan)
  * Benjamin Ascoli: [`bossben`](https://github.com/bossben)

## PyCharm

* Install [PyCharm](https://www.jetbrains.com/pycharm/download/) on your local machine.
  * The following instructions assume that you have "PyCharm 2022.3.x Professional Edition".
  * You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Add your GitHub account:
  * Go to `[Preferences] - [Version Control] - [GitHub]`.
  * Press `[+]`, select `Log in via GitHub`, and follow the procedure.
    <!-- > If you are using two-factor authentication, click `[Use Token]` and login with your [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/). -->
* Create a new project:
  * Press the `[Get from VCS]` button on the `Welcome` prompt.
  * Choose `[GitHub]` on the left menu, select the `conversational-ai` repository, and press `[Clone]`.
    > Make sure the directory name is `conversational-ai`.
* Setup the interpreter:
  * Go to `[Preferences] - [Project: conversational-ai] - [Project Interpreter]`.
  * Click `Add Interpreter` and select `Add Local Interpreter`.
  * In the prompted window, choose `[Virtualenv Environment]` on the left menu, configure as follows then press `[OK]`:<br>
    : Environment: `New`<br>
    : Location: `LOCAL_PATH/conversational-ai/venv`<br>
    : Base interpreter: `Python 3.11`
* Upgrade [`pip`](https://pypi.org/project/pip/) (unless you have the latest version already):
  * Open a terminal by clicking `[Terminal]` at the bottom (or go to `[View] - [Terminal]`).
  * Type the following in the terminal:<br>
    ```bash
    python -m pip install --upgrade pip
    ```
* Install 

## Jupyter Notebook

* Open a terminal in PyCharm.
* Install [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html) by entering the following command in the terminal:
  ```
  pip install jupyter
  ```

## Programming

* Create a new package:
  * Create a python package called [`src.quiz`](../src/quiz/).
    > PyCharm may automatically create two `__init__.py` files, one under [`src`](../src/) and the other under [`src/quiz`](../src/quiz/). They are required for Python to treat these directories as packages, so leave those files as they are.
    > 
  * Create a python file called [`quiz0.py`](../src/quiz/quiz0.py) under the `quiz` package and copy the code.
    ```python
    from elit_tokenizer import EnglishTokenizer
    tokenizer = EnglishTokenizer()
    
    text = 'Welcome to the world of "Computational Linguistics"! We\'ll have lots of fun this semester.'
    sentences = tokenizer.decode(text, segment=2)
  
    for sentence in sentences:
        print(sentence.tokens)
        print(sentence.offsets)
    ```
  * Run `quiz0` by clicking `[Run] - [Run]`.
  * If it prompts the followings, your program runs successfully:
    ```json
    ['Welcome', 'to', 'the', 'world', 'of', '"', 'Computational', 'Linguistics', '"', '!']
    [(0, 7), (8, 10), (11, 14), (15, 20), (21, 23), (24, 25), (25, 38), (39, 50), (50, 51), (51, 52)]
    ['We', "'ll", 'have', 'lots', 'of', 'fun', 'this', 'semester', '.']
    [(53, 55), (55, 58), (59, 63), (64, 68), (69, 71), (72, 75), (76, 80), (81, 89), (89, 90)]
    ```
  * At any step, if it prompts you to add a new file/package to git, press `[Add]`.

* Install a package:
  * Go to `[Preferences] - [Project: conversational-ai] - [Project Interpreter]`.
  * Click the `+` button at the bottom.
  * Search and install for the `elit-tokenizer` package.


* Under the [`src/quiz/`](../src/quiz/) directory, create a new jupyter notebook called [`quiz0.ipynb`](../src/quiz/quiz0.ipynb).
* Copy the above code and run to see if it prompts the same output.