# Quiz 0: Getting Started

## Task

* Follow all instructions in the [Getting Started](../getting_started.md) page.
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
