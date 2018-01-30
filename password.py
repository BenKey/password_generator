from collections import namedtuple
import getopt
import random
import sys

__version__ = '2.0.1'

__doc__ = """

Password generator version %(version)s,
Copyright 2017 by ccminer [https://github.com/ccminer-net].
Copyright 2018 by Ben Key [https://github.com/BenKey].

Password generator is a simple python script that generates a complex pasword.

Usage:
  password.py [options]

Options:
  --help, --HELP, -h, -H, -?
    Print this help message and exit successfully.

  --version, --VERSION, -v, -V
    Print version information and exit successfully.

  --alphabet, --ALPHABET, -a, -A
    Specifies the alphabet that will be used to generate the password.
    Default if not specified, %(default_alphabet)s.

  --length, --LENGTH, -l, -L
    Specifies the length of the password to be generated.
    Default if not specified, %(default_length)s.

"""

__version_info__ = """

Password generator version %(version)s,
Copyright 2017 by ccminer [https://github.com/ccminer-net].
Copyright 2018 by Ben Key [https://github.com/BenKey].

Password generator is a simple python script that generates a complex pasword.

"""

default_alphabet = "abcdefghijklmnopqrstuvwxyz .,!@_-(*)-+/|$%&=?^"
default_pw_length = 37

def usage():
  """Prints the usage information."""
  print(__doc__ % {
    'version' : __version__,
    'default_alphabet' : default_alphabet,
    'default_length' : default_pw_length
  }
  )

def version():
  """Prints the version information."""
  print(__version_info__ % {'version' : __version__})

Arguments = namedtuple("arguments", "ExitCode ShowUsage ShowVersion Alphabet PasswordLength")
def ParseCommandLine():
  """Parses the command line options."""
  exitCode = 0
  showUsage = False
  showVersion = False
  alphabet = default_alphabet
  pw_length = default_pw_length
  if (len(sys.argv) == 1):
    showUsage = True
  elif (len(sys.argv) > 1):
    arg1 = sys.argv[1]
    arg1 = arg1.lower()
    if (arg1 == "/?" or arg1 == "/h" or arg1 == "/help"):
      showUsage = True
    else:
      try:
        opts, args = getopt.getopt(
          sys.argv[1:], "hva:A:l:L:",
          [
            "help", "HELP", "version", "VERSION",
            "alphabet", "ALPHABET", "length", "LENGTH"
          ])
        for o, a in opts:
          if (o in ("-h", "-H", "-?", "--help", "--HELP")):
            showUsage = True
          elif (o in ("-v", "-V", "--version", "--VERSION")):
            showVersion = True
          elif (o in ("-a", "-A", "--alphabet", "--ALPHABET")):
            alphabet = a
          elif (o in ("-l", "-L", "--length", "--LENGTH")):
            pw_length = int(a)
      except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        exitCode = 2
        showUsage = True
    args = Arguments(
      ExitCode=exitCode, ShowUsage=showUsage,
      ShowVersion=showVersion,
      Alphabet=alphabet, PasswordLength=pw_length)
    return args

def main():
  """The main entry point for Password generator."""
  args = ParseCommandLine()
  if args.ShowUsage:
    usage()
    sys.exit(args.ExitCode)
  elif args.ShowVersion:
    version()
    sys.exit(args.ExitCode)
  mypw = ""
  for i in range(args.PasswordLength):
    next_index = random.randrange(len(args.Alphabet))
    mypw = mypw + args.Alphabet[next_index]
  # replace 1 or 2 characters with a number
  for i in range(random.randrange(1, 3)):
    replace_index = random.randrange(len(mypw) // 2)
    mypw = mypw[0 : replace_index] + str(random.randrange(10)) + mypw[replace_index + 1:]
  # replace 1 or 2 letters with an uppercase letter
  for i in range(random.randrange(1, 3)):
    replace_index = random.randrange(len(mypw) // 2, len(mypw))
    mypw = mypw[0 : replace_index] + mypw[replace_index].upper() + mypw[replace_index + 1:]
  print(mypw)

main()
