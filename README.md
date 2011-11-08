Description
===========

This package contains various commands to manipulate the current text selection in useful ways.

Installation
============

You can install this package by running the following command in your ST2 Packages directory:
    
    git clone git://github.com/minism/SublimeBufmod.git

Once installed, be sure to edit the appropriate keybinding config file, as the keys are blank by default.  The files are:

* Default (Linux).sublime-keymap
* Default (OSX).sublime-keymap
* Default (Windows).sublime-keymap

Commands
========

You can run commands by using the key shortcuts, or through the command menu by pressing Ctrl/Cmd+P and typing "Bufmod".  All commands require one or more active selections of text in your editor to have any effect.

Apply function to selection
---------------------------

This is a simple yet powerful command.  An input window will open up which accepts a python function as a string, on a single line, with the following constraints:

* The variable `s` is a unicode object containing the selected text.
* The function must return a unicode or string.

The possibilities are really endless here.  Some examples of what you can do:

    return str(len(s))
    return s.encode('ascii')
    return s.strip().upper().center(80)

Or, perhaps something more complicated (make sure to use semicolons!):

    import os; return '\n'.join(os.path.join(os.path.expanduser('~'), chunk.strip()) for chunk in s.split(','))

Which would turn this:
    
    images, scripts, notes

Into:

    /Users/josh/images
    /Users/josh/scripts
    /Users/josh/notes

Decorate text with border
-------------------------

An input window opens which accepts a single character (extra characters are discarded).  The current selection is wrapped in a padded box using the specified character.

Example:

    bufmod.py - SublimeText2 Helper

Becomes:

    ###################################
    #                                 #
    # bufmod.py - SublimeText2 Helper #
    #                                 #
    ###################################

Discussion
==========


