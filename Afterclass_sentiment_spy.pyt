import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

conversation_history = []
positive_count = 0
negative_count = 0
neutral_count = 0


def get_valid_name():
    while True:
        name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
        if name.isalpha():
            return name
        print(f"{Fore.RED}Please use letters only.{Style.RESET_ALL}")


def show_processing_animation():
    print(f"{Fore.CYAN}Analyzing...{Style.RESET_ALL}")


def analyze_sentiment(text):
    global positive_count, negative_count, neutral_count

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.25:
        sentiment = "Positive"
        color = Fore.GREEN
        emoji = "😊"
        positive_count += 1
    elif polarity < -0.25:
        sentiment = "Negative"
        color = Fore.RED
        emoji = "😞"
        negative_count += 1
    else:
        sentiment = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"
        neutral_count += 1

    conversation_history.append((text, polarity, sentiment))

    print(f"{color}{emoji} {sentiment} sentiment detected! "
          f"Polarity: {polarity:.2f}{Style.RESET_ALL}")


def execute_command(command):
    global positive_count, negative_count, neutral_count

    if command == "summary":
        print(f"{Fore.CYAN}Positive: {positive_count}")
        print(f"Negative: {negative_count}")
        print(f"Neutral: {neutral_count}{Style.RESET_ALL}")

    elif command == "reset":
        conversation_history.clear()
        positive_count = negative_count = neutral_count = 0
        print(f"{Fore.CYAN}All data has been reset!{Style.RESET_ALL}")

    elif command == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No history yet.{Style.RESET_ALL}")
        else:
            for i, (text, polarity, sentiment) in enumerate(
                conversation_history, 1
            ):
                print(f"{i}. {text} | {polarity:.2f} | {sentiment}")

    elif command == "help":
        print(f"{Fore.CYAN}Commands: summary, reset, history, help, exit"
              f"{Style.RESET_ALL}")
    else:
        return False

    return True


print(f"{Fore.CYAN}Welcome to Sentiment Spy!{Style.RESET_ALL}")

user_name = get_valid_name()

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence to analyze it.")
print(f"Type {Fore.YELLOW}summary, reset, history, help or exit"
      f"{Fore.CYAN}.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if user_input.lower() == "exit":
        filename = f"{user_name}_sentiment_analysis.txt"

        with open(filename, "w") as file:
            file.write(f"Sentiment Spy Report for {user_name}\n")
            file.write(f"Positive: {positive_count}\n")
            file.write(f"Negative: {negative_count}\n")
            file.write(f"Neutral: {neutral_count}\n")

        print(f"{Fore.CYAN}Report saved as {filename}!")
        print(f"Goodbye, Agent {user_name}! 😊{Style.RESET_ALL}")
        break

    if execute_command(user_input.lower()):
        continue

    show_processing_animation()
    analyze_sentiment(user_input)