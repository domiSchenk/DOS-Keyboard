from kmk.keys import KC

def get_layer():
    # Cleaner key names
    _______ = KC.TRNS
    XXXXXX = KC.NO

    # Top Left
    KEY_00 = KC.LBRC
    KEY_01 = KC.N7
    KEY_02 = KC.N8
    KEY_03 = KC.N9
    KEY_04 = KC.RBRC

    # Middle Left
    KEY_05 = KC.SCLN
    KEY_06 = KC.N4
    KEY_07 = KC.N5
    KEY_08 = KC.N6
    KEY_09 = KC.EQL    
    
    # Bottom Left
    KEY_10 = KC.GRV
    KEY_11 = KC.N1
    KEY_12 = KC.N2
    KEY_13 = KC.N3
    KEY_14 = KC.BSLS

    # Thumb left
    KEY_17 = KC.DOT
    KEY_18 = KC.N0
    KEY_19 = KC.MINS
    
    
    
     # Top Right
    KEY_24 = XXXXXX
    KEY_23 = KC.TD(XXXXXX, KC.DF(0))
    KEY_22 = KC.TD(XXXXXX, KC.DF(1))
    KEY_21 = KC.TD(XXXXXX, KC.DF(2))
    KEY_20 = KC.TD(XXXXXX, KC.RELOAD)
    
    # Middle Right
    KEY_29 = XXXXXX
    KEY_28 = KC.LSFT
    KEY_27 = KC.LCTL
    KEY_26 = KC.LALT
    KEY_25 = KC.LGUI
    
    # Bottom Right
    KEY_34 = XXXXXX
    KEY_33 = KC.TD(XXXXXX, KC.DF(7))
    KEY_32 = KC.TD(XXXXXX, KC.DF(4))
    KEY_31 = KC.RALT
    KEY_30 = XXXXXX
    
    # Thumb right
    KEY_39 = XXXXXX
    KEY_38 = XXXXXX
    KEY_37 = XXXXXX

    layer = [
        KEY_00, KEY_01, KEY_02, KEY_03, KEY_04,       KEY_24, KEY_23, KEY_22, KEY_21, KEY_20,
        KEY_05, KEY_06, KEY_07, KEY_08, KEY_09,       KEY_29, KEY_28, KEY_27, KEY_26, KEY_25,
        KEY_10, KEY_11, KEY_12, KEY_13, KEY_14,       KEY_34, KEY_33, KEY_32, KEY_31, KEY_30,
        XXXXXX, XXXXXX, KEY_17, KEY_18, KEY_19,       KEY_39, KEY_38, KEY_37, XXXXXX, XXXXXX
    ]

    return layer
