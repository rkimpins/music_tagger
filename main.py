import os
import eyed3
import json

def pick_directory():
    """ Get the user to pick a directory, and move to it"""
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

def print_tags(filename):
    """GIven a filename, pretty prints all the relevent tags"""

# Given a filename in our current directory, asks the user to manually update the tags
def manual_tag(filename, coverage = "basic"):
    """Given a filename, manually updates each ID3 tag

    Keywords:
        coverage -- "full" gives us more options for tagging
    """

    # Basic Tagging
    audiofile = eyed3.load(filename)
    #TODO make all options skippable (C-D for eof error?)
    """
    try:
        raw_input()
    except EOFError:
        pass
    """
    artist = input("Artist:")
    audiofile.tag.artist = artist
    title = input("Title:")
    audiofile.tag.title = title
    album = input("Album:")
    audiofile.tag.album = album
    # More thorough tagging
    #TODO add more tags to this
    if coverage == "full":
        album_artist = input("Album Artist:")
        audiofile.tag.album_artist = album_artist
        while True:
            track_num = input("Track Number:")
            try:
                track_num = int(track_num)
                break
            except:
                print("Track number must be an integer")
                pass
        audiofile.tag.track_num = track_num
    audiofile.tag.save()
    print("done")

def main():
    """Runs entire program, with nice user interface stuff"""

    """
    More information about function here
    """

    pick_directory()
    '''
    os.chdir("test_dir")
    for filename in os.listdir("."):
        print(filename)
        manual_tag(filename)
    '''

if __name__ == "__main__":
    main()