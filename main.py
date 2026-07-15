from src.network.network import get_local_ip


def main():
    print("IP-To Network Scanner")
    print("---------------------")
    print(f"Local IP : {get_local_ip()}")


if __name__ == "__main__":
    main()
