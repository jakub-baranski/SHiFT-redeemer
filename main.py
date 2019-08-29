import sys

from code_redeemer import CodeRedeemer

if __name__ == '__main__':
    game = sys.argv[1]
    print(game)
    redeemer = CodeRedeemer(game)
    redeemer.run()
