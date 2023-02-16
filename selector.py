import os
import random


def _select(path, prev_name):
    files = os.listdir(path)
    try:
        with open(prev_name, "r") as f:
            old_name = f.readline()
            f.close()
    except FileNotFoundError:
        with open("/Users/jasonboyett/.terminal_backgrounds/prev_name.txt"
                  ) as f:
            old_name = f.readline()
            f.close()

    os.rename(
        os.path.join(path, "current.png"),
        os.path.join(path, old_name))
    random_file = random.choice(files)

    try:
        with open(prev_name, "w") as f:
            f.write(random_file)
            f.close()
    except FileNotFoundError:
        with open("/Users/jasonboyett/.terminal_backgrounds/prev_name.txt"
                  ) as f:
            f.readline(random_file)
            f.close()

    os.rename(
        os.path.join(path, random_file),
        os.path.join(path, "current.png"))


def main():
    try:
        _select("images",
                "prev_name.txt"
                )
    except FileExistsError:
        _select("/Users/jasonboyett/.terminal_backgrounds/images",
                "/Users/jasonboyett/.terminal_backgrounds/prev_name.txt"
                )
    except FileNotFoundError:
        _select("/Users/jasonboyett/.terminal_backgrounds/images",
                "/Users/jasonboyett/.terminal_backgrounds/prev_name.txt"
                )
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
