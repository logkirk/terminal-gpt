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
terminal issues. The system prompt is:

> You are an assistant in a terminal window. Your system is {system}
> and shell is {shell}. Your responses should be relevant to this
> environment. Respond as succinctly as possible. If the response is
> primarily a terminal command, respond only with that command and no
> other text.

Installation
------------

1. In your terminal, [set your Anthropic API key as an environment
   variable](https://docs.anthropic.com/en/docs/quickstart-guide#step-3-optional-set-up-your-api-key).

### Homebrew installation

### `pipx` installation

1. [Install `pipx`](https://pipx.pypa.io/stable/installation/)

2. Download the latest build:
    - Look for the latest successful
      build [here](https://builds.sr.ht/~logankirkland/term-assist).
    - Go to the build page and download the artifact
      `term_assist.whl`.
    - Build artifacts are eventually pruned from sourcehut. If the
      artifact no longer exists, **continue to step 2**. Otherwise,
      **skip to step 8**.

3. [Install Rust](https://rustup.rs/)
4. Clone the repository:

   ```shell
   git clone https://git.sr.ht/~logankirkland/term-assist
   ```

5. Create and activate a Python virtual environment.
6. Install the Python `build` module:

   ```shell
   python -m pip install --upgrade build
   ```

7. Build `term-assist`:

   ```shell
   python -m build
   ```

8. Install the wheel using `pipx`:

   ```shell
   pipx install /path/to/whl
   ```

Command line usage
------------------

```
usage: ta [-h] prompt [prompt ...]

A helpful terminal GPT.

positional arguments:
  prompt      prompt for the AI model

options:
  -h, --help  show this help message and exit
```
