from typing import Any
from kivymd.uix.slider import MDSlider
from kivy.metrics import dp
from kivymd.uix.card import  MDCard
from kivymd.uix.label import MDLabel
if not __name__ == '__main__':
    from .Label_MDTooltip import Label_MDTooltip
else:
    from Label_MDTooltip import Label_MDTooltip
class Base_Slider_Card (MDCard):
   
    def __init__(   self,
                    data_model:Any=None, 
                    data_model_overwrite_attribute_name:str=None,
                    label_text:str="nothing",
                    min_slider_value:float=1,
                    max_slider_value:float=100,
                    default_slider_value:float=5,
                    slider_step_size:float=1,
                    
                    id:str="Base_Slider_Card",
                    tooltip_text:str="""Tooltip is missing""",
                    size_hint_value:tuple[float,float]=(0.8,0.1),
                    pos_hint_center_x:float=0.5,
                    pos_hint_center_y:float=0.5,
                    top_pos_hint_y:float=None,
                    tooltip_shift_left:float=0,
                    tooltip_shift_right:float=0,
                    tooltip_display_delay:float=0.5,
                    tooltip_shift_y:float=-150,
                    self_orientation:str='horizontal',
                    label_hint_value:tuple[float,float]=(0.4,1),
                    **kwargs):
        super().__init__(**kwargs)
        #self.overwrite_variable=overwrite_variable
        self.data_model:Any = data_model
        self.data_model_overwrite_attribute_name:str = data_model_overwrite_attribute_name
        self.label_text:str=f"[b]{label_text}:[/b]"
        self.min_slider_value:float=min_slider_value
        self.max_slider_value:float=max_slider_value
        self.default_slider_value:float=default_slider_value
        self.slider_step_size:float=slider_step_size
        self.id:str=id
        self.tooltip_text:str=tooltip_text
        self.size_hint_value:tuple[float,float]=size_hint_value
        self.top_pos_hint_y:float=top_pos_hint_y
        if self.top_pos_hint_y:
            self.pos_hint:dict={"center_x": pos_hint_center_x, "top": self.top_pos_hint_y}
        else:
            self.pos_hint:dict={"center_x": pos_hint_center_x, "center_y": pos_hint_center_y}
        self.tooltip_shift_left:float=tooltip_shift_left
        self.tooltip_shift_right:float=tooltip_shift_right
        self.tooltip_display_delay:float=tooltip_display_delay
        self.tooltip_shift_y:float=tooltip_shift_y
        self.orientation:str= self_orientation 
        self.label_hint_value:tuple[float,float]=label_hint_value
        self.visible:bool=True
        self.hovering:bool=True
        self.opaceValue:float=0.9
        self.transparent_value:float=0.4
        self.opacity:float=self.transparent_value # Set the opacity for transparency
        self.spacing:float=1
        self.str_text_color:str="white"
        
        if self.orientation=='vertical':
             self.label_hint_value=(label_hint_value[1],label_hint_value[0])
        self.size_hint=self.size_hint_value

        self.md_bg_color="grey"
 
        self.Label:Label_MDTooltip=Label_MDTooltip(     text=self.label_text,
                                                        #halign="center",
                                                        halign="left",
                                                        markup=True,
                                                        theme_text_color="Custom",
                                                        text_color=self.str_text_color,
                                                        #adaptive_size=True,
                                                        size_hint=self.label_hint_value,
                                                        pos_hint={"center_x": .5, "center_y": .5},
                                                        tooltip_text=self.tooltip_text,
                                                        shift_left=self.tooltip_shift_left,
                                                        shift_right=self.tooltip_shift_right,
                                                        tooltip_display_delay=self.tooltip_display_delay,
                                                        shift_y=self.tooltip_shift_y,
                                                        
                                                    )
        self.Label.bind(text_size=self.adjust_text_size)
        self.Label.radius=self.radius
        self.Label.padding=(dp(0),dp(0),dp(0),dp(0))
        
       

        self.slider:MDSlider= MDSlider   (   min= self.min_slider_value,
                                            max= self.max_slider_value,
                                            value= self.default_slider_value,
                                            size_hint=(1,1),
                                            pos_hint={"center_x": .5, "center_y": .5},
                                        )
        self.slider.orientation=self.orientation
        self.slider.bind(on_touch_up=self.slider_callback)
        self.slider.bind(on_touch_move=self.slider_on_touch_move)

        self.slider.hint_text_color=self.str_text_color
        self.slider.step=self.slider_step_size
        self.slider.padding_y=0

        self.label_2_hint_value=(0.1,1)
        self.Label_2=MDLabel(   text=str(self.slider.value),
                                halign="center",
                                #halign="left",
                                markup=True,
                                theme_text_color="Custom",
                                text_color=self.str_text_color,
                                size_hint=self.label_2_hint_value,
                                pos_hint={"center_x": .5, "center_y": .5},
                            )
        self.Label_2.md_bg_color="blue"
        self.Label_2.radius=self.radius
        self.Label_2.bind(text_size=self.adjust_text_size_2)

        self.on_enter=self.makeVisible
        self.on_leave=self.make_transparent

        self.add_widget(self.Label)
        self.add_widget(self.slider)
        self.add_widget(self.Label_2)
    
    def update_data_model_attribute(self, new_value):
        if self.data_model and self.data_model_overwrite_attribute_name:
            setattr(self.data_model, self.data_model_overwrite_attribute_name, new_value)

    
    def adjust_text_size(self, instance, value):
        instance.text_size = instance.width  ,None # Adjust the multiplier as needed for font size scaling
        instance.font_size = instance.width *0.08 # Adjust the multiplier as needed for font size scaling

    def adjust_text_size_2(self, instance, value):
        instance.text_size = instance.width  ,None # Adjust the multiplier as needed for font size scaling
        instance.font_size = instance.width *0.3 # Adjust the multiplier as needed for font size scaling



    def hide(self):
        self.scale_value_x=0
        self.Label.size_hint=(None,None)
        self.slider.size_hint=(None,None)
        self.size_hint=(None,None)
        self.slider.size=(0,0)
        self.size=(0,0)
        self.visible=False

    def show(self):
        self.scale_value_x=1
        self.Label.size_hint=self.label_hint_value
        self.slider.size_hint=(1,1)
        self.size_hint=self.size_hint_value
        self.visible=True

    def slider_callback(self,instance,mouse=None):#
        pass
    
    def slider_on_touch_move(self,instance,mouse=None):
        if self.slider.active:
            self.opacity=self.opaceValue
            slider_value:float=instance.value
            if slider_value<=self.max_slider_value and slider_value>=self.min_slider_value:
                self.Label_2.text = str(round(slider_value,3))
                #self.overwrite_variable=round(slider_value,3)
                self.update_data_model_attribute(new_value=round(slider_value,3))
                #self.mocam.set_neck_length(cm_neck_length=slider_value)
    
    def makeVisible(self,):
        self.opacity=self.opaceValue

    def make_transparent(self):
        self.opacity=self.transparent_value


