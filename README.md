# Electric Meatball

*An electric meatball is a silly name for the human brain.*

## Setup
To setup the environment run the ```_setup.py``` script. This will give you an opinionated
environment setup for using the various scripts in this project. You will also need to customize
the configuration file, ```EMConfig.template.json```. To do so copy the template and rename the
copy to ```EMConfig.json```. Then add your OpenAI token, and model you wish to use, though it is
pre-configured for you sans OpenAI key. Keep in mind all things in the file are configurable.

## ```_em.py```
Just a simple prompt and answer system made with OpenAI's Python library. To use the script run the
```_em.py``` file in your terminal; e.g. ```python _em.py```.

The program expects only one "prompt" in the prompt file to be read at a time. The "response answer
file" is always appended to.

Sample of a single response in the answer file:

```
------RESPONSE START------ 2025-03-24 20:17:59.048592
Prompt:
------
Please give me code display date and time in US format from javascript's Date object.

--------
Answer:
------
To display the date and time in US format using JavaScript's `Date` object, you can leverage the `toLocaleString` method,
which allows you to specify the locale and formatting options. Here’s a simple example to achieve this:

'''javascript
const currentDate = new Date();

// Options for US date format
const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: true // Set to true for 12-hour format
};

// Format the date and time
const usFormattedDateTime = currentDate.toLocaleString('en-US', options);

console.log(usFormattedDateTime);
'''

Explanation:
- `new Date()` creates a new date object with the current date and time.
- `toLocaleString('en-US', options)` formats the date to US English format based on the provided `options`.
- The `options` object specifies:
  - `year`, `month`, `day`: To format the date as MM/DD/YYYY.
  - `hour`, `minute`, `second`: To include time.
  - `hour12`: Set to `true` for 12-hour time format (AM/PM).
  
Example Output:
If the current date and time is March 15, 2023, at 2:30:45 PM, the output would be:
'''
03/15/2023, 2:30:45 PM
'''

You can run the code in any JavaScript environment like a web browser console or Node.js.
------RESPONSE END------
```

## ```_pom.py```
A timer I use for Pomodoro focus sessions. After executing, it will ask you for an amount of time
in minutes (positive integer); this will set the timer, and start the clock. If no value, or a bad
value is given, then it defaults to 30 minutes. When the timer runs out, the script will make the
system beep for 2 seconds denoting the session is over (beep works on Windows, but is untested on
Linux/MacOS; however, the hook is there for it).

While ```_pom.py``` is running, you will see a timer counting down in your terminal.

To use the program run the ```_pom.py``` file in your terminal; e.g. ```python _pom.py```.

## ```_http_req.py``` OUTDATED
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
    "test_post" : {
        "verb": "post",
        "url": "http://localhost:3000/test/posttest",
        "body": {
            "name": "Cloud Strife"
        }
    },
    "get_other_thing" : {
        "verb": "get",
        "url": "https://youtube.com"
    },
    ...
}
```

To use the program run the ```_http_req.py``` file in your terminal; e.g. ```python http_req.py```.


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