# Quiz 0: Getting Started

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

## Programming

* Create a package called [`src`](../../src/) under the `conversational-ai` directory. 
  > PyCharm may automatically create the [`__init__.py`](../../src/__init__.py) file under `src`, which is required for Python to treat the directory as a package, so leave the file as it is.
* Create the [`quiz`](../../src/quiz/) package under the `src` package.
* Create a python file called [`quiz0.py`](../../src/quiz/quiz0.py) under the `quiz` package and copy the code.
  > If PyCharm prompts you to add `quiz0.py` to git, press `[Add]`.
  ```python
  from emora_stdm import DialogueFlow

  chatbot = DialogueFlow('start')
  transitions = {
      'state': 'start',
      '"Hello. How are you?"': {
          '[{fine, good, fantastic}]': {
              '"Glad to hear that you are doing well :)"': {
                  'error': {
                      '"See you later!"': 'end'
                  }
              }
          },
          'error': {
              '"I hope your day gets better soon :("': {
                  'error': {
                      '"Take care!"': 'end'
                  }
              }
          }
      }
  }

  if __name__ == '__main__':
      chatbot.load_transitions(transitions)
      chatbot.run()
  ```
* Run `quiz0` by clicking `[Run] - [Run 'quiz0']`.
* Conduct the following two dialogues with the chatbot you just created (`S`: system, `U`: user):
  * Dialogue 1 
    ```
    S: Hello. How are you?
    U: I'm good
    S: Glad to hear that you are doing well :)
    U: Thanks
    S: See you later!
    ```
  * Dialogue 2
    ```
    S: Hello. How are you?
    U: It's not going well
    S: I hope your day gets better soon :(
    U: Hopefully
    S: Take care!
    ```

## Submission

* Create a file called [`.gitignore`](../../.gitignore) under the `conversational-ai` directory and copy the content:
  ```
  .idea/
  venv/
  **/.ipynb_checkpoints/
  ```
* Add the following files to git (if not already) by right-clicking on those files and selecting `[Git] - [Add]`:
  * `quiz/quiz0.py`
  * `.gitignore`
  > Once the files are added to git, they should turn into green. If not, restart PyCharm and try to add them again.
* Commit and push your changes to GitHub:
  * Right-click on `conversational-ai`.
  * Select `[Git] - [Commit Directory]`.
  * Enter a commit message (e.g., _Submit Quiz 0_).
  * Press the `[Commit and Push]` button.
  > Make sure you both `commit` and `push`, not just `commit`.
* Check if the above files are properly pushed to your GitHub respoistory.
* Submit the address of your repository (e.g., https://github.com/your_id/conversational-ai.git) to Canvas.
