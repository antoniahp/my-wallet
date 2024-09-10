from decimal import Decimal

from bank.domain.account import Account


class AccountUpdater:
    def update(self, account: Account,  funds_amount:Decimal)-> Account:
        account.funds_amount = funds_amount
        return account