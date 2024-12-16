from rich.console import Console
from rich.table import Table

console = Console()
console.print('Olá, [bold magenta]Rich[/bold magenta]!', style='bold blue')

table = Table(title='Tabela de Exemplo')
table.add_column('Nome', style='cyan')
table.add_column('Idade', style='magenta')

table.add_row('Alice', '24')
table.add_row('Bob', "30")

console.print(table)