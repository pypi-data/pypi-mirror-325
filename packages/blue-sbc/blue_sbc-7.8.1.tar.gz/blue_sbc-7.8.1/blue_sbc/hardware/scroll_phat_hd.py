import cv2
import time
from .screen import Screen


class Scroll_Phat_HD(Screen):
    def __init__(self):
        super(Scroll_Phat_HD, self).__init__()
        self.size = (7, 17)
        self.animated = True

    def update_screen(self, image, session, header, sidebar):
        import scrollphathd

        image = cv2.resize(
            image,
            self.size,
        )

        super().update_screen(image, session, header, sidebar)

        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY,
        )

        for y in range(0, 17):
            for x in range(0, 7):
                scrollphathd.set_pixel(y, x, image[y, x] / 255.0)

        time.sleep(0.01)
        scrollphathd.show()

        return self
