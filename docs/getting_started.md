# Getting Started

## Python

* Install [Python 3.11.x](https://www.python.org/downloads/).
* Lower versions of Python may not be compatible to this course.

## Git Repository

* Login to [GitHub](https://github.com) (create an account if you do not have one).
* Create a new repository called `conversational-ai` and make it **private**.
* From the `[Settings]` menu, add the instructors as collaborators of this repository.
  * Jinho Choi: [jdchoi77](https://github.com/jdchoi77)
  * Talyn Fan: [talynfan](https://github.com/talynfan)
  * Benjamin Ascoli: [bossben](https://github.com/bossben)

## PyCharm

* Install [PyCharm](https://www.jetbrains.com/pycharm/download/) on your local machine.
  * The following instructions assume that you have "PyCharm 2022.3.x Professional Edition".
  * You can get the professional version by applying for the [academic license](https://www.jetbrains.com/student/).
* Configure your GitHub account:
  * Go to `[Preferences] - [Version Control] - [GitHub]`.
  * Press `[+]`, select `Log in via GitHub`, and follow the procedure.
    <!-- > If you are using two-factor authentication, click `[Use Token]` and login with your [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/). -->
* Create a new project:
  * Press the `[Get from VCS]` button on the `Welcome` prompt.
  * Choose `[GitHub]` on the left menu, select the `conversational-ai` repository, and press `[Clone]`.
    > Make sure the directory name is `conversational-ai`.
* Setup an interpreter:
  * Go to `[Preferences] - [Project: conversational-ai] - [Project Interpreter]`.
  * Click `Add Interpreter` and select `Add Local Interpreter`.
  * In the prompted window, choose `[Virtualenv Environment]` on the left menu, configure as follows then press `[OK]`:
    - Environment: `New`
    - Location: `LOCAL_PATH/conversational-ai/venv`
    - Base interpreter: `Python 3.11`
* Install packages:
  * Open a terminal by clicking `[Terminal]` at the bottom (or go to `[View] - [Terminal]`).
  * Upgrade [pip](https://pypi.org/project/pip/) (if necessary) by entering the following command into the terminal:
    ```
    python -m pip install --upgrade pip
    ```
  * Install [Emora State Transitiona Dialogue Manager (STDM)](https://github.com/emora-chat/emora_stdm) with the following command:
    ```
    pip install emora_stdm
    ```
  * Install [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html) with the following command:
    ```
    pip install jupyter
    ```
  * If the terminal prompts "_Successfully installed_ ...", the packages are installed on your machine.