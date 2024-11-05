import os
import requests
import pypdf

# Function to load chat history from file
def load_history():
    try:
        with open("chat_history.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to save chat history to file
def save_history(history):
    with open("chat_history.txt", "w") as file:
        file.write("\n".join(history))

# Your background information
def get_user_background():
    return (
       "Your prompt"
    )

# Function to generate a response from the local LLaMA model
def generate_response(prompt, conversation_history, file_contents):
    user_background = get_user_background()
    formatted_history = "\n".join(conversation_history)
    combined_file_content = "\n\n".join(file_contents)
    full_prompt = f"{user_background}\n\nFile content:\n{combined_file_content}\n\nConversation history:\n{formatted_history}\n\nHuman: {prompt}\nAI:"

    url = 'http://localhost:11434/v1/completions'
    headers = {'Content-Type': 'application/json'}
    data = {
        'prompt': full_prompt,
        'model': 'llama3.2',
        'max_tokens': 10000  # Adjust as needed
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['text']
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {e}"

# Function to check allowed file types
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'md', 'py', 'js', 'html', 'css', 'json', 'pdf'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to upload files and read their contents
def upload_files():
    file_contents = []
    print("Enter the path of the file(s) to upload (separate multiple paths with commas):")
    file_paths = input().split(',')
    
    for path in file_paths:
        path = path.strip()
        if allowed_file(path):
            try:
                if path.lower().endswith('.pdf'):
                    pdf_reader = pypdf.PdfReader(path)
                    content = ""
                    for page in pdf_reader.pages:
                        content += page.extract_text()
                else:
                    with open(path, 'r', encoding='utf-8') as file:
                        content = file.read()
                
                file_contents.append(content)
                print(f"Successfully uploaded {path}.")
            except Exception as e:
                print(f"Error reading file {path}: {str(e)}")
        else:
            print(f"File type not allowed: {path}")

    return file_contents

# Main CLI loop
def main():
    conversation_history = load_history()
    file_contents = []

    print("Welcome to the AI Assistant CLI!")
    print("Type 'exit' to quit the application.")

    while True:
        command = input("\nEnter 'upload' to upload files or 'chat' to start chatting: ").strip().lower()
        
        if command == 'upload':
            file_contents = upload_files()
        
        elif command == 'chat':
            while True:
                user_input = input("\nYou: ")
                if user_input.lower() == 'exit':
                    break
                conversation_history.append(f"Human: {user_input}")

                ai_response = generate_response(user_input, conversation_history, file_contents)
                conversation_history.append(f"AI: {ai_response}")

                print(f"AI: {ai_response}")
                
        elif command == 'exit':
            break

        else:
            print("Invalid command. Please try again.")
    
    save_history(conversation_history)
    print("Chat history saved. Goodbye!")

if __name__ == "__main__":
    main()
