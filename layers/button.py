from kmk.keys import KC

def get_layer():
    # Cleaner key names
    ______ = KC.TRNS
    XXXXXX = KC.NO

    # Top Left
    KEY_00 = KC.LCTL(KC.Z)
    KEY_01 = KC.LSFT(KC.DEL)
    KEY_02 = KC.LCTL(KC.INS)
    KEY_03 = KC.LSFT(KC.INS)
    KEY_04 = KC.LCTL(KC.Y)

    # Middle Left
    KEY_05 = KC.LGUI
    KEY_06 = KC.LALT
    KEY_07 = KC.LCTL
    KEY_08 = KC.LSFT
    KEY_09 = KC.TG(0) 
    
    # Bottom Left
    KEY_10 = KC.LCTL(KC.Z)
    KEY_11 = KC.LSFT(KC.DEL)
    KEY_12 = KC.LCTL(KC.INS)
    KEY_13 = KC.LSFT(KC.INS)
    KEY_14 = KC.LCTL(KC.Y)

    # Thumb left
    KEY_17 = KC.MB_MMB
    KEY_18 = KC.MB_LMB
    KEY_19 = KC.MB_RMB
    
    
    
     # Top Right
    KEY_24 = KC.LCTL(KC.Y)
    KEY_23 = KC.LSFT(KC.INS)
    KEY_22 = KC.LCTL(KC.INS)
    KEY_21 = KC.LSFT(KC.DEL)
    KEY_20 = KC.LCTL(KC.Z)
    
    # Middle Right
    KEY_29 = XXXXXX
    KEY_28 = KC.LSFT
    KEY_27 = KC.LCTL
    KEY_26 = KC.LALT
    KEY_25 = KC.LGUI
    
    # Bottom Right
    KEY_34 = KC.LCTL(KC.Y)
    KEY_33 = KC.LSFT(KC.INS)
    KEY_32 = KC.LCTL(KC.INS)
    KEY_31 = KC.LSFT(KC.DEL)
    KEY_30 = KC.LCTL(KC.Z)
    
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
