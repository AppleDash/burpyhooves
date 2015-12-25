# This file is part of BuhIRC.
# 
# BuhIRC is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# BuhIRC is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the#  GNU General Public License
# along with BuhIRC.  If not, see <http://www.gnu.org/licenses/>.
class LineBuffer:
    def __init__(self, data=None):
        if not data:
            data = bytes()

        self.data = data

    def append(self, data):
        self.data += data

    def has_line(self):
        return b"\n" in self.data

    def pop_line(self):
        if not self.has_line():
            return None

        lines = self.data.split(b"\n")
        line = lines.pop(0)
        try:
            line = line.decode("utf8")
        except UnicodeDecodeError:
            line = line.decode("ascii")
        self.data = b"\n".join(lines)
        return line.strip()

    def flush(self):
        temp = self.data
        self.data = ""
        return temp

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_line():
            return self.pop_line()

        raise StopIteration