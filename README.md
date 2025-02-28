# Electric Meatball

*An electric meatball is a silly name for the human brain.*

## ```em.py```
Just a simple prompt and answer system made with Python and OpenAI's Python library.

To use the program run the ```em.py``` file in your terminal; e.g. ```python em.py```.

Setup the program by copying the ```EMConfig.template.json``` file, and rename the copy to
```EMConfig.json```. Then add your OpenAI token, and model you wish to use. You must add files
```gptAnswers.txt``` and ```userPrompt.txt``` to the project's root directory. You may use files
with custom names, but you will need to change the config file.

```
//Example EMConfig.json
{
    "openAi": {
        "api_key": "your-api-key", //The API Key from OpenAI.
        "model": "gpt-4o-mini", //Can be any ChatGPT model.
        "organization": "your-organization-name" //Your super cool organization's name.
    },
    "promptFileName": "userPrompt.txt", //The name of the text file to read the prompt from. Must
    be a text file, and in the project's root directory.
    "responseAnswerFileName": "gptAnswers.txt" //The name of the text file where answers will be
    appended to. Must be a text file and in the project's root directory.
}
```

The program expects only one "prompt" in the prompt file to be read at a time. The "response answer
file" is always appended to.

Sample of a single response in the answer file.
```
------RESPONSE START------

Prompt:
------

Tell me a joke.

==========

Answer:
------

Why did the scarecrow win an award? 

Because he was outstanding in his field!
------RESPONSE END------
```


## ```pom.py```
A timer I use for Pomodoro focus sessions. After executing, it will ask you for an amount of time
in minutes (positive integer); this will set the timer, and start the clock. If no value, or a bad
value is given, then it defaults to 30 minutes. When the timer runs out, the script will make the
system beep for 2 seconds denoting the session is over (beep works on Windows, but is untested on
Linux/MacOS; however, the hook is there for it).

While ```pom.py``` is running, you will see a timer counting down in your terminal.

To use the program run the ```pom.py``` file in your terminal; e.g. ```python pom.py```.


## ```http_req.py```
A very basic, quick and dirty, tool for hitting endpoints using a url that has some basic
configurability.

To start using this, copy the file ```http_request_config.template.json``` and rename it to
```http_request_config.json```, then customize it as needed. DO NOT COMMIT THIS FILE!!!!

To use the script to run a "request profile", you will need to modify one line of code in
```http_req.py``` located near the top of the file.
- ```profile_to_run = "get_thing"```
  - Change the value of ```profile_to_run``` to whatever your profile is you wish to run.

Sample config file with the profile ```get_thing```:
```
{
    "data_dump_file_path": "../electric_meatball/http_req_dumps/http_data_req_dump.txt",
    "pretty_json_indent": 2,
    "get_thing" : {
        "verb": "get",
        "url": "https://google.com"
    },
    "get_other_thing" : {
        "verb": "get",
        "url": "https://youtube.com"
    },
    ...
}
```

To use the program run the ```http_req.py``` file in your terminal; e.g. ```python http_req.py```.


## ***Modules Used In the Project***
- OpenAI - https://github.com/openai/openai-python
  - ```python -m pip install openai``` 
- Requests - https://requests.readthedocs.io/en/latest
  - ```python -m pip install requests```

### Style choices
- A line of code should end at 100 columns regardless of how many indents there are. This is
because it keeps it easy to work on with one screen and to review in split windows as there is
little chance for any horizontal overflow. Keep in mind this isn't a *hard* rule, but a
guideline.

### TODOs
- Allow for setting Pom's default timer value in the config file.
- Allow user to press a key to quit Pom.
- Allow user to press a key to pause/resume Pom.
- Save Pom session info to a JSON file for future review.
- Create a setup script that when run adds all files needed for the project to run.
- Allow for "conversations" with ChatGPT. Currently each prompt is treated as separate with no
context.
- Add support for other action verbs, like "POST", in http_req
- Add support for running a sequence of scripts in http_req.
- Add support for saving variables from requests.