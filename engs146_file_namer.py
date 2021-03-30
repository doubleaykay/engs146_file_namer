import pyperclip

# format is:
# ss-gg-yyt-p-xnn descriptor

# FIXED
ss = '09' # for anoush
yyt = '21S'

# NOT FIXED
# gg
gg = input('Enter two digit group number: ')
# gg = '00' # for individual stuff

# p
p_text = \
'''Project identifier options:
    0	No associated project
    1	CAD Lessons
    2	3D Printer Mods
    3	Fidget Spinner
    4	Chronometer
Selection: '''
p = input(p_text)

# x
x = input('\033[1m\033[4m'+'P'+'\033[0m'+'art or '+'\033[1m\033[4m'+'A'+'\033[0m'+'ssembly? ')
# x = 'P' # or 'A' for assembly

# nn
nn = input('Two digit part number: ')
# nn = '01'

# descriptor
descriptor = input('Description: ')
# descriptor = 'widget'

# generate file name
fname = f'{ss}-{gg}-{yyt}-{p}-{x}{nn} {descriptor}'
pyperclip.copy(fname)
print(f'Filename:\n {fname}\nhas been copied to the clipboard.')