import numpy as np
import src.utils.tools as tools


class BoosterStats:
    def __init__(self, c_selected, uc_selected, r_selected, ur_selected, sr_selected, xr_selected, ch_selected,
                 altch_selected):
        self.c_selected = c_selected
        self.uc_selected = uc_selected
        self.r_selected = r_selected
        self.ur_selected = ur_selected
        self.sr_selected = sr_selected
        self.xr_selected = xr_selected
        self.ch_selected = ch_selected
        self.altch_selected = altch_selected

    @staticmethod
    def tally_hits(booster_stats, table):
        card_names = []
        unique_elements, counts = np.unique(booster_stats, return_counts=True)
        for element in unique_elements:
            card_names.append(tools.BoosterTools.table_lookup(table, element))
        result = dict(zip(card_names, counts))
        return result
