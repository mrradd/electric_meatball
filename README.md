# Electric Meatbal

*An electric meatball is a silly name for the human brain.*

Just a simple prompt and answer system made with Python and OpenAI's Python library.

Copy the ```EMConfig.template.json``` file, and rename the copy to ```EMConfig.json```. Then add your OpenAI token, and 
model you wish to use. You may also customize the file names you wish to read the prompt from and write responses to.

```
//Example EMConfig.json
{
    "openAi": {
        "api_key": "your-api-key", //The API Key from OpenAI.
        "model": "gpt-4o-mini", //Can be any ChatGPT model.
        "organization": "your-organization" //Your super cool organization's name.
    },
    "promptFileName": "prompt.txt", //The name of the text file to read the prompt from. Must be a text file, and in the project's root directory.
    "responseAnswerFileName": "answerTextOnly.txt" //The name of the text file where answers will be appended to. Must be a text file and in the project's root directory.
}
```

The program expects only one "prompt" in the prompt file to be read at a time. The "response answer file" is always appended to.

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

Modules Used
- OpenAI ```pipx install openai```
