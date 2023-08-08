"""
File: my_drawing.py
Name: Feng Angie
----------------------
Make a color chart form GObject.
"""

from campy.graphics.gobjects import GRect, GLabel, GArc
from campy.graphics.gwindow import GWindow

WIDTH = 100
HEIGHT = 80


def main():
    """
    Title: 想畫彩虹卻找不到合適的顏色一氣之下就做了色票

    draw a color chart for all GObject color.
    without white, black, palevioletred, papayawhip and -grey.
    """
    window = GWindow(width=1500, height=840, title="GObject Colors")
    label = GLabel("GObject Colors")
    label.font = '-20-bold'
    window.add(label, x=(window.width-label.width)/2, y=label.height)

    rect1 = GRect(WIDTH, HEIGHT)
    rect1.filled = True
    rect1.fill_color = 'aliceblue'
    rect1.color = 'aliceblue'
    window.add(rect1, x=0, y=label.height)
    label1 = GLabel('aliceblue')
    label1.font = '-10'
    window.add(label1, x=0, y=label.height+HEIGHT+label1.height)

    rect2 = GRect(WIDTH, HEIGHT)
    rect2.filled = True
    rect2.fill_color = 'antiquewhite'
    rect2.color = 'antiquewhite'
    window.add(rect2, x=WIDTH, y=label.height)
    label2 = GLabel('antiquewhite')
    label2.font = '-10'
    window.add(label2, x=WIDTH, y=label.height+HEIGHT+label1.height)

    rect3 = GRect(WIDTH, HEIGHT)
    rect3.filled = True
    rect3.fill_color = 'aqua'
    rect3.color = 'aqua'
    window.add(rect3, x=WIDTH*2, y=label.height)
    label3 = GLabel('aqua')
    label3.font = '-10'
    window.add(label3, x=WIDTH*2, y=label.height+HEIGHT+label1.height)

    rect4 = GRect(WIDTH, HEIGHT)
    rect4.filled = True
    rect4.fill_color = 'aquamarine'
    rect4.color = 'aquamarine'
    window.add(rect4, x=WIDTH*3, y=label.height)
    label4 = GLabel('aquamarine')
    label4.font = '-10'
    window.add(label4, x=WIDTH*3, y=label.height+HEIGHT+label1.height)

    rect5 = GRect(WIDTH, HEIGHT)
    rect5.filled = True
    rect5.fill_color = 'azure'
    rect5.color = 'azure'
    window.add(rect5, x=WIDTH*4, y=label.height)
    label5 = GLabel('azure')
    label5.font = '-10'
    window.add(label5, x=WIDTH*4, y=label.height+HEIGHT+label1.height)

    rect6 = GRect(WIDTH, HEIGHT)
    rect6.filled = True
    rect6.fill_color = 'beige'
    rect6.color = 'beige'
    window.add(rect6, x=0, y=label.height + HEIGHT + label1.height)
    label6 = GLabel('beige')
    label6.font = '-10'
    window.add(label6, x=0, y=label.height + (HEIGHT+10)*2)

    rect7 = GRect(WIDTH, HEIGHT)
    rect7.filled = True
    rect7.fill_color = 'bisque'
    rect7.color = 'bisque'
    window.add(rect7, x=WIDTH, y=label.height + HEIGHT + label1.height)
    label7 = GLabel('bisque')
    label7.font = '-10'
    window.add(label7, x=WIDTH, y=label.height + (HEIGHT+10)*2)

    rect108 = GRect(WIDTH, HEIGHT)
    rect108.filled = True
    rect108.fill_color = 'paleturquoise'
    rect108.color = 'paleturquoise'
    window.add(rect108, x=WIDTH * 2, y=label.height + HEIGHT + label1.height)
    label108 = GLabel('paleturquoise')
    label108.font = '-10'
    window.add(label108, x=WIDTH * 2, y=label.height + (HEIGHT+10)*2)

    rect9 = GRect(WIDTH, HEIGHT)
    rect9.filled = True
    rect9.fill_color = 'blanchedalmond'
    rect9.color = 'blanchedalmond'
    window.add(rect9, x=WIDTH * 3, y=label.height + HEIGHT + label1.height)
    label9 = GLabel('blanchedalmond')
    label9.font = '-10'
    window.add(label9, x=WIDTH * 3, y=label.height + (HEIGHT+10)*2)

    rect10 = GRect(WIDTH, HEIGHT)
    rect10.filled = True
    rect10.fill_color = 'blue'
    rect10.color = 'blue'
    window.add(rect10, x=WIDTH * 4, y=label.height + HEIGHT + label1.height)
    label10 = GLabel('blue')
    label10.font = '-10'
    window.add(label10, x=WIDTH * 4, y=label.height + (HEIGHT+10)*2)

    rect11 = GRect(WIDTH, HEIGHT)
    rect11.filled = True
    rect11.fill_color = 'blueviolet'
    rect11.color = 'blueviolet'
    window.add(rect11, x=0, y=label.height + (HEIGHT + label1.height)*2)
    label11 = GLabel('blueviolet')
    label11.font = '-10'
    window.add(label11, x=0, y=label.height + (HEIGHT+10)*3)

    rect12 = GRect(WIDTH, HEIGHT)
    rect12.filled = True
    rect12.fill_color = 'brown'
    rect12.color = 'brown'
    window.add(rect12, x=WIDTH, y=label.height + (HEIGHT + label1.height)*2)
    label12 = GLabel('brown')
    label12.font = '-10'
    window.add(label12, x=WIDTH, y=label.height + (HEIGHT+10)*3)

    rect13 = GRect(WIDTH, HEIGHT)
    rect13.filled = True
    rect13.fill_color = 'burlywood'
    rect13.color = 'burlywood'
    window.add(rect13, x=WIDTH*2, y=label.height + (HEIGHT + label1.height)*2)
    label13 = GLabel('burlywood')
    label13.font = '-10'
    window.add(label13, x=WIDTH*2, y=label.height + (HEIGHT+10)*3)

    rect14 = GRect(WIDTH, HEIGHT)
    rect14.filled = True
    rect14.fill_color = 'cadetblue'
    rect14.color = 'cadetblue'
    window.add(rect14, x=WIDTH*3, y=label.height + (HEIGHT + label1.height)*2)
    label14 = GLabel('cadetblue')
    label14.font = '-10'
    window.add(label14, x=WIDTH*3, y=label.height + (HEIGHT+10)*3)

    rect15 = GRect(WIDTH, HEIGHT)
    rect15.filled = True
    rect15.fill_color = 'chartreuse'
    rect15.color = 'chartreuse'
    window.add(rect15, x=WIDTH*4, y=label.height + (HEIGHT + label1.height)*2)
    label15 = GLabel('chartreuse')
    label15.font = '-10'
    window.add(label15, x=WIDTH*4, y=label.height + (HEIGHT+10)*3)

    rect16 = GRect(WIDTH, HEIGHT)
    rect16.filled = True
    rect16.fill_color = 'chocolate'
    rect16.color = 'chocolate'
    window.add(rect16, x=0, y=label.height + (HEIGHT + label1.height)*3)
    label16 = GLabel('chocolate')
    label16.font = '-10'
    window.add(label16, x=0, y=label.height + (HEIGHT+10)*4)

    rect17 = GRect(WIDTH, HEIGHT)
    rect17.filled = True
    rect17.fill_color = 'coral'
    rect17.color = 'coral'
    window.add(rect17, x=WIDTH, y=label.height + (HEIGHT + label1.height)*3)
    label17 = GLabel('coral')
    label17.font = '-10'
    window.add(label17, x=WIDTH, y=label.height + (HEIGHT+10)*4)

    rect18 = GRect(WIDTH, HEIGHT)
    rect18.filled = True
    rect18.fill_color = 'cornflowerblue'
    rect18.color = 'cornflowerblue'
    window.add(rect18, x=WIDTH*2, y=label.height + (HEIGHT + label1.height)*3)
    label18 = GLabel('cornflowerblue')
    label18.font = '-10'
    window.add(label18, x=WIDTH*2, y=label.height + (HEIGHT+10)*4)

    rect19 = GRect(WIDTH, HEIGHT)
    rect19.filled = True
    rect19.fill_color = 'cornsilk'
    rect19.color = 'cornsilk'
    window.add(rect19, x=WIDTH * 3, y=label.height + (HEIGHT + label1.height) * 3)
    label19 = GLabel('cornsilk')
    label19.font = '-10'
    window.add(label19, x=WIDTH * 3, y=label.height + (HEIGHT + 10) * 4)

    rect20 = GRect(WIDTH, HEIGHT)
    rect20.filled = True
    rect20.fill_color = 'crimson'
    rect20.color = 'crimson'
    window.add(rect20, x=WIDTH * 4, y=label.height + (HEIGHT + label1.height) * 3)
    label20 = GLabel('crimson')
    label20.font = '-10'
    window.add(label20, x=WIDTH * 4, y=label.height + (HEIGHT + 10) * 4)

    rect21 = GRect(WIDTH, HEIGHT)
    rect21.filled = True
    rect21.fill_color = 'cyan'
    rect21.color = 'cyan'
    window.add(rect21, x=0, y=label.height + (HEIGHT + label1.height) * 4)
    label21 = GLabel('cyan')
    label21.font = '-10'
    window.add(label21, x=0, y=label.height + (HEIGHT + 10) * 5)

    rect22 = GRect(WIDTH, HEIGHT)
    rect22.filled = True
    rect22.fill_color = 'darkblue'
    rect22.color = 'darkblue'
    window.add(rect22, x=WIDTH, y=label.height + (HEIGHT + label1.height) * 4)
    label22 = GLabel('darkblue')
    label22.font = '-10'
    window.add(label22, x=WIDTH, y=label.height + (HEIGHT + 10) * 5)

    rect23 = GRect(WIDTH, HEIGHT)
    rect23.filled = True
    rect23.fill_color = 'darkcyan'
    rect23.color = 'darkcyan'
    window.add(rect23, x=WIDTH*2, y=label.height + (HEIGHT + label1.height) * 4)
    label23 = GLabel('darkcyan')
    label23.font = '-10'
    window.add(label23, x=WIDTH*2, y=label.height + (HEIGHT + 10) * 5)

    rect24 = GRect(WIDTH, HEIGHT)
    rect24.filled = True
    rect24.fill_color = 'darkgoldenrod'
    rect24.color = 'darkgoldenrod'
    window.add(rect24, x=WIDTH*3, y=label.height + (HEIGHT + label1.height) * 4)
    label24 = GLabel('darkgoldenrod')
    label24.font = '-10'
    window.add(label24, x=WIDTH*3, y=label.height + (HEIGHT + 10) * 5)

    rect25 = GRect(WIDTH, HEIGHT)
    rect25.filled = True
    rect25.fill_color = 'darkgray'
    rect25.color = 'darkgray'
    window.add(rect25, x=WIDTH*4, y=label.height + (HEIGHT + label1.height) * 4)
    label25 = GLabel('darkgray')
    label25.font = '-10'
    window.add(label25, x=WIDTH*4, y=label.height + (HEIGHT + 10) * 5)

    rect26 = GRect(WIDTH, HEIGHT)
    rect26.filled = True
    rect26.fill_color = 'darkorange'
    rect26.color = 'darkorange'
    window.add(rect26, x=0, y=label.height + (HEIGHT + label1.height) * 5)
    label26 = GLabel('darkorange')
    label26.font = '-10'
    window.add(label26, x=0, y=label.height + (HEIGHT + 10) * 6)

    rect27 = GRect(WIDTH, HEIGHT)
    rect27.filled = True
    rect27.fill_color = 'darkorchid'
    rect27.color = 'darkorchid'
    window.add(rect27, x=WIDTH, y=label.height + (HEIGHT + label1.height) * 5)
    label27 = GLabel('darkorchid')
    label27.font = '-10'
    window.add(label27, x=WIDTH, y=label.height + (HEIGHT + 10) * 6)

    rect28 = GRect(WIDTH, HEIGHT)
    rect28.filled = True
    rect28.fill_color = 'darkred'
    rect28.color = 'darkred'
    window.add(rect28, x=WIDTH*2, y=label.height + (HEIGHT + label1.height) * 5)
    label28 = GLabel('darkred')
    label28.font = '-10'
    window.add(label28, x=WIDTH*2, y=label.height + (HEIGHT + 10) * 6)

    rect29 = GRect(WIDTH, HEIGHT)
    rect29.filled = True
    rect29.fill_color = 'darksage'
    rect29.color = 'darksage'
    window.add(rect29, x=WIDTH*3, y=label.height + (HEIGHT + label1.height) * 5)
    label29 = GLabel('darksage')
    label29.font = '-10'
    window.add(label29, x=WIDTH*3, y=label.height + (HEIGHT + 10) * 6)

    rect30 = GRect(WIDTH, HEIGHT)
    rect30.filled = True
    rect30.fill_color = 'darksalmon'
    rect30.color = 'darksalmon'
    window.add(rect30, x=WIDTH*4, y=label.height + (HEIGHT + label1.height) * 5)
    label30 = GLabel('darksalmon')
    label30.font = '-10'
    window.add(label30, x=WIDTH*4, y=label.height + (HEIGHT + 10) * 6)

    rect31 = GRect(WIDTH, HEIGHT)
    rect31.filled = True
    rect31.fill_color = 'darkseagreen'
    rect31.color = 'darkseagreen'
    window.add(rect31, x=0, y=label.height + (HEIGHT + label1.height) * 6)
    label31 = GLabel('darkseagreen')
    label31.font = '-10'
    window.add(label31, x=0, y=label.height + (HEIGHT + 10) * 7)

    rect32 = GRect(WIDTH, HEIGHT)
    rect32.filled = True
    rect32.fill_color = 'darkslateblue'
    rect32.color = 'darkslateblue'
    window.add(rect32, x=WIDTH, y=label.height + (HEIGHT + label1.height) * 6)
    label32 = GLabel('darkslateblue')
    label32.font = '-10'
    window.add(label32, x=WIDTH, y=label.height + (HEIGHT + 10) * 7)

    rect33 = GRect(WIDTH, HEIGHT)
    rect33.filled = True
    rect33.fill_color = 'darkslategray'
    rect33.color = 'darkslategray'
    window.add(rect33, x=WIDTH*2, y=label.height + (HEIGHT + label1.height) * 6)
    label33 = GLabel('darkslategray')
    label33.font = '-10'
    window.add(label33, x=WIDTH*2, y=label.height + (HEIGHT + 10) * 7)

    rect101 = GRect(WIDTH, HEIGHT)
    rect101.filled = True
    rect101.fill_color = 'olive'
    rect101.color = 'olive'
    window.add(rect101, x=WIDTH*3, y=label.height + (HEIGHT + label1.height) * 6)
    label101 = GLabel('olive')
    label101.font = '-10'
    window.add(label101, x=WIDTH*3, y=label.height + (HEIGHT + 10) * 7)

    rect35 = GRect(WIDTH, HEIGHT)
    rect35.filled = True
    rect35.fill_color = 'darkturquoise'
    rect35.color = 'darkturquoise'
    window.add(rect35, x=WIDTH * 4, y=label.height + (HEIGHT + label1.height) * 6)
    label35 = GLabel('darkturquoise')
    label35.font = '-10'
    window.add(label35, x=WIDTH * 4, y=label.height + (HEIGHT + 10) * 7)

    rect36 = GRect(WIDTH, HEIGHT)
    rect36.filled = True
    rect36.fill_color = 'darkviolet'
    rect36.color = 'darkviolet'
    window.add(rect36, x=0, y=label.height + (HEIGHT + label1.height) * 7)
    label36 = GLabel('darkviolet')
    label36.font = '-10'
    window.add(label36, x=0, y=label.height + (HEIGHT + 10) * 8)

    rect37 = GRect(WIDTH, HEIGHT)
    rect37.filled = True
    rect37.fill_color = 'deeppink'
    rect37.color = 'deeppink'
    window.add(rect37, x=WIDTH, y=label.height + (HEIGHT + label1.height) * 7)
    label37 = GLabel('deeppink')
    label37.font = '-10'
    window.add(label37, x=WIDTH, y=label.height + (HEIGHT + 10) * 8)

    rect38 = GRect(WIDTH, HEIGHT)
    rect38.filled = True
    rect38.fill_color = 'deepskyblue'
    rect38.color = 'deepskyblue'
    window.add(rect38, x=WIDTH*2, y=label.height + (HEIGHT + label1.height) * 7)
    label38 = GLabel('deepskyblue')
    label38.font = '-10'
    window.add(label38, x=WIDTH*2, y=label.height + (HEIGHT + 10) * 8)

    rect39 = GRect(WIDTH, HEIGHT)
    rect39.filled = True
    rect39.fill_color = 'dimgray'
    rect39.color = 'dimgray'
    window.add(rect39, x=WIDTH*3, y=label.height + (HEIGHT + label1.height) * 7)
    label39 = GLabel('dimgray')
    label39.font = '-10'
    window.add(label39, x=WIDTH*3, y=label.height + (HEIGHT + 10) * 8)

    rect102 = GRect(WIDTH, HEIGHT)
    rect102.filled = True
    rect102.fill_color = 'olivedrab'
    rect102.color = 'olivedrab'
    window.add(rect102, x=WIDTH*4, y=label.height + (HEIGHT + label1.height) * 7)
    label102 = GLabel('olivedrab')
    label102.font = '-10'
    window.add(label102, x=WIDTH*4, y=label.height + (HEIGHT + 10) * 8)

    rect41 = GRect(WIDTH, HEIGHT)
    rect41.filled = True
    rect41.fill_color = 'dodgerblue'
    rect41.color = 'dodgerblue'
    window.add(rect41, x=0, y=label.height + (HEIGHT + label1.height) * 8)
    label41 = GLabel('dodgerblue')
    label41.font = '-10'
    window.add(label41, x=0, y=label.height + (HEIGHT + 10) * 9)

    rect42 = GRect(WIDTH, HEIGHT)
    rect42.filled = True
    rect42.fill_color = 'firebrick'
    rect42.color = 'firebrick'
    window.add(rect42, x=WIDTH, y=label.height + (HEIGHT + label1.height) * 8)
    label42 = GLabel('firebrick')
    label42.font = '-10'
    window.add(label42, x=WIDTH, y=label.height + (HEIGHT + 10) * 9)

    rect43 = GRect(WIDTH, HEIGHT)
    rect43.filled = True
    rect43.fill_color = 'floralwhite'
    rect43.color = 'floralwhite'
    window.add(rect43, x=WIDTH*2, y=label.height + (HEIGHT + label1.height) * 8)
    label43 = GLabel('floralwhite')
    label43.font = '-10'
    window.add(label43, x=WIDTH*2, y=label.height + (HEIGHT + 10) * 9)

    rect44 = GRect(WIDTH, HEIGHT)
    rect44.filled = True
    rect44.fill_color = 'forestgreen'
    rect44.color = 'forestgreen'
    window.add(rect44, x=WIDTH*3, y=label.height + (HEIGHT + label1.height) * 8)
    label44 = GLabel('forestgreen')
    label44.font = '-10'
    window.add(label44, x=WIDTH*3, y=label.height + (HEIGHT + 10) * 9)

    rect45 = GRect(WIDTH, HEIGHT)
    rect45.filled = True
    rect45.fill_color = 'fuchsia'
    rect45.color = 'fuchsia'
    window.add(rect45, x=WIDTH*4, y=label.height + (HEIGHT + label1.height) * 8)
    label45 = GLabel('fuchsia')
    label45.font = '-10'
    window.add(label45, x=WIDTH*4, y=label.height + (HEIGHT + 10) * 9)

    rect46 = GRect(WIDTH, HEIGHT)
    rect46.filled = True
    rect46.fill_color = 'gainsboro'
    rect46.color = 'gainsboro'
    window.add(rect46, x=WIDTH*5, y=label.height)
    label46 = GLabel('gainsboro')
    label46.font = '-10'
    window.add(label46, x=WIDTH*5, y=label.height + (HEIGHT + 10))

    rect47 = GRect(WIDTH, HEIGHT)
    rect47.filled = True
    rect47.fill_color = 'ghostwhite'
    rect47.color = 'ghostwhite'
    window.add(rect47, x=WIDTH*6, y=label.height)
    label47 = GLabel('ghostwhite')
    label47.font = '-10'
    window.add(label47, x=WIDTH*6, y=label.height + (HEIGHT + 10))

    rect48 = GRect(WIDTH, HEIGHT)
    rect48.filled = True
    rect48.fill_color = 'gold'
    rect48.color = 'gold'
    window.add(rect48, x=WIDTH*7, y=label.height)
    label48 = GLabel('gold')
    label48.font = '-10'
    window.add(label48, x=WIDTH*7, y=label.height + (HEIGHT + 10))

    rect49 = GRect(WIDTH, HEIGHT)
    rect49.filled = True
    rect49.fill_color = 'goldenrod'
    rect49.color = 'goldenrod'
    window.add(rect49, x=WIDTH*8, y=label.height)
    label49 = GLabel('goldenrod')
    label49.font = '-10'
    window.add(label49, x=WIDTH*8, y=label.height + (HEIGHT + 10))

    rect50 = GRect(WIDTH, HEIGHT)
    rect50.filled = True
    rect50.fill_color = 'gray'
    rect50.color = 'gray'
    window.add(rect50, x=WIDTH*9, y=label.height)
    label50 = GLabel('gray')
    label50.font = '-10'
    window.add(label50, x=WIDTH*9, y=label.height + (HEIGHT + 10))

    rect51 = GRect(WIDTH, HEIGHT)
    rect51.filled = True
    rect51.fill_color = 'green'
    rect51.color = 'green'
    window.add(rect51, x=WIDTH*5, y=label.height + (HEIGHT + label1.height))
    label51 = GLabel('green')
    label51.font = '-10'
    window.add(label51, x=WIDTH*5, y=label.height + (HEIGHT + 10) * 2)

    rect52 = GRect(WIDTH, HEIGHT)
    rect52.filled = True
    rect52.fill_color = 'greenyellow'
    rect52.color = 'greenyellow'
    window.add(rect52, x=WIDTH*6, y=label.height + (HEIGHT + label1.height))
    label52 = GLabel('greenyellow')
    label52.font = '-10'
    window.add(label52, x=WIDTH*6, y=label.height + (HEIGHT + 10) * 2)

    rect103 = GRect(WIDTH, HEIGHT)
    rect103.filled = True
    rect103.fill_color = 'orange'
    rect103.color = 'orange'
    window.add(rect103, x=WIDTH*7, y=label.height + (HEIGHT + label1.height))
    label103 = GLabel('orange')
    label103.font = '-10'
    window.add(label103, x=WIDTH*7, y=label.height + (HEIGHT + 10) * 2)

    rect54 = GRect(WIDTH, HEIGHT)
    rect54.filled = True
    rect54.fill_color = 'honeydew'
    rect54.color = 'honeydew'
    window.add(rect54, x=WIDTH*8, y=label.height + (HEIGHT + label1.height))
    label54 = GLabel('honeydew')
    label54.font = '-10'
    window.add(label54, x=WIDTH*8, y=label.height + (HEIGHT + 10) * 2)

    rect55 = GRect(WIDTH, HEIGHT)
    rect55.filled = True
    rect55.fill_color = 'hotpink'
    rect55.color = 'hotpink'
    window.add(rect55, x=WIDTH*9, y=label.height + (HEIGHT + label1.height))
    label55 = GLabel('hotpink')
    label55.font = '-10'
    window.add(label55, x=WIDTH*9, y=label.height + (HEIGHT + 10) * 2)

    rect56 = GRect(WIDTH, HEIGHT)
    rect56.filled = True
    rect56.fill_color = 'indianred'
    rect56.color = 'indianred'
    window.add(rect56, x=WIDTH*5, y=label.height + (HEIGHT + label1.height)*2)
    label56 = GLabel('indianred')
    label56.font = '-10'
    window.add(label56, x=WIDTH*5, y=label.height + (HEIGHT+10)*3)

    rect57 = GRect(WIDTH, HEIGHT)
    rect57.filled = True
    rect57.fill_color = 'indigo'
    rect57.color = 'indigo'
    window.add(rect57, x=WIDTH*6, y=label.height + (HEIGHT + label1.height)*2)
    label57 = GLabel('indigo')
    label57.font = '-10'
    window.add(label57, x=WIDTH*6, y=label.height + (HEIGHT + 10)*3)

    rect58 = GRect(WIDTH, HEIGHT)
    rect58.filled = True
    rect58.fill_color = 'ivory'
    rect58.color = 'ivory'
    window.add(rect58, x=WIDTH*7, y=label.height + (HEIGHT + label1.height)*2)
    label58 = GLabel('ivory')
    label58.font = '-10'
    window.add(label58, x=WIDTH*7, y=label.height + (HEIGHT + 10)*3)

    rect59 = GRect(WIDTH, HEIGHT)
    rect59.filled = True
    rect59.fill_color = 'khaki'
    rect59.color = 'khaki'
    window.add(rect59, x=WIDTH*8, y=label.height + (HEIGHT + label1.height)*2)
    label59 = GLabel('khaki')
    label59.font = '-10'
    window.add(label59, x=WIDTH*8, y=label.height + (HEIGHT + 10)*3)

    rect60 = GRect(WIDTH, HEIGHT)
    rect60.filled = True
    rect60.fill_color = 'lavender'
    rect60.color = 'lavender'
    window.add(rect60, x=WIDTH*9, y=label.height + (HEIGHT + label1.height)*2)
    label60 = GLabel('lavender')
    label60.font = '-10'
    window.add(label60, x=WIDTH*9, y=label.height + (HEIGHT + 10)*3)

    rect61 = GRect(WIDTH, HEIGHT)
    rect61.filled = True
    rect61.fill_color = 'lavenderblush'
    rect61.color = 'lavenderblush'
    window.add(rect61, x=WIDTH*5, y=label.height + (HEIGHT + label1.height)*3)
    label61 = GLabel('lavenderblush')
    label61.font = '-10'
    window.add(label61, x=WIDTH*5, y=label.height + (HEIGHT + 10) * 4)

    rect62 = GRect(WIDTH, HEIGHT)
    rect62.filled = True
    rect62.fill_color = 'lawngreen'
    rect62.color = 'lawngreen'
    window.add(rect62, x=WIDTH*6, y=label.height + (HEIGHT + label1.height)*3)
    label62 = GLabel('lawngreen')
    label62.font = '-10'
    window.add(label62, x=WIDTH*6, y=label.height + (HEIGHT + 10) * 4)

    rect63 = GRect(WIDTH, HEIGHT)
    rect63.filled = True
    rect63.fill_color = 'lemonchiffon'
    rect63.color = 'lemonchiffon'
    window.add(rect63, x=WIDTH*7, y=label.height + (HEIGHT + label1.height)*3)
    label63 = GLabel('lemonchiffon')
    label63.font = '-10'
    window.add(label63, x=WIDTH*7, y=label.height + (HEIGHT + 10) * 4)

    rect64 = GRect(WIDTH, HEIGHT)
    rect64.filled = True
    rect64.fill_color = 'lightblue'
    rect64.color = 'lightblue'
    window.add(rect64, x=WIDTH*8, y=label.height + (HEIGHT + label1.height)*3)
    label64 = GLabel('lightblue')
    label64.font = '-10'
    window.add(label64, x=WIDTH*8, y=label.height + (HEIGHT + 10) * 4)

    rect65 = GRect(WIDTH, HEIGHT)
    rect65.filled = True
    rect65.fill_color = 'lightcoral'
    rect65.color = 'lightcoral'
    window.add(rect65, x=WIDTH*9, y=label.height + (HEIGHT + label1.height)*3)
    label65 = GLabel('lightcoral')
    label65.font = '-10'
    window.add(label65, x=WIDTH*9, y=label.height + (HEIGHT + 10) * 4)

    rect66 = GRect(WIDTH, HEIGHT)
    rect66.filled = True
    rect66.fill_color = 'lightcyan'
    rect66.color = 'lightcyan'
    window.add(rect66, x=WIDTH*5, y=label.height + (HEIGHT + label1.height)*4)
    label66 = GLabel('lightcyan')
    label66.font = '-10'
    window.add(label66, x=WIDTH*5, y=label.height + (HEIGHT+10)*5)

    rect67 = GRect(WIDTH, HEIGHT)
    rect67.filled = True
    rect67.fill_color = 'lightgoldenrodyellow'
    rect67.color = 'lightgoldenrodyellow'
    window.add(rect67, x=WIDTH*6, y=label.height + (HEIGHT + label1.height)*4)
    label67 = GLabel('lightgoldenrodyellow')
    label67.font = '-10'
    window.add(label67, x=WIDTH*6, y=label.height + (HEIGHT + 10)*5)

    rect68 = GRect(WIDTH, HEIGHT)
    rect68.filled = True
    rect68.fill_color = 'lightgray'
    rect68.color = 'lightgray'
    window.add(rect68, x=WIDTH*7, y=label.height + (HEIGHT + label1.height)*4)
    label68 = GLabel('lightgray')
    label68.font = '-10'
    window.add(label68, x=WIDTH*7, y=label.height + (HEIGHT + 10)*5)

    rect69 = GRect(WIDTH, HEIGHT)
    rect69.filled = True
    rect69.fill_color = 'lightgreen'
    rect69.color = 'lightgreen'
    window.add(rect69, x=WIDTH*8, y=label.height + (HEIGHT + label1.height)*4)
    label69 = GLabel('lightgreen')
    label69.font = '-10'
    window.add(label69, x=WIDTH*8, y=label.height + (HEIGHT + 10)*5)

    rect104 = GRect(WIDTH, HEIGHT)
    rect104.filled = True
    rect104.fill_color = 'orangered'
    rect104.color = 'orangered'
    window.add(rect104, x=WIDTH*9, y=label.height + (HEIGHT + label1.height)*4)
    label104 = GLabel('orangered')
    label104.font = '-10'
    window.add(label104, x=WIDTH*9, y=label.height + (HEIGHT + 10)*5)

    rect71 = GRect(WIDTH, HEIGHT)
    rect71.filled = True
    rect71.fill_color = 'lightpink'
    rect71.color = 'lightpink'
    window.add(rect71, x=WIDTH*5, y=label.height + (HEIGHT + label1.height)*5)
    label71 = GLabel('lightpink')
    label71.font = '-10'
    window.add(label71, x=WIDTH*5, y=label.height + (HEIGHT + 10) * 6)

    rect72 = GRect(WIDTH, HEIGHT)
    rect72.filled = True
    rect72.fill_color = 'lightsage'
    rect72.color = 'lightsage'
    window.add(rect72, x=WIDTH*6, y=label.height + (HEIGHT + label1.height)*5)
    label72 = GLabel('lightsage')
    label72.font = '-10'
    window.add(label72, x=WIDTH*6, y=label.height + (HEIGHT + 10) * 6)

    rect73 = GRect(WIDTH, HEIGHT)
    rect73.filled = True
    rect73.fill_color = 'lightsalmon'
    rect73.color = 'lightsalmon'
    window.add(rect73, x=WIDTH*7, y=label.height + (HEIGHT + label1.height)*5)
    label73 = GLabel('lightsalmon')
    label73.font = '-10'
    window.add(label73, x=WIDTH*7, y=label.height + (HEIGHT + 10) * 6)

    rect74 = GRect(WIDTH, HEIGHT)
    rect74.filled = True
    rect74.fill_color = 'lightseagreen'
    rect74.color = 'lightseagreen'
    window.add(rect74, x=WIDTH*8, y=label.height + (HEIGHT + label1.height)*5)
    label74 = GLabel('lightseagreen')
    label74.font = '-10'
    window.add(label74, x=WIDTH*8, y=label.height + (HEIGHT + 10) * 6)

    rect75 = GRect(WIDTH, HEIGHT)
    rect75.filled = True
    rect75.fill_color = 'lightskyblue'
    rect75.color = 'lightskyblue'
    window.add(rect75, x=WIDTH*9, y=label.height + (HEIGHT + label1.height)*5)
    label75 = GLabel('lightskyblue')
    label75.font = '-10'
    window.add(label75, x=WIDTH*9, y=label.height + (HEIGHT + 10) * 6)

    rect76 = GRect(WIDTH, HEIGHT)
    rect76.filled = True
    rect76.fill_color = 'lightslategray'
    rect76.color = 'lightslategray'
    window.add(rect76, x=WIDTH*5, y=label.height + (HEIGHT + label1.height)*6)
    label76 = GLabel('lightslategray')
    label76.font = '-10'
    window.add(label76, x=WIDTH*5, y=label.height + (HEIGHT+10)*7)

    rect105 = GRect(WIDTH, HEIGHT)
    rect105.filled = True
    rect105.fill_color = 'orchid'
    rect105.color = 'orchid'
    window.add(rect105, x=WIDTH*6, y=label.height + (HEIGHT + label1.height)*6)
    label105 = GLabel('orchid')
    label105.font = '-10'
    window.add(label105, x=WIDTH*6, y=label.height + (HEIGHT + 10)*7)

    rect78 = GRect(WIDTH, HEIGHT)
    rect78.filled = True
    rect78.fill_color = 'lightsteelblue'
    rect78.color = 'lightsteelblue'
    window.add(rect78, x=WIDTH*7, y=label.height + (HEIGHT + label1.height)*6)
    label78 = GLabel('lightsteelblue')
    label78.font = '-10'
    window.add(label78, x=WIDTH*7, y=label.height + (HEIGHT + 10)*7)

    rect79 = GRect(WIDTH, HEIGHT)
    rect79.filled = True
    rect79.fill_color = 'lightyellow'
    rect79.color = 'lightyellow'
    window.add(rect79, x=WIDTH*8, y=label.height + (HEIGHT + label1.height)*6)
    label79 = GLabel('lightyellow')
    label79.font = '-10'
    window.add(label79, x=WIDTH*8, y=label.height + (HEIGHT + 10)*7)

    rect80 = GRect(WIDTH, HEIGHT)
    rect80.filled = True
    rect80.fill_color = 'lime'
    rect80.color = 'lime'
    window.add(rect80, x=WIDTH*9, y=label.height + (HEIGHT + label1.height)*6)
    label80 = GLabel('lime')
    label80.font = '-10'
    window.add(label80, x=WIDTH*9, y=label.height + (HEIGHT + 10)*7)

    rect81 = GRect(WIDTH, HEIGHT)
    rect81.filled = True
    rect81.fill_color = 'limegreen'
    rect81.color = 'limegreen'
    window.add(rect81, x=WIDTH*5, y=label.height + (HEIGHT + label1.height)*7)
    label81 = GLabel('limegreen')
    label81.font = '-10'
    window.add(label81, x=WIDTH*5, y=label.height + (HEIGHT + 10) * 8)

    rect82 = GRect(WIDTH, HEIGHT)
    rect82.filled = True
    rect82.fill_color = 'linen'
    rect82.color = 'linen'
    window.add(rect82, x=WIDTH*6, y=label.height + (HEIGHT + label1.height)*7)
    label82 = GLabel('linen')
    label82.font = '-10'
    window.add(label82, x=WIDTH*6, y=label.height + (HEIGHT + 10) * 8)

    rect83 = GRect(WIDTH, HEIGHT)
    rect83.filled = True
    rect83.fill_color = 'magenta'
    rect83.color = 'magenta'
    window.add(rect83, x=WIDTH*7, y=label.height + (HEIGHT + label1.height)*7)
    label83 = GLabel('magenta')
    label83.font = '-10'
    window.add(label83, x=WIDTH*7, y=label.height + (HEIGHT + 10) * 8)

    rect84 = GRect(WIDTH, HEIGHT)
    rect84.filled = True
    rect84.fill_color = 'maroon'
    rect84.color = 'maroon'
    window.add(rect84, x=WIDTH*8, y=label.height + (HEIGHT + label1.height)*7)
    label84 = GLabel('maroon')
    label84.font = '-10'
    window.add(label84, x=WIDTH*8, y=label.height + (HEIGHT + 10) * 8)

    rect85 = GRect(WIDTH, HEIGHT)
    rect85.filled = True
    rect85.fill_color = 'mediumaquamarine'
    rect85.color = 'mediumaquamarine'
    window.add(rect85, x=WIDTH*9, y=label.height + (HEIGHT + label1.height)*7)
    label85 = GLabel('mediumaquamarine')
    label85.font = '-10'
    window.add(label85, x=WIDTH*9, y=label.height + (HEIGHT + 10) * 8)

    rect86 = GRect(WIDTH, HEIGHT)
    rect86.filled = True
    rect86.fill_color = 'mediumblue'
    rect86.color = 'mediumblue'
    window.add(rect86, x=WIDTH*5, y=label.height + (HEIGHT + label1.height)*8)
    label86 = GLabel('mediumblue')
    label86.font = '-10'
    window.add(label86, x=WIDTH*5, y=label.height + (HEIGHT + 10) * 9)

    rect87 = GRect(WIDTH, HEIGHT)
    rect87.filled = True
    rect87.fill_color = 'mediumorchid'
    rect87.color = 'mediumorchid'
    window.add(rect87, x=WIDTH*6, y=label.height + (HEIGHT + label1.height)*8)
    label87 = GLabel('mediumorchid')
    label87.font = '-10'
    window.add(label87, x=WIDTH*6, y=label.height + (HEIGHT + 10) * 9)

    rect88 = GRect(WIDTH, HEIGHT)
    rect88.filled = True
    rect88.fill_color = 'mediumpurple'
    rect88.color = 'mediumpurple'
    window.add(rect88, x=WIDTH*7, y=label.height + (HEIGHT + label1.height)*8)
    label88 = GLabel('mediumpurple')
    label88.font = '-10'
    window.add(label88, x=WIDTH*7, y=label.height + (HEIGHT + 10) * 9)

    rect89 = GRect(WIDTH, HEIGHT)
    rect89.filled = True
    rect89.fill_color = 'mediumseagreen'
    rect89.color = 'mediumseagreen'
    window.add(rect89, x=WIDTH*8, y=label.height + (HEIGHT + label1.height)*8)
    label89 = GLabel('mediumseagreen')
    label89.font = '-10'
    window.add(label89, x=WIDTH*8, y=label.height + (HEIGHT + 10) * 9)

    rect90 = GRect(WIDTH, HEIGHT)
    rect90.filled = True
    rect90.fill_color = 'mediumslateblue'
    rect90.color = 'mediumslateblue'
    window.add(rect90, x=WIDTH*9, y=label.height + (HEIGHT + label1.height)*8)
    label90 = GLabel('mediumslateblue')
    label90.font = '-10'
    window.add(label90, x=WIDTH*9, y=label.height + (HEIGHT + 10) * 9)

    rect91 = GRect(WIDTH, HEIGHT)
    rect91.filled = True
    rect91.fill_color = 'mediumspringgreen'
    rect91.color = 'mediumspringgreen'
    window.add(rect91, x=WIDTH*10, y=label.height)
    label91 = GLabel('mediumspringgreen')
    label91.font = '-10'
    window.add(label91, x=WIDTH*10, y=label.height + HEIGHT + label1.height)

    rect92 = GRect(WIDTH, HEIGHT)
    rect92.filled = True
    rect92.fill_color = 'mediumturquoise'
    rect92.color = 'mediumturquoise'
    window.add(rect92, x=WIDTH*11, y=label.height)
    label92 = GLabel('mediumturquoise')
    label92.font = '-10'
    window.add(label92, x=WIDTH*11, y=label.height + HEIGHT + label1.height)

    rect93 = GRect(WIDTH, HEIGHT)
    rect93.filled = True
    rect93.fill_color = 'mediumvioletred'
    rect93.color = 'mediumvioletred'
    window.add(rect93, x=WIDTH * 12, y=label.height)
    label93 = GLabel('mediumvioletred')
    label93.font = '-10'
    window.add(label93, x=WIDTH * 12, y=label.height + HEIGHT + label1.height)

    rect94 = GRect(WIDTH, HEIGHT)
    rect94.filled = True
    rect94.fill_color = 'midnightblue'
    rect94.color = 'midnightblue'
    window.add(rect94, x=WIDTH * 13, y=label.height)
    label94 = GLabel('midnightblue')
    label94.font = '-10'
    window.add(label94, x=WIDTH * 13, y=label.height + HEIGHT + label1.height)

    rect95 = GRect(WIDTH, HEIGHT)
    rect95.filled = True
    rect95.fill_color = 'mintcream'
    rect95.color = 'mintcream'
    window.add(rect95, x=WIDTH * 14, y=label.height)
    label95 = GLabel('mintcream')
    label95.font = '-10'
    window.add(label95, x=WIDTH * 14, y=label.height + HEIGHT + label1.height)

    rect96 = GRect(WIDTH, HEIGHT)
    rect96.filled = True
    rect96.fill_color = 'mistyrose'
    rect96.color = 'mistyrose'
    window.add(rect96, x=WIDTH*10, y=label.height + HEIGHT + label1.height)
    label96 = GLabel('mistyrose')
    label96.font = '-10'
    window.add(label96, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 2)

    rect97 = GRect(WIDTH, HEIGHT)
    rect97.filled = True
    rect97.fill_color = 'moccasin'
    rect97.color = 'moccasin'
    window.add(rect97, x=WIDTH*11, y=label.height + HEIGHT + label1.height)
    label97 = GLabel('moccasin')
    label97.font = '-10'
    window.add(label97, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 2)

    rect98 = GRect(WIDTH, HEIGHT)
    rect98.filled = True
    rect98.fill_color = 'navajowhite'
    rect98.color = 'navajowhite'
    window.add(rect98, x=WIDTH * 12, y=label.height + HEIGHT + label1.height)
    label98 = GLabel('navajowhite')
    label98.font = '-10'
    window.add(label98, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 2)

    rect99 = GRect(WIDTH, HEIGHT)
    rect99.filled = True
    rect99.fill_color = 'navy'
    rect99.color = 'navy'
    window.add(rect99, x=WIDTH * 13, y=label.height + HEIGHT + label1.height)
    label99 = GLabel('navy')
    label99.font = '-10'
    window.add(label99, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 2)

    rect100 = GRect(WIDTH, HEIGHT)
    rect100.filled = True
    rect100.fill_color = 'oldlace'
    rect100.color = 'oldlace'
    window.add(rect100, x=WIDTH * 14, y=label.height + HEIGHT + label1.height)
    label100 = GLabel('oldlace')
    label100.font = '-10'
    window.add(label100, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 2)

    rect111 = GRect(WIDTH, HEIGHT)
    rect111.filled = True
    rect111.fill_color = 'peachpuff'
    rect111.color = 'peachpuff'
    window.add(rect111, x=WIDTH*10, y=label.height + (HEIGHT + label1.height) * 2)
    label111 = GLabel('peachpuff')
    label111.font = '-10'
    window.add(label111, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 3)

    rect112 = GRect(WIDTH, HEIGHT)
    rect112.filled = True
    rect112.fill_color = 'peru'
    rect112.color = 'peru'
    window.add(rect112, x=WIDTH*11, y=label.height + (HEIGHT + label1.height) * 2)
    label112 = GLabel('peru')
    label112.font = '-10'
    window.add(label112, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 3)

    rect113 = GRect(WIDTH, HEIGHT)
    rect113.filled = True
    rect113.fill_color = 'pink'
    rect113.color = 'pink'
    window.add(rect113, x=WIDTH * 12, y=label.height + (HEIGHT + label1.height) * 2)
    label113 = GLabel('pink')
    label113.font = '-10'
    window.add(label113, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 3)

    rect114 = GRect(WIDTH, HEIGHT)
    rect114.filled = True
    rect114.fill_color = 'plum'
    rect114.color = 'plum'
    window.add(rect114, x=WIDTH * 13, y=label.height + (HEIGHT + label1.height) * 2)
    label114 = GLabel('plum')
    label114.font = '-10'
    window.add(label114, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 3)

    rect115 = GRect(WIDTH, HEIGHT)
    rect115.filled = True
    rect115.fill_color = 'powderblue'
    rect115.color = 'powderblue'
    window.add(rect115, x=WIDTH * 14, y=label.height + (HEIGHT + label1.height) * 2)
    label115 = GLabel('powderblue')
    label115.font = '-10'
    window.add(label115, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 3)

    rect116 = GRect(WIDTH, HEIGHT)
    rect116.filled = True
    rect116.fill_color = 'purple'
    rect116.color = 'purple'
    window.add(rect116, x=WIDTH*10, y=label.height + (HEIGHT + label1.height) * 3)
    label116 = GLabel('purple')
    label116.font = '-10'
    window.add(label116, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 4)

    rect117 = GRect(WIDTH, HEIGHT)
    rect117.filled = True
    rect117.fill_color = 'red'
    rect117.color = 'red'
    window.add(rect117, x=WIDTH*11, y=label.height + (HEIGHT + label1.height) * 3)
    label117 = GLabel('red')
    label117.font = '-10'
    window.add(label117, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 4)

    rect118 = GRect(WIDTH, HEIGHT)
    rect118.filled = True
    rect118.fill_color = 'rosybrown'
    rect118.color = 'rosybrown'
    window.add(rect118, x=WIDTH * 12, y=label.height + (HEIGHT + label1.height) * 3)
    label118 = GLabel('rosybrown')
    label118.font = '-10'
    window.add(label118, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 4)

    rect119 = GRect(WIDTH, HEIGHT)
    rect119.filled = True
    rect119.fill_color = 'royalblue'
    rect119.color = 'royalblue'
    window.add(rect119, x=WIDTH * 13, y=label.height + (HEIGHT + label1.height) * 3)
    label119 = GLabel('royalblue')
    label119.font = '-10'
    window.add(label119, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 4)

    rect120 = GRect(WIDTH, HEIGHT)
    rect120.filled = True
    rect120.fill_color = 'saddlebrown'
    rect120.color = 'saddlebrown'
    window.add(rect120, x=WIDTH * 14, y=label.height + (HEIGHT + label1.height) * 3)
    label120 = GLabel('saddlebrown')
    label120.font = '-10'
    window.add(label120, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 4)

    rect121 = GRect(WIDTH, HEIGHT)
    rect121.filled = True
    rect121.fill_color = 'sage'
    rect121.color = 'sage'
    window.add(rect121, x=WIDTH*10, y=label.height + (HEIGHT + label1.height) * 4)
    label121 = GLabel('sage')
    label121.font = '-10'
    window.add(label121, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 5)

    rect122 = GRect(WIDTH, HEIGHT)
    rect122.filled = True
    rect122.fill_color = 'salmon'
    rect122.color = 'salmon'
    window.add(rect122, x=WIDTH*11, y=label.height + (HEIGHT + label1.height) * 4)
    label122 = GLabel('salmon')
    label122.font = '-10'
    window.add(label122, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 5)

    rect123 = GRect(WIDTH, HEIGHT)
    rect123.filled = True
    rect123.fill_color = 'sandybrown'
    rect123.color = 'sandybrown'
    window.add(rect123, x=WIDTH * 12, y=label.height + (HEIGHT + label1.height) * 4)
    label123 = GLabel('sandybrown')
    label123.font = '-10'
    window.add(label123, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 5)

    rect124 = GRect(WIDTH, HEIGHT)
    rect124.filled = True
    rect124.fill_color = 'seagreen'
    rect124.color = 'seagreen'
    window.add(rect124, x=WIDTH * 13, y=label.height + (HEIGHT + label1.height) * 4)
    label124 = GLabel('seagreen')
    label124.font = '-10'
    window.add(label124, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 5)

    rect125 = GRect(WIDTH, HEIGHT)
    rect125.filled = True
    rect125.fill_color = 'seashell'
    rect125.color = 'seashell'
    window.add(rect125, x=WIDTH * 14, y=label.height + (HEIGHT + label1.height) * 4)
    label125 = GLabel('seashell')
    label125.font = '-10'
    window.add(label125, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 5)

    rect126 = GRect(WIDTH, HEIGHT)
    rect126.filled = True
    rect126.fill_color = 'sienna'
    rect126.color = 'sienna'
    window.add(rect126, x=WIDTH*10, y=label.height + (HEIGHT + label1.height) * 5)
    label126 = GLabel('sienna')
    label126.font = '-10'
    window.add(label126, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 6)

    rect127 = GRect(WIDTH, HEIGHT)
    rect127.filled = True
    rect127.fill_color = 'silver'
    rect127.color = 'silver'
    window.add(rect127, x=WIDTH*11, y=label.height + (HEIGHT + label1.height) * 5)
    label127 = GLabel('silver')
    label127.font = '-10'
    window.add(label127, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 6)

    rect128 = GRect(WIDTH, HEIGHT)
    rect128.filled = True
    rect128.fill_color = 'skyblue'
    rect128.color = 'skyblue'
    window.add(rect128, x=WIDTH * 12, y=label.height + (HEIGHT + label1.height) * 5)
    label128 = GLabel('skyblue')
    label128.font = '-10'
    window.add(label128, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 6)

    rect129 = GRect(WIDTH, HEIGHT)
    rect129.filled = True
    rect129.fill_color = 'slateblue'
    rect129.color = 'slateblue'
    window.add(rect129, x=WIDTH * 13, y=label.height + (HEIGHT + label1.height) * 5)
    label129 = GLabel('slateblue')
    label129.font = '-10'
    window.add(label129, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 6)

    rect130 = GRect(WIDTH, HEIGHT)
    rect130.filled = True
    rect130.fill_color = 'slategray'
    rect130.color = 'slategray'
    window.add(rect130, x=WIDTH * 14, y=label.height + (HEIGHT + label1.height) * 5)
    label130 = GLabel('slategray')
    label130.font = '-10'
    window.add(label130, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 6)

    rect106 = GRect(WIDTH, HEIGHT)
    rect106.filled = True
    rect106.fill_color = 'palegoldenrod'
    rect106.color = 'palegoldenrod'
    window.add(rect106, x=WIDTH*10, y=label.height + (HEIGHT + label1.height) * 6)
    label106 = GLabel('palegoldenrod')
    label106.font = '-10'
    window.add(label106, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 7)

    rect132 = GRect(WIDTH, HEIGHT)
    rect132.filled = True
    rect132.fill_color = 'snow'
    rect132.color = 'snow'
    window.add(rect132, x=WIDTH*11, y=label.height + (HEIGHT + label1.height) * 6)
    label132 = GLabel('snow')
    label132.font = '-10'
    window.add(label132, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 7)

    rect133 = GRect(WIDTH, HEIGHT)
    rect133.filled = True
    rect133.fill_color = 'springgreen'
    rect133.color = 'springgreen'
    window.add(rect133, x=WIDTH * 12, y=label.height + (HEIGHT + label1.height) * 6)
    label133 = GLabel('springgreen')
    label133.font = '-10'
    window.add(label133, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 7)

    rect134 = GRect(WIDTH, HEIGHT)
    rect134.filled = True
    rect134.fill_color = 'steelblue'
    rect134.color = 'steelblue'
    window.add(rect134, x=WIDTH * 13, y=label.height + (HEIGHT + label1.height) * 6)
    label134 = GLabel('steelblue')
    label134.font = '-10'
    window.add(label134, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 7)

    rect135 = GRect(WIDTH, HEIGHT)
    rect135.filled = True
    rect135.fill_color = 'tan'
    rect135.color = 'tan'
    window.add(rect135, x=WIDTH * 14, y=label.height + (HEIGHT + label1.height) * 6)
    label135 = GLabel('tan')
    label135.font = '-10'
    window.add(label135, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 7)

    rect136 = GRect(WIDTH, HEIGHT)
    rect136.filled = True
    rect136.fill_color = 'teal'
    rect136.color = 'teal'
    window.add(rect136, x=WIDTH*10, y=label.height + (HEIGHT + label1.height) * 7)
    label136 = GLabel('teal')
    label136.font = '-10'
    window.add(label136, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 8)

    rect137 = GRect(WIDTH, HEIGHT)
    rect137.filled = True
    rect137.fill_color = 'thistle'
    rect137.color = 'thistle'
    window.add(rect137, x=WIDTH*11, y=label.height + (HEIGHT + label1.height) * 7)
    label137 = GLabel('thistle')
    label137.font = '-10'
    window.add(label137, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 8)

    rect138 = GRect(WIDTH, HEIGHT)
    rect138.filled = True
    rect138.fill_color = 'tomato'
    rect138.color = 'tomato'
    window.add(rect138, x=WIDTH * 12, y=label.height + (HEIGHT + label1.height) * 7)
    label138 = GLabel('tomato')
    label138.font = '-10'
    window.add(label138, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 8)

    rect139 = GRect(WIDTH, HEIGHT)
    rect139.filled = True
    rect139.fill_color = 'turquoise'
    rect139.color = 'turquoise'
    window.add(rect139, x=WIDTH * 13, y=label.height + (HEIGHT + label1.height) * 7)
    label139 = GLabel('turquoise')
    label139.font = '-10'
    window.add(label139, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 8)

    rect140 = GRect(WIDTH, HEIGHT)
    rect140.filled = True
    rect140.fill_color = 'violet'
    rect140.color = 'violet'
    window.add(rect140, x=WIDTH * 14, y=label.height + (HEIGHT + label1.height) * 7)
    label140 = GLabel('violet')
    label140.font = '-10'
    window.add(label140, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 8)

    rect141 = GRect(WIDTH, HEIGHT)
    rect141.filled = True
    rect141.fill_color = 'wheat'
    rect141.color = 'wheat'
    window.add(rect141, x=WIDTH*10, y=label.height + (HEIGHT + label1.height) * 8)
    label141 = GLabel('wheat')
    label141.font = '-10'
    window.add(label141, x=WIDTH*10, y=label.height + (HEIGHT + 10) * 9)

    rect107 = GRect(WIDTH, HEIGHT)
    rect107.filled = True
    rect107.fill_color = 'palegreen'
    rect107.color = 'palegreen'
    window.add(rect107, x=WIDTH*11, y=label.height + (HEIGHT + label1.height) * 8)
    label107 = GLabel('palegreen')
    label107.font = '-10'
    window.add(label107, x=WIDTH*11, y=label.height + (HEIGHT + 10) * 9)

    rect143 = GRect(WIDTH, HEIGHT)
    rect143.filled = True
    rect143.fill_color = 'whitesmoke'
    rect143.color = 'whitesmoke'
    window.add(rect143, x=WIDTH * 12, y=label.height + (HEIGHT + label1.height) * 8)
    label143 = GLabel('whitesmoke')
    label143.font = '-10'
    window.add(label143, x=WIDTH * 12, y=label.height + (HEIGHT + 10) * 9)

    rect144 = GRect(WIDTH, HEIGHT)
    rect144.filled = True
    rect144.fill_color = 'yellow'
    rect144.color = 'yellow'
    window.add(rect144, x=WIDTH * 13, y=label.height + (HEIGHT + label1.height) * 8)
    label144 = GLabel('yellow')
    label144.font = '-10'
    window.add(label144, x=WIDTH * 13, y=label.height + (HEIGHT + 10) * 9)

    rect145 = GRect(WIDTH, HEIGHT)
    rect145.filled = True
    rect145.fill_color = 'yellowgreen'
    rect145.color = 'yellowgreen'
    window.add(rect145, x=WIDTH * 14, y=label.height + (HEIGHT + label1.height) * 8)
    label145 = GLabel('yellowgreen')
    label145.font = '-10'
    window.add(label145, x=WIDTH * 14, y=label.height + (HEIGHT + 10) * 9)




    arc1 = GArc(900, 1700, 0, 180)
    arc2 = GArc(800, 1500, 0, 180)
    arc3 = GArc(700, 1300, 0, 180)
    arc4 = GArc(600, 1100, 0, 180)
    arc5 = GArc(500, 900, 0, 180)
    arc6 = GArc(400, 700, 0, 180)
    window.add(arc1, x=(window.width - arc1.width) / 2, y=100)
    window.add(arc2, x=(window.width - arc2.width) / 2, y=150)
    window.add(arc3, x=(window.width - arc3.width) / 2, y=200)
    window.add(arc4, x=(window.width - arc4.width) / 2, y=250)
    window.add(arc5, x=(window.width - arc5.width) / 2, y=300)
    window.add(arc6, x=(window.width - arc6.width) / 2, y=350)


if __name__ == '__main__':
    main()
