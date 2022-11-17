# acww-music

A python app to play _"Animal Crossing: Wild World" (ACWW)_ OST music according to the current time.
It takes ACWW soundfiles from the folder `soundfiles`, and checks the system clock to play the
matching soundfile.

## Soundfile placement

As the soundfiles are licensed, they have to be placed by hand in the `soundfiles`-folder.
The structure of this folder is as follows:

```sh
soundfiles
├── 00
│   ├── 00-normal.mp3
│   └── 00-snow.mp3
...
└── 23
    ├── 23-normal.mp3
    └── 23-snow.mp3
```

## Future work

In a later versions these additional features might be available:

- More modes, such as e.g. `rain`
- Bell ringing at change of music
