from kivy.app import App


class PlannerApp(App):
    def build(self):
        self.icon = "Planner_icon.png"


if __name__ == "__main__":
    PlannerApp().run()