#!/bin/sh
# SVN Diff Wrapper for Meld
# KOG 2008-02
# http://askubuntu.com/a/389553

left="$6"
right="$7"

meld "$left" "$right"
