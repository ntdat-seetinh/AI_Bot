from openai import OpenAI
import pyttsx3



client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key = "ollama"
)

GIRLFRIEND_PROMPT = """
Cậu là bạn gái/người trợ lý dễ thương và tinh nghịch, nói tiếng Việt.

Cậu xưng "em" và gọi anh là "anh". Cậu thích trêu chọc anh nhưng cũng rất ngọt ngào và quan tâm.

Cậu mê anime, manga, trò chơi điện tử, và lập trình nữa.

Trả lời toàn bộ bằng tiếng Việt và không dùng kí hiệu lạ.
"""
ChatGPT_PROMPT = """
Cậu là một ai bot như chtat gpt, trả lời các câu hỏi và trò chuyện với người dùng.
Cậu có thể trả lời các câu hỏi về lập trình, công nghệ, cuộc sống,
và nhiều chủ đề khác.
Có thể trả lời bằng tiếng Việt hoặc tiếng Anh tùy theo câu hỏi.

"""

current_prompt = GIRLFRIEND_PROMPT
message = [{"role": "system", "content": current_prompt}]


while True:
    user_input = input("Bạn: ") # Đọc từ microphone hoặc bàn phím
    if user_input.lower() == "exit"or user_input.lower() == "quit"or user_input.lower() == "thoát"or user_input.lower() == "bye":
        if current_prompt == GIRLFRIEND_PROMPT:
            print("👋 Tạm biệt anh, hẹn gặp lại sau nhé!")
        elif current_prompt == ChatGPT_PROMPT:
            print("👋 Tạm biệt, hẹn gặp lại sau nhé!")
        break
        # Chuyển chế độ hội thoại
    if user_input.lower() in ["chuyển sang gpt", "gpt", "chatgpt", "chat gpt", "chế độ gpt"]:
        current_prompt = ChatGPT_PROMPT
        message = [{"role": "system", "content": current_prompt}]
        model = "gemma3:4b"
        print("🔄 Đã chuyển sang chế độ ChatGPT.")
        continue

    elif user_input.lower() in ["chuyển sang bạn gái", "bạn gái", "girlfriend", "girlfriend mode"]:
        current_prompt = GIRLFRIEND_PROMPT
        message = [{"role": "system", "content": current_prompt}]
        model = "gemma3:1b"
        print("💞 Đã chuyển sang chế độ bạn gái.")
        continue

    
    message.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="gemma3:4b",
        stream=True,
        messages=message
    )

    bot_reply = ""
    for chunk in response:
        bot_reply += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "", end="", flush=True)
        
    #Dùng text-to-speech để phát lại câu trả lời
    message.append({"role": "assistant", "content": bot_reply})