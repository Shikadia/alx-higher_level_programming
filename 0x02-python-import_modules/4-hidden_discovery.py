#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for index in names:
        if index[:2] != "__":
            print(index)
