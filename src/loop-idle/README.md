# Calling idle function in the Loop

## Why

For different reasons, maybe we want to do something when the loop is idling say. If we want to trigger garbage collection but don't want to effect the application performance, then we can start the garbage collection when the loop is idling for few seconds(assuming it's doesn't have other thing to do).

## How to

1. Initialize and register a idle handler/callback.
2. `start` the idle handler
3. start running the loop
4. stops the idle handle manually

## How it works

In `main_loop` example, it explains how `uv_run` function works. But only contains
the `kevent` part. So in the `infinity` loop, it check if the loop is stop, but
in the same time. It calls these functions in order:

```c
uv__update_time(loop);
uv__run_timers(loop);
uv__run_pending(loop);
uv__run_idle(loop);
uv__run_prepare(loop);
```

It means that when all the `real` task finished, it will run all the `idle` handlers
which are in the loop. Since all the callbacks which runs in `uv__run_#name` are
`uv_#name_t`. It means that they will have same process procedure. If we know how
to create and register a idle callback in a loop. Other handles will be the same.

Other handler which will have the same logic are:

1. prepare
2. check

## What happens in the code

### `uv_idle_init`

It creates the handler object, and register it with the loop, that's it.

### `uv_idle_start`

1. `Prepend` the handler in the running queue.
2. Set the callback function
3. Mark the handler is a active handler.
4. And it doesn't actually start running the loop until `uv_run` calls.

Yes, it's prepend. In the code `loop-idle/main.c`. We can see the register order:

```c
uv_idle_start(&idler, wait_for_a_while);
uv_idle_start(&idler2, wait_for_a_while2);
```

But in the output, it will shows:

```bash
Calling idle2
Calling idle1
```

### `uv_idle_stop`

1. Remove the handler in the loop.
2. Mark the handler is not active.
