from kmk.keys import KC

def get_layer():
    # Cleaner key names
    ______ = KC.TRNS
    XXXXXX = KC.NO

    # Top Left
    KEY_00 = KC.Q
    KEY_01 = KC.W
    KEY_02 = KC.F
    KEY_03 = KC.P
    KEY_04 = KC.B
    
    # Middle Left
    KEY_05 = KC.A
    KEY_06 = KC.R
    KEY_07 = KC.S
    KEY_08 = KC.T
    KEY_09 = KC.G
    
    # Bottom Left
    KEY_10 = KC.Z
    KEY_11 = KC.X
    KEY_12 = KC.C
    KEY_13 = KC.D
    KEY_14 = KC.V 
    
    # Thumb left
    KEY_17 = KC.ESC
    KEY_18 = KC.SPC
    KEY_19 = KC.TAB
    
    
    # Top Right
    KEY_24 = KC.J
    KEY_23 = KC.L
    KEY_22 = KC.U
    KEY_21 = KC.Y
    KEY_20 = KC.QUOT
   
    # Middle Right
    KEY_29 = KC.M
    KEY_28 = KC.N
    KEY_27 = KC.E
    KEY_26 = KC.I
    KEY_25 = KC.O
    
    # Bottom Right
    KEY_34 = KC.K
    KEY_33 = KC.H
    KEY_32 = KC.COMM
    KEY_31 = KC.DOT
    KEY_30 = KC.SLSH
    
    # Thumb right
    KEY_39 = KC.ENT
    KEY_38 = KC.BSPC
    KEY_37 = KC.DEL

    layer = [
        KEY_00, KEY_01, KEY_02, KEY_03, KEY_04,       KEY_24, KEY_23, KEY_22, KEY_21, KEY_20,
        KEY_05, KEY_06, KEY_07, KEY_08, KEY_09,       KEY_29, KEY_28, KEY_27, KEY_26, KEY_25,
        KEY_10, KEY_11, KEY_12, KEY_13, KEY_14,       KEY_34, KEY_33, KEY_32, KEY_31, KEY_30,
        XXXXXX, XXXXXX, KEY_17, KEY_18, KEY_19,       KEY_39, KEY_38, KEY_37, XXXXXX, XXXXXX
    ]

    return layer
