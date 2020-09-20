
label summon_daphne:

    $ active_girl = "daphne"
    $ last_character = "daphne"

    $ daphne_busy = True

    call update_dap_tier

    call play_music("daphne")
    call play_sound("door")

    # Clothes Events
    call daphne_summon_setup

    label daphne_requests:
    # Hair fix
    #$ daphne.get_equipped("hair").color = daphne_haircolor
    #$ daphne_haircolor = daphne.get_equipped("hair").color

    # Reset
    call reset_menu_position
    call dap_main(xpos="base",ypos="base")
    $ hide_transitions = False

    menu:

        # Talk
        "-Talk-" (icon="interface/icons/small/talk.png"):
            if not chitchated_with_daphne:
                call daphne_chit_chat
                jump daphne_talk
            else:
                jump daphne_talk


        # Favours
        #"-Sexual favours-" (icon="interface/icons/small/condom.png"):
        #    jump daphne_favor_menu

        # Fireplace Chats
        #"-Let's hang-" (icon="interface/icons/small/toast.png") if (wine_ITEM.number > 0 and nt_he_drink.counter == 0) or (firewhisky_ITEM.number > 0 and nt_he_drink.counter > 0):
        #    jump daphne_hangout

        #"{color=[menu_disabled]}-Let's hang-{/color}" (icon="interface/icons/small/toast.png") if (firewhisky_ITEM.number < 1 and nt_he_drink.counter > 0):
        #    m "(I don't have any firewhisky...)"
        #    jump daphne_requests

        #"{color=[menu_disabled]}-Let's hang-{/color}" (icon="interface/icons/small/toast.png") if (wine_ITEM.number < 1 and nt_he_drink.counter == 0):
        #    m "(I don't have any wine...)"
        #    jump daphne_requests

        # Wardrobe
        "-Wardrobe-" (icon="interface/icons/small/wardrobe.png") if daphne_wardrobe_unlocked:
            hide screen daphne_main with d1
            $ screenshot_image = ScreenshotImage.capture()
            $ renpy.call_in_new_context("wardrobe", "dap_main")
            with d2
            jump daphne_requests

        "{color=[menu_disabled]}-Hidden-{/color}" if not daphne_wardrobe_unlocked:
            call nar(">You haven't unlocked this feature yet.")
            jump daphne_requests


        # Gifts
        "-Gifts-" (icon="interface/icons/small/gift.png") if not gave_daphne_gift:
            call gift_menu
            jump daphne_requests

        "{color=[menu_disabled]}-Gifts-{/color}" (icon="interface/icons/small/gift.png") if gave_daphne_gift:
            m "I already gave her a gift today."
            jump daphne_requests

        # Dismiss
        "-Never mind-":
            stop music fadeout 3.0

            if daytime:
                dap "I'm going back to class then, [dap_genie_name]."
            else:
                dap "Good night then, [dap_genie_name]."

            call play_sound("door")

            jump end_daphne_event


# daphne level up
label update_dap_tier:
    if dap_tier == 1 and nt_he.favors_E2:
        $ dap_level_up = 1

    return

label daphne_level_up(tier=None):

    call bld
    if tier == 1:
        g9 "(Time to teach those students something useful!)"

    $ dap_tier = tier+1
    $ dap_level_up = None

    pause.5
    call nar(">Daphne has reached level "+str(dap_tier)+"!")

    call update_dap_tier

    return


