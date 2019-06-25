# Bus Company - Genetic Algorithms
Using genetic algorithm to find the most profitable routes for a bus company

# Graph
Graph that represents cities on a map. Green lines represent connections between cities, and purple ones represent current best bus route.
![G1](https://user-images.githubusercontent.com/37414943/60082755-b149ad00-9734-11e9-971f-d8004ace4970.JPG)

# Fitness chart
![Fit](https://user-images.githubusercontent.com/37414943/60082839-e1914b80-9734-11e9-9d95-ee1c39032d83.JPG)

# Short description
There a are few different companies and each of them has the same number of buses. Each bus has a limited number of seats, and therefore can travel with a limited number of passengers. Bus travels along it's route which consists of cities and connections beetweend those cities. Each connection is different, which means they have a different length and weight - that results in different travel cost. In every generation that route is mutated acording to one randomly selected method of mutation.

![image](https://user-images.githubusercontent.com/37414943/60104132-1ca97400-9761-11e9-965c-68dcb8b51db1.png)

After mutation process all buses are randomly assigned to different companies, which constitutes crossing of their genome. Crossed individuals then become new parent generation and whole process will repeat itself until limit of generations is reached.



