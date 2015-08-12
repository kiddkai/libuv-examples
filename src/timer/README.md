# Timer

> setTimeout & setInterval in libuv

## Create a Timer

If we want to create a timer, we always need to use these 2 functions
to help us:

1. uv_timer_init
2. uv_timer_start

To use `uv_timer_init`, it will just be the same with other `uv_*_t`
structures which need to specify which loop it want to use and which
timer pointer want to use to point to a new timer handler.

But the `uv_timer_start` will be a little bit different with the idle
start, it need to pass in few things:

1. the `timer handler` which init by the `uv_timer_init`.
2. the callback function
3. the number that specifies the first timeout
4. the number that specifies the interval

It means that if we left the third argument as `0`, then the timer will run
directly when first run. And then interval calls the callback with the 4th
argument.

When we set the 4th argument 0, means that this timer never repeats.

### Simulate the `setTimeout` in JavaScript

So when we know how it runs, it's super easy to simulate a `setTimeout` function.
We just need to:

```c
uv_timer_start(&timer_req, callback, 1000, 0);
```

Then this timer will wait 1000ms then call the callback once.

### Simulate the `setInterval` in JavaScript

```c
uv_timer_start(&timer_req, callback, 0, 1000);
```

### Simulate the `setTimeout -> setInterval`

```c
uv_timer_start(&timer_req, callback, 1000, 1000);
```

### clearTimeout & clearInterval

In order to clear a timeout or interval. There's a function called `uv_timer_stop`
to helps us to clears the timer. Just pass in the timer handler we need then it
will clear the timer from the event loop.

## How it implemented

The timer implementation is super simple. It just checking that if the destination
time is smaller than current system time. If it is then call the callback, if it's
not just keep running the loop.

All the detail implementation will be in:

1. [timer.c]
2. [core.c]
