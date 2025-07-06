import subprocess
import os
import yaml

CPP_FILE = "main.cpp"
PROMPT_FILE = "yaml_prompts/generate_tests.yaml"
OUTPUT_DIR = "tests"
MODEL = "codellama:7b"

def read_cpp_code():
    with open(CPP_FILE, 'r') as f:
        return f.read()

def read_yaml_prompt():
    with open(PROMPT_FILE, 'r') as f:
        data = yaml.safe_load(f)
        return data['instructions']

def run_ollama(prompt, cpp_code):
    full_prompt = f"{prompt}\n\nCode:\n{cpp_code}"
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=full_prompt,
        capture_output=True,
        text=True
    )
    return result.stdout

def save_test(output):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(f"{OUTPUT_DIR}/test_main.cpp", "w") as f:
        f.write(output)

if __name__ == "__main__":
    prompt = read_yaml_prompt()
    cpp_code = read_cpp_code()
    print("⏳ Sending code to Ollama...")
    output = run_ollama(prompt, cpp_code)
    save_test(output)
    print("✅ Test generated and saved in tests/test_main.cpp")
