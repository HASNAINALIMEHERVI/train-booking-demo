# Train Booking Demo

A personal Python object-oriented learning project by Hasnain Ali Mehervi (Sunny), expanded from the supplied `train system class .py` exercise.

This is a terminal simulation with fictional routes and fares. It does not issue real tickets, connect to a railway, process payments or represent client work.

## Run

Python 3.10+; standard library only.

```sh
python train.py
python -m unittest discover -s tests -v
```

Select **Routes** to see the two sample routes, **Book** to reserve demo seats, **Cancel** to release them using the printed reference, or **Exit** to stop. Fares use fictional demo units, not railway prices.

## Behavior

- Deterministic quotes replace the original randomly generated fares.
- Reservations check shared capacity before changing booking state.
- Cancellation restores capacity and cannot cancel the same reference twice.
- References are not reused during one run.
- Invalid route, seat count and menu input receive readable errors.
- Importing the module does not prompt or make a booking.

## Verification and limits

Four unittest cases cover booking and cancellation, quote totals, overselling, invalid input and capacity validation. CLI smoke checks cover invalid route input and clean exit.

All bookings live only in memory and reset when the program exits. Capacity is shared across both routes for a simple single-service demonstration; segment scheduling, persistence, concurrent booking, authentication, passenger data and real payment processing are not implemented. No personal passenger records are bundled.
