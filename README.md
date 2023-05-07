# Grill Valley Bot
This is the official repository of the one and only *Grill Valley Bot*. You can peek around the code we wrote to handle the bot. If you think that there are features to add or bug to fix contact us. **No merge-request will be accepted** if not discussed beforehand. If you instead think that my software engineer skills are really low, you are probably right, but trust me that I will still sleep tonight.

## How to:
To run the bot (obviosuly on an unix-like system) the steps are quite simple:
- copy or edit the `example_vars.sh` and fill the required variables
- source the file:
    ```
    $> source vars.sh
    ```
- make sure that python3 is installed. Create a virtual environment (if you name it differently remember to update the `.gitignore` accordingly):
    ```
    $> python3 -m venv virtual
    $> . virtual/bin/activate
    ```
- install the requirements
    ```
    $> pip install -r requirements.txt
    ```
- run the bot
    ```
    $> python3 bot.py
    ```

## Change Log
*Disclaimer: this is not a standardized changelog, nor a precise one that will track everything we do. Just some reminder*

- May 3rd, 2023 (night): Placed the first stone of the bot, after some days of discussing about it. The `start` command is finished. Lost really a lot of time into writing a funny and catchy intro message for our bot. Lots of ideas useful for implement for this bot
- May 4th, 2023 (morning): Setted up the github repository, and tidied a little bit up. Now I should get back to my real job.
- May 6th, 2023 (morning to night, with pauses): Created a DB for the bot. Added some basic tables to the schema. Created all the functions to query the DB. They should have been done using some DTO, of course I am a pig and I did not, just plain (but sanitized) SQL queries. Feels like *ridin' in the 90s*.
- May 7th, 2023 (morning): The subscription part is almost done. The backbone of the bot is basically set. Now it is only about tweaking it.

## (Funny) Milestones
Here we will score our funny/interesting milestones on this project:

- There are two languages for the bot: Italian, if your telegram language is set to italian, and English in any other case. First step to welcome also Erasmus' students and foreigners (and to make me swear a lot when re-writing the messages). Yay! *EDIT: Yes it made me swear a lot and only 3 days have passed*
- The flower near your name in the `/start` command is actually *for you*. It is not random, but it is picked by a function that takes in input your name and returns a flower. You might want to check it out in `utils.py`. There is also an easter egg in that function