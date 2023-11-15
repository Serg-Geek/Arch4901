from ticket import Ticket

class User:
    def __init__(self, _id: int, _name: str, _tickets: list[Ticket], _login: str, _password_hash_code: int, _account_id: int):
        self._id = _id
        self._name = _name
        self._tickets = _tickets
        self._login = _login
        self._password_hash_code = _password_hash_code
        self._account_id = _account_id



    def purchase_ticket(self, new_ticket: Ticket):
        self._tickets.append(new_ticket)

    def cancel_ticket(self, ticket_id: int):
        for ticket in self._tickets:
            if ticket.id == ticket_id:
                self._tickets.remove(ticket)
                return

    def change_password(self, new_password: str):
        self._password_hash_code = hash(new_password)

    def buy_ticket(self, ticket: Ticket):
        # проверяет, достаточно ли средств на аккаунте пользователя, чтобы купить билет.
        if self._account.get_balance() >= ticket.get_price():
            self._account.set_balance(self._account.get_balance() - ticket.get_price())
            self._tickets.append(ticket)
            return True
        else:
            return False