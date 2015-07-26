{
    'target_defaults': {
        'type': 'executable',
        'include_dirs': ['./src'],
        'sources': [],
        'cflags': [ '-pthread' ],
        'dependencies': ['./deps/libuv/uv.gyp:libuv'],
    },
    'targets': [
        {
            'target_name': 'init-main-loop',
            'sources': ['./src/main-loop/main.c']
        },
    ],
}
