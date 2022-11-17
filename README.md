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

- [ ] Smooth inner-hour transitions:
  - [ ] Every song seems to have a starting sequence, this is once played when starting the player or at the hour change, so omit this for inner-hour song changes
  - [ ] Every song has a point from which on it will only loop. Find this point for each song and cut it afterwards
- [ ] Smooth hour transitions:
  - [ ] Fade out in the last 10-20s of an hour
  - [ ] Find a Bell tune and play it at the hour change
  - [ ] After a short pause, start the first play of the new hour with the starting sequence
- [ ] More modes, such as e.g. `rain`
