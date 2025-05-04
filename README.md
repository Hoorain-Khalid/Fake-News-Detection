
# CPU Scheduler Project

This repository contains an implementation of a CPU Scheduling Simulator developed in **C#**. CPU scheduling is a fundamental aspect of modern operating systems, allowing efficient management of processes by allocating CPU time to various tasks. This project demonstrates various CPU scheduling algorithms and provides insights into their performance.

---

## Features

- **Scheduling Algorithms:** Implements popular CPU scheduling algorithms such as:
  - First-Come-First-Serve (FCFS)
  - Shortest Job Next (SJN)
  - Priority Scheduling
  - Round Robin (RR)
  - Multilevel Queue Scheduling
- **Interactive User Interface:** A user-friendly interface to simulate scheduling scenarios.
- **Performance Metrics:** Displays metrics such as average waiting time, turnaround time, and CPU utilization.
- **Visualization:** Visual representation of process execution timelines (Gantt charts).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Hoorain-Khalid/CPU_Scheduler_Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CPU_Scheduler_Project
   ```
3. Open the solution file (`*.sln`) in Visual Studio.
4. Build the solution to restore dependencies and compile the project.

---

## Usage

1. Run the application in Visual Studio.
2. Input process details such as:
   - Process IDs
   - Arrival time
   - Burst time
   - Priority (if applicable)
3. Select a scheduling algorithm to simulate.
4. View the Gantt chart and performance metrics for the selected algorithm.

---

## Project Structure

```plaintext
CPU_Scheduler_Project/
├── src/                    # Source code for the CPU Scheduler
├── docs/                   # Documentation and resources
├── tests/                  # Unit tests for scheduling algorithms
├── bin/                    # Compiled binaries
├── CPU_Scheduler_Project.sln # Visual Studio solution file
└── README.md               # Project documentation (you are here!)
```

---

## Technologies Used

- **C#:** 100% of the codebase
- **Development Environment:** Visual Studio

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- This project is inspired by the need to understand and visualize CPU scheduling concepts taught in operating systems courses.
- Special thanks to the open-source community for providing tools and libraries that facilitate development.

---

## Contact

For any questions or suggestions, feel free to contact the owner:

- **GitHub:** [Hoorain-Khalid](https://github.com/Hoorain-Khalid)
