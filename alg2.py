
def successors(s, is_solid, region_width, region_height):
    """Implementare le funzioni di successione e costo.

    Parametri:
    - s: stato del quale vanno calcolati i successori e i costi delle
      relative transizioni
    - is_solid: funzione da usare come is_solid(p) che ritorna True
      se e solo se la cella in posizione p è piena
    - region_width: numero di colonne della griglia
    - region_height: numero di righe della griglia

    Questa funzione deve ritornare una lista di tuple (s1, c), dove s1
    è un successore di s, mentre c è il costo della transizione da s
    ad s1.
    """
    i, j = s
    directions = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]
    return [((ni, nj), 1) if 0 <= ni < region_height and 0 <= nj < region_width and not is_solid((ni, nj)) else ((ni, nj), float("inf")) for ni, nj in directions]
    


def heuristic(s, goal, is_solid, region_width, region_height):
    """Implementare l'euristica da utilizzare per l'esercizio 2.

    Parametri:
    - s: stato sul quale va calcolato il valore di h(s)
    - goal: posizione (x, y) della cella di goal
    - is_solid: funzione da usare come is_solid(p), che ritorna True
      se e solo se la cella in posizione p = (x_p, y_p) è piena
    - region_width: numero di colonne della griglia
    - region_height: numero di righe della griglia

      Questa funzione deve ritornare un valore numerico.
    """
    h = abs(s[0] - goal[0]) + abs(s[1] - goal[1])
    solid_count = sum(1 for i in range(min(s[0], goal[0]), max(s[0], goal[0]) + 1) for j in range(min(s[1], goal[1]), max(s[1], goal[1]) + 1) if is_solid((i, j)))
    h += h * solid_count * region_height * region_width
    
    return h
   
"""
    L'euristica utilizzata in questa funzione combina la distanza di Manhattan 
    con un fattore basato sul numero di posizioni solide e sulle dimensioni della regione.
"""
