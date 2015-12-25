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
import random

from modules import Module


class BuhModule(Module):
    name = "Buh"
    description = "buuuuuuuuuuuuuuuuh"

    def module_init(self, bot):
        self.hook_command("bored", self.command_bored)
        self.hook_command("boredx", self.command_boredx)

    def gen_buh(self, limit):
        colors = [random.randint(1,15) for i in range(2)]
        uColors = [random.randint(1,15) for i in range(random.randint(1, limit))]
        blast = random.randint(1,25) == 1

        msg = '\x03' + str(colors[0])
        if blast:
            msg += 'h'
        else:
            msg += 'b'
        msg += self.gen_u(uColors)
        msg += '\x03' + str(random.randint(1,15))

        if blast:
            msg += 'b'
        else:
            msg += 'h'

        return msg

    def gen_u(self, colors):
        return "".join("\x03%su" % color for color in colors)

    def command_bored(self, bot, event_args):
        msg = self.gen_buh(random.randint(1, 20))
        bot.reply(msg)

    def command_boredx(self, bot, event_args):
        msg = self.gen_buh(random.randint(1, 50))
        bot.reply(msg)
