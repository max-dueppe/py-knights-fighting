class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = Effect(effect)


class Effect:
    def __init__(self, effect_dict: dict) -> None:
        self.hp = effect_dict["hp"] if effect_dict.get("hp") else 0
        self.power = effect_dict["power"] if effect_dict.get("power") else 0
        self.protection = (effect_dict["protection"]
                           if effect_dict.get("protection")
                           else 0)
