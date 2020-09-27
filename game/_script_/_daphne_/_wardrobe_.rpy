###############
## Character ##
###############

default daphne = Doll(name="daphne",
                        clothes={"hat":        [None, 15, True],
                                 "hair":       [None, 22, True],
                                 "earring":    [None, 14, True],
                                 "neckwear":   [None, 11, True],
                                 "robe":       [None, 28, True],
                                 "gloves":     [None, 21, True],
                                 "top":        [None, 15, True],
                                 "bra":        [None, 9, True],
                                 "bottom":     [None, 8, True],
                                 "garterbelt": [None, 7, True],
                                 "panties":    [None, 6, True],
                                 "stockings":  [None, 5, True],
                                 "buttplug":   [None, -1, True],
                                 "pubes":      [None, 3, True],
                                 "tattoo0":    [None, 1, True],
                                 "tattoo1":    [None, 1, True],
                                 "tattoo2":    [None, 1, True],
                                 "tattoo3":    [None, 1, True],
                                 "tattoo4":    [None, 1, True],
                                 "piercing0":  [None, 2, True],
                                 "piercing1":  [None, 2, True],
                                 "piercing2":  [None, 2, True],
                                 "piercing3":  [None, 2, True],
                                 "piercing4":  [None, 2, True],
                                 "accessory0": [None, 12, True],
                                 "accessory1": [None, 12, True],
                                 "accessory2": [None, 12, True],
                                 "accessory3": [None, 12, True],
                                 "accessory4": [None, 12, True],
                                 "makeup0":    [None, 3, True],
                                 "makeup1":    [None, 3, True],
                                 "makeup2":    [None, 3, True],
                                 "makeup3":    [None, 3, True],
                                 "makeup4":    [None, 3, True]},
                        face={"tears":    [None, 12, True],
                              "cheeks":   [None, 7, True],
                              "eyebrows": ["base", 11, True],
                              "eyes":     ["base", 8, True],
                              "pupils":   ["mid", 9, True],
                              "mouth":    ["base", 13, True]},
                        body={"armleft": ["on_hips", 3],
                              "armright":["on_hips", -1],
                              "base":    ["front", 0],
                              "breasts": ["normal", 2]})

###################
## School Outfit ##
###################

default dap_hair_base = DollCloth("daphne", ("head", "hair"), "hair", "base", [[255, 235, 180, 255]], unlocked=True)

default dap_top_school_1  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_1",[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_2  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_2",[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_3  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_3",[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_4  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_4",[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_5  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_5",[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_6  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_6",[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_7  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_7",[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_8  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_8",[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True)
default dap_top_school_9  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_9",[[183, 183, 184, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True, level=3)
default dap_top_school_10  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_10",[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True, level=10)
default dap_top_school_11  = DollCloth("daphne", ("tops", "shirts"), "top", "top_school_11",[[183, 183, 184, 255], [109, 105, 121, 255], [58, 115, 75, 255], [205, 205, 206, 255]], armfix=True, unlocked=True, level=13)


default dap_top_casual_1  = DollCloth("daphne", ("tops", "shirts"), "top", "casual_1",[[130, 100, 160, 255]], armfix=True, unlocked=True)
default dap_top_casual_2  = DollCloth("daphne", ("tops", "shirts"), "top", "casual_2",[[130, 100, 160, 255]], armfix=True, unlocked=True, level=3)
default dap_top_casual_3  = DollCloth("daphne", ("tops", "shirts"), "top", "casual_3",[[135, 200, 225, 255]], armfix=True, unlocked=True)
default dap_top_casual_4  = DollCloth("daphne", ("tops", "shirts"), "top", "casual_4",[[135, 200, 225, 255]], armfix=True, unlocked=True, level=3)
default dap_top_casual_5  = DollCloth("daphne", ("tops", "shirts"), "top", "casual_5",[[135, 200, 225, 255]], armfix=True, unlocked=True, level=6)

default dap_bottom_school_1  = DollCloth("daphne", ("bottoms", "skirts"), "bottom", "school_skirt_1",[[103, 90, 108, 255]], armfix=True, unlocked=True)
default dap_bottom_school_2  = DollCloth("daphne", ("bottoms", "skirts"), "bottom", "school_skirt_2",[[103, 90, 108, 255]], armfix=True, unlocked=True)
default dap_bottom_school_3  = DollCloth("daphne", ("bottoms", "skirts"), "bottom", "school_skirt_3",[[103, 90, 108, 255]], armfix=True, unlocked=True, level=3)
default dap_bottom_school_4  = DollCloth("daphne", ("bottoms", "skirts"), "bottom", "school_skirt_4",[[103, 90, 108, 255]], armfix=True, unlocked=True, level=10)
default dap_bottom_school_5  = DollCloth("daphne", ("bottoms", "skirts"), "bottom", "school_skirt_5",[[103, 90, 108, 255]], armfix=True, unlocked=True, level=13)

default dap_bottom_casual_1  = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "casual_bottom_1",[[100, 115, 150, 255], [112, 112, 112, 255]], armfix=True, unlocked=True)
default dap_bottom_casual_2  = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "casual_bottom_2",[[255, 255, 255, 255], [255, 255, 255, 255], [185, 185, 200, 255]], armfix=True, unlocked=True)
default dap_bottom_casual_3  = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "casual_bottom_3",[[255, 255, 255, 255], [255, 255, 255, 255], [185, 185, 200, 255]], armfix=True, unlocked=True, level=3)
default dap_bottom_casual_4  = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "casual_bottom_4",[[255, 255, 255, 255], [255, 255, 255, 255], [185, 185, 200, 255]], armfix=True, unlocked=True, level=6)

