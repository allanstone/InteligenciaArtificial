# muestras iniciales
mi=(
    (1, 12.5), 
    (3, 10.5), 
    (3, 12.5),
    (3, 14.5),
    (3, 18),
    (5, 18),
    (5, 16),
    (5, 14.5),
    (5, 13),
    (6, 9),
    (8, 10),
    (9, 11),
    (8.5, 12),
    (7, 13.5),
    (8, 16),
    (0.5, 10.5))

k_medias=[[6,9],[5,13]]
k_mediasAnt=[[0,0],[0,0]]

print('-----------MUESTRAS INICIALES-----------')
for x in mi:
    print(x)

iteracion=0

#mientras las k_medias actuales sean diferentes de las anteriores
while k_medias != k_mediasAnt :
    #Se generan las listas para las distancias, y para las siguientes muestras
    distanciask1=list()
    distanciask2=list();
    muestrasK1=list();
    muestrasK2=list();

    #Recorremos las muestras iniciales y calculamos las distancias a las medias sqrt( (deltaX)^2 + (deltaY)^2 )
    for i in mi:
        dist=((i[0]-k_medias[0][0])**2 + (i[1]-k_medias[0][1])**2)**0.5
        distanciask1.append(dist)
        dist=((i[0]-k_medias[1][0])**2 + (i[1]-k_medias[1][1])**2)**0.5
        distanciask2.append(dist)   


    print "\t\t\t\t=======================ITERACION: "+str(iteracion)+"====================="
    print('============================Medias ============================')
    print(k_medias)
    print('\n============================Distancias a k1============================')
    for y in distanciask1:
            print(y)
    # print(distanciask1)
    print('\n============================Distancias a k2============================')
    for y in distanciask2:
        print(y)
    # print(distanciask2)


    sumx1=0.0
    sumy1=0.0
    sumx2=0.0
    sumy2=0.0
    #Recorremos las distancias para asignarles su media mas cercana
    #hacemos una suma acomulativa para el nuevo valor de las medias
    for x in range(0,len(distanciask1)):
        #Si esta mas cercano a k1
        if distanciask1[x]<distanciask2[x]:
            muestrasK1.append(mi[x])
            sumx1+=mi[x][0]
            sumy1+=mi[x][1]
        #si esta mas cercano a k2
        else:
            muestrasK2.append(mi[x])
            sumx2+=mi[x][0]
            sumy2+=mi[x][1]     
    print('\n============================muestras cercanas a K1 ============================')
    for y in muestrasK1:
        print(y)
    # print(muestrasK1)
    print('\n============================muestras cercanas a K2 ============================')
    for y in muestrasK2:
        print(y)
    # print(muestrasK2)
    
    
    #Calculamos las nuevas medias. media = suma/longitudLista
    k_mediasAnt=k_medias
    k_medias=((sumx1/len(muestrasK1),sumy1/len(muestrasK1)),(sumx2/len(muestrasK2),sumy2/len(muestrasK2)))
    print('\n============================Nuevas medias ============================')
    print k_medias
    iteracion+=1