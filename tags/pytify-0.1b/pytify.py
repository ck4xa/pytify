#!/usr/bin/python
# coding=UTF-8

# Copyright (c) 2009, Bjørge Næss
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the Bjørge Næss nor the names of its contributors may
#    be used to endorse or promote products derived from this software without
#    specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import win32gui

class Spotify(object):

	APPCOMMAND      = 0x0319

	# Command IDs
	CMD_NONE        = 0
	CMD_PLAYPAUSE   = 917504
	CMD_MUTE        = 524288
	CMD_VOLUMEDOWN  = 589824
	CMD_VOLUMEUP    = 655360
	CMD_STOP        = 851968
	CMD_PREVIOUS    = 786432
	CMD_NEXT        = 720896

	# Instance vars
	_hwnd            = None

	def __init__(self):
		try:
			self._hwnd = win32gui.FindWindow("SpotifyMainWindow", None)
		except:
			raise self.SpotifyWindowNotFoundException()

	def playpause(self):
		self._sendCommand(self.CMD_PLAYPAUSE)

	def mute(self):
		self._sendCommand(self.CMD_MUTE)

	def volumeUp(self):
		self._sendCommand(self.CMD_VOLUMEUP)

	def volumeDown(self):
		self._sendCommand(self.CMD_VOLUMEDOWN)

	def stop(self):
		self._sendCommand(self.CMD_STOP)

	def previous(self):
		self._sendCommand(self.CMD_PREVIOUS)

	def next(self):
		self._sendCommand(self.CMD_NEXT)

	def getCurrentTrack(self):
		return self._parseWindowTitle()['track']

	def getCurrentArtist(self):
		return self._parseWindowTitle()['artist']

	def focus(self):
		win32gui.ShowWindow(self._hwnd, 1)
		win32gui.SetForegroundWindow(self._hwnd)
		win32gui.SetFocus(self._hwnd)

	def isPlaying(self):
		return self.getCurrentArtist() != None

	def _sendCommand(self, id):
		win32gui.SendMessage(self._hwnd, self.APPCOMMAND, 0, id)

	def _parseWindowTitle(self):
		trackinfo = win32gui.GetWindowText(self._hwnd).split(" - ")

		if len(trackinfo) == 1:
			return {'artist': None, 'track': None}

		artist, track = trackinfo[1].split(" \x96 ")
		return {'artist': artist, 'track': track}

	def __str__(self):
		if self.isPlaying():
			nowplaying = "Now playing "+self.getCurrentArtist()+ " - "+self.getCurrentTrack()
		else:
			nowplaying = "Not playing anything at the moment."
		return "Spotify running! "+nowplaying

	class SpotifyWindowNotFoundException:
		def __str__(self):
			return "Spotify window not found. Is Spotify really running?"

# Dict of spotify commands available from command line
COMMANDLINE_COMMANDS = {
		'playpause': Spotify.playpause,
		'stop': Spotify.stop,
		'previous': Spotify.previous,
		'next': Spotify.next,
		'volup': Spotify.volumeUp,
		'voldown': Spotify.volumeDown,
		'mute': Spotify.mute,
		'isplaying': Spotify.isPlaying,
		'focus': Spotify.focus,
		'currenttrack': Spotify.getCurrentTrack,
		'currentartist': Spotify.getCurrentArtist,
		'status': Spotify.__str__
}

if __name__ == "__main__":
	def fail():
		print "Usage: pytify.py "+"|".join(COMMANDLINE_COMMANDS.keys())
		sys.exit(0)

	if len(sys.argv) < 2: fail()

	cmd_name = sys.argv[1]
	if not COMMANDLINE_COMMANDS.has_key(cmd_name): fail()

	cmd = COMMANDLINE_COMMANDS[cmd_name]

	try:
		spotify = Spotify()
	except:
		print "Spotify is not running"
		sys.exit(0)

	res = cmd(spotify)
	if res: print res