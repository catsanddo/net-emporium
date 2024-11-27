import socket
from random import choice

def get_joke():
    jokes = [
                "What do you call an alligator in a vest? An investigator.",
                "I’m addicted to brake fluid, but it’s OK because I can stop at any time.",
                "I can’t stand Russian dolls. They’re so full of themselves.",
                "Why couldn’t the pony sing in the choir? He was a little horse.",
                "I stayed up all night to see where the sun went. Then it dawned on me."
            ]
    return choice(jokes)

def get_fortune():
    fortunes = [
                "You will have a lucky streak soon.",
                "Too bad, you are about to have some bad luck.",
                "You will have the opportunity to make a good friend soon.",
                "A small act of kindness will have a ripple effect.",
                "Do not go to the moon."
            ]
    return choice(fortunes)

def get_quote():
    quotes = [
                "“Do the best you can until you know better. Then when you know better, do better.” - Maya Angelou",
                "“There is nothing noble in being superior to your fellow man; true nobility is being superior to your former self.” - Ernest Hemingway",
                "“One can choose to go back toward safety or forward toward growth. Growth must be chosen again and again; fear must be overcome again and again.” - Abraham Maslow",
                "“We can’t become what we need to be by remaining what we are.” - Oprah Winfrey",
                "“Be not afraid of growing slowly; be afraid only of standing still.” - Chinese Proverb"
            ]
    return choice(quotes)

def read_request(client):
    file = client.makefile("r")
    
    request = file.readline()

    file.close()

    request = request.split(" ")
    if len(request) < 2 or request[0] != "REQUEST":
        return None

    return request[1].strip()

def main():
    # Start listening for connections on port 2023
    server = socket.socket()
    server.bind(("", 2023))

    server.listen(8)

    print("Listening on 127.0.0.1:2023")

    try:
        while True:
            # Accept a connection
            client, addr = server.accept()

            print("Recevied connection from:", addr)

            # Read request type
            request = read_request(client)

            if request == None:
                print("Invalid request. Ignoring.")
                client.close()
                continue

            print("Requested:", repr(request))

            # Respond to requests
            if request == "BANNER":
                client.send("Welcome to the Net Emporium! Make requests and be delighted with my answers!\n".encode())
            elif request == "GOODBYE":
                client.send("Thank you for visiting. Please connect again some time.".encode())
            elif request == "JOKE":
                joke = get_joke() + "\n"
                client.send(joke.encode())
            elif request == "FORTUNE":
                fortune = get_fortune() + "\n"
                client.send(fortune.encode())
            elif request == "QUOTE":
                quote = get_quote() + "\n"
                client.send(quote.encode())

            # Close client
            client.close()
    except KeyboardInterrupt:
            server.close()

if __name__ == "__main__":
    main()
