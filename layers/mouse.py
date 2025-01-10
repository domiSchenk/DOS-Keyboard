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
    KEY_12 = KC.TD(XXXXXX, KC.DF(8))
    KEY_13 = KC.TD(XXXXXX, KC.DF(5))
    KEY_14 = XXXXXX

    # Thumb left
    KEY_17 = XXXXXX
    KEY_18 = XXXXXX
    KEY_19 = XXXXXX
    
    
    
     # Top Right
    KEY_24 = KC.LCTL(KC.Y)
    KEY_23 = KC.LSFT(KC.INS)
    KEY_22 = KC.LCTL(KC.INS)
    KEY_21 = KC.LSFT(KC.DEL)
    KEY_20 = KC.LCTL(KC.Z)
    
    # Middle Right
    KEY_29 = XXXXXX
    KEY_28 = KC.MS_LT
    KEY_27 = KC.MS_DN
    KEY_26 = KC.MS_UP
    KEY_25 = KC.MS_RT
    
    # Bottom Right
    KEY_34 = XXXXXX
    KEY_33 = KC.MW_LT
    KEY_32 = KC.MW_DN
    KEY_31 = KC.MW_UP
    KEY_30 = KC.MW_RT
    
    # Thumb right
    KEY_39 = KC.MB_RMB
    KEY_38 = KC.MB_LMB
    KEY_37 = KC.MB_MMB

    layer = [
        KEY_00, KEY_01, KEY_02, KEY_03, KEY_04,       KEY_24, KEY_23, KEY_22, KEY_21, KEY_20,
        KEY_05, KEY_06, KEY_07, KEY_08, KEY_09,       KEY_29, KEY_28, KEY_27, KEY_26, KEY_25,
        KEY_10, KEY_11, KEY_12, KEY_13, KEY_14,       KEY_34, KEY_33, KEY_32, KEY_31, KEY_30,
        XXXXXX, XXXXXX, KEY_17, KEY_18, KEY_19,       KEY_39, KEY_38, KEY_37, XXXXXX, XXXXXX
    ]

    return layer