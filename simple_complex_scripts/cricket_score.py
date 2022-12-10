import requests
from clint.arguments import Args
from clint.textui import puts, colored, indent
def cricket():
    x = requests.get("https://api.cricapi.com/v1/currentMatches?apikey=7e98fe25-ddbf-456e-9cc3-6a2e4d8634c1")
    core_data = x.json()["data"][0]
    name = core_data['name']
    status = core_data['status']
    date = core_data['date']
    score = core_data['score']
    first_inning = score[0]
    secound_inning = score[1]
    information = {
        "name":name,
        "status":status,
        "date":date,
        "first_inning":first_inning,
        "secound_inning":secound_inning,
    }

    puts(f"{colored.blue('name')} = {colored.red(name)}")
    puts(f"{colored.blue('status')} = {colored.red(status)}")
    puts(f"{colored.blue('date')} = {colored.red(date)}")
    puts(f"{colored.green(first_inning['inning'])}")
    puts(f"{colored.blue('runs')} = {colored.red(first_inning['r'])}")
    puts(f"{colored.blue('wickets')} = {colored.red(first_inning['w'])}")
    puts(f"{colored.blue('overs')} = {colored.red(first_inning['o'])}")
    puts(f"{colored.green(secound_inning['inning'])}")
    puts(f"{colored.blue('runs')} = {colored.red(secound_inning['r'])}")
    puts(f"{colored.blue('wickets')} = {colored.red(secound_inning['w'])}")
    puts(f"{colored.blue('overs')} = {colored.red(secound_inning['o'])}")
    #puts(f"{colored.blue('first innings')} = {colored.red(first_inning)}")
    #puts(f"{colored.blue('secound innings')} = {colored.red(secound_inning)}")
    #return (information)

if __name__ == '__main__':
    cricket()