import win32api
import win32gui
import win32con

from kivy.core.window import Window
from kivymd.app import MDApp
class Transparent_window_App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style= "Dark"
    def build(self):
        self.window_transparency:int=60
        Window.set_title(self.__class__.__name__)
        # HWND = win32gui.FindWindow(None, self.__class__.__name__)
        # win32gui.SetWindowLong(HWND, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(HWND, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        # win32gui.SetLayeredWindowAttributes(HWND, win32api.RGB(0,0,0),self.window_transparency, win32con.LWA_ALPHA)
        

        self.HWND = win32gui.FindWindow(None, self.__class__.__name__)
        win32gui.SetWindowLong(self.HWND, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(self.HWND, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        win32gui.SetLayeredWindowAttributes(self.HWND, win32api.RGB(0,0,0),self.window_transparency,win32con.LWA_ALPHA)
        self.data_model:Any=None 
        self.data_model_overwrite_attribute_name:str=None
        self.label_text:str="Window transparency 0 to 255"
        self.min_slider_value:float=0
        self.max_slider_value:float=255
        self.default_slider_value:float=(self.min_slider_value+self.max_slider_value)/2
        self.slider_step_size:float=1
        
        self.id:str="Base_Slider_Card"
        self.tooltip_text:str="""Tooltip is missing"""
        self.size_hint_value:tuple[float,float]=(0.8,0.1)
        self.pos_hint_center_x:float=0.5
        self.pos_hint_center_y:float=0.5
        self.top_pos_hint_y:float=None
        self.tooltip_shift_left:float=0
        self.tooltip_shift_right:float=0
        self.tooltip_display_delay:float=0.5
        self.tooltip_shift_y:float=-150
        self.self_orientation:str='horizontal'
        self.label_hint_value:tuple[float,float]=(0.4,1)





        self.base_slider_card:Base_Slider_Card=Base_Slider_Card(
                                                                data_model=self.data_model, 
                                                                data_model_overwrite_attribute_name=self.data_model_overwrite_attribute_name,
                                                                label_text=self.label_text,
                                                                min_slider_value=self.min_slider_value,
                                                                max_slider_value=self.max_slider_value,
                                                                default_slider_value=self.default_slider_value,
                                                                slider_step_size=self.slider_step_size,
                                                                
                                                                id=self.id,
                                                                tooltip_text=self.tooltip_text,
                                                                size_hint_value=self.size_hint_value,
                                                                pos_hint_center_x=self.pos_hint_center_x,
                                                                pos_hint_center_y=self.pos_hint_center_y,
                                                                top_pos_hint_y=self.top_pos_hint_y,
                                                                tooltip_shift_left=self.tooltip_shift_left,
                                                                tooltip_shift_right=self.tooltip_shift_right,
                                                                tooltip_display_delay=self.tooltip_display_delay,
                                                                tooltip_shift_y=self.tooltip_shift_y,
                                                                self_orientation=self.self_orientation,
                                                                label_hint_value=self.label_hint_value,
                                                                )
        #self.base_slider_card.on_touch_move=self.set_window_transparency()
        self.base_slider_card.bind(on_touch_move=self.set_window_transparency)
        return self.base_slider_card
    def set_window_transparency(self,instance=None,value=None,test=None):
        if instance:
            self.window_transparency=int(instance.slider.value)
        else:
            self.window_transparency:int=60
        win32gui.SetLayeredWindowAttributes(self.HWND, win32api.RGB(0,0,0),self.window_transparency,win32con.LWA_ALPHA) 
        


if __name__ == '__main__':
    Transparent_window_App().run()