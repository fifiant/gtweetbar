#!/usr/bin/env python

import pygtk
pygtk.require("2.0")
import gtk

# make local copy of twitter api importable
import sys
sys.path.append('./python_twitter')
import twitter


class TweetBar(object):

	username = "gtweetbar"
	password = "newman"
	oldContent = ""

	def __init__(self):
		''' setup everthing, load glade ui, set objects, defaults, etc '''
		
		self.builder=gtk.Builder()
		self.builder.add_from_file("ui/tweetbar.glade")
		self.builder.connect_signals( 
			{ 
				"on_mainwindow_destroy" : gtk.main_quit,
				"on_txtTweet_changed" : self.on_txtTweet_changed,
				"on_btnSend_clicked" : self.on_btnSend_clicked,
				"on_txtTweet_button_release_event" : self.on_txtTweet_button_release_event,
			} 
		)
			
		self.window = self.builder.get_object("mainwindow")
		
		# Lets grab all controls before we reuse them elsewhere
		self.lblLeft = self.builder.get_object ("lblLeft")
		self.txtTweet = self.builder.get_object ("txtTweet")
		self.btnSend = self.builder.get_object ("btnSend")
		self.txtTweet
		# init twitter API
		self.api = twitter.Api()
		self.api.SetSource ("TweetBar")
		self.MaxChars = 140

		self.window.show()


	def on_txtTweet_button_release_event(self,widget,event):
		''' select old tweet for easy disappearance '''
		widget.grab_focus()
		widget.select_region(0,-1)


	def on_txtTweet_changed(self,textbox):
		''' Update remaining characters '''
		tweet = textbox.get_text()
		
		if (len(tweet) == 0):
			self.btnSend.set_sensitive(False)
		else:
			self.btnSend.set_sensitive(True)
			
		self.lblLeft.set_text( str(self.MaxChars - len(tweet)) )


	def on_btnSend_clicked(self,button):
		''' validate, authenticate and post the tweet '''
		self.TweetThat()


	def TweetThat(self):
		''' tweets the content of txtTweet '''
		tweet = self.txtTweet.get_text()
		
		if (len(tweet.strip())==0):
			# a tweet made up of only spaces is not a tweet
			return
		
		self.api.SetCredentials (self.username, self.password)
		self.api.PostUpdate(tweet)


if __name__=="__main__":
	app = TweetBar()
	gtk.main()
	