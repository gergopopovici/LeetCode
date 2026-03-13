class ScatteredHanoi:
    def __init__(self, initial_positions):
        self.positions = initial_positions
        self.pegs = {'A', 'B', 'C'}

    def standard_hanoi(self, n, source, target, helper):
        if n == 0: return
        self.standard_hanoi(n - 1, source, helper, target)
        print(f"{source} {target}")
        self.positions[n] = target
        self.standard_hanoi(n - 1, helper, target, source)

    def solve_scattered(self, n, target):
        if n == 0: return 
        
        current_peg = self.positions[n]

        if current_peg == target:
            self.solve_scattered(n - 1, target)
        else:
            helper = (self.pegs - {current_peg, target}).pop()
            self.solve_scattered(n - 1, helper)
            print(f"{current_peg} {target}") 
            self.positions[n] = target
            self.standard_hanoi(n - 1, helper, target, current_peg)

positions_8 = {
    8: 'C', 7: 'B', 6: 'A', 5: 'C', 
    4: 'A', 3: 'B', 2: 'B', 1: 'C'
}

game = ScatteredHanoi(positions_8)
game.solve_scattered(8, 'A')