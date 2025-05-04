import random

class Chromosome:    
    def __init__(self, genes, knapsack):
        self.genes = list(genes)
        self.knapsack = knapsack
        self.fitness = self.calculate_fitness(knapsack)

    def calculate_fitness(self, knapsack):
        fitness = 0
        weight = 0
        value=0
        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                weight+=knapsack[i][1]
                value+=knapsack[i][0]

        if weight>0 and weight<w:
            fitness=value/weight
        else:
            fitness=0
        return fitness

   
    def __str__(self):
        result = ""  
        for i in range(len(self.genes)):
            result += str(self.genes[i]) 
        return result  

class GeneticAlgorithm:
    def __init__(self, weight_limit, knapsack, population_size, mutation_rate):
        self.weight_limit = weight_limit
        self.knapsack = knapsack
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for i in range(self.population_size):  
            genes = [random.randint(0, 1) for j in range(len(self.knapsack))] 
            chromosome = Chromosome(genes, self.knapsack) 
            population.append(chromosome) 
        return population

    def selection(self):
        #Use elitishm and roulette-wheel to select chromosomes
        t_fitness=0
        for chromosome in self.population:
            t_fitness+=chromosome.fitness
        if t_fitness==0:
            return self.population
        prob=[]
        for chromosome in self.population:
            p=chromosome.fitness/t_fitness
            prob.append(p)
        selected=[]
        for i in range(self.population_size//2):
            r=random.random()
            s=0
            for j in range(len(self.population)):
                s+=prob[j]
                if r<=s:
                    selected.append(self.population[j])
                    break
        return selected

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, len(parent1.genes) - 1)  

        child1,child2 = Chromosome([],parent1.knapsack),Chromosome([],parent2.knapsack)

        child1.genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        child2.genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]

        return child1, child2

    def mutation(self, chromosome):
        n = len(chromosome.genes) 
        num_mutations = int(self.mutation_rate * n) 
        for i in range(num_mutations):
            j = random.randint(0, n - 1) 
            chromosome.genes[j] = 1 - chromosome.genes[j] 

        return chromosome

    def evolve(self):
        #Evolve and generate new population
        new_population = []
        for i in range(self.population_size // 2):
            parents = self.selection()
            parent1,parent2=parents[:2]
            child1, child2 = self.crossover(parent1, parent2)
            child1 = self.mutation(child1)
            child2 = self.mutation(child2)
            new_population.append(child1)
            new_population.append(child2)
        #selection, cross-over, mutation and replacement
        self.population = new_population

    def get_solution(self):
        #Fetch the best solution on the basis of fitness#
        return max(self.population, key=lambda c: c.calculate_fitness(knapsack))

def build_knapsack(file):
    knapsack = {}
    with open(file, 'r') as f:
        items, w = map(int, f.readline().split())
        for i in range(items):
            worth, volume = map(int, f.readline().split())
            knapsack[i] = (worth, volume)

    return w, knapsack


if __name__ == "__main__":
    w, knapsack = build_knapsack("test.txt")
    ga = GeneticAlgorithm(w, knapsack, population_size=10, mutation_rate=0.2)
    
    for _ in range(50):
        ga.evolve()
    
    best_solution = ga.get_solution()
    print("Best solution found:", best_solution)
    print("Fitness of best solution:", best_solution.calculate_fitness(knapsack))
