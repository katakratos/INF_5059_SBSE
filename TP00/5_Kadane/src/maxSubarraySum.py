def  maxSubarraySum (arr):
    """
        Trouver la somme maximale d'un sous-tableau contigu avec l'algorithme de Kadane.

        :param arr: Liste d'entiers
        :return: Somme maximale d'un sous-tableau contigu
    """
    resultat = arr[0]
    maxSumCurrent = arr[0]

    for i in range(1, len(arr)):
        maxSumCurrent = max(maxSumCurrent + arr[i], arr[i])

        resultat = max( resultat, maxSumCurrent)
    return resultat    


if __name__ == "__main__":

    arr1 = [3, 2, -8, 2, 6, -4]
    print(f"Somme maximale pour {arr1} : {maxSubarraySum(arr1)}")  # Résultat : 8

    arr2 = [2, 3, -8, 7, -1, 2, 3]
    print(f"Somme maximale pour {arr2} : {maxSubarraySum(arr2)}")  # Résultat : 11

    arr3 = [-2, -4, -5]
    print(f"Somme maximale pour {arr3} : {maxSubarraySum(arr3)}")  # Résultat : -2

    arr4 = [3, 3, 9, 9, 5]
    print(f"Somme maximale pour {arr4} : {maxSubarraySum(arr4)}")  # Résultat : 29