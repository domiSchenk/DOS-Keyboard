from kmk.keys import KC

def get_layer():
    # Cleaner key names
    ______ = KC.TRNS
    XXXXXX = KC.NO

    # Top Left
    KEY_00 = 
    KEY_01 = 
    KEY_02 = 
    KEY_03 = 
    KEY_04 = 

    # Middle Left
    KEY_05 = 
    KEY_06 = 
    KEY_07 = 
    KEY_08 = 
    KEY_09 =     
    
    # Bottom Left
    KEY_10 = 
    KEY_11 = 
    KEY_12 = 
    KEY_13 = 
    KEY_14 = 

    # Thumb left
    KEY_17 =
    KEY_18 =
    KEY_19 =
    
    
    
     # Top Right
    KEY_24 = 
    KEY_23 = 
    KEY_22 = 
    KEY_21 = 
    KEY_20 = 
    
    # Middle Right
    KEY_29 = 
    KEY_28 = 
    KEY_27 = 
    KEY_26 = 
    KEY_25 = 
    
    # Bottom Right
    KEY_34 = 
    KEY_33 = 
    KEY_32 = 
    KEY_31 = 
    KEY_30 = 
    
    # Thumb right
    KEY_39 = 
    KEY_38 = 
    KEY_37 = 

    layer = [
        KEY_00, KEY_01, KEY_02, KEY_03, KEY_04,       KEY_24, KEY_23, KEY_22, KEY_21, KEY_20,
        KEY_05, KEY_06, KEY_07, KEY_08, KEY_09,       KEY_29, KEY_28, KEY_27, KEY_26, KEY_25,
        KEY_10, KEY_11, KEY_12, KEY_13, KEY_14,       KEY_34, KEY_33, KEY_32, KEY_31, KEY_30,
        XXXXXX, XXXXXX, KEY_17, KEY_18, KEY_19,       KEY_39, KEY_38, KEY_37, XXXXXX, XXXXXX
    ]

    return layer
