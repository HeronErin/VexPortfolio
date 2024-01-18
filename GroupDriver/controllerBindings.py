# Copyright (C) 2024 HeronErin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

    screen = Screen()
    screen.render()
    controller_1.buttonUp.pressed(lambda: screen.changeScroll(-1))
    controller_1.buttonDown.pressed(lambda: screen.changeScroll(1))
    controller_1.buttonLeft.pressed(lambda: screen.left())
    controller_1.buttonRight.pressed(lambda: screen.right())

    controller_1.buttonB.pressed(lambda: screen.b())







    ###############



    controller_1.axis3.changed(driver)
    controller_1.axis4.changed(driver)

    controller_1.axis2.changed(conv_belt)

    controller_1.buttonR2.pressed(fire)
    # controller_1.buttonR2.pressed(spin360)