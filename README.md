terminal-gpt
============

Description
-----------

A basic wrapper around Anthropic's API to help out with terminal
issues. The system prompt is:

> You are an assistant in a terminal window. Respond as succinctly as 
> possible.

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

License
-------

Copyright 2024 Logan Kirkland <logan@logankirk.land>

This file is part of terminal-gpt.

terminal-gpt is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

terminal-gpt is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with terminal-gpt. If not, see <https://www.gnu.org/licenses/>.
