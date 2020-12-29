from user import CreateAccount, AccountSearch
import click
import ed25519
from block import BlockChain

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
    AccountName = ed25519.SigningKey(bytes(AccountName, encoding="utf8"))
    blockChain = BlockChain().FileTo()
    coinList = AccountSearch().ShowCoins(AccountName, blockChain)
    for coin in coinList:
        click.echo(coin)
cli.add_command(ShowAllCoins)

@click.command()
@click.argument('AccountName')
def ShowAllTransHistory(AccountName):
    AccountName = ed25519.SigningKey(bytes(AccountName, encoding="utf8"))
    blockChain = BlockChain().FileTo()
    tranList = AccountSearch().ShowTransHistory(AccountName, blockChain)
    for tran in tranList:
        click.echo(tran)
cli.add_command(ShowAllTransHistory)

@click.command()
@click.argument('SendName')
@click.argument('ReciveName')
@click.argument('key')
@click.argument('coin')
def Transparant(SendName, ReciveName, key, coin):
    SendName = ed25519.SigningKey(bytes(SendName, encoding="utf8"))
    blockChain = BlockChain().FileTo()
    coinList = AccountSearch().ShowCoins(SendName, blockChain)
    if coin not in coinList:
        click.echo('coin do not exist!!!')
    coin_list = []
    coin_list.append(coin)
    ex_mesg = ''
    AccountSearch().SendCoins(SendName, ReciveName, key, coin_list, ex_mesg)
cli.add_command(Transparant)

if __name__ == '__main__':
    cli()





