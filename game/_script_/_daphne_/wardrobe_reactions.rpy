define dap_requirements = {
    "change_underwear": 5,
    "unequip_underwear": 15,
    "unequip_clothes": 3,
    "tattoos": 18,
    "headpat": 4,
    "touch_boobs": 12,
    "touch_pussy": 18
    }

label daphne_wardrobe_check(section, arg=None):
    if isinstance(arg, DollOutfit):
        python:
            temp_count = [0, 0, 0]
            temp_score = 0
            for item in arg.group:
                if dap_whoring < item.level and temp_count[0] < item.level:
                    temp_count[0] = item.level
                if item.type in ("bra", "panties"):
                    temp_count[2] += 1
                    if char_active.get_equipped(item.type) != None:
                        if not char_active.get_equipped(item.type).id == item.id:
                            if dap_whoring < dap_requirements["change_underwear"]:
                                temp_count[1] += 1

        # Outfit outrage score check
        if dap_whoring < temp_count[0]:
            call dap_main("Uh... I don't think so.",face="annoyed")
            $ temp_score += 1
        if temp_count[2] < 2 and dap_whoring < dap_requirements["unequip_underwear"]:
            if temp_score > 0:
                call dap_main("I'm not wearing that without underwear!",face="annoyed")
            else:
                call dap_main("Sorry [dap_genie_name] but I'm keeping my panties on.",face="annoyed")
            $ temp_score += 1
        elif temp_count[1] > 0:
            call dap_main("I like what I have on already, thanks.",face="annoyed")
            $ temp_score += 1

        if temp_score > 0:
            call dap_main("I'm not going to wear that, [dap_genie_name].",face="annoyed")
            #Hint
            $ wardrobe_fail_hint(max(temp_count[0], dap_requirements["change_underwear"], dap_requirements["unequip_underwear"]))
            return
    else:
        if section == "tabswitch":
            if dap_whoring < dap_requirements["tattoos"]:
                if wardrobe_chitchats:
                    call dap_main("I don't think so.",face="angry")
                #Hint
                $ wardrobe_fail_hint(dap_requirements["tattoos"])
                return False
            return True
        elif section == "category":
            # TODO: Simplify
            python:
                _value = arg
                _failure = False
                if arg[1] in ("bras", "panties"): # Intentional double check.
                    if dap_whoring < dap_requirements["change_underwear"]:
                        _value = ("category", None)
                        _failure = True

                    for i in char_active.clothes.itervalues():
                        if i[0]:
                            if i[0].blacklist and "bra" in i[0].blacklist and arg[1] == "bras":
                                _value = ("category", None)
                                break
                            if i[0].blacklist and "panties" in i[0].blacklist and arg[1] == "panties":
                                _value = ("category", None)
                                break
            if _failure:
                $ renpy.play('sounds/fail.mp3')
                call dap_main("Not happening.", face="annoyed")
                $ wardrobe_fail_hint(dap_requirements["change_underwear"])
            return _value
        elif section == "touching":
            $ random_number = renpy.random.randint(1, 3)
            if arg == "head":
                if dap_whoring < dap_requirements["headpat"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call dap_main("Don't!", face="angry")
                        elif random_number == 2:
                            call dap_main("I'm not interested, [dap_genie_name]...", face="annoyed")
                        elif random_number == 3:
                            call dap_main("Enough!", face="angry")
                        return
                else:
                    $ mouse_headpat()
                    call dap_main("", face="happy")
                    return
            elif arg == "boobs":
                if dap_whoring < dap_requirements["touch_boobs"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call dap_main("Don't make this weird!",face="annoyed")
                        elif random_number == 2:
                            call dap_main("{size=+5}Do NOT touch me like that!{/size}",face="angry")
                        elif random_number == 3:
                            call dap_main("Stop that!",face="annoyed")
                    return
            elif arg == "pussy":
                if dap_whoring < dap_requirements["touch_pussy"]:
                    $ mouse_slap()
                    if wardrobe_chitchats:
                        if random_number == 1:
                            call dap_main("Don't you dare!",face="annoyed")
                        elif random_number == 2:
                            call dap_main("Get your hands off me, [dap_genie_name].",face="annoyed")
                        elif random_number == 3:
                            call dap_main("I didn't come here to get molested.",face="annoyed")
                    return
            $ mouse_heart()
            call dap_main("", face="horny")
            return
        elif section == "toggle":
            if arg in ("bra", "panties"):
                if dap_whoring < dap_requirements["unequip_underwear"]:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 2)
                        if random_number == 1:
                            call dap_main("Uhm... No?",face="angry")
                        elif random_number == 2:
                            call dap_main("I'm keeping my underwear on...",face="angry")
                    #Hint
                    $ wardrobe_fail_hint(dap_requirements["unequip_underwear"])
                    return
            elif arg in ("top", "bottom"):
                if dap_whoring < dap_requirements["unequip_clothes"]:
                    if wardrobe_chitchats:
                        if arg == "top":
                            call dap_main("You... want me to take my clothes off?",face="annoyed")
                            g4 "Yes, please!"
                            call dap_main("{size=+5}NOT HAPPENING!{/size}",face="annoyed",mouth="shout")
                            m "......"
                        elif arg == "bottom":
                            call dap_main("Stay away, [dap_genie_name]!",face="annoyed",mouth="shout")
                    #Hint
                    $ wardrobe_fail_hint(dap_requirements["unequip_clothes"])
                    return
            $ char_active.toggle_wear(arg)
            return
        elif section == "equip":
            if arg.type in ("bra", "panties"):
                if dap_whoring < dap_requirements["unequip_underwear"]:
                    if char_active.get_equipped("bra"):
                        if arg.id == char_active.get_equipped("bra").id:
                            if wardrobe_chitchats:
                                call dap_main("Nope. Not happening.",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(dap_requirements["unequip_underwear"])
                            return
                    if char_active.get_equipped("panties"):
                        if arg.id == char_active.get_equipped("panties").id:
                            if wardrobe_chitchats:
                                call dap_main("You wish.",face="angry")
                            #Hint
                            $ wardrobe_fail_hint(dap_requirements["unequip_underwear"])
                            return
                if dap_whoring < arg.level:
                    call .too_much
                    return
            else:
                if dap_whoring < dap_requirements["unequip_clothes"]:
                    if arg.type in ("top", "bottom"):
                        if char_active.get_equipped("top"):
                            if arg.id == char_active.get_equipped("top").id:
                                if wardrobe_chitchats:
                                    call dap_main("No thanks.",face="annoyed")
                                #Hint
                                $ wardrobe_fail_hint(dap_requirements["unequip_clothes"])
                                return
                        if char_active.get_equipped("bottom"):
                            if arg.id == char_active.get_equipped("bottom").id:
                                if wardrobe_chitchats:
                                    call dap_main("Absolutely not.",face="angry")
                                #Hint
                                $ wardrobe_fail_hint(dap_requirements["unequip_clothes"])
                                return

                label .too_much:
                if dap_whoring < arg.level:
                    if wardrobe_chitchats:
                        $ random_number = renpy.random.randint(1, 3)
                        if random_number == 1:
                            call dap_main("I am NOT putting that on.",face="annoyed")
                        elif random_number == 2:
                            call dap_main("You are being creepy, old man.",face="annoyed")
                        else:
                            call dap_main("Not going to happen!",face="annoyed")
                    #Hint
                    $ wardrobe_fail_hint(arg.level)
                    return

                # Blacklist support
                if arg.blacklist:
                    if dap_whoring < dap_requirements["unequip_underwear"] and any(x in arg.blacklist for x in ("bra", "panties")):
                        call dap_main("I can't wear my underwear with this...", face="angry")
                        call dap_main("Well... I guess I can take it off for a little while...", face="annoyed")
                    elif dap_whoring < dap_requirements["unequip_clothes"] and any(x in arg.blacklist for x in ("top", "bottom")):
                        call dap_main("Ugh... I can't believe I'm doing this...", face="angry")

    $ renpy.play('sounds/equip.ogg')
    $ current_item = arg
    if isinstance(current_item, DollCloth) and current_item.type != "hair" and char_active.is_equipped(current_item.type) and char_active.clothes[current_item.type][0].id == current_item.id:
        $ char_active.unequip(current_item.type)
    else:
        $ char_active.equip(current_item)
    $ char_active.reset_blacklist()

    # Blacklist fallbacks
    if dap_whoring < dap_requirements["unequip_underwear"]:

        $ underwear_pass = True

        if not "bra" in char_active.blacklist and not char_active.is_equipped("bra"):
            $ underwear_pass = False
            $ char_active.equip(dap_bra_basic1)

        if not char_active.is_equipped("panties") and not "panties" in char_active.blacklist:
            $ underwear_pass = False
            $ char_active.equip(dap_panties_basic1)

        if not underwear_pass:
            call dap_main("My underwear is going back on.", face="annoyed")

    if dap_whoring < dap_requirements["unequip_clothes"]:
        $ clothes_pass = True

        if not "top" in char_active.blacklist and not char_active.is_equipped("top"):
            $ clothes_pass = False
            $ char_active.equip(dap_top_school1)

        if not char_active.is_equipped("bottom") and not "bottom" in char_active.blacklist:
            $ clothes_pass = False
            $ char_active.equip(dap_bottom_skirt1)

        if not clothes_pass:
            call dap_main("I'm just going to put my normal outfit back on then.", face="neutral")
    return
