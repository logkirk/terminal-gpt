"""
Copyright 2024 Logan Kirkland

This file is part of terminal-gpt.

terminal-gpt is free software: you can redistribute it and/or modify it under the terms
of the GNU Affero General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

terminal-gpt is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with
terminal-gpt. If not, see <https://www.gnu.org/licenses/>.
"""

import anthropic
import argparse


def main():
    args = _parse_args()

    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        temperature=0.0,
        system="You are an assistant in a terminal window. Respond as succinctly as "
        "possible.",
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
        prog="terminal-gpt",
        description="A helpful terminal GPT.",
    )
    arg_parser.add_argument(
        "prompt",
        nargs="+",
        type=str,
        help="prompt for the AI model",
    )
    return arg_parser.parse_args()


if __name__ == "__main__":
    main()
