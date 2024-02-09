import pygame as pg
import sys
import moderngl as mgl
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene


class GraphicsEngine:
    def __init__(self, win_size=(1400, 750)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings, are commented out
        # ###pg.event.set_grab(True)
        # ###pg.mouse.set_visible(False)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.frame_rate = 0
        # Class objects
        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear frame buffer
        self.ctx.clear(color=(0.08, 0.16, 0.18, 1))
        # render scene
        self.scene.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        # yields time in seconds
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.frame_rate = self.clock.tick(60)  # sets up how fast the game should run.
            # There will be ~ 60 frames per second. self.delta_time will be the frame rate

if __name__ == '__main__':
    # runs everything
    app = GraphicsEngine()
    app.run()
