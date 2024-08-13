"""debug this script by pdb

https://docs.python.org/3/library/pdb.html

1.  insert "breakpoint()" in script, or
2.  python -m pdb myscript.py

(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb
"""


def main():
    breakpoint()  # replace "import pdb; pdb.set_trace()"
    print("hello, world")


if __name__ == "__main__":
    main()
