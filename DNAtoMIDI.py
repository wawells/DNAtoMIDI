#import os

#from midiutil.MidiFile import MIDIFile

class DNAtoMidi:
    def __init__(self, filename):
        self.trackNum = None
        self.tempo = None
        self.toParse = None

        self.filename = filename

    def parseFile(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                #do something with content here
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file {str(e)}")

    def toString(self):
        print("track number: " + str(self.trackNum))
        print("tempo: " + str(self.tempo))
        print("Notes: " + self.toParse)



filename = input("Enter filename: ")

converter = DNAtoMidi(filename)
converter.parseFile