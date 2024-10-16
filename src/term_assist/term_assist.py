"""
Copyright 2024 Logan Kirkland

This file is part of term-assist.

term-assist is free software: you can redistribute it and/or modify it under the terms
of the GNU Affero General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

term-assist is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with
term-assist. If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import os
import platform
from importlib.resources import files
from subprocess import run

import anthropic
from yaml import safe_load


def main():
    args = _parse_args()
    prefs = _load_prefs()
    models = _load_models()
    system, shell = _load_environment()

    client = anthropic.Anthropic()

    message = client.messages.create(
        model=models[prefs["model"]],
        max_tokens=prefs["max_tokens"],
        temperature=prefs["temperature"],
        system=prefs["system_prompt"].format(system=system, shell=shell),
        messages=[
            {
                "role": "user",
                "content": " ".join(args.prompt),
            }
        ],
    )

    print(message.content[0].text)


def _parse_args() -> argparse.Namespace:
    """Parses any command line arguments."""
    arg_parser = argparse.ArgumentParser(
        prog="ta",
        description="term-assist: a helpful terminal GPT.",
    )
    arg_parser.add_argument(
        "prompt",
        nargs="+",
        type=str,
        help="prompt for the AI model",
    )
    return arg_parser.parse_args()


def _load_prefs():
    try:
        with files("term_assist.data").joinpath("config.yaml").open("r") as f:
            return safe_load(f)
    except FileNotFoundError:
        with files("term_assist.data").joinpath("config_default.yaml").open("r") as f:
            return safe_load(f)


def _load_models():
    with files("term_assist.data").joinpath("models.yaml").open("r") as f:
        return safe_load(f)


def _load_environment():
    system = f"{platform.system()} {platform.release()}"
    shell = (
        run(f"{os.environ.get("SHELL")} --version", shell=True, capture_output=True)
        .stdout.decode()
        .strip("\n")
    )
    return system, shell


if __name__ == "__main__":
    main()
