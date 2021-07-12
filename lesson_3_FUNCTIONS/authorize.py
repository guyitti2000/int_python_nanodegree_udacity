def authorize(quote, **speaker_info):
    print('>', quote)
    print('-' * (len(quote) + 2))
    for key, value in speaker_info.items():
        print(key, value, sep=': ')


print(authorize(
    "Roses are red, violets are blue, I know that I just love you.",
      name='Guy',
      age=20,
      ethnicity='Asian',
      nationality='American'))
