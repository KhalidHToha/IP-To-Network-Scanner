from src.network.network import get_local_ip, get_default_gateway


def main():
    print("IP-To Network Scanner")
    print("---------------------")
    print(f"Local IP : {get_local_ip()}")
    print(f"Gateway  : {get_default_gateway()}")


if __name__ == "__main__":
    main()
