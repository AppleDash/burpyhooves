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
from modules import Module


class CoreModule(Module):
    name = "Core"
    description = "Provides core management functionality for the bot."

    def module_init(self, bot):
        self.hook_command("modload", self.on_command_modload, "Load the given module.")
        self.hook_command("modunload", self.on_command_modunload, "Unload the given module.")
        self.hook_command("modreload", self.on_command_modreload, "Reload the given module.")
        self.hook_command("modlist", self.on_command_modlist, "Show a list of modules the bot has loaded.")
        self.hook_command("rehash", self.on_command_rehash, "Reload the bot's configuration file.")
        self.hook_command("join", self.on_command_join, "Cause the bot to join the given channel.")
        self.hook_command("part", self.on_command_part, "Cause the bot to part the given channel.")
        self.hook_command("commands", self.on_command_commands, "Show a list of commands the bot accepts.")
        self.hook_command("help", self.on_command_help, "Show help for the given command.")

    def on_command_modload(self, bot, event_args):
        args = event_args["args"]
        if not bot.check_permission():
            return

        if not bot.check_condition(len(args) == 1, "Usage: MODLOAD <module name>"):
            return

        to_load = args[0]
        result = bot.module_manager.load_module(to_load)
        if not result:
            bot.reply(bot.module_manager.last_error)
        else:
            bot.reply("Successfully loaded module %s!" % to_load)

    def on_command_modunload(self, bot, event_args):
        args = event_args["args"]
        if not bot.check_permission():
            return

        if not bot.check_condition(len(args) == 1, "Usage: MODUNLOAD <module name>"):
            return

        to_unload = args[0]
        result = bot.module_manager.unload_module(to_unload)
        if not result:
            bot.reply(bot.module_manager.last_error)
        else:
            bot.reply("Successfully unloaded module %s!" % to_unload)

    def on_command_modreload(self, bot, event_args):
        args = event_args["args"]
        if not bot.check_permission():
            return

        if not bot.check_condition(len(args) == 1, "Usage: MODRELOAD <module name>"):
            return

        to_reload = args[0]
        result = bot.module_manager.unload_module(to_reload, True)
        if not result:
            bot.reply(bot.module_manager.last_error)
            return

        result = bot.module_manager.load_module(to_reload)
        if not result:
            bot.reply(bot.module_manager.last_error)
        else:
            bot.reply("Successfully reloaded module: %s!" % to_reload)

    def on_command_modlist(self, bot, event_args):
        if not bot.check_permission():
            return

        modules = bot.module_manager.modules.keys()
        bot.reply("I have the following modules: %s." % ", ".join(modules))

    def on_command_rehash(self, bot, event_args):
        if not bot.check_permission():
            return

        bot.rehash()
        bot.reply("Successfully rehashed!")

    def on_command_join(self, bot, event_args):
        args = event_args["args"]
        if not bot.check_permission():
            return

        if not bot.check_condition((len(args) == 1) and args[0][0] == "#", "Usage: JOIN <channel>"):
            return

        bot.join(args[0])
        bot.reply("I have joined %s." % args[0])

    def on_command_part(self, bot, event_args):
        args = event_args["args"]
        if not bot.check_permission():
            return

        if not bot.check_condition((len(args) == 1) and args[0][0] == "#", "Usage: PART <channel>"):
            return

        bot.part(args[0])
        bot.reply("I have parted %s." % args[0])

    def on_command_commands(self, bot, event_args):
        commands = bot.list_commands()
        bot.reply("I respond to the following commands: %s. Try !help <command> for more information on a particular command." % ", ".join(commands))

    def on_command_help(self, bot, event_args):
        args = event_args["args"]
        if not bot.check_condition(len(args) == 1, "Usage: HELP <command name>"):
            return

        help = bot.help.get(args[0].lower(), "")
        if help:
            bot.reply("Help for command %s: %s" % (args[0], help))
        else:
            bot.reply("No help for command %s." % args[0])