Initialize a loop in uv
-----------------------

> Simple initialize in osx(kqueue)

[Source code](./main.c)

## Steps

- create a [uv_loop_t] object using malloc
- initialize the loop [uv_loop_init]
- run the loop [uv_run]
- stop the loop [uv_stop]
- free the [uv_loop_t] object

### What happen in the `init`?

- initialize the [uv_loop_t] object
- call kqueue() which sets uv_loop_t->backend_fd as the queue file descriptor

### What happen in the `run`?

- run timer callbacks in `timer_heap`
- run pendending callbacks in `pending_queue`
- run prepare handle, defines in [loop-watcher.c]
- calls [uv__io_poll] to runs `kevent()`
- get the watcher for event_identity in the loop and runs the `cb`
- stop until `QUEUE_EMPTY(&loop->watcher_queue)`
- clean up

### close

Just mark close

### clean up the loop

Just free

## References

- `man kqueue(2)`
- [libuv](https://github.com/libuv/libuv)



[uv_loop_t]:(https://github.com/libuv/libuv/blob/v1.x/include/uv.h#L1436)
[uv_loop_init]:(https://github.com/libuv/libuv/blob/v1.x/include/uv.h#L258)
[uv_run]:(https://github.com/libuv/libuv/blob/c8eebc93a9efcdcc2913723ccd86b35498cc271f/src/unix/core.c#L308)
[uv_stop]:(https://github.com/libuv/libuv/blob/c0c26a0f07346bfe6340fc2541a6dc64f69de177/src/uv-common.c#L402)
[loop-watcher.c]:(https://github.com/libuv/libuv/blob/v1.x/src/unix/loop-watcher.c)
