import requests, subprocess, argparse


def create_ssl_certificate(CN:str="", OU:str="", O:str="", L:str="", ST:str="", C:str="") -> bool:
    """
    This method will create a self-signed SSL certificate
    :param CN: Common Name
    :param OU: Organizational Unit
    :param O: Organization
    :param L: Locality
    :param ST: State
    :param C: Country
    :type CN: str
    :type OU: str
    :type O: str
    :type L: str
    :type ST: str
    :type C: str
    :return: bool
    """

    if CN == "":
        own_ip = get_own_ip()
        CN = own_ip
    
    values = "/CN=" + CN
    if OU != "":
        values += "/OU=" + OU
    if O != "":
        values += "/O=" + O
    if L != "":
        values += "/L=" + L
    if ST != "":
        values += "/ST=" + ST
    if C != "":
        values += "/C=" + C
    
    subprocess.run(f"openssl genpkey -algorithm RSA -out /etc/nginx/ssl/key.pem -aes256 -pass pass:your_password", shell=True)
    subprocess.run(f'openssl req -new -key /etc/nginx/ssl/key.pem -out /etc/nginx/ssl/cert.csr -passin pass:your_password -subj "{values}"', shell=True)
    subprocess.run(f"openssl x509 -req -days 365 -in /etc/nginx/ssl/cert.csr -signkey /etc/nginx/ssl/key.pem -out /etc/nginx/ssl/cert.pem -passin pass:your_password", shell=True)

    return True

def get_own_ip() -> str:
    """
    This function makes a http request to one of a few apis to get the own ip.
    :param config: expects a config to get the urls
    :type config: ConfigParser
    :param logger: The Logger object to allow this helper function to work with logging aswell.
    :type Logger: JsonLogger
    :return: str of ip if successful, `127.0.0.1` if not
    """
    
    ret_value = "127.0.0.1"

    api_list = ["https://api.seeip.org/","https://api.ipify.org/","https://api.ipy.ch"]

    for url in api_list:
        try: 
            response = requests.get(url,timeout=5)
            response.raise_for_status()
            ret_value = response.text
            break
        except Exception as e:
            pass
    return ret_value




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate SSL configuration.")
    
    # First argument to decide whether to create SSL
    parser.add_argument('create_ssl', type=str, choices=["True", "False",], help='Boolean flag to decide SSL creation (True/False)')

    # Optional arguments for SSL details
    parser.add_argument('CN', type=str, nargs='?', default=None, help='Common Name')
    parser.add_argument('OU', type=str, nargs='?', default=None, help='Organizational Unit')
    parser.add_argument('O', type=str, nargs='?', default=None, help='Organization Name')
    parser.add_argument('L', type=str, nargs='?', default=None, help='Locality Name')
    parser.add_argument('ST', type=str, nargs='?', default=None, help='State or Province Name')
    parser.add_argument('C', type=str, nargs='?', default=None, help='Country Name')
    args = parser.parse_args()
    if args.CN is None:
        args.CN = ""
    if args.OU is None:
        args.OU = ""
    if args.O is None:
        args.O = ""
    if args.L is None:
        args.L = ""
    if args.ST is None:
        args.ST = ""
    if args.C is None:
        args.C = ""
    if args.create_ssl == "True":
        create_ssl_certificate(args.CN, args.OU, args.O, args.L, args.ST, args.C)
