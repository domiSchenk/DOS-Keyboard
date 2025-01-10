import board

from kb import DOSKeyboard

from kmk.keys import KC, make_key
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide

# Miryoku modules
from kmk.modules.holdtap import HoldTap; # Old ModTap
from kmk.modules.tapdance import TapDance; 
from kmk.modules.mouse_keys import MouseKeys; 
from kmk.modules.capsword import CapsWord;
from kmk.modules.macros import Macros, Press, Release, Tap, UnicodeModeWinC;
from kmk.modules.combos import Combos, Chord, Sequence;

from kmk.extensions.media_keys import MediaKeys; 
from kmk.extensions.international import International

# from kmk.modules.power import Power; Does not work


# Debug
# print(dir(board))

# Initialize the keyboard
keyboard = DOSKeyboard()

# Modules
layers = Layers()

holdtap = HoldTap()
holdtap.tap_time = 300

tabdance = TapDance()
tabdance.tap_time = 200

mousekeys = MouseKeys()
capsword = CapsWord()
macros = Macros(unicode_mode=UnicodeModeWinC)
combos = Combos()

# Extensions
mediakeys = MediaKeys()
international = International()
# power = Power()

# Import base layer
import layers.base as baseLayer; base = baseLayer.get_layer()
import layers.game as gameLayer; game = gameLayer.get_layer()
import layers.tap as tabLayer; tap = tabLayer.get_layer()
import layers.nav as navLayer; nav = navLayer.get_layer()
import layers.button as buttonLayer; button = buttonLayer.get_layer()
import layers.mouse as mouseLayer; mouse = mouseLayer.get_layer()
import layers.media as mediaLayer; media = mediaLayer.get_layer()
import layers.num as numLayer; num = numLayer.get_layer()
import layers.sym as symLayer; sym = symLayer.get_layer()
import layers.fun as funLayer; fun = funLayer.get_layer()



# Define the QWERTZ layout keymap for the left half
keyboard.keymap = [
    base,
    game,
    tap,
    button,
    nav,
    mouse,
    media, 
    num,
    sym,
    fun
]

# Configure the Split module
split = Split(
    data_pin = board.D1,
    split_type = SplitType.UART,
    uart_flip = True,
    use_pio = True
    # split_side=side,
    )

keyboard.modules = [layers, holdtap, tabdance, mousekeys, capsword, combos, macros, split]
keyboard.extensions = [international, mediakeys]

if __name__ == '__main__':
    print('starting keyboard DOS')
    keyboard.go()

