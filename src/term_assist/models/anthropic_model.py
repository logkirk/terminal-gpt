from anthropic import Anthropic

from term_assist.models.model import Model


class AnthropicModel(Model):
    def __init__(self, config, models, system, shell):
        super().__init__(config, models, system, shell)
        self.client = Anthropic()

    def message(self, prompt):
        message = self.client.messages.create(
            model=self.models["anthropic"][self.config["model"]],
            max_tokens=self.config["max_tokens"],
            temperature=self.config["temperature"],
            system=self.config["system_prompt"].format(
                system=self.system, shell=self.shell
            ),
            messages=[{"role": "user", "content": prompt}],
        )

        return message.content[0].text
