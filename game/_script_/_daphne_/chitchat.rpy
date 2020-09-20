

### daphne Chitchats ###

label daphne_chit_chat:
    $ chitchated_with_daphne = True

    $ renpy.dynamic("chitchat_choices")
    $ chitchat_choices = set(range(1, 3))
    $ random_number = renpy.random.choice(list(chitchat_choices))

    # Chitchats
    if random_number == 1:
        call dap_main("A mudblood girl ran into me in the halls the other day.",face="annoyed")
        call dap_main("If you ask me, we shouldn't be wasting school resources teaching their kind magic.",face="annoyed")

    elif random_number == 2:
        call dap_main("Has Astoria been pestering you again, [dap_genie_name]?",face="annoyed")
        call dap_main("I swear, that girl doesn't know how to keep out of trouble.",face="annoyed",pupils="R")

    elif random_number == 3:
        call dap_main("Professor Snape seems to always have his eyes on me.",face="annoyed")
        call dap_main("That creep should mind his own business, or I might have to teach him a lesson.",face="annoyed")
    return