
c=VideoFileClip("D:/EDI/Scripting/testVideo.mp4")
text=TextClip('''Advances in technology have led to the development of methods that can create desired visual
multimedia. In particular, image generation using
fields.''',fontsize=35,color="yellow",font="Arial-Rounded-MT-Bold",stroke_color="white",stroke_width=1).set_position((100,900)).set_duration(10)
final=CompositeVideoClip([c,text])
final.ipython_display(width=300)
# print(TextClip.list('font'))
