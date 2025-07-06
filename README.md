# C++ Unit Test Generator using Ollama 🚀

This project is part of the **Keploy API Fellowship - Day 5 Assignment**.

It demonstrates how to use **Ollama** (running open-source Large Language Models locally) to automatically generate **unit tests** for a C++ application and optionally refine them based on feedback.

---

## 📝 Project Overview

- ✅ Takes existing C++ source code (`main.cpp`)
- ✅ Uses AI (via Ollama and Codellama model) to generate unit tests
- ✅ Stores generated tests in `tests/test_main.cpp`
- ✅ Compiles and runs the tests using `g++`

---

## 📂 Project Structure
cpp-unit-test-generator/
├── main.cpp
├── generator.py
├── yaml_prompts/
│ └── generate_tests.yaml
├── tests/
│ ├── functions.cpp
│ ├── functions.h
│ └── test_main.cpp
└── README.md

 ⚙️ How to Run

1. **Install Ollama** and pull the model:
2. llama pull codellama:7b


2. **Generate Unit Tests**:
python generator.py

3. **Compile and Run**:
g++ main.cpp tests/functions.cpp tests/test_main.cpp -o test_program.exe
test_program.exe


## 📊 Coverage & Improvements

- Test cases are auto-generated covering positive, negative, and edge cases.
- Currently no code coverage tool integrated (can be added using `gcov` later).

## 🙌 Acknowledgements

- **Ollama**: For running open-source LLMs locally.
- **Keploy API Fellowship**: For providing this hands-on learning opportunity.
GitHub: [https://github.com/toughcodersir](https://github.com/toughcodersir)



