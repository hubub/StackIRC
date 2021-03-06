'''
Copyright (c) 2012 Nathan Osman

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from sys import exit
from twisted.internet import reactor

from factory import StackIRCFactory
from config import StackIRCConfig

class StackIRCBot:
    
    def __init__(self):
        self.factory = StackIRCFactory()
    
    def run(self):
        # Ensure the settings are loaded before proceeding.
        if not StackIRCConfig.load():
            print 'The file "%s" does not exist. StackIRC will now create the file and exit. Please open the file in a text editor, adjust the configuration values, and start StackIRC again.' % StackIRCConfig.cfile
            StackIRCConfig.create()
            exit()
        # Now connect and start the client.
        print 'Connecting to %s:%s...' % (StackIRCConfig.server, StackIRCConfig.port,)
        reactor.connectTCP(StackIRCConfig.server, StackIRCConfig.port, self.factory)
        reactor.run()

