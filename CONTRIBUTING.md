# Contributing to FreeLunch 
Welcome to the contributing guidelines for the FreeLunch repository.

We use github to host code, to track issues and feature requests, as well as accept pull requests. So make sure you know how to develop using GitHub. You can refer to this [git-guide](http://rogerdudler.github.io/git-guide/) for a quick reference.

You can contribute to this project by:

- Discussing the current state of the code
- Directly committing an easier change
- Reporting a Bug
- Submitting a Fix

 ### Discussing the current state of the code

In case you have something to discuss about the current state of code, you can always contact the owners of the repository.
To contact us, send a mail to <freelunchbits@gmail.com>

 ### Directly committing an easier change
- If you are making slight changes in documentation, adding comments or docstrings, changing small pieces of code, fixing minor bugs or doing anything that does not require any further discussion with the mentors, feel free to send a pull request by creating a new branch. :)

**Note: All PRs must be directed only to the development branch unless instructed otherwise.**
 - You can use the commands below to push a commit after making required changes.
    - Check the status of the files you have changed. Red text corresponds to the unadded changes.
    ```
    git status
    ```
    - **Note** : Before pushing please ensure that all cache files(like __pycache__) have been removed.
    ```
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
    ```
    - Add the changes you have made. You can add a specific chnage or all the changes at once.
    ```
    git add <filename>
    git add *
    ```
    - Commit the changes you have added.  
    ```
    git commit -m "Commit message"
    ```
    - Push the changes to the remote repository.
    ```
    git push origin master
    ```
**Note** : If your patch is accepted kindly make necessary changes to the documentation as well it helps us keep a track of the features. Refer to [#48](https://github.com/BITS-Periodical-Society/freelunch/issues/48) for notes on Sphinx.
 ### Reporting a Bug
We use GitHub [issues](https://github.com/BITS-Periodical-Society/freelunch/issues) to track bugs.  Report a bug by [opening a new issue](https://github.com/BITS-Periodical-Society/freelunch/issues/new)(If a issue doesn't already exist addressing the bug); it's that easy!

 Write bug reports with detail, background, and sample code.

 **Great Bug Reports** tend to have:

 - A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

 ### Submitting a Fix
If you are not sure what you are doing or if you need to discuss a change with the mentors make a pull request instead of committing directly.
Pull requests are the best way to propose changes to the codebase and discuss it with other developers.
**Kindly note that all pull requests must be directed to the development branch only unless instructed otherwise.**
All kinds of pull requests are welcome, so don't hesitate and go ahead. You can initiate a pull request [here](https://github.com/BITS-Periodical-Society/freelunch/pulls).
