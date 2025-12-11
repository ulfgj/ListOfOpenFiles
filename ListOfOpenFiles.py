import sublime, sublime_plugin, os

class ListOpenFilesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        window = sublime.active_window()
        views = window.views()
        fileNames = ""
        for view in views:
            if view and view.file_name():
                fileNames += os.path.abspath(os.path.join(directory, view.file_name()))+'\n'

        # window.new_file().insert(edit, 0, "## Currently open files ({}):\n".format(len(fileNames),fileNames))
        window.new_file().insert(edit, 0, "## Currently open files:\n" + fileNames)