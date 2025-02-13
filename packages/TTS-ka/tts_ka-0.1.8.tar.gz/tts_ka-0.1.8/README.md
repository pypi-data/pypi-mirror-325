# Text to Speech 
This is a simple text to speech program that uses the `edge-tts` library to convert text to speech.

## Languages Supported
- Georgian
- English
- Russian

## Requirements
- [Python 3.6 or higher](https://www.python.org/downloads/)

## Installation and Usage
1. Install the package from PyPI:
    ```sh
    pip install text-to-speech
    ```
2. Use the package in your Python code:
    ```python
    from text_to_speech import text_to_speech

    text = "Hello, this is a text to speech conversion."
    text_to_speech(text, 'en')
    ```

## Running Tests
To run the tests, navigate to the `tests` directory and execute:
```sh
python -m unittest discover
```
