label dap_chibi(action=None, xpos=None, ypos=None, flip=False):
    $ daphne_chibi.position(xpos, ypos, flip)

    if action == "hide":
        $ daphne_chibi.hide()
        return
    elif action == "leave":
        hide screen daphne_main
        hide screen bld1
        hide screen blktone
        call play_sound("door")
        $ daphne_chibi.hide()
        with d3
        pause .5
        return
    elif action == "reset":
        $ daphne_chibi.do(None)
        return

    $ daphne_chibi.do(action)

    return

label dap_walk(xpos=None, ypos=None, speed=1.0, action=None, reduce=False, path=None):
    call hide_characters
    hide screen bld1
    hide screen blktone
    with d3

    if action == "enter":
        call play_sound("door")
        call dap_chibi(None, "door", "base", False)
        if xpos or ypos:
            $ daphne_chibi.move(xpos, ypos, speed, reduce)
    elif action == "leave":
        $ daphne_chibi.show()
        $ daphne_chibi.move("door", "base", speed, reduce)
        call play_sound("door")
        $ daphne_chibi.hide()
        with d3
        pause .5
    elif path:
        $ daphne_chibi.show()
        $ daphne_chibi.path_move(path, speed)
    else:
        $ daphne_chibi.show()
        $ daphne_chibi.move(xpos, ypos, speed, reduce)

    return

# Screens
screen dap_cloth_pile(position=(440, 425)): # Default position: Right of desk, below feet.
    tag dap_cloth_pile
    zorder daphne_chibi.zorder
    add "characters/chibis/cloth_pile_r.png" pos position zoom 0.5

label dap_sit(xpos=nxpos, ypos=nypos, flip=None, chair=True): # TODO: replace this with the regular chibi call and add a sitting pose/action -- call dap_chibi("sit", chair=False)

    # call dap_sit(chair=False, xpos=0, ypos=0)
    # Quidditch stands position: xpos=-140, ypos=125

    python:

        xpos = nxpos
        ypos = nypos

        if flip != None:
            daphne_flip = -1 if flip else 1

    show screen daphne_sit_ani(nxpos, nypos, chair)

    return

screen daphne_sit_ani(xpos=nxpos, ypos=nypos, chair=True): # TODO: use daphne' regular chibi position for this -- daphne_chibi.pos
    tag dap_chibi
    zorder daphne_chibi.zorder

    #if chair == True:
        #add "ch_ton sit_chair" xpos nxpos ypos nypos xzoom daphne_flip

    #add "ch_ton sit" xpos nxpos ypos nypos xzoom daphne_flip

    #if daphne.is_worn("bottom"):
        #add "ch_ton sit_trousers" xpos nxpos ypos nypos xzoom daphne_flip
    #if daphne.is_any_worn("bottom", "stockings"):
        #add "ch_ton sit_shoes" xpos nxpos ypos nypos xzoom daphne_flip
    #if daphne.is_worn("top"):
        #add "ch_ton sit_top" xpos nxpos ypos nypos xzoom daphne_flip

screen with_daphne_animated():
    tag dap_chibi
    zorder daphne_chibi.zorder

    #if daytime:
        #add "ch_gen toast_goblet_daytime" xpos 435 ypos 200
    #else:
        #add "ch_gen toast_goblet" xpos 435 ypos 200

    #add "ch_ton sit_chair" xpos 610 ypos 175
    #add "ch_ton sit" xpos 610 ypos 175

    #if daphne.is_worn("bottom"):
        #add "ch_ton sit_trousers" xpos 610 ypos 175
    #if daphne.is_any_worn("bottom", "stockings"):
        #add "ch_ton sit_shoes" xpos 610 ypos 175
    #if daphne.is_worn("top"):
        #add "ch_ton sit_top" xpos 610 ypos 175
    #if daphne.is_worn("neckwear"):
        #add "ch_ton sit_choker" xpos 610 ypos 175


# Chibi definition
default daphne_chibi = Chibi("daphne", ["fix", "base", "bottom", "shoes", "top", "robe", "gloves", "neck"], update_daphne_chibi)

init python:
    def update_daphne_chibi(chibi):
        pass
        # Assume chibi action has a matching image definition
        #chibi_image = "ch_ton {}".format(chibi.action or "stand")
        #chibi["base"] = chibi_image

        # Determine clothing state

        #if daphne.is_worn("top"):
            #chibi["top"] = "nt_top.png"

        #if daphne.is_worn("bottom"):
            #if chibi.action == "walk":
                #chibi["bottom"] = "ch_ton walk trousers"
            #else:
                #chibi["bottom"] = "nt_trousers.png"

        #if daphne.is_worn("gloves"):
            #chibi["gloves"] = "nt_gloves.png"

        #if daphne.is_worn("robe"):
            #chibi["robe"] = "nt_robe.png"

        #if daphne.is_worn("bottom") or daphne.is_worn("stockings"):
            #if chibi.action == "walk":
                #chibi["shoes"] = "ch_ton walk shoes"
            #else:
                #chibi["shoes"] = "nt_shoes.png"

        #if daphne.is_worn("neckwear"):
            #chibi["neck"] = "nt_choker.png"
