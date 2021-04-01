import sys

# import pyperclip if it exists, if it does not then don't try to use it
try:
    __import__('pyperclip')
except ImportError:
    clpbrd = False
else:
    import pyperclip
    clpbrd = True

# function to handle logic
def gen_fname(ss, gg):
    # format is:
    # ss-gg-yyt-p-xnn descriptor

    # ss = student number
    # ss = '09' # for anoush

    # gg = group number
    if not gg:
        gg = input('Enter two digit group number: ')
        # gg = '00' # for individual stuff
    
    # yyt = year and term
    yyt = '21S'

    # p = project identifier
    p_text = \
    '''Project identifier options:
        0	No associated project
        1	CAD Lessons
        2	3D Printer Mods
        3	Fidget Spinner
        4	Chronometer
    Selection: '''
    p = input(p_text)

    # x = drawing identifier
    x = input('\033[1m\033[4m'+'P'+'\033[0m'+'art or '+'\033[1m\033[4m'+'A'+'\033[0m'+'ssembly? ')
    # x = 'P' # or 'A' for assembly

    # nn = part number
    nn = input('Two digit part number: ')
    # nn = '01'

    # descriptor
    descriptor = input('Description: ')
    # descriptor = 'widget'

    # generate file name
    fname = f'{ss}-{gg}-{yyt}-{p}-{x}{nn} {descriptor}'

    # display result, and copy to clipboard if possible
    if clpbrd:
        pyperclip.copy(fname)
        print(f'Filename:\n {fname}\nhas been copied to the clipboard.')
    else:
        print(f'Filename:\n {fname}')

# person info dictionaries
anoush = {
    'ss': '09',
    'gg': None
}

bridger = {
    'ss': '08',
    'gg': None
}

vann = {
    'ss': '07',
    'gg': None
}

# handle running script
if __name__ == "__main__":
    if len(sys.argv) == 1:
        # assume anoush is running script
        print(f'Running script as anoush')
        gen_fname(anoush['ss'], anoush['gg'])
    else:
        person = sys.argv[-1]
        print(f'Running script as {person}')
        if person == 'anoush' or person == 'a':
            gen_fname(anoush['ss'], anoush['gg'])
        elif person == 'bridger' or person == 'b':
            gen_fname(bridger['ss'], bridger['gg'])
        elif person == 'vann' or person == 'v':
            gen_fname(vann['ss'], vann['gg'])