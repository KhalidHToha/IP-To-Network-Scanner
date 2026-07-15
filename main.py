from src.network.network import (
    get_local_ip,
    get_default_gateway,
    get_network,
)


def main():
    print("IP-To Network Scanner")
    print("---------------------")
    print(f"Local IP : {get_local_ip()}")
    print(f"Gateway  : {get_default_gateway()}")
    print(f"Network : {get_network()}")

if __name__ == "__main__":
    main()
