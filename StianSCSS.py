import sublime, sublime_plugin
import re

class StianScssCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        reg = sublime.Region(0, self.view.size())
        text = self.view.substr(reg)

        # Remove trailing whitespace
        text = re.sub(r'[^\S\n]+$', '', text, 0, re.M)

        # Space before opening curly bracket
        text = re.sub(r'(\w){', r'\1 {', text)

        # Newline before new selector
        text = re.sub(r'([;}])\n([^\n]*){', r'\1\n\n\2{', text)

        # Remove excessive newlines
        text = re.sub(r'{\n\n+', r'{\n', text)
        text = re.sub(r'}\n\n+(\s*)}', r'}\n\1}', text)
        text = re.sub(r';\n\n+(.*);', r';\n\1;', text)

        # Ensure one selector per line
        # TODO

        # Ensure one propery per line
        # TODO

        self.view.replace(edit, reg, text)
