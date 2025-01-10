from kmk.keys import KC

def get_layer():
    # Cleaner key names
    ______ = KC.TRNS
    XXXXXX = KC.NO

    # Top Left
    KEY_00 = KC.Q
    KEY_01 = KC.W
    KEY_02 = KC.E
    KEY_03 = KC.R
    KEY_04 = KC.T

    # Middle Left
    KEY_05 = KC.HT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True)
    KEY_06 = KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True)
    KEY_07 = KC.HT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True)
    KEY_08 = KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True)
    KEY_09 = KC.G
    
    # Bottom Left
    KEY_10 = KC.LT(3, KC.Y, prefer_hold=True, tap_interrupted=False)
    KEY_11 = KC.HT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True)
    KEY_12 = KC.C
    KEY_13 = KC.V
    KEY_14 = KC.B

    # Thumb left
    KEY_17 = KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False)
    KEY_18 = KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False)
    KEY_19 = KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False)
    
    
    
     # Top Right
    KEY_24 = KC.Z
    KEY_23 = KC.U
    KEY_22 = KC.I
    KEY_21 = KC.O
    KEY_20 = KC.P
    
    # Middle Right
    KEY_29 = KC.H
    KEY_28 = KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True)
    KEY_27 = KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True)
    KEY_26 = KC.HT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True)
    KEY_25 = KC.HT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True)
    
    # Bottom Right
    KEY_34 = KC.N
    KEY_33 = KC.M
    KEY_32 = KC.COMM,
    KEY_31 = KC.HT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True)
    KEY_30 = KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False)
    
    # Thumb right
    KEY_39 = KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False)
    KEY_38 = KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False)
    KEY_37 = KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False)

    layer = [
        KEY_00, KEY_01, KEY_02, KEY_03, KEY_04,       KEY_24, KEY_23, KEY_22, KEY_21, KEY_20,
        KEY_05, KEY_06, KEY_07, KEY_08, KEY_09,       KEY_29, KEY_28, KEY_27, KEY_26, KEY_25,
        KEY_10, KEY_11, KEY_12, KEY_13, KEY_14,       KEY_34, KEY_33, KEY_32, KEY_31, KEY_30,
        XXXXXX, XXXXXX, KEY_17, KEY_18, KEY_19,       KEY_39, KEY_38, KEY_37, XXXXXX, XXXXXX
    ]

    return layer
