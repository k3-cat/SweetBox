from pathlib import Path
from typing import Dict

import toml

from .model import Model


class ModelMgr():
    def __init__(self, path=Path(__file__).parents[1] / 'config.toml'):
        self.path = path
        self.models: Dict[str, Model] = dict()
        if not self.path.exists():
            return
        for name, parm in toml.load(self.path)['models'].items():
            self.models[name] = Model(**parm)
        self.dump()

    def __getitem__(self, key: str) -> Model:
        return self.models[key]

    def dump(self) -> None:
        toml.dump(
            {
                'models':
                {name: self.models[name].to_dict()
                 for name in self.models.keys()}
            },
            self.path.open('w'),
        )

    def new_model(self, **kwargs) -> None:
        name = kwargs.pop('name').upper()
        if name in self.models:
            raise Exception()
        self.models[name] = Model(**kwargs)
        self.dump()
