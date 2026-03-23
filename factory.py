

class Factory:

    def __init__(self):
        self.n_machines = 0
        self.n_jobs = 0
        self.p_times = []
        self.name = ""

        self.seed = None
        self.upper_bound = None
        self.lower_bound = None
    
    
    def evaluate(self, sequence: list) -> int:
        """
        Gets an order of execution of Jobs
        Must return what time takes to perform the jobs
        The time that takes is the sum of time of last machine
        """
        J = self.n_jobs
        M = self.n_machines
        p = self.p_times

        # Creates a [M][pos] array
        completion = [[0]*J for _ in range(M)]

        for pos in range(J):

            # Actual job being performed
            job = sequence[pos]
            for m in range(M):
                # Actual machine being used

                # time that takes the machine for the process
                process = p[m][job]

                if pos == 0 and m == 0:
                    completion[m][pos] = process
                if pos == 0 and m != 0:
                    completion[m][pos] = completion[m-1][pos] + process
                if pos != 0 and m ==0:
                    completion[m][pos] = completion[m][pos-1] + process
                else:
                    completion[m][pos] = max(completion[m-1][pos], completion[m][pos-1]) + process
        

        total_time = sum(completion[M-1])
        return total_time

    def load_data(self, fp: str) -> None:
        """
        Load the data from .fsp files
        format:

            number of jobs, number of machines, initial seed, upper bound and lower bound :
            <J>  <M>  -  -  -
            processing times :
            <row for machine 1>   (J values)
            <row for machine 2>
            ...
            <row for machine M>
        """

        self.name = fp.split("/")[-1]

        with open(fp, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        p_times = []
        for i, line in enumerate(lines):
            tokens = line.split()

            # Cheks the Jobs and Machines, and saves them
            if i==1 and len(tokens) >= 2 and tokens[0].isdigit() and tokens[1].isdigit():
                j, m = int(tokens[0]), int(tokens[1])

                seed = int(tokens[2]) if tokens[2].isdigit() else None
                upper = int(tokens[3]) if tokens[3].isdigit() else None
                lower = int(tokens[4]) if tokens[4].isdigit() else None
            
            # Checks the processing times and saves them
            if i>=3:
                tokens = line.split()
                p_times.append(tokens)
        

        self.n_jobs = j
        self.n_machines = m
        self.seed = seed
        self.upper_bound = upper
        self.lower_bound = lower
        self.p_times = p_times

    def __str__(self):
        s = "number of jobs, number of machines, initial seed, upper bound and lower bound :\n" \
            f"{self.n_jobs}\t{self.n_machines}\t{self.seed}\t{self.upper_bound}\t{self.lower_bound}" \
            "Processing Times:\n"
        
        for m in self.p_times:
            s += f"{m}\n"
        
        return f"{self.name}\n" + s
    

