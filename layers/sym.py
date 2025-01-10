from kmk.keys import KC

def get_layer():
    # Cleaner key names
    ______ = KC.TRNS
    XXXXXX = KC.NO

    # Top Left
    KEY_00 = XXXXXX
    KEY_01 = KC.AMPR
    KEY_02 = KC.ASTR
    KEY_03 = KC.HASH
    KEY_04 = KC.PIPE

    # Middle Left
    KEY_05 = KC.COLN
    KEY_06 = KC.DLR
    KEY_07 = KC.PERC
    KEY_08 = KC.CIRC
    KEY_09 = KC.PLUS 
    
    # Bottom Left
    KEY_10 = KC.TILD
    KEY_11 = KC.EXLM
    KEY_12 = KC.AT
    KEY_13 = KC.LBRC
    KEY_14 = KC.RBRC

    # Thumb left
    KEY_17 = KC.TD(KC.LPRN, KC.LCBR)
    KEY_18 = KC.TD(KC.RPRN, KC.RCBR)
    KEY_19 = KC.SCLN
    
    
    
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
    KEY_33 = KC.TD(XXXXXX, KC.DF(8))
    KEY_32 = KC.TD(XXXXXX, KC.DF(5))
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
