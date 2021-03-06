#TODO Move variable defaults to appropriate files, leave common ones here (and rename this file to _Variables_.rpy or something)
init offset = -1

# Menu placement
default menu_x = 0.5
default menu_y = 0.5

# Summoned character
default active_girl = None
default last_character = None

# Turns commentaries on/off in gallery
default commentaries = False

# GUI color scheme
default interface_color = "gold"
default interface_style = "night"
default btn_hover = "#7d75aa40"

default gallery_active = False
default ball_ending_2  = False

default game_difficulty = 2

default day = 0

default daytime        = False
default gold           = 0
default rum_times      = 0 # Counts how many times have you rummaged the cupboard.
default current_payout = 0

# Hermione main screen flags
default uni_sperm     = False # OBSOLETE! Untouched for backwards compatibility and references in the code.

default public_whore_ending = False # If TRUE the game will end with "Public Whore Ending".

# House points
default slytherin  = 180
default gryffindor = 53
default hufflepuff = 25
default ravenclaw  = 31

# Duel
default potions = 0 # Amount of healing potions Genie has in stock.

# Cupboard
default searched = False # Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.

# Books
default found_voucher = False # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.

# Clothing
default gave_miniskirt = False # Turns True when Hermione has the miniskirt.

# Used to pause events/summons for a number of days
default ss_event_pause  = 0
default ss_summon_pause = 0
default nt_event_pause  = 0
default nt_summon_pause = 0
default hg_event_pause  = 0
default hg_summon_pause = 0
default cc_event_pause  = 0
default cc_summon_pause = 0
default ll_event_pause  = 0
default ll_summon_pause = 0
default ag_event_pause  = 0
default ag_summon_pause = 0
default sb_event_pause  = 0
default sb_summon_pause = 0
default dg_event_pause  = 0
default dg_summon_pause = 0

default always_read_letter = False
default owl_away           = False
default owl_away_counter   = 0

# Sprite positioning
default nxpos        = 0
default nypos        = 0
default nscale       = 0.5
default walk_xpos    = 750
default walk_ypos    = 250
default chibi_xpos   = 0
default chibi_ypos   = 0
default chibi_zorder = 1
default desk_zorder  = 2

default unlocked_7th       = False
default charName           = "genie"

# Phoenix
default phoenix_is_fed         = False
default phoenix_is_petted      = False
default phoenix_fed_counter    = 0
default phoenix_petted_counter = 0

# Paperwork related flags
default day_of_week          = 0 # Counts days of the week. Everyday +1. When day_of_week = = 7 resets to zero.
default report_chapters      = 0 # Number of chapters of current report completed so far. Resets to zero when report is finished.
default finished_report      = 0 # Number of completed reports.
default stat_reports_counter = 0

# Fireplace
default fire_in_fireplace = False
default stat_fireplace_counter = 0

# Examine room flags
default desk_examined = False
default cupboard_examined = False
default bird_examined = False
default door_examined = False
default fireplace_examined = False

# Room decoration
default current_room  = "main_room"
default room_deco     = ""
default cupboard_deco = ""

# CGs
default ccg_folder = "luna_bj"
default ccg1       = "herm"
default ccg2       = 1
default ccg3       = "gene"
default loopimage  = None
default cg_image   = "e2"
default cg_path    = "images/CG/"+cg_image+".webp"

# CG or chibis
default face_on_cg = False # `call her_main(,ypos="head")` will use screen "her_face". Face gets positioned automatically.
default use_cgs = False
