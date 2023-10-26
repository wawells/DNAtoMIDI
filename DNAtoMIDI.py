import mido, random

from mido import MidiFile, MidiTrack, Message


class DNAtoMidi:
    def __init__(self, filename):
        self.trackNum = None
        self.tempo = None
        self.toParse = None
        self.filename = filename

    def str2Int(self, letter):
        if letter == "A":
            val = 69
        elif letter == "G":
            val = 60
        elif letter == "C":
            val = 64
        elif letter == "T":
            val = 67
        else:
            print("Invalid letter in str2Int")
        return val
    
    def getTime(self):
        return random.randint(1, 3000)
    
    def getVelocity(self):
        return random.randint(1, 100)

    def parseFile(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                #do something with content here
                for letter in content:
                    curNote = self.str2Int(letter)
                    curVel = self.getVelocity
                    curTime = self.getTime
                    #may need to start time at 0 and work up from there. How can we do this?

                    
                    
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
converter.parseFile()