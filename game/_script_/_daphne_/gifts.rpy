### Give daphne Gift ###

label give_dap_gift(gift_item):
    $ gave_daphne_gift = True

    if gift_item == lollipop_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the lollipop to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == chocolate_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the chocolate to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == plush_owl_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the stuffed owl to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == butterbeer_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the butterbeer to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == science_mag_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the science magazine to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == girls_mag_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the girl's magazine to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == adult_mag_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the adult magazine to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == porn_mag_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the porn magazine to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == krum_poster_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the Krum poster to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == sexy_lingerie_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the sexy lingerie to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == sexy_stockings_ITEM :
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the sexy stockings to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == pink_condoms_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the condoms to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == vibrator_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the vibrator to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == anal_lube_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the anal lube to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == ballgag_and_cuffs_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the ball gag and cuffs to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == anal_plugs_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the anal plugs to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == testral_strapon_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the strap-on to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == broom_2000_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the broom to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == sexdoll_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the sex doll to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == anal_beads_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the anal beads to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == wine_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the wine to Daphne...", gift_item)
        call dap_mood(-1)

    elif gift_item == firewhisky_ITEM:
        call dap_main("Thank you, [dap_genie_name].",face="neutral",xpos="mid",ypos="base",trans=d5)
        call give_gift(">You give the firewhisky to Daphne...", gift_item)
        call dap_mood(-1)

    call dap_main(xpos="base", ypos="base",trans=d5)

    return

label dap_mood(value=0):
    show screen blktone5
    with d3

    if value > 0:
        if value == 1:
            "Daphne's mood worsened slightly."
        else:
            "Daphne's mood just got a whole lot worse!"
    elif value < 0:
        if value == -1:
            "Daphne's mood has improved slightly."
        else:
            "Daphne's mood has improved significantly."
    else:
        "Daphne's mood hasn't changed."

    $ dap_mood = max(min(dap_mood+value, 100), 0)
    hide screen blktone5
    return
