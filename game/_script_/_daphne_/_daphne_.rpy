define dap_face = {
    "mouth": {
        "neutral":      ["base"],
        "happy":        ["base", "smile"],
        "naughty":      ["base", "smile"],
        #"horny":        ["smile","smile_big"],#ADD HORNY MOUTH#
        "annoyed":      ["skeptical","frown"],
        "disgusted":    ["skeptical","frown"],
        "angry":        ["frown"],
        "sad":          ["frown"],
        "surprised":   ["frown"]
    },

    "eyes": {
        "neutral":      ["base"],
        "happy":        ["base"],
        "naughty":      ["base"],
        "horny":        ["glare"],
        "annoyed":      ["glare"],
        "disgusted":    ["glare"],
        "angry":        ["glare"],
        "sad":          ["sad"],
        "surprised" :    ["surprised"]
    },

    "eyebrows": {
        "neutral":      ["base"],
        "happy":        ["base","up"],
        "naughty":      ["base","up","angry"],
        "horny":        ["base","up","angry"],
        "annoyed":      ["base","angry"],
        "disgusted":    ["up","puzzled"],
        "angry":        ["angry"],
        "sad":          ["sad"],
        "surprised":    ["horror"]
    },

    "pupils": {
        "neutral":      ["mid"],
        "happy":        ["mid","R"],
        "naughty":      ["mid","ahegao"],
        "horny":        ["mid","ahegao"],
        "annoyed":      ["mid","R"],
        "disgusted":    ["mid","down"],
        "angry":        ["mid"],
        "sad":          ["mid"],
        "surprised":    ["surprised"]
    }
}

label dap_main(text="", mouth=False, eyes=False, eyebrows=False, pupils=False, cheeks=None, tears=None, extra=None, emote=None, face=None, xpos=None, ypos=None, flip=None, trans=None, animation=False):
    if renpy.predicting():
        dap "predict"

    python:

        if flip != None:
            daphne_flip = -1 if flip else 1

        if animation != False:
            daphne_animation = animation

        if xpos:
            daphne_xpos = int(sprite_pos["x"].get(xpos, xpos))

        if ypos:
            if ypos == "head":
                use_daphne_head = True
            elif ypos in ("base", "default"):
                use_daphne_head = False

            daphne_ypos = int(sprite_pos["y"].get(ypos, ypos))

        daphne.set_face(mouth=mouth, eyes=eyes, eyebrows=eyebrows, pupils=pupils, cheeks=cheeks, tears=tears)

        if face:
            if not mouth:
                daphne.set_face(mouth=renpy.random.choice(dap_face["mouth"].get(face, None)))
            if not eyes:
                daphne.set_face(eyes=renpy.random.choice(dap_face["eyes"].get(face, None)))
            if not eyebrows:
                daphne.set_face(eyebrows=renpy.random.choice(dap_face["eyebrows"].get(face, None)))
            if not pupils:
                daphne.set_face(pupils=renpy.random.choice(dap_face["pupils"].get(face, None)))

    if not renpy.get_screen("wardrobe_menu"):
        show screen daphne_main()
    show screen bld1

    if trans:
        with trans

    if text:
        $ renpy.say(dap, text)

    if use_daphne_head:
        hide screen daphne_main
    return

label update_daphne:

    # Chibi Update
    $ daphne_chibi.update()
    $ daphne_chibi.position(flip=False)
    $ daphne_flip = 1
    hide screen dap_cloth_pile
    
    return

label end_daphne_event:
    call dap_chibi("hide")
    hide screen daphne_main
    with d3
    pause.5

    call update_daphne

    $ active_girl = None
    $ daphne_busy = True
    $ daphne.wear("all")

    $ renpy.stop_predict(daphne.get_image())
    $ renpy.stop_predict("characters/daphne/face/*.png")

    call music_block
    jump main_room


screen daphne_main():
    tag daphne_main
    zorder daphne_zorder
    sensitive False

    default daphne_img = apply_doll_transition(daphne.get_image(), "daphne_main", use_daphne_head)
    if daphne_animation != None:
        add daphne_img xpos daphne_xpos ypos daphne_ypos xzoom daphne_flip zoom (1.0/daphne_scaleratio) at daphne_animation
    else:
        add daphne_img xpos daphne_xpos ypos daphne_ypos xzoom daphne_flip zoom (1.0/daphne_scaleratio)
