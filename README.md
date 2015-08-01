Libuv Examples
---------------

> Libuv examples for self learning

## Build And Runs The Examples

Initialize with ninja

```bash
./gyp_libuv_examples.py -f ninja
```

Build the source

```bash
ninja -C out/Debug
# or
ninja -C out/Release
```

Run the example files

```bash
./out/Debug/init-main-loop
```

## Examples

1. [main-loop](src/main-loop)
2. [idle-hanler](src/loop-idle)

## License - MIT

See [LICENSE](LICENSE)
