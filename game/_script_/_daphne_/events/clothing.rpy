label daphne_summon_setup:

    $ daphne_wardrobe_unlocked = True

    $ daphne.wear("all")
    $ daphne.set_cum(None)

    if daphne_outfits_schedule:
        $ daphne.equip_random_outfit()

    call play_sound("door")
    call dap_chibi("stand","mid","base")
    with d3

    #daphne greeting.
    call play_music("daphne")

    if dap_mood > 0:
        if 5 > dap_mood >= 1:
            call dap_main("Yes, [dap_genie_name]?", mouth="base", eyes="base", eyebrows="base", pupils="R", xpos="base", ypos="base", trans=d3)
            call dap_main("", "base", "base", "base", "R")
        elif 10 > dap_mood >= 5:
            call dap_main("Did you need something?", mouth="skeptical", eyes="base", eyebrows="base", pupils="mid", xpos="base", ypos="base", trans=d3)
        elif 20 > dap_mood >= 10:
            call dap_main("Can we hurry this up, [dap_genie_name]?", mouth="skeptical", eyes="base", eyebrows="base", pupils="R", xpos="base", ypos="base", trans=d3)
        elif 30 > dap_mood >= 20:
            call dap_main("What is it now? I'm busy.", mouth="angry", eyes="glare", eyebrows="angry", pupils="mid", xpos="base", ypos="base", trans=d3)
        elif 40 > dap_mood >= 30:
            call dap_main("Grr...", mouth="angry", eyes="glare", eyebrows="angry", pupils="R", xpos="base", ypos="base", trans=d3)
        elif 50 > dap_mood >= 40:
            call dap_main("You have some nerve!", mouth="angry", eyes="glare", eyebrows="angry", pupils="mid", xpos="base", ypos="base", trans=d3)
        elif dap_mood >= 50:
            call dap_main("(She glares at you in silence, clearly very upset)", mouth="angry", eyes="glare", eyebrows="angry", pupils="mid", xpos="base", ypos="base", trans=d3)

        call describe_mood("daphne", dap_mood)
        call tutorial("moodngifts")
    else:
        call dap_main("You wanted to see me, [dap_genie_name]?","base","base","base","mid", xpos="base", ypos="base", trans=d3)
    return
