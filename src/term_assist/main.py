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
from pathlib import Path
from shutil import copy
from subprocess import run

from yaml import safe_load

from term_assist.models.anthropic_model import AnthropicModel
from term_assist.models.openai_model import OpenAIModel

config_dir = Path.home() / ".config" / "term-assist"
config_file = config_dir / "config.yaml"
config_default_file = config_dir / "config_default.yaml"
models_file = config_dir / "models.yaml"


def main():
    args = _parse_args()
    _initialize_config()
    config, models = _load_config()
    system, shell = _load_environment()

    try:
        brand, brand_model = config["model"].split(":")
        config["model"] = brand_model
    except ValueError as e:
        if len(config["model"].split(":")) < 2:
            raise ValueError(
                f"Cannot parse model string '{config["model"]}'. Check configuration "
                f"file and ensure model brand and model type are separated by ':'."
            ) from e
        else:
            raise ValueError(
                f"Cannot parse model string '{config["model"]}'. Check configuration "
                f"file."
            ) from e

    if brand == "openai":
        model = OpenAIModel(config, models, system, shell)
    elif brand == "anthropic":
        model = AnthropicModel(config, models, system, shell)
    else:
        raise ValueError(f"Unknown brand '{brand}'. Check configuration file.")

    print(model.message(prompt=" ".join(args.prompt)))


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


def _initialize_config():
    # Create our config directory if it does not exist
    if not config_dir.exists():
        config_dir.mkdir(parents=True, exist_ok=True)

    # Copy over data files for easier user access
    for file in [config_default_file, models_file]:
        if not file.exists():
            copy(
                src=str(files("term_assist.data").joinpath(file.name)),
                dst=file,
            )

    # Copy default config if user config does not exist
    if not config_file.exists():
        copy(src=config_default_file, dst=config_file)


def _load_config():
    with open(config_file, "r") as f:
        config = safe_load(f)
    with open(models_file, "r") as f:
        models = safe_load(f)

    return config, models


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
