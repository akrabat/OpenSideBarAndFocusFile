import sublime_plugin

class OpenSideBarAndFocusFile(sublime_plugin.WindowCommand):
    def run(self):
        self.window.set_sidebar_visible(True)
        self.window.run_command("reveal_in_side_bar")
        self.window.run_command("focus_side_bar")

