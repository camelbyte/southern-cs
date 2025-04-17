# Project 1 -- Population Data


# Phase 1

print("\n Population data for 1950-1990 \n\n")

# Print the population data to the console 


with open("../data/USPopulation.txt", "r") as file:
    for line in file:
        lines = [line.strip() for line in file]
        # print(f'The raw population data: \n\n{lines} \n')


        

# Phase 2

poplist = []

annual_increase = []

percent_increase = []

def get_data():
    """
    Gets the population data from the USPopulation.txt file and returns it as a list.

    Returns:
     list: A list of population data from 1950 to 1990.
    """
    with open("../data/USPopulation.txt", "r") as file:
        local_poplist = [int(l.strip()) for l in file]
        print(local_poplist) 
        return local_poplist
        print(poplist) 
        return poplist

def put_data(poplist):
    """
    Formats the population data and prints it to the console.
    
    
    Parameters:
    poplist (list): A list of population data from 1950 to 1990.
    """
    poplist = [format(population, ',d') for population in poplist]
    for p in poplist:
        print(p)
        
        
# Phase 3


def pop_change(poplist):
    
    """
    This function calculates the annual increase in population and the percent increase in population
    for each year from 1951 to 1990. It then prints the results to the console.
    
    Parameters:
    poplist (list): A list of population data from 1950 to 1990.
    
    Returns:
    None
    """
    for i in range(1, len(poplist)):
        old_val = poplist[i - 1]
        new_val = poplist[i]
        increase = ((new_val - old_val) / old_val) * 100
        net_change = new_val - old_val
        annual_increase.append(net_change)
        percent_increase.append(increase)
        
        
        # Basically i'm starting i at 1951. 
        print(f'Annual increase in {i + 1950}: \t {increase: .2f}% \n')
        
        print(f'Net change in {i + 1950}: \t\t {net_change} \n')
    return None


        
if __name__ == "__main__":
    
    print("\n Getting the cleaned data: \n")
    poplist = get_data()
    

    print("\n Put it into a list and render it to the console. \n")
    put_data(poplist)
    
    print("\n Population increase time!! :)\n")
    pop_change(poplist)
    
    
    
    print("Net changes in population: \n")
    print("Maximum:", max(annual_increase))
    print("Minimum", min(annual_increase))
    print("Average", sum(annual_increase) / len(annual_increase))
    
    
    print("\n YoY percent change in population:\n")
    print(f'Maximum: {max(percent_increase): .2f}%')
    print(f'Minimum: {min(percent_increase): .2f}%')
    print(f'Average: {sum(percent_increase) / len(percent_increase): .2f}% \n')
    