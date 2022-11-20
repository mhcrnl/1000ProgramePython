

import tkinter
import Pmw

def callback(tag):
    # This is called whenever the user clicks on a
    # button in the RadioSelect widget.
    print (tag, 'was pressed.')

# Initialise Tkinter and Pmw.
root = Pmw.initialise(fontScheme = 'pmw1')
root.title('Pmw RadioSelect demonstration')

# Create and pack a RadioSelect widget.
radio = Pmw.RadioSelect(
        command = callback,
        labelpos = 'w',
        label_text = 'Food group:')
radio.pack(padx = 20, pady = 20)

# Add some buttons to the RadioSelect.
for text in ('Fruit', 'Vegetables', 'Cereals', 'Legumes'):
    radio.add(text)
radio.invoke('Vegetables')

# Create an exit button.
exit = Tkinter.Button(text = 'Exit', command = root.destroy)
exit.pack(pady = 20)

# Let's go.
root.mainloop()
