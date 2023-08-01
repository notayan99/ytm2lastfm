
# Yt music to last fm ( the easy way)

A simple script made by @anonymousx97 to add your yt music history to last fm.




![Pic.png real](https://github.com/notayan99/ytm2lastfm/blob/f33f51f3f1a6a5bb5348e4608c484062037e7811/real.png)


# Steps to use:

    1) Go to https://takeout.google.com/ 
    2) Tap on deselect all 
    3) Scroll down and find 'YouTube and YouTube Music'
    4) Tap on multiple formats and select json
    5) Now click on next step and wait for it to export your data
    6) After you get your data , extract the zip and find a file named 'watch-history.json' .
    7) Clone this repo
    8) Copy your 'watch-history.json' to the cloned folder/directory .
    9) Open main.py with any text editor  and change "path to your file" to "watch-history.json"
    10) Install python with the help of your very own friend google & yt_dlp with python-pip if you dont already have it
    11) Run ' python main.py ' & wait for it to complete
    12) You will get some files named 'new_json( insert a number here).json' 
    13) Go to https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases and find the latest version of Scrubbler.
    14) Download the ZIP under Assets, ignoring the source code, then Open when done.
    15) Once you’ve extracted the ZIP folder, open the application (the only file with a logo)
    16) Run into this window by any chance? Hit More info and you’ll see the Run anyway button tucked neatly inside.
    17) Sign into Last.fm where it says Not logged in.
    18) Click the green plus sign and enter your username and password. If, by any chance, you are logged out in the future, click your username under Available Users: then the blue button to sign back in.
    19) Under the File Parse Scrobbler tab, Parser will be set to CSV by default. Change this to JSON, then in your Imports folder, upload your first file using the ellipsis (...).
    20) Load the file by clicking Parse, then click Check All to tick all 2600 scrobbles.
    21) On the bottom left next to Scrobble, Preview your scrobbles to review them. This is exactly how they will be imported, so it’s important to make any last-minute corrections. Once you’ve made sure everything is in proper order, hit Scrobble.

# If, for whatever reason, you receive the Error while scrobbling: Cached message, be sure that 1. You haven’t exceeded the daily scrobble limit (3000) or 2. That you’ve using disconnected and reconnected Scrubbler from your Last.fm Application settings if you’ve changed your Last.fm handle since using the app.

