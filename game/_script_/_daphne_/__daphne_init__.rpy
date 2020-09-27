# Main
default daphne_xpos = 600
default daphne_ypos = 0
default daphne_zorder = 15
default daphne_flip = 1
default use_daphnes_head = False
default daphne_animation = None

#default daphne_haircolor = [[243, 158, 189, 255], [254, 218, 238, 255]]

# Stats
default dap_tier           = 1
default dap_whoring     = 0 #Max is 100.
default dap_support        = 0
default dap_reputation     = 0
default dap_clothing_level = 100
default dap_mood           = 0

# Flags
default daphne_busy              = False
default daphne_unlocked          = True
default daphne_favors_unlocked   = False
default daphne_requests_unlocked = False
default daphne_shaming_unlocked  = False
default daphne_wardrobe_unlocked = False
default chitchated_with_daphne   = False
default daphne_outfits_schedule = True

default gave_daphne_gift = False
default daphne_mail_list = []

# Names
default daphne_name       = "Daphne"
default dap_genie_name   = "Professor"
default dap_astoria_name = "Brat"

# Stat Screen
#default ton_clothing_upgrades     = 0
#default ton_astoria_date_counter  = 0
#default ton_hermione_date_counter = 0

default dap_level_up = None
default daphne_shared = False

# Hangout Events

#default nt_he_counter = 0

# Public requests
#default nt_pr_teach = event_class(
    #title = "Detention with Tonks.", start_label = "nt_pr_teach_start", start_tier = 1,
    #events = [
        #[
            #["nt_pr_teach_T1_E1"], # Slytherin boy
            #["nt_pr_teach_T1_E2"], # Ravenclaw boy
            #["nt_pr_teach_T1_E3"], # Potter & Weasley
            #["nt_pr_teach_T1_E4"]  # Slytherin girl
        #],
        #[
            #["nt_pr_teach_T2_E1"], # Hufflepuff girl
            #["nt_pr_teach_T2_E2"], # Ravenclaw boy
            #["nt_pr_teach_T2_E3"], # Slytherin boy
            #["nt_pr_teach_T2_E4"]  # Slytherin girl
        #]
    #],
    #iconset = [["star_empty", "star_pink"]] # You have to add icons at least for first tier, the rest will be copied over automatically.
#)

#default nt_requests_list = [
    #nt_pr_teach,
    #nt_pr_grope,
    #nt_pr_kiss
#]

label reset_daphne_progress:
    $ reset_variables(
        # Stats
        "dap_tier",
        "dap_friendship",
        "dap_support",
        "dap_reputation",
        "dap_clothing_level",

        # Flags
        "daphnes_busy",
        "daphne_unlocked",
        "daphne_favors_unlocked",
        "daphnes_requests_unlocked",
        "daphne_shaming_unlocked",
        "daphne_wardrobe_unlocked",
        "chitchated_with_daphne",
        "gave_daphne_gift",

        # Names
        "daphne_name",
        "dap_genie_name",
        "dap_astoria_name"#,

        # Stat Screen
        #"ton_level_up",
        #"tonks_shared"#,

        # Events
        #"nt_he_counter",
        #"nt_he_drink",
        #"nt_pr_teach",
        #"nt_pr_grope",
        #"nt_pr_kiss",
        #"nt_requests_list"
    )
    return
