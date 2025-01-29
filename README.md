# Electric Meatbal

*An electric meatball is a silly name for the human brain.*

## ```Main.py```
Just a simple prompt and answer system made with Python and OpenAI's Python library.

To use the program run the Main.py file in your terminal; e.g. ```python Main.py```.

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

## ```Pom.py```
A timer I use for Pomodoro focus sessions. After executing, it will ask you for an amount of time
in minutes (positive integer); this will set the timer, and start the clock. If no value, or a bad
value is given, then it defaults to 30 minutes. When the timer runs out, the script will make the
system beep for 2 seconds denoting the session is over (beep works on Windows, but is untested on
Linux/MacOS; however, the hook is there for it).

While ```Pom.py``` is running, you will see a timer counting down in your terminal.

To use the program run the Pom.py file in your terminal; e.g. ```python Pom.py```.

## ***Modules Used In the Project***
- OpenAI ```python -m pip install openai``` https://github.com/openai/openai-python

### TODOs
- Allow for setting Pom's default timer value in the config file.
- Allow user to press a key to quit Pom.
- Allow user to press a key to pause/resume Pom.
- Save Pom session info to a JSON file for future review.
- Create a setup script that when run adds all files needed for the project to run.
- Allow for "conversations" with ChatGPT. Currently each prompt is treated as separate with no
context.