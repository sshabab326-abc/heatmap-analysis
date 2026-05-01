from mplsoccer import Pitch
import matplotlib.pyplot as plt
x=[80,85,90,75]
y=[40,45,30,50]
Pitch=Pitch(pitch_type="statsbomb",pitch_color="grass",line_color="white")
fig,ax=Pitch.draw()
Pitch.scatter(x,y,ax=ax,color="red",s=100)
plt.title("shot map of player")
plt.show()