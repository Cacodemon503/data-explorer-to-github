### CSV reader
#### It checks if user exists on GitHub and configure new CSV with users basic info & languages statistics

Just create a CSV file with at least one column & make a name of it (for exapmle: `names`).

You can also use it for [StackOverflow Data Explorer](https://data.stackexchange.com/) to analyze if user with the same username exists on GitHub

You can make your own DB query or use an existed one from the [list](https://data.stackexchange.com/stackoverflow/queries?q=resume)
And they have their own simple [sql tutorial](https://data.stackexchange.com/tutorial)

#### Preparings:

[Create your token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

Copy token to `token.txt`, file must be in the same directory with an executable script

Or just copy your token directly into the code:

`headers = {"Authorization": "Token " +  "yourabcdefgh0123token"}`

#### How to launch:
* Open cmd/powershell/terminal
* `cd ~/path to script directory`
* `python3 ./csv-reader.py`
* Follow further program instructions

#### If you want to make it easily executable on linux:
Make a new empty `csv-reeader.py` file in the directory where you want to store it with `touch csv-reader.py` command

Add `#!/usr/bin/python3` at the top of the script

Copy all of the code to the new file & save it

Run: `chmod +x csv-reader.py` 

Add a Directory with your script to `$PATH:` permanently by running the following in Terminal:`nano ~/.bashrc`

Add in the end of the file `PATH=$PATH:~/YOUR NEW PATH TO SCRIPT`, mark it with `##PATH##` for further needs

Save & exit wtih: `ctrl+O` `ctrl+X`

Run: `source ~/.bashrc`

Confirm changes: `echo $PATH`

You'll see the path to your new directory in the end of the line

Now you can launch it in Terminal from every directory by running: `csv-reader.py` 
