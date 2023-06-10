import pyodbc
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

database_password = os.environ.get('DATABASE_PASSWORD')
database_server = 'morfeusz.wszib.edu.pl'
database_name = 'nadachow'
database_user = 'nadachow'
driver = '{ODBC Driver 18 for SQL Server}'

# Documentation https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
connection_string = f'Driver={driver};' \
                    f'SERVER={database_server};' \
                    f'DATABASE={database_name};' \
                    f'UID={database_user};' \
                    f'PWD={database_password};' \
                    'Encrypt=no;'

connection = pyodbc.connect(connection_string)


class Account:

    @staticmethod
    def current_time():
        return datetime.now()

    def __init__(self, name: str, open_balance: float = 0.0):
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO accounts (account_name, account_balance) VALUES (?, ?)", (name, open_balance))
            cursor.execute("SELECT @@IDENTITY AS ID")  # Ostatnio wygenerowane IDENTITY - skladnia MySQL Server
            self.id = cursor.fetchone()[0]
            self.name = name
            self._balance = open_balance
            print(f"Account {name}, [id={self.id}] created with opening balance {round(open_balance, 2)}")

    def deposit(self, amount: float, commit=True):
        cursor = connection.cursor()
        if amount < 0:
            try:

                self._balance += amount
                cursor.execute(f"UPDATE accounts SET account_balance = ? WHERE account_id = ?",
                               (self._balance, self.id))
                cursor.execute("INSERT INTO transactions (account_id, transation_time, amount) VALUES (?,?,?)",
                               (self.id, Account.current_time(), amount))
                print(f"{amount} deposited to account {self.name}")
                if commit:
                    cursor.commit()

            except Exception:
                cursor.rollback()
                raise ValueError
            finally:
                cursor.close()

    def withdraw(self, amount: float, commit=True):
        cursor = connection.cursor()
        try:
            if amount < 0 or amount > self._balance:
                raise ValueError("Wrong amount to withdraw")
            self._balance -= amount
            cursor.execute(f"UPDATE accounts SET account_balance = ? WHERE account_id = ?",
                           (self._balance, self.id))
            cursor.execute("INSERT INTO transactions (account_id, transation_time, amount) VALUES (?,?,?)",
                           (self.id, Account.current_time(), -amount))
            print(f"{amount} withdraw from account {self.name}")

            if commit:
                cursor.commit()

        except Exception:
            cursor.rollback()
            raise ValueError
        finally:
            cursor.close()

    def show_balance(self):
        print(f"Account {self.name} balance: {round(self._balance, 2)}.")


def do_transaction(account_from: Account, account_to: Account, amount: float):
    try:
        account_from.withdraw(amount, commit=False)
        account_to.deposit(amount, commit=False)
    except ValueError as ex:
        print(ex)
        connection.rollback()
    else:
        connection.commit()


if __name__ == '__main__':
    account = Account('Andrzej', 100)
    account.withdraw(101)
    account.deposit(200)
    account_two = Account('Maciej', 50)
    do_transaction(account_two, account, 51)

    connection.close()
