from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, config, models, system, shell):
        self.config = config
        self.models = models
        self.system = system
        self.shell = shell
        self.client = None

    @abstractmethod
    def message(self, prompt):
        pass
