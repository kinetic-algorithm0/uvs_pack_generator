import json
import random as rng

import src.booster_sets.mha06 as mha06
import src.generators.booster_pack as pack_gen
import src.utils.stats as stats


class BoosterBox:
    def generate_box(self):
        card_tables = mha06.CardTables
        new_box = mha06.BoosterSetCharacteristics
        slot_pools = mha06.SlotPools
        ur_sr_packs = [rng.choice(new_box.packs_in_a_box)]
        xr_packs = [rng.choice(new_box.packs_in_a_box)]
        altch_packs = [rng.choice(new_box.packs_in_a_box)]
        booster_stats = stats.BoosterStats(c_selected=[], uc_selected=[], r_selected=[],
                                           ur_selected=[], sr_selected=[], xr_selected=[],
                                           ch_selected=[], altch_selected=[])
        box_layout = []

        x = 1
        while x < new_box.ur_sr_qty:
            ur_sr_packs.append(rng.choice([item for item in new_box.packs_in_a_box if item not in
                                           ur_sr_packs]))
            x += 1

        x = 1
        while x < new_box.xr_qty:
            xr_packs.append(rng.choice([item for item in new_box.packs_in_a_box if item not in
                                        xr_packs]))
            x += 1

        pack_number = 1
        while pack_number < new_box.packs_in_a_box.__len__() + 1:
            if pack_number == 1:
                new_pack, char = pack_gen.BoosterPack.slot_rng(card_tables, slot_pools, new_box, ur_sr_packs, xr_packs,
                                                               altch_packs, pack_number, booster_stats, prev_ch=None)
                box_layout.append({"pack_number": pack_number, "content": new_pack})
            else:
                new_pack, char = pack_gen.BoosterPack.slot_rng(card_tables, slot_pools, new_box, ur_sr_packs, xr_packs,
                                                               altch_packs, pack_number, booster_stats, prev_ch=char)
                box_layout.append({"pack_number": pack_number, "content": new_pack})
            pack_number += 1

        return json.dumps(box_layout, indent=4, sort_keys=True)
