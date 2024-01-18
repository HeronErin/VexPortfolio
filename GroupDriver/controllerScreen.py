# Copyright (C) 2024 HeronErin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


#!ignoreNextLine
##controller_1 = Controller(PRIMARY)




class Screen:
    def __init__(self) -> None:
        self.scrollPos = 0
        self.baseList = listView(Menu)
        self.currenList = self.baseList

    def render(self):
        controller_1.screen.clear_screen()
        controller_1.screen.set_cursor(0, 0)
        controller_1.screen.print("-->")
        lvi = list(self.currenList.data)
        for c in range(3):
            citemI = (self.scrollPos+c)
            if len(lvi) > citemI:
                citem = lvi[citemI]
                controller_1.screen.print(citem[0])
                controller_1.screen.print(": ")
                
                if type(citem[1]) is not type(Screen.left) and type(citem[1]) is not listView:
                    controller_1.screen.print(str(citem[1]))
            controller_1.screen.next_row()
    def changeScroll(self, off):
        self.scrollPos = self.scrollPos+off
        if  len(list(self.currenList.data)) == self.scrollPos:
            self.scrollPos = self.scrollPos-1
        elif -1 == self.scrollPos:
            self.scrollPos = 0
        self.render()
    def left(self):
        lvi = list(self.currenList.data)
        citem = lvi[self.scrollPos]
        if len(lvi) > self.scrollPos:
            if type(citem[1]) is int or type(citem[1]) is float:
                self.currenList.set(citem[0], citem[1]-1)
            elif type(citem[1]) is bool:
                self.currenList.set(citem[0], False)
            elif type(citem[1]) is type(Screen.left):
                citem[1]()
            elif type(citem[1]) is listView:
                self.currenList = citem[1]
                self.scrollPos = 0
        self.render()
    def right(self):
        lvi = list(self.currenList.data)
        citem = lvi[self.scrollPos]
        if len(lvi) > self.scrollPos:
            if type(citem[1]) is int or type(citem[1]) is float:
                self.currenList.set(citem[0], citem[1]+1)
            elif type(citem[1]) is bool:
                self.currenList.set(citem[0], True)
            elif type(citem[1]) is type(Screen.left):
                citem[1]()
            elif type(citem[1]) is listView:
                self.currenList = citem[1]
                self.scrollPos = 0

        self.render()
    def b(self):
        self.currenList = self.baseList
        self.render()