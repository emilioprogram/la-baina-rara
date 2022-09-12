def on_forever():
    super_chip: game.LedSprite = None
    pins.set_audio_pin_enabled(False)
    super_chip.delete()
basic.forever(on_forever)
