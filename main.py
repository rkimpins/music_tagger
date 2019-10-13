import os
import eyed3
import json

def pick_directory():
    valid = False
    while not valid:
        try:
            target_dir = input("Enter the name of the directory containing your music:")
            os.chdir(target_dir)
            valid = True
        except:
            print(f"os.chdir({target_dir}) failed")
    print(f"Chose directory {os.getcwd()}")

def one():
    print("one")
def two():
    print("two")
def read_action(letter):
    switcher = {
        'a': one,
        'b': two
    }
    func = switcher.get(letter)
    func()

# Given a filename in our current directory, asks the user to manually update the tags
def manual_tag(filename):
    audiofile = eyed3.load(filename)
    artist = input("Artist:")
    audiofile.tag.artist = artist
    title = input("Title:")
    audiofile.tag.title = title
    album = input("Album:")
    audiofile.tag.album = album
    #audiofile.tag.album_artist = u"Integrity"
    #audiofile.tag.track_num = 2
    audiofile.tag.save()
    print("done")

def main():
    pick_directory()
    '''
    os.chdir("test_dir")
    for filename in os.listdir("."):
        print(filename)
        manual_tag(filename)
    '''
    '''
   import json
    jsonData = '{"name": "Frank", "age": 39}'
    jsonToPython = json.loads(jsonData) 

    pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
    dictionaryToJson = json.dumps(pythonDictionary)
    json.dump(object, file)
    x = json.load(file)
    
    x = dict() ...
    file = open("file", "x")
    json.dump(x, file)
    file.close()
    file = open("file", "r")
    x = json.load(file)
    file.close()
    
    '''
    ''' open files
    file = open("name", "opt") 
        'r' reading 
        'w' writing (overwrite) 
        'x' create and write to new 
        'a' append 
        'r+' read write
    file.read() "one\ntwo\n"
    file.readline() "one\n", watch for overlap, only read this once
    file.readlines() list of "one\n", "two\n"
    file.write("testline") only work if we are in some sort of read mode
    file.close() to see changes
    
    with open("test.txt") as file:
        x = file.readlines()
        ...
    file will be closed by this point, this i how we should do it
    file.seek(offset, whence)
    whence 0 from start, 1 from current post, 2 from end of file
    seek(5) go to 6th bit of file
    '''
main()