default dap_bra_1 = DollCloth("daphne", ("bras", "bras"), "bra", "bra_1",[[58, 115, 75, 255]], unlocked=True)
default dap_bra_2 = DollCloth("daphne", ("bras", "bras"), "bra", "bra_2",[[58, 115, 75, 255], [255, 255, 255, 255], [28, 28, 28, 255]], unlocked=True)
default dap_bra_3 = DollCloth("daphne", ("bras", "bras"), "bra", "bra_3",[[58, 115, 75, 255], [255, 255, 255, 255], [28, 28, 28, 255], [28, 28, 28, 255]], unlocked=True)

default dap_panties_1 = DollCloth("daphne", ("panties", "panties"), "panties", "panties_1",[[58, 115, 75, 255], [255, 255, 255, 255]], armfix=True, unlocked=True)
default dap_panties_2 = DollCloth("daphne", ("panties", "panties"), "panties", "panties_2",[[58, 115, 75, 255], [255, 255, 255, 255], [28, 28, 28, 255]], armfix=True, unlocked=True)
default dap_panties_3 = DollCloth("daphne", ("panties", "panties"), "panties", "panties_3",[[58, 115, 75, 255], [255, 255, 255, 255], [28, 28, 28, 255], [28, 28, 28, 255]], armfix=True, unlocked=True)

default dap_stockings_1 = DollCloth("daphne", ("legwear", "stockings"), "stockings", "stockings_1",[[255, 255, 255, 255]], armfix=True, unlocked=True)
default dap_stockings_2 = DollCloth("daphne", ("legwear", "stockings"), "stockings", "stockings_2",[[96, 96, 96, 255], [45, 45, 48, 255]], armfix=True, unlocked=True)
default dap_stockings_3 = DollCloth("daphne", ("legwear", "stockings"), "stockings", "stockings_3",[[45, 45, 48, 255], [45, 45, 48, 255]], armfix=True, unlocked=True, level=3)
default dap_stockings_4 = DollCloth("daphne", ("legwear", "stockings"), "stockings", "stockings_4",[[45, 45, 48, 255], [45, 45, 48, 255], [45, 45, 48, 255], [45, 45, 48, 255]], armfix=True, unlocked=True, level=3)

