# 🎲 Dice Simulator

A dice rolling simulator implemented in **C** and **x86 Assembly**, developed as a Computer Organization & Architecture course project.

---

## 📋 Description

This project simulates rolling one or more standard 6-sided dice. It uses a **Linear Congruential Generator (LCG)** algorithm — a classic pseudo-random number generation technique — to produce dice roll results. The project demonstrates low-level programming concepts by implementing the core logic in both C and Assembly language.

---

## ✨ Features

- Roll any number of dice in a single turn
- Pseudo-random number generation using the LCG algorithm (multiplier: `1103515245`, a standard LCG constant)
- Displays each individual die result
- Shows the **total sum** of all dice rolled
- Prompts the user to roll again or exit
- Input validation (rejects zero or negative dice counts)

---

## 🛠️ Technologies Used

| Language | Purpose |
|----------|---------|
| C | High-level logic, I/O, and control flow |
| x86 Assembly | Low-level implementation of the simulation core |

---

## 🚀 How to Run

### Compile (C version)

```bash
gcc dice_simulator.c -o dice_simulator
./dice_simulator
```

### Compile (Assembly version)

```bash
nasm -f elf64 dice_simulator.asm -o dice_simulator.o
gcc dice_simulator.o -o dice_simulator -no-pie
./dice_simulator
```

---

## 🎮 Sample Output

```
How many dice will you roll? 3
Die 1: 4
Die 2: 2
Die 3: 6
Total Sum: 12
Roll again? (y/n): n
Game ended.
```

---

## 🔢 Algorithm — Linear Congruential Generator (LCG)

The random number generation follows the formula:

```
Roll = ((Roll × 1103515245) + numOfDice) % 6 + 1
```

- **Multiplier**: `1103515245` — a well-known LCG constant used in many standard C library `rand()` implementations
- **Increment**: number of dice (adds variability per session)
- **Modulus**: `6` — maps the result to the range `[1, 6]`

---

## 👥 Team

Developed by a group of 3 students as part of a **Computer Organization & Architecture** course project.

---

## 📚 Concepts Demonstrated

- Pseudo-random number generation
- Integer arithmetic at the assembly level
- C and Assembly integration
- User input handling and validation
- Loop control and conditional branching
