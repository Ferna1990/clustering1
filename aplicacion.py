
#librerias importadas
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.cluster import KMeans



#creacion de los datos
data1= np.random.random(size=(20,2))
data=data1
#print(data) #aca confirmo que los datos esten creados.
#La grafica sin los centroides
#plt.scatter(data[:,0],data[:,1])

#creamos el objeto Kmeans
#la desventaja que tiene esto, es que tenemos que ingresar la cantidad de clusters que nosotros consideremos.

KMeans=KMeans(n_clusters=4).fit(data)
centroids=KMeans.cluster_centers_

# definimos la grafica con los centroides.
#plt.scatter(data[:,0],data[:,1], c=KMeans.labels_.astype(float),s=50)
#plt.scatter(centroids[:,0],centroids[:,1],c='red',marker= '*',s=50)
#plt.show


#creamos la ventana de la aplicacion.

ventana= tk.Tk()
ventana.geometry('900x1000')
ventana.title('K-means')
ventana.configure(background= "lightblue")

#creamos el frame

frame1= tk.Frame(ventana, bg='dodger blue')
frame1.pack(side='left')
frame2= tk.Frame(ventana, bg='dodger blue')
frame2.pack(side='right')

rotulo1= tk.Label(frame1, text= 'Estos son los valores generados aleatoriamente ',relief=tk.GROOVE)
rotulo1.pack()
rotulo2= tk.Label(frame1, text= data,relief=tk.GROOVE)
rotulo2.pack()
rotulo3= tk.Label(frame1, text= 'Estos son los centroids generados por la aplicacion ',relief=tk.GROOVE)
rotulo3.pack()
rotulo4= tk.Label(frame1, text= centroids,relief=tk.GROOVE)
rotulo4.pack()

#creamos las graficas para imprimirlas en el programa
fig, axs = plt.subplots(1,2, dpi=80, figsize=(13,4), sharey=True, facecolor='#00f9f844')

fig.suptitle('Graficas')


axs[0].scatter(data1[:,0],data1[:,1], c=KMeans.labels_.astype(float),s=50)
axs[1].scatter(data[:,0],data[:,1], c=KMeans.labels_.astype(float),s=50)
axs[1].scatter(centroids[:,0],centroids[:,1], c='red',marker= '*',s=50)

#imprimimos la grafica
canvas = FigureCanvasTkAgg(fig,master= frame2)
canvas.draw()
canvas.get_tk_widget().pack()


