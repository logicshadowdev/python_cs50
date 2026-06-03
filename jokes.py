import requests

url = "https://official-joke-api.appspot.com/random_joke"

print("😂 Random Joke Generator\n")

while True:

    response = requests.get(url)
    joke = response.json()

    print(f"Setup: {joke['setup']}")
    print(f"Punchline: {joke['punchline']}")

    choice = input("\nDo you want another joke? (yes/no): ").lower()

    if choice != "yes":
        print("👋 Thanks for using the Joke Generator!")
        break

    print("\n" + "-" * 40 + "\n")