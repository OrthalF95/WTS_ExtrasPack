
# House Elf
screen house_elf():
    add "characters/misc/house-elf/house-elf.webp" xpos 700 ypos 200
    zorder snape_zorder

label helf_main(text="", trans=None, remove=False):
    hide screen house_elf
    show screen bld1

    if remove == True:
        pause 0.1
        return

    show screen house_elf
    show screen bld1

    with trans

    helf "[text]"

    return

# Narrator (not the same as 'nar' character)
label nar(text="",action=""):

    if action != "end": #Narration ended, blktone was already active.
        show screen blktone5
        with d3

    if text != "":
        "[text]"

    if action != "start": #Narration just started, blktone won't get hidden.
        hide screen blktone5
        with d3

    return

# Characters

# Add to character store to avoid name conflict with Doll instance
define character.cho = Character('[cho_name]', predict_function=doll_prediction("cho"))

init python:

    # Genie
    gen = Character('Genie')
    m = Character("", show_side_image=Image("characters/genie/mage.webp", xpos=20))
    g2 = Character("", show_side_image=Image("characters/genie/mage2.webp", xpos=20))
    g3 = Character("", show_side_image=Image("characters/genie/mage3.webp", xpos=20))
    g4 = Character("", show_side_image=Image("characters/genie/mage4.webp", xpos=20))
    g5 = Character("", show_side_image=Image("characters/genie/mage5.webp", xpos=20))
    g6 = Character("", show_side_image=Image("characters/genie/mage6.webp", xpos=20))
    g7 = Character("", show_side_image=Image("characters/genie/mage7.webp", xpos=20))
    g8 = Character("", show_side_image=Image("characters/genie/mage8.webp", xpos=20))
    g9 = Character("", show_side_image=Image("characters/genie/mage9.webp", xpos=20))
    g10 = Character("", show_side_image=Image("characters/genie/mage10.webp", xpos=20))
    g11 = Character("", show_side_image=Image("characters/genie/mage11.webp", xpos=20))
    g12 = Character("", show_side_image=Image("characters/genie/mage12.webp", xpos=20))
    g13 = Character("", show_side_image=Image("characters/genie/mage13.webp", xpos=20))
    g14 = Character("", show_side_image=Image("characters/genie/mage14.webp", xpos=20))
    g15 = Character("", show_side_image=Image("characters/genie/mage15.webp", xpos=20))
    g16 = Character("", show_side_image=Image("characters/genie/mage16.webp", xpos=20))

    # Dumbledore
    dum_ = [""]
    for i in xrange(1,6):
        dum_.append("")
        dum_[i] = Character("Dumbledore", show_side_image=Image("characters/misc/dumbledore/dum_"+str(i)+".webp", xpos=20))

    # Santa
    san_ = [""]
    for i in xrange(1,7):
        san_.append("")
        san_[i] = Character("Santa", show_side_image=Image("characters/misc/santa/santa_"+str(i)+".webp", xpos=20))

    # Students
    her = Character('[hermione_name]', predict_function=doll_prediction("hermione"))
    lun = Character('[lun_name]')
    sus = Character('[susan_name]')
    ast = Character('[astoria_name]', predict_function=doll_prediction("astoria"))
    dap = Character('[daphne_name]', predict_function=doll_prediction("daphne"))
    twi = Character('Fred and George', show_side_image=Image("characters/misc/weasley_twins/base_01.webp", xalign=1.0))
    fre = Character('Fred', show_side_image=Image("characters/misc/weasley_twins/fred_01.webp", xalign=1.0))
    ger = Character('George', show_side_image=Image("characters/misc/weasley_twins/george_01.webp", xalign=1.0))

    # Teachers
    sna = Character('Severus Snape')
    ton = Character('[tonks_name]', predict_function=doll_prediction("tonks"))
    spo = Character('Professor Sprout')
    hoo = Character('Madam Hooch')

    # Other characters
    hat = Character('Sorting Hat', show_side_image=Image("characters/misc/hat/hat.webp", xalign=1.0))
    helf = Character("House-Elf")
    nar = Character('Narrator', show_side_image=Image("characters/misc/dumbledore/dum_narritor.webp"))
    sil = Character('Team Silver', show_side_image=Image("characters/misc/dumbledore/dum_narritor.webp"))

    malf = Character('Malfoy')
    cra = Character('Crabbe')
    goy = Character('Goyle')

    maf = Character('Madam Mafkin', show_side_image=Image("characters/misc/mafkin/maf_1.webp", xalign=1.0))
    abe = Character('Aberforth')
    myr = Character('Moaning Myrtle')
    vol = Character('Lord Voldemort')
    faw = Character('Fawkes', color="#f21111")

    fem = Character('Female Student')
    mal = Character('Male Student')
    mal2 = Character('Another Male Student')
    sly1 = Character('Slytherin student')
    sly2 = Character('Another Slytherin student')
    qcr = Character('Quidditch Crowd')
    who = Character('Female voice')
    whom = Character('Male voice')
    who2 = Character('???')
