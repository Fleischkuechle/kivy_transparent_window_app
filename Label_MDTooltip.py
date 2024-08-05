from kivymd.uix.tooltip.tooltip import MDTooltip
from kivymd.uix.label import MDLabel
from kivy.metrics import dp


class Label_MDTooltip (MDLabel,MDTooltip):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.md_bg_color="blue"
        self.pos_hint= {"center_x": .5, "center_y": .5}
        
        
                