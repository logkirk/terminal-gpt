terminal-gpt
============

[project](https://sr.ht/~logankirkland/terminal-gpt/) / 
[repo](https://git.sr.ht/~logankirkland/terminal-gpt) / 
[mailing list](https://lists.sr.ht/~logankirkland/terminal-gpt) /
[issues](https://todo.sr.ht/~logankirkland/terminal-gpt)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![builds.sr.ht status](https://builds.sr.ht/~logankirkland/terminal-gpt.svg)](https://builds.sr.ht/~logankirkland/terminal-gpt?)

> ℹ️ **Note**  
> The canonical project locations are linked above. Other locations are mirrors.

A basic CLI wrapper around Anthropic's Claude API to help out with 
terminal issues. The system prompt is:

> You are an assistant in a terminal window. Your system is {system} 
> and shell is {shell}. Your responses should be relevant to this 
> environment. Respond as succinctly as possible. If the response is 
> primarily a terminal command, respond only with that command and no 
> other text.

Installation
------------

In your terminal, [set your Anthropic API key as an environment
variable](https://docs.anthropic.com/en/docs/quickstart-guide#step-3-optional-set-up-your-api-key).

Create a virtual environment, activate it, and install dependencies
using:

```shell
python -m pip install requirements.txt
```

Command line usage
------------------

```shell
python terminal_gpt.py "unzip a tgz archive"
```
