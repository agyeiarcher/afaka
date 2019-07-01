from fontParts.world import *
import random
font = OpenFont("afaka.ufo")

bez = BezierPath()
bez.text("hey girl", (100,100))

# # create a bezier path
# path = BezierPath()
# # draw a triangle
# # move to a point
# path.moveTo((100, 100))
# # line to a point
# path.lineTo((100, 900))
# path.lineTo((900, 900))
# # close the path
# path.closePath()
# save the graphics state so the clipping happens only
# temporarily

with savedState():
    # set the path as a clipping path
    fontSize(100)
    clipPath(bez)
    # the oval will be clipped inside the path
    oval(100, 100, 800, 800)