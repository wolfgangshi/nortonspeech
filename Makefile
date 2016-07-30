.phony: clean

srt_%:
	ffmpeg -y -i mp4src/$*.mp4  -i $*.srt -vcodec copy -acodec copy -scodec mov_text -metadata:s:s:0 language=eng output/$*-testoutput.mp4

ass_%:
	ffmpeg -y -i mp4src/$*.mp4  -i $*.ass  -vf ass=$*.ass output/$*-testoutput.mp4

p_%:
	/Applications/MPlayerX.app/Contents/MacOS/MPlayerX output/$*-testoutput.mp4

clean:
	rm *~ output/*~ || true
