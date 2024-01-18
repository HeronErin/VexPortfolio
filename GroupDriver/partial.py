# Copyright (C) 2024 HeronErin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# stores func call perams
class partial:
    def __init__(self, func, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.func = func
    def __call__(self):
        self.func(*self.args, **self.kwargs)

