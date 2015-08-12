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
        {
            'target_name': 'loop-idle',
            'sources': ['./src/loop-idle/main.c']
        },
        {
            'target_name': 'timer',
            'sources': ['./src/timer/main.c']
        },
    ],
}
