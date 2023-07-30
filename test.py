from predict_using_logisticRegression import predict_LR

def main():
    print("Bot: Hi! I'm your chat bot. Type 'exit' to end the conversation.")
    import os
    current_directory = os.path.dirname(os.path.abspath(__file__))
    while True:
        # Nhận dữ liệu từ bàn phím
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        # Gọi hàm chat_bot_LR để nhận phản hồi từ mô hình
        response = predict_LR(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()