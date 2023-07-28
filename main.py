import os
import multiprocessing
import check_inputKeys
import check_playersKills
import time

programs=[check_inputKeys, check_playersKills]



if __name__ == '__main__':
    multiprocessing.freeze_support()
    print("""\

                    (, , )           .-----._  ___
                   ( <  /)           |     | ||==||
                   _(())\)           |     | /|==||  __
                .-' (()/  '-.        :_____:/ |"_|/)  /|
              _/     ()      \    / .-------.  __.'  / |
             oo)__/   ()  \  |   / '======='  ()    /  |
             :~    \_  ) _/ _/  /__________________/   |
             |      |- (--|(,/ |           [___o___]   |
             |     /   )   \   |   /       [___o___]   /
             |     |  (     \  |  /        [___o___]  /
             |     |        (  | /                 | /
             |     /  .     |  |/      __          |/
             |     |  :     |        <`,,'>,--,--..-,
  JustIdeas  |     |__/_____\         |  / (  ( ) )  /
            .,,.  oo='  oo='          '-'\ ) )     ) )/
     ___.---;  <                         (,_)_)(_,)_/
    /    \ .-\_/_,__                      |||    |||
 _ _\_\_  \ \   __\-'                      ~~     ~~
( ) ( )  _/ '-'
/_/-/_/-'
          
          """)
    time.sleep(4)
    jobs = []
    for i in programs:
        p = multiprocessing.Process(target=i.start)
        jobs.append(p)
        p.start()