#default dap_hair_base_new = DollCloth("daphne", ("head", "hair"), "hair", "new", [[243, 158, 189, 255], [254, 218, 238, 255]], unlocked=True)
#default dap_neckwear_beads = DollCloth("daphne", ("head", "neckwear"), "neckwear", "choker_beads",[[45, 45, 48, 255], [177, 168, 172, 255]], unlocked=True)
#default dap_gloves_auror = DollCloth("daphne", ("misc", "gloves"), "gloves", "auror_gloves",[[45, 45, 48, 255]], armfix=True, unlocked=True)
#default dap_top_auror  = DollCloth("daphne", ("tops", "auror"), "top", "auror",[[28, 27, 31, 255], [124, 42, 50, 255]], armfix=True, unlocked=True)
#default dap_top_auror2 = DollCloth("daphne", ("tops", "auror"), "top", "auror2",[[124, 42, 50, 255]], armfix=True, unlocked=True)
#default dap_robe_auror = DollCloth("daphne", ("tops", "robes"), "robe", "auror_coat",[[40, 40, 41, 255], [174, 165, 169, 255]], armfix=True, unlocked=True)
#default dap_bottoms_leggings = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "leggings",[[45, 45, 48, 255]], armfix=True, unlocked=True)
#default dap_bottoms_leggings_hole = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "leggings_hole",[[45, 45, 48, 255]], level=60, armfix=True, unlocked=True)
#default dap_stockings_auror = DollCloth("daphne", ("legwear", "stockings"), "stockings", "auror",[[45, 45, 48, 255], [177, 168, 172, 255]], armfix=True, unlocked=True)

default dap_outfit_default = DollOutfit([dap_hair_base, dap_top_school_1, dap_bottom_school_1, dap_bra_1, dap_panties_1, dap_stockings_1], True)
default dap_outfit_last = DollOutfit([dap_hair_base])

##########
## Misc ##
##########

#default dap_top_corset = DollCloth("daphne", ("tops", "auror"), "top", "corset",[[247, 206, 146, 255]], blacklist=["bra"], unlocked=True)
#default dap_bottoms_jeans = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "jeans",[[51, 104, 105, 255]], unlocked=True)
#default dap_panties_base = DollCloth("daphne", ("panties", "panties"), "panties", "base",[[124, 42, 50, 255]], unlocked=True)
#default dap_bra_base = DollCloth("daphne", ("bras", "bras"), "bra", "bikini",[[124, 42, 50, 255], [177, 168, 172, 255]], unlocked=True)

############
## Extras ##
############

#default dap_top_exauror3  = DollCloth("daphne", ("tops", "shirts"), "top", "extras_auror3",[[28, 27, 31, 255], [124, 42, 50, 255]], armfix=True, unlocked=True)
#default dap_top_exauror4  = DollCloth("daphne", ("tops", "shirts"), "top", "extras_auror4",[[28, 27, 31, 255], [124, 42, 50, 255]], armfix=True, unlocked=True)
#default dap_top_excorset2 = DollCloth("daphne", ("tops", "shirts"), "top", "extras_corset2",[[247, 206, 146, 255]], level=30, unlocked=True)
#default dap_top_exshirt1 = DollCloth("daphne", ("tops", "shirts"), "top", "extras_shirt_1",[[230, 50, 70, 255]], unlocked=True)
#default dap_top_exshirt2 = DollCloth("daphne", ("tops", "shirts"), "top", "extras_shirt_2",[[230, 50, 70, 255]], unlocked=True)
#default dap_top_exshirt3 = DollCloth("daphne", ("tops", "shirts"), "top", "extras_shirt_3",[[230, 50, 70, 255]], unlocked=True)

#default dap_bottoms_expants1 = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "extras_pants_1",[[240, 200, 155, 255], [130, 130, 120, 255], [205, 205, 205, 255]], armfix=True, unlocked=True)
#default dap_bottoms_expants2 = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "extras_pants_2",[[155, 200, 220, 255], [130, 130, 120, 255], [205, 205, 205, 255]], armfix=True, unlocked=True)
#default dap_bottoms_expants3 = DollCloth("daphne", ("bottoms", "trousers"), "bottom", "extras_pants_3",[[155, 200, 220, 255], [130, 130, 120, 255], [205, 205, 205, 255], [245, 245, 255, 255]], armfix=True, unlocked=True)

#default dap_extras_bikini1 = DollCloth("daphne", ("bras", "bras"), "bra", "extras_bikini_1",[[100, 220, 200, 255], [255, 255, 255, 255], [200, 200, 200, 255]], unlocked=True)
#default dap_extras_bikinib1 = DollCloth("daphne", ("panties", "panties"), "panties", "extras_bikinib_1",[[100, 220, 200, 255], [255, 255, 255, 255]], unlocked=True)

#default dap_extras_stockings1 = DollCloth("daphne", ("legwear", "stockings"), "stockings", "extras_stockings_1",[[177, 168, 172, 255], [45, 45, 48, 255]], armfix=True, unlocked=True)