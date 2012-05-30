import sublime_plugin
import sublime

class Bufmod_apply_function(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(
            "Apply function to selection:",
            "return s",
            _bufmod_apply_function,
            None,
            None
        )

class Bufmod_apply_function_lines(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(
            "Apply function to each line:",
            "return s",
            _bufmod_apply_function_lines,
            None,
            None
        )

class Bufmod_decorate(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(
            "Decorate text with character:",
            "#",
            _bufmod_decorate,
            None,
            None
        )

def _bufmod_decorate(padding):
    # Validate arg
    char = padding[0]

    # Grab buffer and pad
    view = sublime.active_window().active_view()
    edit = view.begin_edit()
    for region in view.sel():
        lines = view.substr(region).split('\n')
        size = max(map(len, lines))
        buf = [char * (size + 4)]
        for line in [''] + lines + ['']:
            buf.append('%s %s %s' % (char, line.ljust(size), char))
        buf.append(char * (size + 4))
        view.replace(edit, region, '\n'.join(buf))
    view.end_edit(edit)

def _bufmod_apply_function(func):
    view = sublime.active_window().active_view()
    edit = view.begin_edit()
    exec('def f(s): %s;' % func)
    for region in view.sel():
        newtext = f(view.substr(region))
        view.replace(edit, region, newtext)
    view.end_edit(edit)

def _bufmod_apply_function_lines(func):
    view = sublime.active_window().active_view()
    edit = view.begin_edit()
    namespace = {}
    exec 'def f(s): %s;' % func in namespace
    f = namespace.get('f', lambda x: x)
    for region in view.sel():
        newtext = '\n'.join(map(lambda line: namespace['f'](line), view.substr(region).splitlines()))
        view.replace(edit, region, newtext)
    view.end_edit(edit)
