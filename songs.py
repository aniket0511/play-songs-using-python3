#playing songs

import vlc

location="/home/aniket/Music/"

print("choose the song :")
print("1.circles-ananya birla\n2.Rockabye\n3.Believer\n4.see You again -Wiz khalifa\n5.Hym for the weekend")
x=input('enter number :')

if(x == '1'):
	l="circles.flac"
elif(x == '2'):
	l="Rockabye.flac"
elif(x == '3'):
	l="Believer.flac"
elif(x == '4'):
	l="Wiz Khalifa.flac"
elif(x == '5'):
	l="coldplay.flac"
else:
	print("choose correct song ")

p=vlc.MediaPlayer(location+l)

p.play()

while(1):
	print('1.stop \n2.pause')
	y=input()

	if(y== '1'):
		p.stop()
		break
	elif(y== '2'):
		p.pause()
		print('1.play \n2.stop')
		z=input()
		if(z == '1'):
			p.play()
		elif(z == '2'):
			p.stop()
			break
		else:
			print('choose correct option')
	else:
		print('choose correct option')
		
	