# Daphne Requests Menu
label daphne_favor_menu:
    # call update_daphne_favors

    menu:
        "-Level Up-" (icon="interface/icons/small/levelup.png") if dap_level_up != None:
            call daphne_level_up(tier=dap_level_up)
            jump daphne_requests

        "{color=[menu_disabled]}-Personal Favours-{/color}" (icon="interface/icons/small/heart_red.png"):
            call not_available
            jump daphne_favor_menu
            #
            # Uncomment once favours are ready
            #

            # label .personal:
            # python:
                # menu_choices = []
                # for i in nt_favor_list:
                    # if i in []: # Not in the game yet.
                        # menu_choices.append(("{color=[menu_disabled]}-Not Available-{/color}","na"))
                    # elif i.start_tier > dap_tier:
                        # menu_choices.append(("{color=[menu_disabled]}-Not ready-{/color}","vague"))
                    # else:
                        # menu_choices.append(i.get_menu_item())

                # menu_choices.append(("-Never mind-", "nvm"))
                # result = renpy.display_menu(menu_choices)
            # if result == "nvm":
                # jump daphne_favor_menu
            # elif result == "vague":
                # call favor_not_ready
                # jump .personal
            # elif result == "na":
                # call not_available
                # jump .personal
            # else:
                # $ renpy.jump(result)

        "-Public Requests-" (icon="interface/icons/small/star_yellow.png") if daytime and daphne_requests_unlocked:
            jump daphne_requests_menu

        "{color=[menu_disabled]}-Public Requests-{/color}" (icon="interface/icons/small/star_yellow.png") if not daytime or not daphne_requests_unlocked:
            if not daphne_requests_unlocked:
                call nar(">You haven't unlocked this feature yet.")
            elif not daytime:
                call nar(">Public requests are available during the day only.")
            jump daphne_favor_menu

        "-Never mind-":
            jump daphne_requests

label daphne_requests_menu:
    call update_dap_requests
    python:
        menu_choices = []
        for i in nt_requests_list:
            if i in []: # Not in the game yet.
                menu_choices.append(("{color=[menu_disabled]}-Not Available-{/color}","na"))
            elif i.start_tier > dap_tier:
                menu_choices.append(("{color=[menu_disabled]}-Not ready-{/color}","vague"))
            else:
                menu_choices.append(i.get_menu_item())
        menu_choices.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(menu_choices)

    if result == "nvm":
        jump daphne_favor_menu
    elif result == "vague":
        call favor_not_ready
        jump daphne_requests_menu
    elif result == "na":
        call not_available
        jump daphne_requests_menu
    else:
        $ renpy.jump(result)

label update_dap_requests:
    # Set event tier to current daphne tier if they are different
    python:
        for i in nt_requests_list:
            if i.tier != dap_tier and i.max_tiers >= dap_tier:
                i.tier = dap_tier

    return



