term-assist
===========

[project](https://sr.ht/~logankirkland/term-assist/) /
[repo](https://git.sr.ht/~logankirkland/term-assist) /
[mailing list](https://lists.sr.ht/~logankirkland/term-assist) /
[issues](https://todo.sr.ht/~logankirkland/term-assist)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![builds.sr.ht status](https://builds.sr.ht/~logankirkland/term-assist.svg)](https://builds.sr.ht/~logankirkland/term-assist?)

> ℹ️ **Note**  
> The canonical project locations are linked above. Other locations are
> mirrors.

A basic CLI wrapper around Anthropic's Claude API to help out with
terminal issues.

<img src="tgz.png" width="300" alt="[screenshot: ta unzip a tgz archive]"/>
<img src="vim.png" width="530" alt="[screenshot: ta how to exit vim]"/>

Features
--------

- **Configurable parameters**: change Claude model, system prompt,
  response length, and other parameters
- **Automatic environment detection**: automatically detects your system
  and shell environment for accurate responses

Installation
------------

1. [Install `pipx`](https://pipx.pypa.io/stable/installation/)

2. Install `term-assist` using `pipx`:

   ```shell
   pipx install term-assist
   ```

3. In your terminal, [set your Anthropic API key as an environment
   variable](https://docs.anthropic.com/en/docs/quickstart-guide#step-3-optional-set-up-your-api-key).

Usage
-----

```
usage: ta [-h] prompt [prompt ...]

A helpful terminal GPT.

positional arguments:
  prompt      prompt for the AI model

options:
  -h, --help  show this help message and exit
```

### Examples

```
> ta unzip a tgz archive
```

```
> ta how to exit vim
```

Configuration
-------------

The configuration file is `~/.config/term-assist/config.json` and will
be created on first run and initialized with default configuration
parameters if it does not already exist.

See `~/.config/term-assist/config_default.json` for the default
configuration.

### `model`

The AI model to use.

See `~/.config/term-assist/models.json` for available models.

### `max_tokens`

The maximum number of tokens that will be generated for output.

### `temperature`

The amount of randomness injected into the response. Ranges from 0.0 to
1.0.

### `system_prompt`

The system prompt that is given to the model.

This prompt must contain the format strings `{system}` and `{shell}`,
which the program will replace with information it gathers from your
system.
