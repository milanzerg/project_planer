from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem

KV = '''
<ContentNavigationDrawer>

    ScrollView:

        MDList:
            OneLineIconListItem:
                
                text: "Main Menu"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "main"
                # IconLeftWidget:
                #     icon: "Notes.png"
            
            OneLineIconListItem:
                
                text: "Notes"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "notes"
                IconLeftWidget:
                    icon: "Notes.png"

            OneLineIconListItem:
                text: "Plans"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "plans"
                IconLeftWidget:
                    icon: "Plans.png"
            
            OneLineIconListItem:
                text: "Notifications"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "notifications"
                IconLeftWidget:
                    icon: "Notifications.png"
            
            OneLineIconListItem:
                text: "Birthday Calendar"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "birthday"
                IconLeftWidget:
                    icon: "calendar.png"
            
            OneLineIconListItem:
                text: "Alarm clock"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "alarm"
                IconLeftWidget:
                    icon: "alarm.png"

                
                


MDScreen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: ""
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
                       
                    
            MDScreen:
                name: "main"

                MDLabel:
                    text: "Main Screen"
                    halign: "center"
                    
                    
            MDScreen:
                name: "notes"
                ScrollView:
                    StackLayoutExample: #!!!!!!!!!!!!!!!!!
                        size_hint: 1, None
                        height: self.minimum_height
                                    
                #MDLabel:
                    
                    
                        
                    
            MDScreen:
                name: "plans"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
            
            MDScreen:
                name: "notifications"

                MDLabel:
                    text: "Screen 3"
                    halign: "center"
            
            MDScreen:
                name: "birthday"

                MDLabel:
                    text: "Screen 4"
                    halign: "center"
            
            MDScreen:
                name: "alarm"

                MDLabel:
                    text: "Screen 5"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            Label = Button(text=str(i), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(Label)

class Note():
    def __init__(self, text, ):


# class ContentNavigationDrawer(MDBoxLayout):
#     def on_start(self):
#         icons_item = {
#             "Notes": "Notes",
#             "Plans": "Plans",
#             "Notifications": "Notifications",
#             "calendar": "Birthday Calendar",
#             "alarm": "Alarm clock",
#         }
#         for icon_name in icons_item.keys():
#             self.root.ids.content_drawer.ids.md_list.add_widget(
#                 ItemDrawer(icon=icon_name, text=icons_item[icon_name])
#             )


class PlannerApp(MDApp):
    def build(self):
        self.icon = "Planner_icon.png"
        return Builder.load_string(KV)


if __name__ == "__main__":
    PlannerApp().run()

# class MainWindow(Screen):
#     pass
#
#
# class SettingsWindow(Screen):
#     pass
#
#
# class WindowManager(ScreenManager):
#     pass
#
#
# kv = Builder.load_file("main.kv")


# class PlannerApp(App):
#
#     def build(self):
#
#         btn = Button(text="Push Me !",
#                      color=(1, 0, .65, 1),
#                      background_normal='normal.png',
#                      background_down='down.png',
#                      size_hint=(.3, .3),
#                      pos_hint={"x": 0.35, "y": 0.3}
#                      )
#         return kv
