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
