from time import sleep

def get_printing_first()->None:
    pict_list = ['MY FIRST SKRIPT\n\n',
                  '    *********',
                  '   *       **',
                  '  *       * *',
                  ' *********  *',
                  ' *       *  *',
                  ' *       *  *',
                  ' *       * *',
                  ' *********',
                 '\n\nI LOVE PYTHON']
    for i in pict_list:
      sleep(.4)
      print(i)