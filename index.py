# bot.py
import discord
import requests
import json
a = ["Bulbasaur ",
     "Bulbasaur ","Bulbasaur ","Ivysaur ","Venusaur",
     "Charmander","Charmeleon","Charizard","Squirtle",
     "Wartortle","Blastroise","Caterpie","Metapod",
     "Butterfree","Weedle","Weedle","Kakuna","Beedrill",
     "Pidgey","Pidgey","Pidgey","Pidgey","Pidgey","Pidgey",
     "Pidgey","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate",
     "Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu",
     "Sandshrew","Sandslash","Nidoran♀","Nidoran♀","Nidoran♀",
     "Nidoran♀","Nidorina","Nidoqueen","Nidoran♀","Nidorino",
     "Nidoking","Clefairy","Clefable","Vulpix","Ninetales",
     "Jigglypuff","Wigglytuff","Zubat","Zubat","Zubat","Golbat",
     "Oddish","Gloom","Vileplume","Paras","Parasect","Venomat","Venomoth",
     "Diglett","Diglett","Diglett","Dugtrio","Meowth","Meowth","Meowth",
     "Persian","Psyduck","Golduck","Mankey","Primeape","Primeape","Growlithe",
     "Growlithe","Growlithe","Arcanine","Poliwag","Poliwhirl","Polywrath","Abra",
     "Abra","Abra","Abra","Kadabra","Alakazam","Machop","Machop","Machop","Machop",
     "Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool",
     "Tentacruel","Geodude","Graveler","Golem","Ponyta","Ponyta","Ponyta","Rapidash",
     "Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo",
     "Dodrio","Seel","Dewgong","Grimer","Grimer","Grimer","Grimer","Muk",
     "Shellder","Cloyster","Gastly","Haunter","Gengar","Gengar","Onix","Drowzee",
     "Hypno","Krabby","Krabby","Krabby","Krabby","Kingler","Voltrob","Electrode",
     "Exeggcute","Exeggutor","Cubone","Marowak","Marowak","Marowak","Hitmonlee",
     "Hitmonchan","Lickitung","Koffing","Koffing","Koffing","Weezing","Rhyhorn",
     "Rhydon","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie",
     "Mr. Mime","Scyther","Scyther","Jynx","Electrabuzz","Magmar","Magmar","Magmar",
     "Magmar","Pinsir","Tauros","Magikarp","Magikarp","Magikarp","Magikarp","Magikarp",
     "Gyrados","Eevee","Vaperon","Joltob","Joltob","Flareon","Porygon","Omanyte","Omastar",
     "Kabuto","Kabutops","Kabutops","Areodactyl","Snorlax","Articuno","Zapdos","Moltres",
     "Dratini","Dratini","Dratini","Dragonair","Dragonite","Mewtwo","Mew","MissingNo","Marshadow"]
# command handler class

class CommandHandler:

    # constructor
    def __init__(self, client):
        self.client = client
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def command_handler(self, message):
        for command in self.commands:
            if message.content.startswith(command['trigger']):
                args = message.content.split(' ')
                if args[0] == command['trigger']:
                    args.pop(0)
                    if command['args_num'] == 0:
                        return self.client.send_message(message.channel, str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >= command['args_num']:
                            return self.client.send_message(message.channel, str(command['function'](message, self.client, args)))
                            break
                        else:
                            return self.client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
                            break
                else:
                    break


# create discord client
client = discord.Client()
token = 'NTgwODI2NTg3ODg5NjY0MDAw.XOWW_Q.DRnqBC9V3mAklbMRwS-2nQTzYQk'

# create the CommandHandler object and pass it the client
ch = CommandHandler(client)

## start commands command
def commands_command(message, client, args):
    try:
        count = 1
        coms = '**Commands List**\n'
        for command in ch.commands:
            coms += '{}.) {} : {}\n'.format(count, command['trigger'], command['description'])
            count += 1
        return coms
    except Exception as e:
        print(e)
ch.add_command({
    'trigger': '^^commands',
    'function': commands_command,
    'args_num': 0,
    'args_name': [],
    'description': 'Prints a list of all the commands!'
})
## end commands command

## start ip commad
def ip_command(message, client, args):
    try:
        req = requests.get('http://ip-api.com/json/{}'.format(args[0]))
        resp = json.loads(req.content.decode())
        if req.status_code == 200:
            if resp['status'] == 'success':
                template = '**{}**\n**IP: **{}\n**City: **{}\n**State: **{}\n**Country: **{}\n**Latitude: **{}\n**Longitude: **{}\n**ISP: **{}'
                out = template.format(args[0], resp['query'], resp['city'], resp['regionName'], resp['country'], resp['lat'], resp['lon'], resp['isp'])
                return out
            elif resp['status'] == 'fail':
                return 'API Request Failed'
        else:
            return 'HTTP Request Failed: Error {}'.format(req.status_code)
    except Exception as e:
        print(e)
ch.add_command({
    'trigger': '^^ip',
    'function': ip_command,
    'args_num': 1,
    'args_name': ['IP\Domain'],
    'description': 'Prints information about provided IP/Domain!'
})
## end ip command
def catchpokemon_function(message, client, args):
    try:
        return 'You have caught a', random.choice(a) 
    except Exception as e:
        return 'please type a number to catch a pokemon'
ch.add_command({
    'trigger': '*spawn',
    'function': catchpokemon_function,
    'args_num': 0,
    'args_name': [],
    'description': 'Will catch a pokimane (IN BETA TESTING)'
})
# bot is ready
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)
    except Exception as e:
        print(e)

# on new message
@client.event
async def on_message(message):
    # if the message is from the bot itself ignore it
    if message.author == client.user:
        pass
    else:
        # try to evaluate with the command handler
        try:
            await ch.command_handler(message)
        # message doesn't contain a command trigger
        except TypeError as e:
            pass
        # generic python error
        except Exception as e:
            print(e)

# start bot
client.run(token)
