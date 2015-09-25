# This file is part of BurpyHooves.
# 
# BurpyHooves is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# BurpyHooves is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the#  GNU General Public License
# along with BurpyHooves.  If not, see <http://www.gnu.org/licenses/>.
from modules import Module
from collections import defaultdict

class NickTrackingModule(Module):
    name = "Nick Tracking"
    description = "Tracks users' nicks and stores them in the bot's memory"
    
    def module_init(self, bot):
        self.bot.names = collections.defaultdict(list)
        self.setup_hooks()

    def setup_hooks(self):
        hooks = {
            "353": self.on_raw_353,
            "366": self.on_raw_366,
            "PART": self.on_raw_part,
            "QUIT": self.on_raw_quit,
            "JOIN": self.on_raw_join,
            "NICK": self.on_raw_nick
        }
        for cm, cb in hooks.items():
            self.hook_numeric(cm, cb)

    def on_raw_353(self, bot, ln):
        chan = ln.params[2]
        names = ln.params[-1].split(" ")
        if self.bot.state.get("names_%s" % chan, False):
            self.bot.names[chan].extend(names)
        else:
            self.bot.state["names_%s" % chan] = True
            self.bot.names[chan] = names

    def on_raw_366(self, bot, ln):
        self.bot.state["names_%s" % ln.params[1]] = False

    def on_raw_part(self, bot, ln):
        nick = ln.hostmask.nick
        chan = ln.params[0]
        self.bot.names[chan].remove(nick)

    def on_raw_quit(self, bot, ln):
        nick = ln.hostmask.nick
        for chan, names in self.bot.names.iteritems():
            if nick in names:
                names.remove(nick)

    def on_raw_join(self, bot, ln):
        nick = ln.hostmask.nick
        chan = ln.params[0]
        self.bot.names[chan].append(nick)

    def on_raw_nick(self, bot, ln):
        old = ln.hostmask.nick
        new = ln.params[0]
        for chan, names in self.bot.names.iteritems():
            if old in names:
                names.remove(old)
                names.append(new)