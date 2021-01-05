from user import CreateAccount, AccountSearch
import click
import ed25519
from block import BlockChain

def createNewAccount():
    NewAccount = CreateAccount()
    return {'AccountName': str(NewAccount.PublicKey),
            'SigningKey' : str(NewAccount.PrivateKey)
        }

def showAllCoins(AccountName):
    blockChain = BlockChain()
    blockChain.FileTo()
    coinList = AccountSearch().ShowCoins(AccountName, blockChain)
    return coinList

def showAllTransHistory(AccountName):
    AccountName = ed25519.SigningKey(bytes(AccountName, encoding="utf8"))
    blockChain = BlockChain().FileTo()
    tranList = AccountSearch().ShowTransHistory(AccountName, blockChain)
    return tranList

def transparant(SendName, ReciveName, key, coin):
    SendName = ed25519.SigningKey(bytes(SendName, encoding="utf8"))
    blockChain = BlockChain().FileTo()
    coinList = AccountSearch().ShowCoins(SendName, blockChain)
    if coin not in coinList:
        return {'status': 'coin do not exist, trans cecal'}
    coin_list = []
    coin_list.append(coin)
    ex_mesg = ''
    AccountSearch().SendCoins(SendName, ReciveName, key, coin_list, ex_mesg)

@click.group()
@click.version_option(version='0.0.1')
def cli():
    pass

@click.command()
def CreateNewAccount():
    NewAccount = CreateAccount()
    click.echo('AccountName:' + str(NewAccount.PublicKey))
    click.echo('SigningKey:' + str(NewAccount.PrivateKey))
cli.add_command(CreateNewAccount)

@click.command()
@click.argument('AccountName')
def ShowAllCoins(AccountName):
    coinList = showAllCoins(AccountName)
    for coin in coinList:
        click.echo(coin)
cli.add_command(ShowAllCoins)

@click.command()
@click.argument('AccountName')
def ShowAllTransHistory(AccountName):
    tranList = showAllTransHistory(AccountName)
    for tran in tranList:
        click.echo(tran)
cli.add_command(ShowAllTransHistory)

@click.command()
@click.argument('SendName')
@click.argument('ReciveName')
@click.argument('key')
@click.argument('coin')
def Transparant(SendName, ReciveName, key, coin):
    transparant(SendName, ReciveName, key, coin)
cli.add_command(Transparant)

if __name__ == '__main__':
    cli()





