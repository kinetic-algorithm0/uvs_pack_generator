import random as rng


class BoosterSlot:
    @staticmethod
    def card_rng(pool):
        card_number = rng.choice(pool)
        return card_number
