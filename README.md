**Task** 
Create Jenkin pipeline with custom validation rules for GIT checking

**Description**

Validate lint errors - especially syntax and indendation errors upon git push to the main repository and notify devs about the lint failure and list of errors
by sending out an email notification 

Repository name is - Jenkins-task

**Tools required**

Utilizing Lint tool such as flake8 to perform lint validation
          SMTP library to send out email notifications

**Methodology**
Combination of Git hooks, a linter (such as flake8), and a simple Python script named - lint_email.py
Creating a pre commit hook and making sure it runs the above python script upon git push 
Storing email passwords and username as environment variables in the py script and storing their values as GIT secrets 
Creating a yaml workflow that triggers the lint_email.py script upon each push.

**Script breakdown**
script automatically extracts the email and name of the developer who made the latest commit using the git log command. 
The _get_latest_commit_author_ function retrieves the author's information, and this information is then used to send the email. 
The email is sent to the author of the latest commit, and no manual entry of email or username is required in the script.
