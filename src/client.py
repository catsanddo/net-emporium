import socket

def make_request(request):
    requests = {
        0: "REQUEST GOODBYE\n",
        1: "REQUEST JOKE\n",
        2: "REQUEST FORTUNE\n",
        3: "REQUEST QUOTE\n",
        4: "REQUEST BANNER\n"
    }

    message = requests.get(request)
    if message == None:
        return None

    try:
        # Establish connection
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(("127.0.0.1", 2023))
        
        server.send(message.encode())

        # Read 1 line from the socket
        file = server.makefile(mode="r")
        response = file.readline()

        # Close the socket
        file.close()
        server.close()

        return response
    except:
        print("Could not connect to the server. Is it still running?")
        return ""

def main():
    print("Connecting to the server...")

    # Initial connection to server; get and print banner
    banner = make_request(4)

    if banner == "":
        print("Quitting.")
        return

    print(banner)

    running = True
    while running:
        print("Requests:")
        print("\t1. Tell me a joke.")
        print("\t2. Tell my fortune.")
        print("\t3. Inspire me.")
        print("\t0. Quit")

        # Get input from user
        user_choice = input("> ")
        try:
            user_choice = int(user_choice)
        except:
            print("Choose one of the options!")
            print()
            continue

        if user_choice == 0:
            running = False

        if user_choice < 0 or user_choice > 3:
            print("Choose one of the options!")
            print()
            continue

        # Make the request
        response = make_request(user_choice)

        # Is the response valid? print it
        if response == "":
            print("Quitting.")
            return
        elif response == None:
            print("That wasn't a valid request!")
            continue

        print(response)
    # end while running:

if __name__ == "__main__":
    main()
