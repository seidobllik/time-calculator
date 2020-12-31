def add_time(start, duration, dotw = None):
  days = tuple(('sunday', 'monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday'))

  try:
    start_h = int(start.split(':')[0]) + (12 if start[-2:] == 'PM' else 0)
    start_m = int(start[-5:-3])
  except Exception as e:
    print(e)

  duration_h = int(duration.split(':')[0])
  duration_m = int(duration.split(':')[1])

  result_h = start_h + duration_h
  result_m = start_m + duration_m
  result_d = 0

  while result_m > 59:
    result_h += 1
    result_m -= 60

  while result_h > 23:
    result_d += 1
    result_h -= 24

  result_tail = days[(days.index(dotw.lower()) + result_d) % 7].capitalize() if dotw is not None else ''
  
  if result_d == 1:
    result_tail += ' (next day)'
  elif result_d > 1:
    result_tail += f' ({result_d} days later)'
  result_modifier = ''

  if result_h >= 12:
    result_h -= 12
    result_modifier = 'PM'
  else:
    result_modifier = 'AM'
  
  if result_h == 0:
    result_h = 12

  return f'{str(result_h)}:{str(result_m).rjust(2, "0")} {result_modifier}{", " + result_tail if dotw is not None else result_tail}'
