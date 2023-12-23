import src.generators.booster_slot as slot_gen
import src.utils.tools as tools


class BoosterPack:
    @staticmethod
    def slot_rng(card_tables, slot_pools, new_box, ur_sr_packs, xr_packs, altch_packs, pack_number, booster_stats,
                 prev_ch):
        pack_contents = []
        char_roll = prev_ch
        for slot in new_box.slots_in_a_pack:
            if slot in new_box.c_slots:
                roll = slot_gen.BoosterSlot.card_rng(slot_pools.c_pool)
                pack_contents.append(tools.BoosterTools.table_lookup(card_tables.c_table, roll))
                booster_stats.c_selected.append(roll)
            if slot in new_box.uc_slots:
                pack_contents.append(tools.BoosterTools.table_lookup(card_tables.uc_table,
                                                                     slot_gen.BoosterSlot.card_rng(slot_pools.uc_pool)))
            if slot in new_box.xr_slots:
                if pack_number in xr_packs:
                    pack_contents.append(f"{slot_gen.BoosterSlot.card_rng(slot_pools.xr_pool)} XR")
                else:
                    pack_contents.append(tools.BoosterTools.table_lookup(card_tables.uc_table,
                                                                         slot_gen.BoosterSlot.card_rng(slot_pools.uc_pool)))
            if slot in new_box.r_plus_slots:
                if pack_number in ur_sr_packs and pack_number == ur_sr_packs[6]:
                    pack_contents.append(tools.BoosterTools.table_lookup(card_tables.sr_table,
                                                                         slot_gen.BoosterSlot.card_rng(slot_pools.sr_pool)))
                elif pack_number in ur_sr_packs:
                    pack_contents.append(tools.BoosterTools.table_lookup(card_tables.ur_table,
                                                                         slot_gen.BoosterSlot.card_rng(slot_pools.ur_pool)))
                else:
                    pack_contents.append(tools.BoosterTools.table_lookup(card_tables.r_table,
                                                                         slot_gen.BoosterSlot.card_rng(slot_pools.r_pool)))
            if slot in new_box.altch_slots:
                if pack_number in altch_packs:
                    pack_contents.append(f"{tools.BoosterTools.table_lookup(card_tables.altch_table, slot_gen.BoosterSlot.card_rng(slot_pools.altch_pool))} ALT-CH")
                elif pack_number == 1:
                    char_roll = slot_gen.BoosterSlot.card_rng(slot_pools.ch_pool)
                    pack_contents.append(tools.BoosterTools.table_lookup(card_tables.ch_table, char_roll))
                else:
                    char_roll = slot_gen.BoosterSlot.card_rng([item for item in slot_pools.ch_pool if item not in [prev_ch]])
                    pack_contents.append(tools.BoosterTools.table_lookup(card_tables.ch_table, char_roll))

        return pack_contents, char_roll
