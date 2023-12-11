#import kivy

import pyttsx3
from kivy.app import App
# from kivy.properties.ObservableDict.getattr import
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

# Window.size = (900, 100)
#Window.clearcolor = (1,2,3,4)

screen_helper = """
ScreenManager:
    MenuScreen:
    MeScreen:
    

<MenuScreen>:
    name: 'menu'
    
    BoxLayout:	
        orientation: 'vertical'
           
                                
        ActionBar:
            size: 1, 70
            pos: 0,0
            background_color: 1,2,3,4
                    
            ActionView:
                ActionPrevious:
                    title:'     ITIMUS ACADEMY'
                    font_size: 100
                    app_icon: 'image/menu1.png'
                    with_previous: False
                    on_press: root.manager.current = 'me'
        
    TextInput:
        
        id: sul
        base_direction:'weak_ltr'
               #hadle_image_left: 'image/kalem.png'
        hint_text: 'Write the text'
        hint_text_color:[.5,.3,.5,1]
        size_hint:  .6, .3
       # background_active: 1,1,1,10
        pos_hint: {'center_x': .5, 'center_y': .7}
        background_color: 1,2,3,4
        font_size: '.6cm'
       
    Button:
        text: 'Read'
        background_color: 1,2,3,4
        bold: True
        font_size: 22
        size_hint:  .3, .1
        pos_hint: {'center_x': .5, 'center_y': .4}
        on_press: app.speak(sul.text)
        padding: 100, 150
        
<MeScreen>:
    name: "me"
    ScrollView:
		do_scroll_x:False
		do_scroll_y: True
		BoxLayout:	
			orientation: 'vertical'
			size_hint_x: 1
			size_hint_y: 1
							
			ActionBar:
				size: 1, 70
				pos: 0,0
				background_color: 1,2,3,4
				
				ActionView:
					ActionPrevious:
						title:'     ITIMUS ACADEMY'
						font_size: 80
						app_icon: 'image/menu1.png'
						with_previous: False
						on_press: root.manager.current = 'menu'
			GridLayout:
			    cols:1
			    rows:8
			    Label:
                    text:" Dastur nomi:"
                    size_hint_y: None
                    bold:True
                    italic:True
                    size_hint_x: 1
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 30, 8 
                    
                Label:
                    text:"Reader."
                    size_hint_y: None
                    bold:True
                    italic:True
                    size_hint_x: 1
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 30, 8 
                    			
                Label:
                    text:"Turkcha videolar:"
                    size_hint_y: None
                    bold:True
                    italic:True
                    size_hint_x: 1
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 30, 8 
                
                GridLayout:
                    cols:2
                    rows:2
                    padding: 30, 8 
                    Button:
                        text:'Videolar'
                        size_hint_y: 1
                        on_release: app.any_Function2()
                    
                    Button:
                        text:'Kinolar'
                        on_release: app.any_Function2()
                        
                    Label:
                        text:''
                        
                    Label:
                        text:''
                    Label:
                        text:''
                
                Label:
                    text:" Bizni ijtimoiy tarmoqlarda kuzatib boring:"
                    size_hint_y: None
                    bold:True
                    italic:True
                    size_hint_x: 1
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 30, 8 
                
                GridLayout:
                    cols:2
                    rows:3
                    Label:
                        text:'Telegram:'
                    
                    Button:
                        text:'Tiklang'
                        on_release: app.any_Function1()
                    Label:
                        text:'Instagram:'
                    
                    Button:
                        text:'Tiklang'
                        on_release: app.any_Function()
                    Label:
                        text:'YouTube:'
                    
                    Button:
                        text:'Tiklang'
                        on_release: app.any_Function2()         

    """


class MenuScreen(Screen):
    pass

class MeScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(MeScreen(name="me"))

class MyApp(App):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume - 0)
    engine.setProperty('voice', 'venezuala-mbrola-1')

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def speak(self, hello):
        self.engine.say(hello)
       # self.engine.setProperty('voice', voices[1].id)
        self.engine.runAndWait()


if __name__ == '__main__':
    MyApp().run()