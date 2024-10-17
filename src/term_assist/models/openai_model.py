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

from openai import OpenAI

from term_assist.models.model import Model


class OpenAIModel(Model):
    def __init__(self, config, models, system, shell):
        super().__init__(config, models, system, shell)
        self.client = OpenAI()

    def message(self, prompt):
        client = OpenAI()

        completion = client.chat.completions.create(
            model=self.models["openai"][self.config["model"]],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"],
            messages=[
                {
                    "role": "system",
                    "content": self.config["system_prompt"].format(
                        system=self.system, shell=self.shell
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        )

        return completion.choices[0].message.content
