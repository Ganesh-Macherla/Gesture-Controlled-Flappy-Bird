# 📊 Sorting Visualizer

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Swing](https://img.shields.io/badge/Swing-GUI-blue?style=for-the-badge)
![Algorithms](https://img.shields.io/badge/DSA-Visualization-green?style=for-the-badge)

An interactive sorting algorithm visualizer built in **Java Swing**. This tool demonstrates the internal mechanics of classic sorting techniques through real-time animation, step-by-step debugging, and mathematical analysis. 

Designed as a learning aid for Data Structures and Algorithms, it allows users to pause execution, rewind states, and observe how data moves during sorting in real time.

---

## 🚀 Key Features

* **📸 Snapshot Debugger:** Records every array state. Pause the sort and scrub through history using `← Previous` and `Next →`.
* **🎨 Fluid Animation Engine:** High-performance `Graphics2D` rendering with anti-aliasing and rounded bar geometry.
* **📊 Live Operation Tracking:** Real-time counters for comparisons and array swaps/moves.
* **📖 Theory Panel:** Displays time complexity, recurrence equations, and evaluated formulas based on current array size.
* **⏱️ Deep Time Analysis:** Estimates actual CPU execution time versus the visualized delay scale.
* **🚦 Thread-safe Control System:** Monitor-based pause, resume, and step execution for a glitch-free experience.

---

## 🧠 Supported Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
| :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ |
| **Shell Sort** | $O(n \log n)$ | $\sim O(n^{3/2})$ | $O(n^2)$ |

---

## 🎨 Visual Legend

To help you understand the sorting process, the visualizer uses the following color coding:
* **Blue:** Default/Unsorted state.
* **Red:** Elements currently being compared.
* **Yellow:** Elements being swapped or moved.
* **Green:** Elements in their final sorted position.

---

## 🎮 How to Use

1.  **Select an algorithm** from the dropdown menu.
2.  **Generate a dataset** using the "Randomize" button.
3.  **Start the sort** to watch the animation.
4.  **Pause anytime** to enter "Debug Mode" and step backward or forward through the snapshots.
5.  **Resume** from any specific snapshot to continue the sort from that state.

---

## ⚙️ Installation & Running

### Prerequisites
* **Java 11 or higher** installed on your system.

### Build and Run
```bash
# Compile the project
javac DSAVisualizer.java

# Run the application
java DSAVisualizer
