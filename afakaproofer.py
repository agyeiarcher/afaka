from fontParts.world import *
import random

font = OpenFont("afaka.ufo")

print(font.info.xHeight)

letters=[]
columnchecker=0

def drawGlyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)

def proof_caption(gName):
    text("SYMBOL NAME: "+gName, (30,height()-30))
    text("AFAKA SCRIPT // AGYEI ARCHER 2019", (width()-240,height()-30))
    
def text_path_main(samplestring1, samplestring2, pos, font_path, thisGlyph):
    # using code from Jens Kutilek's SVG Builder
    # https://github.com/jenskutilek/sudo-font/blob/master/scripts/BuildWebSVGs.py
    x, y = pos
    save()
    translate(x, y)
    fill(0.8)
    h=font[thisGlyph.name]
    if h in samplestring1:
        samplestring1=samplestring1.remove(h)
    for l in samplestring1:
        g = font[l]
        drawGlyph(g)
        translate(g.width)
    fill(0)
    drawGlyph(h)
    translate(h.width)
    fill(0.8)
    if h in samplestring2:
        samplestring2=samplestring2.remove(h)
    for l in samplestring2:
        g = font[l]
        drawGlyph(g)
        translate(g.width)
    restore()

def char_list(font):
    for g in font:
        if g.markColor:
            if not g.isEmpty():
                letters.append(g.name)
    return letters        
        
def make_sheet(font):
    for thisGlyph in font:
        if thisGlyph.markColor:
            if not thisGlyph.isEmpty():
                newPage("LetterLandscape")
                proof_caption(thisGlyph.name)
                translate(20,0)
                samplestring=[]
                # print(g.name)
                char_list(font)
                samplestring1=random.sample(letters, 5)
                samplestring2=random.sample(letters, 5)
                samplestring3=random.sample(letters, 2)
                samplestring4=random.sample(letters, 2)
                with savedState():
                    translate(0,50)
                    scale(0.05)
                    text_path_main(samplestring1, samplestring2, (50,50), font, thisGlyph)
                with savedState():
                    translate(0,400)
                    with savedState():
                        scale(0.15)
                        text_path_main(samplestring3, samplestring4, (5,100), font, thisGlyph)
                    stroke(0)
                    translate(-20,15)
                    line((0,0),(width(),0))
                    translate(0,font.info.xHeight)
                
make_sheet(font)
saveImage("Afaka Studies_Round 1_AA.pdf")