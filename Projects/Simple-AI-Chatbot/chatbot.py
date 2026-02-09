import random

def chatbot():
    print("🤖 Welcome to AI & SysAdmin Chatbot!")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            responses = ["Hello there!", "Hi, how can I help you?", "Hey! Ask me anything about AI or SysAdmin."]
            print("Bot:", random.choice(responses))

        elif "what is ai" in user_input:
            responses = [
                "AI means Artificial Intelligence — making machines think like humans.",
                "It's a branch of computer science for creating smart machines.",
                "AI allows systems to learn from data and improve over time."
            ]
            print("Bot:", random.choice(responses))

        elif "machine learning" in user_input:
            responses = [
                "Machine Learning is a subset of AI that learns from data.",
                "ML helps computers improve automatically through experience.",
                "It's used in spam filters, recommendations, and self-driving cars."
            ]
            print("Bot:", random.choice(responses))

        elif "deep learning" in user_input:
            responses = [
                "Deep Learning uses neural networks with many layers to analyze complex data.",
                "It powers facial recognition, voice assistants, and more.",
                "It's like teaching a brain-like system to understand patterns."
            ]
            print("Bot:", random.choice(responses))

        elif "system administration" in user_input or "sysadmin" in user_input:
            responses = [
                "System Administration involves maintaining and managing IT systems.",
                "Sysadmins ensure networks, servers, and user systems work smoothly.",
                "It's like being the doctor of computer systems and servers."
            ]
            print("Bot:", random.choice(responses))

        elif "active directory" in user_input:
            responses = [
                "Active Directory is a Microsoft service for managing users, computers, and resources.",
                "It helps in authentication and authorization in a Windows network.",
                "Used for organizing and securing a network environment."
            ]
            print("Bot:", random.choice(responses))

        elif "linux" in user_input:
            responses = [
                "Linux is a free, open-source operating system used in servers and systems.",
                "Sysadmins love Linux for its power, flexibility, and stability.",
                "It's widely used in cloud servers, supercomputers, and even Android."
            ]
            print("Bot:", random.choice(responses))

        elif "ip address" in user_input:
            responses = [
                "An IP address is a unique number that identifies a device on a network.",
                "It's like the home address for your computer in the digital world.",
                "IP addresses come in IPv4 and IPv6 formats."
            ]
            print("Bot:", random.choice(responses))

        elif "firewall" in user_input:
            responses = [
                "A firewall protects your system from unauthorized access.",
                "It acts like a security guard for your network.",
                "Firewalls can be hardware or software based."
            ]
            print("Bot:", random.choice(responses))

        elif "bye" in user_input or "exit" in user_input:
            print("Bot: 👋 Goodbye! Keep exploring AI and SysAdmin!")
            break

        else:
            responses = [
                "I'm still learning! Ask me something about AI or System Administration.",
                "Hmm, I don't know that yet. Try asking about machine learning or servers.",
                "Let's stick to AI or SysAdmin topics. I'm still a student bot!"
            ]
            print("Bot:", random.choice(responses))

chatbot()
