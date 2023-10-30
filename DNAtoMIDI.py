import mido, random

from mido import MidiFile, MidiTrack, Message


class DNAtoMidi:
    def __init__(self, filename):
        self.trackNum = None
        self.tempo = None
        self.toParse = None
        self.filename = filename
        self.time = 0
        self.mid = MidiFile()
        self.track = MidiTrack()
        self.mid.tracks.append(self.track)

    def str2Int(self, char):
        if char == "A":
            val = 69
        elif char == "G":
            val = 60
        elif char == "C":
            val = 64
        elif char == "T":
            val = 67
        else:
            val = 50
        return val
    
    def getVelocity(self):
        return random.randint(1, 127)

    def parseFile(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
                for char in content:
                    if not char.isspace():
                        curNote = self.str2Int(char)
                        curVel = self.getVelocity()

                        note_on = Message('note_on', note = curNote, velocity = curVel, time = self.time)
                        self.track.append(note_on)

                        self.time += random.randint(1, 500)

                        note_off = Message('note_off', note = curNote, velocity = curVel, time = self.time)
                        self.track.append(note_off)
                    
                self.mid.save('output.mid')
                    
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {str(e)}")

    def toString(self):
        print("track number: " + str(self.trackNum))
        print("tempo: " + str(self.tempo))
        print("Notes: " + self.toParse)


    



filename = input("Enter filename: ")

converter = DNAtoMidi(filename)
converter.parseFile()