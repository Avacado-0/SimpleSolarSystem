from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        add(Sun(app))
        add(Planet(app, tex_id=0, radius=3, period=3, scale=(0.1, 0.1, 0.1)))
        add(Planet(app, tex_id=1, radius=6, period=6, scale=(0.29, 0.29, 0.29)))
        add(Planet(app, tex_id=2, radius=9, period=9, scale=(0.3, 0.3, 0.3)))
        add(Planet(app, tex_id=3, radius=12, period=12, scale=(0.25, 0.25, 0.25)))

    def render(self):
        for obj in self.objects:
            obj.render()
