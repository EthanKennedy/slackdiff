# slackdiff

Slackdiff is your tool for transparent employee evacuation. The tool is inspired by hipdiff: https://github.com/Calabresi/hipdiff 

# How to use

To use, clone this repository to a directory on your laptop. Create a file called `.key` that contains your slack API key. run `./slackdiff.py` in the directory of the script. The first run will populate a `slackdiff.json` file with a current breakdown of your organizations slack directory. Subsequent runs will alert you when accounts have been set to a `deleted` status, and new accounts have been added/existing accounts have changed names. 