from braillebase import BrailleBase

class BrailleBaseFrench(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠨", "⠨⠨", "⠐") 
        #lowercase
        self.append_braille_letter("é", ["⠿"]) #2026/09/10
        self.append_braille_letter("à", ["⠷"]) #2026/09/10
        self.append_braille_letter("è", ["⠮"]) #2026/09/10
        self.append_braille_letter("ù", ["⠾"]) #2026/09/10
        self.append_braille_letter("â", ["⠡"]) #2026/09/10
        self.append_braille_letter("ê", ["⠣"]) #2026/09/10
        self.append_braille_letter("î", ["⠩"]) #2026/09/10
        self.append_braille_letter("ô", ["⠹"]) #2026/09/10
        self.append_braille_letter("û", ["⠱"]) #2026/09/10
        self.append_braille_letter("ë", ["⠫"]) #2026/09/10
        self.append_braille_letter("ï", ["⠻"]) #2026/09/10
        self.append_braille_letter("ü", ["⠳"]) #2026/09/10
        self.append_braille_letter("ç", ["⠯"]) #2026/09/10
        self.append_braille_letter("œ", ["⠪"]) #2026/09/10
        self.append_braille_letter("ÿ", ["⠽"]) #2026/09/10
        self.append_braille_letter("æ", ["⠁", "⠑"]) #2026/09/10
        #uppercase
        self.append_braille_letter("É", ["⠿"],1) #2026/09/10
        self.append_braille_letter("À", ["⠷"],1) #2026/09/10
        self.append_braille_letter("È", ["⠮"],1) #2026/09/10
        self.append_braille_letter("Ù", ["⠾"],1) #2026/09/10
        self.append_braille_letter("Â", ["⠡"],1) #2026/09/10
        self.append_braille_letter("Ê", ["⠣"],1) #2026/09/10
        self.append_braille_letter("Î", ["⠩"],1) #2026/09/10
        self.append_braille_letter("Ô", ["⠹"],1) #2026/09/10
        self.append_braille_letter("Û", ["⠱"],1) #2026/09/10
        self.append_braille_letter("Ë", ["⠫"],1) #2026/09/10
        self.append_braille_letter("Ï", ["⠻"],1) #2026/09/10
        self.append_braille_letter("Ü", ["⠳"],1) #2026/09/10
        self.append_braille_letter("Ç", ["⠯"],1) #2026/09/10
        self.append_braille_letter("Œ", ["⠪"],1) #2026/09/10
        self.append_braille_letter("Ÿ", ["⠽"],1) #2026/09/10
        self.append_braille_letter("Æ", ["⠁", "⠑"]) #2026/09/10
        
        