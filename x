#! /bin/sh
# basic initializations
xmonad &
xfce4-session &
xmodmap ~/.Xmodmap
emacs --daemon &
keynav
