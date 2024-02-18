import random
import json


class Vocabulary():
    def __init__(self, file_name="ci.json", seed=0, n=5) -> None:
        self.seed = seed

        self.file_name = file_name
        self.vocabulary_set = self.read_json()

        self.n = n

    def read_json(self, file_name=None):
        if file_name is None:
            file_name = self.file_name
        with open(file_name, "r") as f:
            data = json.load(f)
        return data

    def select_words(self):
        random.seed(self.seed)
        return random.sample(self.vocabulary_set, self.n)

    def set_seed(self, seed):
        self.seed = seed
