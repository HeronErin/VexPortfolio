# Copyright (C) 2024 HeronErin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class listView:
    def __init__(self, data=None) -> None:
        self.data = [] if data is None else data
    def set(self, a, b):
        i=0
        for c in (self.data):
            if c[0] == a:
                self.data[i] = (a,b)
            i+=1
    def get(self, a):
        for c in self.data:
            if c[0] == a:
                return c[1]