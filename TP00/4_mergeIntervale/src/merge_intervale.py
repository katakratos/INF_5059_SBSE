def merge_intervals(intervals):
    if not intervals:
        return []
    
    # 1. Trier les intervalles par heure de début
    intervals.sort(key=lambda x: x[0])
    
    # 2. Liste pour stocker les intervalles fusionnés
    merged = [intervals[0]]  # Ajouter le premier intervalle

    # 3. Parcourir les intervalles
    for current in intervals[1:]:
        previous = merged[-1]  # Dernier intervalle fusionné
        if current[0] <= previous[1]:  # Chevauchement
            # Fusionner les deux intervalles
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            # Pas de chevauchement, ajouter l'intervalle actuel
            merged.append(current)
    
    return merged

if __name__ == "__main__":
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    print(merge_intervals(intervals))

    intervals = [(1, 5), (2, 3), (4, 6)]
    print(merge_intervals(intervals))