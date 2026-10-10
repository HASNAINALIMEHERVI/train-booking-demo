"""In-memory train booking exercise. No real tickets or railway connection."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Booking:
    reference: str
    origin: str
    destination: str
    seats: int
    fare: int


class Train:
    def __init__(self, capacity=5):
        if type(capacity) is not int or capacity < 1:
            raise ValueError('Capacity must be a positive integer')
        self.capacity = capacity
        self.routes = {('Demo City A', 'Demo City B'): 500,
                       ('Demo City A', 'Demo City C'): 900}
        self._bookings = {}
        self._next_reference = 1

    @property
    def available_seats(self):
        return self.capacity - sum(b.seats for b in self._bookings.values())

    def quote(self, origin, destination, seats=1):
        if (origin, destination) not in self.routes:
            raise ValueError('Choose a listed demo route')
        if type(seats) is not int or not 1 <= seats <= self.capacity:
            raise ValueError('Seats must be a positive integer within capacity')
        return self.routes[(origin, destination)] * seats

    def book(self, origin, destination, seats=1):
        fare = self.quote(origin, destination, seats)
        if seats > self.available_seats:
            raise ValueError('Not enough seats available')
        reference = f'DEMO-{self._next_reference:04d}'
        booking = Booking(reference, origin, destination, seats, fare)
        self._bookings[reference] = booking
        self._next_reference += 1
        return booking

    def cancel(self, reference):
        if reference not in self._bookings:
            raise ValueError('Unknown or already cancelled booking')
        return self._bookings.pop(reference)


def main():
    train = Train()
    routes = list(train.routes)
    print('TRAIN BOOKING DEMO — no real tickets or payments; data resets on exit.')
    while True:
        print(f'\nAvailable seats: {train.available_seats}/{train.capacity}')
        print('1: Routes / 2: Book / 3: Cancel / 4: Exit')
        try:
            choice = input('Choose: ').strip()
            if choice == '1':
                for i, (origin, destination) in enumerate(routes, 1):
                    print(f'{i}: {origin} → {destination}: {train.quote(origin, destination)} demo units/seat')
            elif choice == '2':
                route = int(input('Route number (see Routes): '))
                if not 1 <= route <= len(routes):
                    raise ValueError('Choose a listed route number')
                seats = int(input('Number of seats: '))
                booking = train.book(*routes[route - 1], seats)
                print(f'Demo booking: {booking.reference}; total {booking.fare} demo units')
            elif choice == '3':
                booking = train.cancel(input('Demo reference: ').strip().upper())
                print(f'Cancelled {booking.reference}; released {booking.seats} seat(s)')
            elif choice == '4':
                return
            else:
                print('Choose 1, 2, 3 or 4')
        except ValueError as error:
            print(f'Error: {error}')
        except (EOFError, KeyboardInterrupt):
            print('\nDemo closed')
            return


if __name__ == '__main__':
    main()
