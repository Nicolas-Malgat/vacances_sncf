def journey(prefecture1, prefecture2):
    """Select the smallest way from a prefecture to another one, using the SNCF API (journey).

    Returns:
        [coll]: ids of the stations.
        [decimal]: [value of the smallest way (duration or CO2 emission).]
    """
    #On utilise l'API pour trouver tous les journey, stockées dans un tableau
    return result
    
    def dijkstra(start, stop):
    """Select the smallest path through all the prefectures using the dijkstra algorythm.

    Returns:
        [decimal]: [value of the smallest way (duration or CO2 emission).]
    """

    """
    distance = 0
    priorite = set(noeud) #liste de priorites

    while len(priorite) > 0:
      Défiler le nœud au début de la file

      Si c'est le nœud d'arrivée
         Retourner nœud.distance

      Marquer le nœud comme visité
      Pour chaque voisin du nœud
         Si le voisin n'est pas visité
            voisin.distance = nœud.distance + arc
            Enfiler le voisin

    return result
"""



"""
def dijkstra(graph, origine):

    sommets, voisins = graph
    distance = {}
    precedent ={}

    for sommet in sommets:
        distance[sommet] = float("inf")
        precedent[sommet] = None

    distance[origine] = 0
    Q = set(sommets)

    while len(Q) > 0:
        u = minimum_distance(distance, Q)
        print('Currently considering', u, 'with a distance of', distance[u])
        Q.remove(u)

        if distance[u] == float('inf'):
            break

        n = get_neighbours(graph, u)
        for sommet in n:
            alt = distance[u] + distance_between(graph, u, sommet)
            if alt < distance[sommet]:
                distance[sommet] = alt
                precedent[sommet] = u

    return precedent
"""


#({'A', 'B', 'C', 'D'}, {('A', 'B', 5), ('B', 'A', 5), ('B', ' C ', 10), (' B ',' D ', 6), (' C ',' D ', 2), (' D ',' C ', 2)})


"""
chemins=[]
chemin_voisin=()

for all item in table :
    for voisin in table2 :
        chemin_voisin=(chemin_voisin), (voisin.temps, '"'voisin.code'"')
    chemins = chemins, '"'item'"': [chemin_voisin]

graph={chemins}
"""