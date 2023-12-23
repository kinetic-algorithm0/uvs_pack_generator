class CardTables:
    c_table = []
    uc_table = []
    r_table = []
    ur_table = []
    sr_table = []
    xr_table = []
    ch_table = []
    altch_table = []

    with open("sets/mha/jet_burn/mha06_commons.txt", "r") as f:
        raw_content = f.readlines()

    for line in raw_content:
        c_table.append(line.strip())

    with open("sets/mha/jet_burn/mha06_uncommons.txt", "r") as f:
        raw_content = f.readlines()

    for line in raw_content:
        uc_table.append(line.strip())

    with open("sets/mha/jet_burn/mha06_rares.txt", "r") as f:
        raw_content = f.readlines()

    for line in raw_content:
        r_table.append(line.strip())

    with open("sets/mha/jet_burn/mha06_ultra_rares.txt", "r") as f:
        raw_content = f.readlines()

    for line in raw_content:
        ur_table.append(line.strip())

    with open("sets/mha/jet_burn/mha06_secret_rares.txt", "r") as f:
        raw_content = f.readlines()

    for line in raw_content:
        sr_table.append(line.strip())

    # with open("mha06_extra_rares.txt", "r") as f:
    #     raw_content = f.readlines()
    #
    # for line in raw_content:
    #     full_set_table.append(line.strip())

    with open("sets/mha/jet_burn/mha06_characters.txt", "r") as f:
        raw_content = f.readlines()

    for line in raw_content:
        ch_table.append(line.strip())

    with open("sets/mha/jet_burn/mha06_alt_characters.txt", "r") as f:
        raw_content = f.readlines()

    for line in raw_content:
        altch_table.append(line.strip())


class SlotPools:
    c_pool = list(range(0, 47))
    uc_pool = list(range(0, 38))
    r_pool = list(range(0, 29))
    ur_pool = list(range(0, 22))
    sr_pool = list(range(0, 6))
    xr_pool = list(range(0, 195))
    ch_pool = list(range(0, 17))
    altch_pool = list(range(0, 17))


class BoosterSetCharacteristics:
    slots_in_a_pack = list(range(1, 12))
    packs_in_a_box = list(range(1, 25))
    c_slots = list(range(1, 7))
    uc_slots = list(range(7, 9))
    r_plus_slots = [10]
    xr_slots = [9]
    altch_slots = [11]
    ur_sr_qty = 7
    xr_qty = 4
