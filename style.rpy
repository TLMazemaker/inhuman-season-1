# This is for notification pop-up.

screen notification(title, message, color_title="#00FF00", color_message="#FFFFFF"):
    zorder 200
    modal False

    frame:
        at notification_slide
        xalign 0.50
        yalign 0.10
        padding (15, 10)
        background "#000000"

        vbox:
            spacing 4
            xalign 0.5

            text title color color_title size 36 xalign 0.5
            text message color color_message size 30 xalign 0.5


transform notification_slide:
    alpha 0.0
    linear 0.2 alpha 1.0
    pause 2.0
    linear 0.2 alpha 0.0


init python:
    def notify(title: str, msg: str, color_title:str="#00FF00", color_message:str="#FFFFFF")-> None:
        renpy.show_screen("notification", title=title, message=msg, color_title=color_title, color_message=color_message)
        renpy.restart_interaction()
        renpy.pause(2.5)
        renpy.hide_screen("notification")

# This is for timer screen

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time-0.01), false=[Hide('countdown'), Jump(timer_jump)])

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve