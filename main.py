import random

options = ('piedra', 'papel', 'tijera')


computer_wins = 0
user_wins = 0
rounds = 1

while True: 

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)

  print('Computadora:', computer_wins)
  print('Usuario:', user_wins)
  

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  rounds += 1
  
  if not user_option in options:
    print('Esa opción no es válida.')
    continue
    
  computer_option = random.choice(options)
  
  print('User option => ', user_option)
  print('Computer option => ', computer_option)
  
  if user_option == computer_option:
    print('¡Es un empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera.')
      print('¡Gana el usuario!')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('¡Gana la compu!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('¡Gana el usuario!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('¡Gana la compu!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('¡Gana el usuario!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('¡Gana la compu!')  
      computer_wins += 1
  
  if computer_wins == 2:
    print('Ganó la compu che... ¡Mejor suerte para la próxima')
    break
    
  if user_wins == 2:
    print('Ganaste por fin :D')
    break
    
  