from kmk.keys import KC

def get_layer():
    # Cleaner key names
    ______ = KC.TRNS
    XXXXXX = KC.NO

    # Top Left
    KEY_00 = KC.TD(XXXXXX, KC.RELOAD)
    KEY_01 = KC.TD(XXXXXX, KC.DF(2))
    KEY_02 = KC.TD(XXXXXX, KC.DF(1))
    KEY_03 = KC.TD(XXXXXX, KC.DF(0))
    KEY_04 = XXXXXX

    # Middle Left
    KEY_05 = KC.LGUI
    KEY_06 = KC.LALT
    KEY_07 = KC.LCTL
    KEY_08 = KC.LSFT
    KEY_09 = XXXXXX  
    
    # Bottom Left
    KEY_10 = XXXXXX
    KEY_11 = KC.RALT
    KEY_12 = KC.TD(XXXXXX, KC.DF(9))
    KEY_13 = KC.TD(XXXXXX, KC.DF(6))
    KEY_14 = XXXXXX

    # Thumb left
    KEY_17 = XXXXXX
    KEY_18 = XXXXXX
    KEY_19 = XXXXXX
    
    
    
     # Top Right
    KEY_24 = XXXXXX
    KEY_23 = XXXXXX
    KEY_22 = XXXXXX
    KEY_21 = XXXXXX
    KEY_20 = XXXXXX
    
    # Middle Right
    KEY_29 = XXXXXX 
    KEY_28 = KC.MPRV
    KEY_27 = KC.VOLD
    KEY_26 = KC.VOLU
    KEY_25 = KC.MNXT
    
    # Bottom Right
    KEY_34 = KC.HID
    KEY_33 = XXXXXX
    KEY_32 = XXXXXX
    KEY_31 = XXXXXX
    KEY_30 = XXXXXX
    
    # Thumb right
    KEY_39 = KC.MSTP
    KEY_38 = KC.MPLY
    KEY_37 = KC.MUTE

    layer = [
        KEY_00, KEY_01, KEY_02, KEY_03, KEY_04,       KEY_24, KEY_23, KEY_22, KEY_21, KEY_20,
        KEY_05, KEY_06, KEY_07, KEY_08, KEY_09,       KEY_29, KEY_28, KEY_27, KEY_26, KEY_25,
        KEY_10, KEY_11, KEY_12, KEY_13, KEY_14,       KEY_34, KEY_33, KEY_32, KEY_31, KEY_30,
        XXXXXX, XXXXXX, KEY_17, KEY_18, KEY_19,       KEY_39, KEY_38, KEY_37, XXXXXX, XXXXXX
    ]

    return layer