label daphne_talk:
    menu:
        # TODO: Finish up
        # "-Ask about outfit upgrades-" (icon="interface/icons/small/wardrobe.png"):
            # call clothing_upgrades
            # jump daphne_requests

        #"-Ask for help with Quidditch-" (icon="interface/icons/small/quidditch.png") if cho_quid.lock_practice and cc_st.match_counter == 1:
        #    m "Got a moment?"
        #    call dap_main("Sure just make it quick.","open","base","base","mid")
        #    m "I have a problem with...{w=0.5}{nw}"
        #    call dap_main("I'll have to stop you right there.","upset","base","worried","mid")
        #    call dap_main("if you want to cry out about your problems, at least offer me a drink first...","open","closed","worried","mid")
        #    call dap_main("","upset","closed","worried","mid")
        #    m "(Is in this school at least ONE person that has no problems with alcohol...?)"
        #    jump daphne_talk

        #"-Get naked!-" if daphne_strip_happened and (not daphne.is_worn("top") or not daphne.is_worn("bottom") or not daphne.is_worn("robe")):
        #    m "Get naked, [daphne_name]!"
        #    call dap_main("Of course, [dap_genie_name].","horny","base","base","ahegao")
        #    hide screen daphne_main
        #    with d3
        #
        #    $ daphne.strip("all")
        #    pause.8

        #    call dap_main("Do you like it, [dap_genie_name]?","horny","base","raised","mid")
        #    call dap_main("The exposed body of one of your subordinates?","open_wide_tongue","base","raised","ahegao")
        #    g4 "I do, [daphne_name]!"
        #    g9 "You should teach like that!"
        #    call dap_main("Hmm...","base","base","base","R")
        #    call dap_main("I like the way you think, [dap_genie_name]!","horny","base","base","mid")
        #    jump daphne_requests

        #"-Get dressed-" if daphne_strip_happened and not daphne.is_any_worn("top", "bottom", "robe"):
        #    m "Put on some clothes, would you..."
        #    m "This is a school, after all."
        #    call dap_main("Of course, [dap_genie_name].","base","base","base","mid")
        #    hide screen daphne_main
        #    with d3
        #
        #    $ daphne.wear("all")
        #    pause.8

        #    call dap_main("...","base","base","base","mid")
        #    jump daphne_requests

        "-Address me only as-":
            menu:
                "-Sir-":
                    label .sir: # Local label unavailable from global scope
                    $ dap_genie_name = "Sir"
                    call dap_main("Very well, [dap_genie_name].",face="neutral")
                    jump daphne_talk
                "-Dumbledore-":
                    label .dumbledore:
                    $ dap_genie_name = "Dumbledore"
                    call dap_main("Fine, [dap_genie_name].",face="neutral")
                    jump daphne_talk
                "-Professor-":
                    label .professor:
                    $ dap_genie_name = "Professor"
                    call dap_main("Very well, [dap_genie_name].",face="neutral")
                    jump daphne_talk

                "-Old man-":
                    label .old_man:
                    $ dap_genie_name = "Old man"
                    call dap_main("You actually want me to call you Old Man?",face="annoyed",mouth="skeptical")
                    m "It's in good humor of course!"
                    g9 "I like being called silly names."
                    call dap_main("As you wish, [dap_genie_name].",face="neutral")
                    jump daphne_talk

                "-Snake Tamer-":
                    label .snake_tamer:
                    call dap_main("Snake Tamer?",face="surprised")
                    call dap_main("What is that supposed to mean exactly?",face="annoyed")
                    m "Well, you and your sister are both from House Slytherin."
                    g9 "So I'm a snake tamer of sorts."
                    if dap_whoring < 10:
                        call dap_main("What?! You think you've tamed me?",face="angry")
                        g11 "Uh... no! That's not what I meant at all."
                        call dap_main("I am NOT calling you that.",face="angry")
                        call nar(">Try again at whoring 10.")
                    else:
                        $ dap_genie_name = "Snake Tamer"
                        call dap_main("You think you've tamed me?",face="happy",mouth="skeptical")
                        call dap_main("Very well, [dap_genie_name].",face="happy",mouth="skeptical",pupils="R")
                        call dap_main("Just remember, this snake can bite.",face="happy",mouth="skeptical")
                        g11 "..."
                    jump daphne_talk

                "-Big Boss-":
                    label .big_boss:
                    $ dap_genie_name = "Big Boss"
                    call dap_main("You want me to call you [dap_genie_name]?",face="annoyed")
                    g9 "I think it's a pretty solid name."
                    call dap_main("What exactly makes you a big boss?",face="annoyed")
                    m "..."
                    m "... ..."
                    m "... ... ..."
                    call dap_main("Sir?",face="annoyed")
                    g9 "Kept you waiting, huh?"
                    call dap_main("(Sigh)",face="annoyed",eyes="closed")
                    jump daphne_talk

                "-Daddy-":
                    label .daddy:
                    call dap_main("Daddy?",face="surprised")
                    if dap_whoring < 10:
                        call dap_main("You want me to call you... Daddy?",face="surprised", mouth="frown")
                        g16 "I'm probably old enough to be your daddy."
                        call dap_main("Sir, I think that's a bit too personal.",face="annoyed")
                        if ast_genie_name == "Daddy":
                            g16 "Astoria calls me Daddy, so why can't you?"
                            if dap_whoring < 6:
                                call dap_main("That doesn't surprise me in the slightest.",face="annoyed")
                                call dap_main("The answer is still no.",face="annoyed")
                                call nar(">Try again at whoring 6.")
                                jump daphne_talk
                            else:
                                $ dap_genie_name = "Daddy"
                                call dap_main("Fine! If that's what you really want.",face="annoyed")
                                call dap_main("...",face="annoyed")
                                call dap_main("...[dap_genie_name].",face="annoyed")
                                jump daphne_talk
                        else:
                            call nar(">Try again at whoring 10.")
                            jump daphne_talk
                    else:
                        $ dap_genie_name = "Daddy"
                        call dap_main("Very well, [dap_genie_name].",face="happy")
                        call dap_main("You better treat me like a daughter then!",face="happy")
                        jump daphne_talk

                "-Master-":
                    label .master:
                    call dap_main("Master?",face="surprised")
                    if dap_whoring < 15:
                        call dap_main("Okay, that's just weird.",face="annoyed")
                        if dap_genie_name == "Daddy":
                            m "So \"Master\" is weird, but \"Daddy\" isn't?"
                            call dap_main("...",face="annoyed")
                        m "Come on, it's like when you are learning karate or something."
                        m "The teacher is always the master!"
                        call dap_main("It's NOT like that, and you know it.",face="annoyed")
                        m "Fine... nevermind."
                        call nar(">Try again at loyalty 15.")
                        jump daphne_talk
                    else:
                        $ dap_genie_name = "Master"
                        call dap_main("Hmm...",face="neutral")
                        call dap_main("Very well, [dap_genie_name].",face="neutral")
                        jump daphne_talk

                "{color=[menu_disabled]}-Custom Input--{/color}" if dap_whoring < 60:
                    m "(I don't think she's yet ready for that)"
                    jump daphne_talk

                "-Custom Input-" if dap_whoring >= 60:
                    $ temp_name = renpy.input("(Please enter the name.)", dap_genie_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()

                    if temp_name.lower() in ("sir", "dumbledore", "professor", "old man", "snake tamer", "big boss", "daddy", "master"):
                        #if temp_name.lower() == "master" and dap_whoring < 15:
                        #    jump daphne_talk.master_fail
                        $ renpy.jump("daphne_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump daphne_talk
                    else:
                        $ dap_genie_name = temp_name
                        call dap_main("Very well, [dap_genie_name].",face="neutral")
                    jump daphne_talk

                "-Never mind-":
                    jump daphne_talk


        "-From now on I will address you as-":
            menu:
                "-Daphne-":
                    label .daphne: # Local label unavailable from global scope.
                    $ daphne_name = "Daphne"
                    call dap_main("Sure, [dap_genie_name].",face="neutral")
                    jump daphne_talk

                "-Miss Greengrass-":
                    $ daphne_name = "Miss Greengrass"
                    call dap_main("I'm fine with that, [dap_genie_name].",face="neutral")
                    jump daphne_talk

                "-Girl-":
                    $ daphne_name = "Girl"
                    call dap_main("If that's what you want, [dap_genie_name].",face="neutral")
                    jump daphne_talk

                "-Bitch-":
                    if dap_whoring < 15:
                        call dap_main("What?!",face="surprised")
                        call dap_main("Absolutely not!",face="surprised")
                        m "Jeez, no need to be a bitch about it."
                        call dap_main("Grr...",face="surprised")
                        call nar(">Try again at loyalty 15.")
                    else:
                        $ daphne_name = "Bitch"
                        call dap_main("Bitch?",face="surprised")
                        call dap_main("More like Queen Bitch.",face="happy")
                        m "Yes, the queen is implied of course."
                        call dap_main("Very well, Bitch it is.",face="happy")
                    jump daphne_talk

                "-Slut-":
                    if dap_whoring < 10:
                        call dap_main("What?!",face="surprised")
                        call dap_main("I am not a slut!",face="angry")
                        m "Hey, what's wrong with being a slut?"
                        call dap_main("Grr...",face="angry")
                        call nar(">Try again at whoring 10.")
                    else:
                        $ daphne_name = "Slut"
                        call dap_main("Slut?",face="surprised")
                        call dap_main("Do you think I'm a slut?",face="surprised")
                        g16 "I call all my favorite students \"Slut\"!"
                        g16 "It's in a playful way, you know."
                        #if daphne_wear_top == False and daphne_wear_bra == False:
                        #    call dap_main("Well, having my boobs out is pretty slutty.","open","down")
                        call dap_main("Very well, Slut it is.",face="neutral")
                    jump daphne_talk

                "{color=[menu_disabled]}-Custom Input--{/color}" if dap_whoring < 60:
                    m "(I don't think she's yet ready for that)"
                    jump daphne_talk

                "-Custom Input-" if dap_whoring >= 15:
                    $ temp_name = renpy.input("(Please enter the name.)", daphne_name, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ", length=14)
                    $ temp_name = temp_name.strip()
                    if temp_name.lower() in ("daphne", "miss greengrass", "girl", "bitch", "slut"):
                        #if temp_name.lower() == "slut" and dap_whoring < 15:
                        #    jump daphne_talk.slut_fail
                        $ renpy.jump("daphne_talk."+temp_name.lower().replace(" ", "_")) # Jump to local label
                    elif temp_name == "":
                        jump daphne_talk
                    else:
                        $ daphne_name = temp_name
                        call dap_main("Very well, [dap_genie_name], you may call me [daphne_name].",face="neutral")
                    jump daphne_talk
                "-Never mind-":
                    jump daphne_talk

        "-Never mind-":
            jump daphne_requests
