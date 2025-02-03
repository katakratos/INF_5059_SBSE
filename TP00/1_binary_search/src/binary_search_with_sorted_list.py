def binary_search(tab, target_value):
    left = 0
    right = len(tab) - 1

    while left <= right:
        middle = (left + right) // 2  # Division entière pour obtenir un indice valide
        
        if tab[middle] == target_value:
            print(f"The target value is in position {middle} of the list")
            return middle
        elif target_value < tab[middle]:
            right = middle - 1  # Réduire la plage à la partie gauche
        else:
            left = middle + 1  # Réduire la plage à la partie droite
    
    print("The target value is not in the list")
    return -1

def element_list(m):
    tab_number=[]
    
    for i in range(m):
          numb  = int(input(f"Enter the element {i+1} of list : "))
          tab_number.append(numb)
          
    return tab_number

def check_list_is_sorted(tab_number):
     return tab_number == sorted(tab_number) or tab_number == sorted(tab_number, reverse=True)
      
   

if __name__ == "__main__":
      m = int(input("Enter the length of list :") )
      sort_list = element_list(m)
      if check_list_is_sorted(sort_list):
         target = int(input("Enter the target value :"))
         binary_search(sort_list, target)

      else: 
        print("Our List is not in order, Please enter element in order ")
   

      
        