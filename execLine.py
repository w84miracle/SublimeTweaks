import sublime, sublime_plugin

class ExeclineCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Execute Line:", "", self.ondone, None, None)
		pass
	def ondone(self,text):
		line = int(text)
		self.window.active_view().run_command("goto_line",{ "line": line})
		self.window.active_view().run_command("toggle_comment",{ "block": False })
		self.window.run_command("build")
		self.window.run_command("hide_panel", {"panel": "output.exec"})
		# print(self.window.active_view().panels())
		self.window.active_view().run_command("toggle_comment",{ "block": False })