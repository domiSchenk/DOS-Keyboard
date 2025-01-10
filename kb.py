import board 

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation




class DOSKeyboard(_KMKKeyboard):
    col_pins = (
        board.D27, board.D26, board.D22, board.D20, board.D23  # Columns
    )
    
    row_pins = (
        board.D4, board.D5, board.D6, board.D7  # Rows
    )

    debug_enabled = False
    diode_orientation = DiodeOrientation.ROWS
